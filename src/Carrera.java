import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Carrera extends JFrame {

    // interfaz gráfica y la gestion de eventos

    private boolean carreraEnCurso = false; // Controla si la carrera está activa
    private int corredoresFinalizados = 0; // Contador de corredores que terminan
    private JButton iniciarCarrera; // Boton para iniciar la carrera

    private JButton Salir; //Boton para salir del programa

    public Carrera() {
        super("Carrera de Corredores");
        setSize(600, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(null);

        // Labels para los corredores y sus posiciones
        JLabel corredor1 = crearLabelCorredor(50, 50);
        JLabel corredor2 = crearLabelCorredor(50, 100);
        JLabel corredor3 = crearLabelCorredor(50, 150);
        JLabel corredor4 = crearLabelCorredor(50, 200);

        JLabel c1Pos = crearLabelPosicion(350, 50);
        JLabel c2Pos = crearLabelPosicion(350, 100);
        JLabel c3Pos = crearLabelPosicion(350, 150);
        JLabel c4Pos = crearLabelPosicion(350, 200);

        //icono del

        // Botón para iniciar la carrera
        iniciarCarrera = new JButton("Iniciar Carrera");
        iniciarCarrera.setBounds(100, 350, 150, 50);



        iniciarCarrera.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (!carreraEnCurso) { // Evita iniciar múltiples carreras
                    carreraEnCurso = true;
                    corredoresFinalizados = 0;
                    iniciarCarrera.setEnabled(false);

                    // Inicializar hilos de los corredores
                    new HilosCorredores("Corredor 1", corredor1, c1Pos, Carrera.this);
                    new HilosCorredores("Corredor 2", corredor2, c2Pos, Carrera.this);
                    new HilosCorredores("Corredor 3", corredor3, c3Pos, Carrera.this);
                    new HilosCorredores("Corredor 4", corredor4, c4Pos, Carrera.this);
                }
            }
        });


        Salir = new JButton("Salir");
        Salir.setBounds(350, 350, 150, 50);
        //listener para salit del prpgrama
        Salir.addActionListener(e -> System.exit(0));



        // Agregar elementos al panel
        panel.add(corredor1);
        panel.add(c1Pos);
        panel.add(corredor2);
        panel.add(c2Pos);
        panel.add(corredor3);
        panel.add(c3Pos);
        panel.add(corredor4);
        panel.add(c4Pos);
        panel.add(iniciarCarrera);
        panel.add(Salir);

        add(panel);
        setVisible(true);
    }

    // Método sincronizado para notificar cuando un corredor termina
    public synchronized void corredorTermino() {
        corredoresFinalizados++;
        if (corredoresFinalizados == 4) { // Cuando todos terminan
            carreraEnCurso = false;
            SwingUtilities.invokeLater(() -> iniciarCarrera.setEnabled(true));
        }
    }

    // Método para crear el JLabel de un corredor
    private JLabel crearLabelCorredor(int x, int y) {
        ImageIcon iconoCorredor = new ImageIcon(
                new ImageIcon("src/imagenes/Corredor.png").getImage()
                        .getScaledInstance(50, 50, Image.SCALE_DEFAULT)
        );
        JLabel label = new JLabel();
        label.setIcon(iconoCorredor);
        label.setBounds(x, y, 50, 50);
        return label;
    }

    // Método para crear el JLabel de la posición
    private JLabel crearLabelPosicion(int x, int y) {
        JLabel label = new JLabel();
        label.setBounds(x, y, 200, 50);
        return label;
    }

}
