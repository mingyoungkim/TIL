package hello.core.singleton;

public class SingletonService {
    // 자기 자신을 내부의 private static 으로 생성 (즉, class 레벨에 올라가기 때문에 딱 하나만 존재하게 됨)
    // JVM 자바가 딱 뜰때, SingletonService static 영역에 new 를 보고 내부적으로 실행해서
    // 해당 객체를 생성해서 instance 에 참조를 넣어둠
    private static final SingletonService instance = new SingletonService();
    // 그러면 조회할때, getInstance 를 쓰면 됨
    public static SingletonService getInstance() {
        return instance;
    }
    // 외부에서 new SingletonService() 로 객체생성 남발을 방지하기 위해 private 으로 설정
    private SingletonService() {
    }
    public void logic() {
        System.out.println("싱글톤 로직을 호출했음");
    }
}
