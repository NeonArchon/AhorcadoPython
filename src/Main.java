import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Main {

    public static void main(String[] args) {

        //llamar la interfaz al main
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new carrera();
            }
        });

    }

}

//clase de los hilos
class HilosCorredores implements Runnable{

    //atributos

    Thread t;
    String nombre; //Nombre del personaje
    JLabel Personaje; //La imagen del personaje
    JLabel Final; //la posicion del personaje

    public static int Posicion; //para guardar la posicion de lo spersonajes

    public HilosCorredores(String nombre, JLabel personaje, JLabel Final) {
        this.nombre = nombre;
        this.Personaje = personaje;
        this.Final = Final;
        t = new Thread(this, nombre);
        t.start();
    }

    @Override
    public void run() {

        int delay;

        try{
            Posicion = 1;
          delay = (int) (Math.random()*15) +1;
          Final.setVisible(false);
          Personaje.setVisible(true);
          for (int i=50; i<= 500; i++){
                Personaje.setLocation(i,Personaje.getY());
                Thread.sleep(delay);
            }
          Personaje.setVisible(false);
          Final.setVisible(true);
          Final.setText(nombre + "Ha llegado es el numero" + Posicion);
            Posicion++;

        }catch(Exception e){
            System.out.println(e.getMessage());
        }

        }

    }

class carrera extends JFrame{

    public carrera(){

        //Codigo de la Interfaz

        super("carrera ");
        JLabel Corredor1, Corredor2, Corredor3, Corredor4, C1Pos, C2Pos, C3Pos, C4Pos;
        JButton IniciarCarera;

        setSize(600,500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(null);

        //PLACEHLDER DE COREDORES CAMBIAR AL TERMINAR CODIGO Y CARGAR LAS VERSADERA IMAGENES
        //CORREDOR 1
        Image ImageCorredor = new ImageIcon("src/imagenes/Corredor.png").getImage();
        ImageIcon IconoCorredor = new ImageIcon(ImageCorredor.getScaledInstance(50,50,Image.SCALE_DEFAULT));
        Corredor1 = new JLabel();
        Corredor1.setIcon(IconoCorredor);
        Corredor1.setBounds(50,50,50,50);

        //CORREDOR 2
        Image ImageCorredor2 = new ImageIcon("src/imagenes/Corredor.png").getImage();
        ImageIcon IconoCorredor2 = new ImageIcon(ImageCorredor2.getScaledInstance(50,50,Image.SCALE_DEFAULT));
        Corredor2 = new JLabel();
        Corredor2.setIcon(IconoCorredor2);
        Corredor2.setBounds(50,100,50,50);

        //CORREDOR 3
        Image ImageCorredor3 = new ImageIcon("src/imagenes/Corredor.png").getImage();
        ImageIcon IconoCorredor3 = new ImageIcon(ImageCorredor3.getScaledInstance(50,50,Image.SCALE_DEFAULT));
        Corredor3 = new JLabel();
        Corredor3.setIcon(IconoCorredor3);
        Corredor3.setBounds(50,150,50,50);

        //CORREDOR 4
        Image ImageCorredor4 = new ImageIcon("src/imagenes/Corredor.png").getImage();
        ImageIcon IconoCorredor4 = new ImageIcon(ImageCorredor2.getScaledInstance(50,50,Image.SCALE_DEFAULT));
        Corredor4 = new JLabel();
        Corredor4.setIcon(IconoCorredor4);
        Corredor4.setBounds(50,200,50,50);

        //Posiciones (NOMBRES DE ATRIBUTOS CON PLACEHOLDERS DE MOMENTO+

        C1Pos = new JLabel();
        C1Pos.setBounds(50,50, 350,50);

        C2Pos = new JLabel();
        C2Pos.setBounds(50,100, 350,50);

        C3Pos = new JLabel();
        C3Pos.setBounds(50,200, 350,50);

        C4Pos = new JLabel();
        C4Pos.setBounds(50,250, 350,50);

        //Boton para iniciar la carrera

        IniciarCarera = new JButton("IniciarCarera");
        IniciarCarera.setBounds(150,300,150,50);

        IniciarCarera.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                    HilosCorredores ThreadC1 = new HilosCorredores("Corredor1", Corredor1, C1Pos);
                    HilosCorredores ThreadC2 = new HilosCorredores("Corredor2", Corredor2, C2Pos);
                    HilosCorredores ThreadC3 = new HilosCorredores("Corredor3", Corredor3, C3Pos);
                    HilosCorredores ThreadC4 = new HilosCorredores("Corredor4", Corredor4, C4Pos);
            }
        });



        //añadir elementos al label
        panel.add(Corredor1);
        panel.add(C1Pos);

        panel.add(Corredor2);
        panel.add(C2Pos);

        panel.add(Corredor3);
        panel.add(C3Pos);

        panel.add(Corredor4);
        panel.add(C4Pos);

        panel.add(IniciarCarera);

        add(panel);
        setVisible(true);

    }
}