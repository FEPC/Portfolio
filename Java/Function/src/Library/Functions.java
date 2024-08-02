package Library;

public class Functions {
	public static double power(double b, byte e) {
		double r = 1;
		for (byte i = 1; i <= e; i++) {
			r *= b;
		}
		return r;
	}
	public static double factorial(byte f) {
		double r = 1;
		for (byte i = f; i > 0; i--) {
			r *= i;
		}
		return r;
	}
	public static double squareRoot(short a){
		double r=a;
		double t=0;
		while(t!=r){
			t=r;
			r=((a/r)+r)/2;
		}
 		return r;
	}
	public static double absoluteValue(double a){
		double r=0;
        if (a<0){
        	r=-a;
        }else{
        	r=a;
        }
 		return r;
	}
	public static double naturalLogarithm(short v) {
		double r = 1;
		double s;
		for (byte i = 1; i <=50; i++) {
			s=(v-1);
			r=((Functions.power(s, i))/(i))*(Functions.power(-1, (byte)(i+1)));
		}
		return r;
	}

	public final static double PI() {
		return 3.141596;
	}
    public final static double e(){
    	double r=0;
    	for(byte i=0;i<10;i++){
    		r +=1/(Functions.factorial(i));
    	}
    	return r;
    }
	public static double sine(short g) {
		double r;
		byte a;
		double ra;
		ra = g * Functions.PI();
		ra = ra / 180;
		r=ra;
		for (byte i = 1; i <=50; i++) {
			a = (byte) (2*i+1);
			r +=((Functions.power(-1, i))*(Functions.power(ra, a)))/(Functions.factorial(a));			
		}
		return r;
	}
	public static double cosine(short g) {
		double r;
		byte a;
		double ra;
		ra = g * Functions.PI();
		ra = ra / 180;
		r=1;
		for (byte i = 1; i <=50; i++) {
			a = (byte) (2*i);
			r +=((Functions.power(-1, i))*(Functions.power(ra, a)))/(Functions.factorial(a));			
		}
		return r;
	}
	public static double tangent(short g){
		double r;
		r=(Functions.sine((short)g))/(Functions.cosine(g));
		return r;
	}
	public static double cotangent(short g){
		double r;
		r=(Functions.cosine((short)g))/(Functions.sine(g));
		return r;
	}
	public static double secant(short g){
		double r;
		r=1/(Functions.cosine(g));
		return r;
	}
	public static double cosecant(short g){
		double r;
		r=1/(Functions.sine(g));
		return r;
	}
	public static double arcsine(double v) {
		double r;
		byte a;
		byte b;
		double c;
		double d;
		r=v;
		for (byte i = 1; i <=50; i++) {
			a = (byte) (2*i+1);
			b = (byte) (2*i);
			c = (Functions.power(4, i));
			d = (Functions.factorial(i));
			r +=(((Functions.factorial(b)))/((c)*(Functions.power(d, (byte)2))*(a)))*(Functions.power(v, a));
		}
		r=(r*180)/Functions.PI();
		return r;
	}
	public static double arccosine(double v) {
		double r;
		byte a;
		byte b;
		double c;
		double d;
		r=v;
		for (byte i = 1; i <=50; i++) {
			a = (byte) (2*i+1);
			b = (byte) (2*i);
			c = (Functions.power(4, i));
			d = (Functions.factorial(i));
			r +=(((Functions.factorial(b)))/((c)*(Functions.power(d, (byte)2))*(a)))*(Functions.power(v, a));
		}
		r=((Functions.PI())/2)-r;
		r=(r*180)/Functions.PI();
		return r;
	}
	public static double arctangent(double v){
		double r;
		r=(Functions.arcsine((short)v))/(Functions.arccosine(v));
		return r;
	}
	public static double arcotangent(double v){
		double r;
		r=(Functions.arccosine((short)v))/(Functions.arcsine(v));
		return r;
	}
	public static double arcosecant(double v){
		double r;
		r=1/(Functions.arccosine(v));
		return r;
	}
	public static double arcocosecant(double v){
		double r;
		r=1/(Functions.arcsine(v));
		return r;
	}
	public static double hyperbolicBreast(byte v) {
		double r=0;
        double a;
        double b;
        a=(Functions.power(Functions.e(), v));
        b=1/(Functions.power(Functions.e(), v));
        r=(a-b)/2;
		return r;
	}
	public static double hyperbolicCosine(byte v) {
		double r=0;
        double a;
        double b;
        a=(Functions.power(Functions.e(), v));
        b=1/(Functions.power(Functions.e(), v));
        r=(a+b)/2;
		return r;
	}
	public static double hyperbolicTangent(byte v){
		double r;
		r=(Functions.hyperbolicBreast(v))/(Functions.hyperbolicCosine(v));
		return r;
	}
	public static double hyperbolicCotangent(byte v){
		double r;
		r=(Functions.hyperbolicCosine(v))/(Functions.hyperbolicBreast(v));
		return r;
	}
	public static double hyperbolicSecant(byte v){
		double r;
		r=1/(Functions.hyperbolicCosine(v));
		return r;
	}
	public static double hyperbolicCosecant(byte v){
		double r;
		r=1/(Functions.hyperbolicBreast(v));
		return r;
	}
}

