package Logic;

public class operations 
{
	//Global variables
	private String Numero,Numero2;
	private double n1,n2;
	
	//Default constructor method
	public operations(){}
	
	//Constructor method for base conversion
	public operations(String Numero){
	 this.Numero=Numero;
	}
	
	//Conversion to binary
	public String Binary(){
	 n1=Double.parseDouble(Numero);
	    Numero2=Integer.toBinaryString((int) n1);
	 return Numero2;
	}
	
	//Conversion to octal
	public String Octal(){
	 n1=Double.parseDouble(Numero);
	    Numero2=Integer.toOctalString((int) n1);
	 return Numero2;
	}
	
	//Conversion to decimal
	public String Decimal(){
	 Numero2=Numero;
	 return Numero2;
	}
	
	//Conversion to hexadecimal
	public String Hexadecimal(){
	 n1=Double.parseDouble(Numero);
	    Numero2=Integer.toHexString((int) n1);
	 return Numero2;
	}
	
	//Constructor method for operations
	public operations(String Numero,String Numero2){
	 this.Numero=Numero;
	 this.Numero2=Numero2;
	}
	
	//Methods to operate
	public String Add(){
	 n1=Double.parseDouble(Numero);
	 n2=Double.parseDouble(Numero2);
	 n2=n2+n1;
	 Numero2=String.valueOf(n2);
	 return Numero2;
	}
	public String Subtract(){
	 n1=Double.parseDouble(Numero);
	 n2=Double.parseDouble(Numero2);
	 n2=n2-n1;
	 Numero2=String.valueOf(n2);
	 return Numero2;
	}
	public String Multiply(){
	 n1=Double.parseDouble(Numero);
	 n2=Double.parseDouble(Numero2);
	 n2=n2*n1;
	 Numero2=String.valueOf(n2);
	 return Numero2;
	}
	public String Divide(){
	 n1=Double.parseDouble(Numero);
	 n2=Double.parseDouble(Numero2);
	 n2=n2/n1;
	 Numero2=String.valueOf(n2);
	 return Numero2;
	}
}