import java.util.ArrayList;

public class bhargavpractice {
   
    public static void main(String[] args){
  ArrayList<String> s = new ArrayList<>();
  
  for(int i=1;i<=100;i++){
s.add(Integer.toString(i));
  }
int i=3;
    while (i<=100){
        s.set(i-1,"Buzz");
        i+=3;
    }
    i=5;
    while (i<=100){
        s.set(i-1,"Fizz");
        i+=5;
    }
    i=15;
    while (i<=100){
        s.set(i-1,"FizzBuzz");
        i+=15;
    }
    System.out.println(s);
  }
   
        

}

