public class java_test {
    public static boolean sleepIn(boolean weekday, boolean vacation) {
        return (!weekday || vacation);
    }

    public static void main(String[] args) {
        Boolean A = true;
        Boolean B = true;
        Boolean C = false;
        Boolean D = false;
        System.out.println(sleepIn(D, B));
    }
}
