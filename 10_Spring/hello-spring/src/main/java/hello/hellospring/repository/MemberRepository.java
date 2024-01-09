package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import javax.swing.text.html.Option;
import java.util.List;
import java.util.Optional;

public interface MemberRepository {
    Member save(Member member);

    /* Optional
    * 해당 메서드의 반환값이 null 일 수 있으니, null을 처리하는 방법 중 하나
    * */
    Optional<Member> findById(Long id);
    Optional<Member> findByName(String name);
    List<Member> findAll();
}
