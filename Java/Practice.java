public class Practice {
    public static void main(String[] args) {
        System.out.print("Hello there");
        if (args.length > 0) {
            System.out.print(", " + args[0]);
        }
        System.out.println(".");
    }
}