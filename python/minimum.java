import java.util.Scanner;

class minimumGifts

{

public static void main(String args[])

{

 Scanner sc = new Scanner(System.in); //creating object for sccaner

 byte T=sc.nextByte();

 byte i=0,total,p,N,a,cu,pre;

 while(i<T)

 {

  total=1;

  p=1;

  N=sc.nextByte();

  pre=sc.nextByte();

  for(a=1;a<N;a++)

  {

   cu=sc.nextByte();

   if(cu>pre)

    p++;

   else

    p=1;

   total+=p;

   pre=cu;

  }

  System.out.println(total);

  i++;

 }

}

}