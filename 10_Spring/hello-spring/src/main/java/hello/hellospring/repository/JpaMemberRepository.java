package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import jakarta.persistence.EntityManager;

import java.util.List;
import java.util.Optional;

public class JpaMemberRepository implements MemberRepository {
    // JPA는 EntityManager로 동작함
    // gradle에 data-jpa 라이브러리로 받으면, 스프링부트가 자동으로 현재 데이터베이스와 다 연결하고 EntityManager를 만들어줌
    // 만들어진 EntityManager를 주입만 하면 됨.
    private final EntityManager em;

    public JpaMemberRepository(EntityManager em) {
        this.em = em;
    }

    @Override
    public Member save(Member member) {
        // JPA가 자동으로 insert쿼리 만들어서 실행
        em.persist(member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        Member member = em.find(Member.class, id);
        return Optional.ofNullable(member);
    }

    @Override
    public Optional<Member> findByName(String name) {
        // pk가 아닌 조건을 붙여 조회하는 경우, jpql을 작성
        return em.createQuery("select m from Member m where m.name = :name", Member.class)
                .setParameter("name", name)
                .getResultList().stream().findAny();
    }

    @Override
    public List<Member> findAll() {
        // JPQL
        // table 대상으로 쿼리를 날라는 것이 아니라, 객체 대상으로 쿼리 날리면 sql로 변환됨
        return em.createQuery("select m from Member m", Member.class)
                .getResultList();
    }
}
