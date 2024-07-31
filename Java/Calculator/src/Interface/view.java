package Interface;

//Libraries
import java.awt.Image;
import java.awt.Toolkit;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

//Classes
import Logic.operations;

public class view extends JFrame {

	//Global variables
	private JPanel contentPanel;
	private JTextField display;
	private JButton ce;
	private JButton n1;
	private JButton n2;
	private JButton n3;
	private JButton n4;
	private JButton n5;
	private JButton n6;
	private JButton n7;
	private JButton n8;
	private JButton n9;
	private JButton n0;
	private JButton plus;
	private JButton minus;
	private JButton times;
	private JButton divided;
	private JButton point;
	private JButton equal;
	private JButton binary;
	private JButton octal;
	private JButton decimal;
	private JButton hexadecimal;
	String numberA="";
    String numberB="";
    String bases;
    int operation=0;
    operations operations;
    operations base;
		
	public view() {
		//Window settings
		setTitle("Calculadora");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(250,250,241,347);
		contentPanel= new JPanel();
		setContentPane(contentPanel);
		contentPanel.setLayout(null);
		
		//Icon
		Image icon = Toolkit.getDefaultToolkit().getImage("Calculadora.jpg");
	    setIconImage(icon);
	    setVisible(true);
	    
	    //Display settings
	    display=new JTextField();
	    display.setBounds(65, 11, 141, 26);
	    contentPanel.add(display);
	    
	    //Reset button
		ce=new JButton("C");
		ce.setFont(new Font("Arial", Font.PLAIN, 8));
		ce.setBounds(16, 11, 40, 26);
		contentPanel.add(ce);
		ce.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberA="";
				numberB="";
				display.setText(numberA);
			}
		});
	    
		//Numbers
	    n1=new JButton("1");
	    n1.setFont(new Font("Arial", Font.PLAIN, 10));
		n1.setBounds(16, 202, 40, 40);
		contentPanel.add(n1);
		n1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberA=numberA+"1";
				display.setText(numberA);
			}
		});
		n2=new JButton("2");
	    n2.setFont(new Font("Arial", Font.PLAIN, 10));
		n2.setBounds(66, 202, 40, 40);
		contentPanel.add(n2);
		n2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberA=numberA+"2";
				display.setText(numberA);
			}
		});
		n3=new JButton("3");
	    n3.setFont(new Font("Arial", Font.PLAIN, 10));
		n3.setBounds(116, 202, 40, 40);
		contentPanel.add(n3);
		n3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberA=numberA+"3";
				display.setText(numberA);
			}
		});
		n4=new JButton("4");
	    n4.setFont(new Font("Arial", Font.PLAIN, 10));
		n4.setBounds(16, 151, 40, 40);
		contentPanel.add(n4);
		n4.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberA=numberA+"4";
				display.setText(numberA);
			}
		});
		n5=new JButton("5"); 
	    n5.setFont(new Font("Arial", Font.PLAIN, 10));
		n5.setBounds(66, 151, 40, 40);
		contentPanel.add(n5);
		n5.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberA=numberA+"5";
				display.setText(numberA);
			}
		});
		n6=new JButton("6");
	    n6.setFont(new Font("Arial", Font.PLAIN, 10));
		n6.setBounds(116, 151, 40, 40);
		contentPanel.add(n6);
		n6.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberA=numberA+"6";
				display.setText(numberA);
			}
		});
		n7=new JButton("7");
	    n7.setFont(new Font("Arial", Font.PLAIN, 10));
		n7.setBounds(16, 99, 40, 40);
		contentPanel.add(n7);
		n7.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberA=numberA+"7";
				display.setText(numberA);
			}
		});
		n8=new JButton("8");
	    n8.setFont(new Font("Arial", Font.PLAIN, 10));
		n8.setBounds(66, 99, 40, 40);
		contentPanel.add(n8);
		n8.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberA=numberA+"8";
				display.setText(numberA);
			}
		});
		n9=new JButton("9");
	    n9.setFont(new Font("Arial", Font.PLAIN, 10));
		n9.setBounds(116, 99, 40, 40);
		contentPanel.add(n9);
		n9.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberA=numberA+"9";
				display.setText(numberA);
			}
		});
		n0=new JButton("0");
	    n0.setFont(new Font("Arial", Font.PLAIN, 10));
		n0.setBounds(66, 251, 40, 40);
		contentPanel.add(n0);
		n0.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberA=numberA+"0";
				display.setText(numberA);
			}
		});
		
		//Operation buttons
		plus=new JButton("+");
		plus.setFont(new Font("Arial", Font.PLAIN, 10));
		plus.setBounds(166, 251, 40, 40);
		contentPanel.add(plus);
		plus.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberB=numberA;
				numberA="";
				operation=1;
            }
		});
		minus=new JButton("-");
		minus.setFont(new Font("Arial", Font.PLAIN, 9));
		minus.setBounds(166, 202, 40, 40);
		contentPanel.add(minus);
		minus.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberB=numberA;
				numberA="";
				operation=2;
            }
		});
		times=new JButton("*");
		times.setFont(new Font("Arial", Font.PLAIN, 9));
		times.setBounds(166, 151, 40, 40);
		contentPanel.add(times);
		times.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberB=numberA;
				numberA="";
				operation=3;
            }
		});
		divided=new JButton("/");
		divided.setFont(new Font("Arial", Font.PLAIN, 9));
		divided.setBounds(166, 99, 40, 40);
		contentPanel.add(divided);
		divided.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberB=numberA;
				numberA="";
				operation=4;
            }
		});
		
		//Decimal point
		point=new JButton(".");
		point.setFont(new Font("Arial", Font.PLAIN, 9));
		point.setBounds(16, 251, 40, 40);
		contentPanel.add(point);
		point.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				numberA=numberA+".";
				display.setText(numberA);
			}
		});
		
		//Result button
		equal=new JButton("=");
		equal.setFont(new Font("Arial", Font.PLAIN, 9));
		equal.setBounds(116, 251, 40, 40);
		contentPanel.add(equal);
		equal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				operations=new operations(numberA,numberB);
				if (operation==1){
					numberA=operations.Add();
					display.setText(numberA);
				}
				if (operation==2){
					numberA=operations.Subtract();
					display.setText(numberA);
				}
				if (operation==3){
					numberA=operations.Multiply();
					display.setText(numberA);
				}
				if (operation==4){
					numberA=operations.Divide();
					display.setText(numberA);
				}
            }
		});
		
		//Base conversion button
		binary=new JButton("B");
		binary.setFont(new Font("Arial", Font.PLAIN, 9));
		binary.setBounds(16, 48, 40, 40);
		contentPanel.add(binary);
		binary.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				base=new operations(numberA);
				bases=base.Binary();
				display.setText(bases);
			}
		});
		octal=new JButton("O");
		octal.setFont(new Font("Arial", Font.PLAIN, 8));
		octal.setBounds(66, 48, 40, 40);
		contentPanel.add(octal);
		octal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				base=new operations(numberA);
				bases=base.Octal();
				display.setText(bases);
			}
		});
		decimal=new JButton("D");
		decimal.setFont(new Font("Arial", Font.PLAIN, 8));
		decimal.setBounds(116, 48, 40, 40);
		contentPanel.add(decimal);
		decimal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				base=new operations(numberA);
				bases=base.Decimal();
				display.setText(bases);
			}
		});
		hexadecimal=new JButton("H");
		hexadecimal.setFont(new Font("Arial", Font.PLAIN, 8));
		hexadecimal.setBounds(166, 48, 40, 40);
		contentPanel.add(hexadecimal);
		hexadecimal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				base=new operations(numberA);
				bases=base.Hexadecimal();
				display.setText(bases);
			}
		});
	}

}
