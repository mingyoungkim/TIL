package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

/** @Service
 * spring 컨테이너에 해당 서비스를 등록해서 관리함
 */
@Service
@Transactional // jpa를 쓸려면 항상 트랜젝션이 있어야함 (데이터를 저장, 변경할때 transaction이 있어야하니까)
public class MemberService {
    //private final MemberRepository memberRepository = new MemoryMemberRepository();
    /* Dependancy Injection (DI)
     service에서 new로 다시 생성하지말고,
     외부에서 들어오는 repository 그대로 사용
     */
    private final MemberRepository memberRepository;

    @Autowired
    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    /**
     * 회원가입
     */
    public long join(Member member) {
        /*
        // 중복 회원 검증
        // command + option + V : 리턴 자동 생성
        Optional<Member> result = memberRepository.findByName(member.getName());
        // optional 이기에 isPresent 가능
        result.ifPresent(m -> {
            throw new IllegalStateException("이미 존재하는 회원입니다.");
        });
        */

        // join메서드의 시간 측정하는 로직 -> 공통관심사항
        long start = System.currentTimeMillis();

        try {
            // 메서드 따로 빼서 작성하기
            validateDuplicateMember(member);

            memberRepository.save(member);
            return member.getId();
        }
        finally {
            long finish = System.currentTimeMillis();
            long timeMs = finish - start;
            System.out.println("join AOP == " + timeMs + "ms");
        }
    }

    private void validateDuplicateMember(Member member) {
        // optional 구현 권장
        memberRepository.findByName(member.getName())
                .ifPresent(m -> {
                    throw new IllegalStateException("이미 존재하는 회원입니다.");
                });
    }

    /*
    * 전체 회원 조회
    */
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }
}
