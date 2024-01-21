package hello.hellospring.domain;

import jakarta.persistence.*;

// JDBC가 관리하는 Entity
@Entity
public class Member {
    // @Id : PK
    // IDENTITY : db에 값을 넣으면 자동으로 pk 인 id를 자동으로 생성
    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // db의 컬럼과 매핑
    @Column(name="name")
    private String name;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
