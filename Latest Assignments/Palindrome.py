import java.util.Scanner;

public class palindrome {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter five digits: ");
        String number = input.nextLine();
              
        int reversed = 0;
        
        if (number.Length() == 5) {
            int numbers = Integer.parseInt(number);
            
            int original = number;
            
            while (number > 0) {
            int digit = number % 10;
            reversed = reversed * 10 + digit;
            number = number / 10;
        }

            if (original == reversed) {
            System.out.println(original + " is a palindrome");
        } else {
            System.out.println(original + " is not a palindrome");
        }
    }
}    
