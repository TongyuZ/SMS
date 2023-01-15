import java.text.DecimalFormat;

/** Create a class with 5 features which includes car name, battery size, state of charge,
 *  default efficiency and current efficiency.
 *  There are three methods inside the class, which separately calculates the miles,
 *  current efficiency and describe the basic information of the car.
 */
public class ElectricVehicle {
    private String name;
    private double batterySize;
    private double stateOfCharge;
    private double defaultEfficiency;

    //    constructor
    public ElectricVehicle(String name, double batterySize, double stateOfCharge, double defaultEfficiency) {
        if (batterySize > 150.0) {
            batterySize = 150.0;
        } else if (batterySize < 10.0) {
            batterySize = 10.0;
        }
        this.batterySize = batterySize;

        if (defaultEfficiency > 4.5) {
            defaultEfficiency = 4.5;
        } else if (defaultEfficiency < 0.5) {
            defaultEfficiency = 0.5;
        }
        this.defaultEfficiency = defaultEfficiency;

        if (name == null || name == "" || name.length() == 0) {
            name = "unknown EV";
        }
        this.name = name;

        if (stateOfCharge < 0.15) {
            stateOfCharge = 0.15;
        } else if (stateOfCharge > 1.0) {
            stateOfCharge = 1.0;
        }
        this.stateOfCharge = stateOfCharge;
    }

    // calculate miles in terms of 3 features
    public double range(){
        return stateOfCharge * batterySize * defaultEfficiency;
    }

    public void updateEfficiency(double currentTemp){
        if (currentTemp >= 65.0F && currentTemp <= 77.0){
            defaultEfficiency = 1.0 * defaultEfficiency;
        }
        if (currentTemp > 77.0F){
            defaultEfficiency = 0.85 * defaultEfficiency;
        }
        if (currentTemp < 65.0F){
            double dif = 65.0F - currentTemp;
            if (dif < 50.0F){
                defaultEfficiency = (1 - dif/ 100.0F) * defaultEfficiency;
            }
            else {
                defaultEfficiency = (1 - 50.0F/ 100.0F) * defaultEfficiency;
            }
        }
    }

    //    getters and setters
    public double getEfficiency(){
        return defaultEfficiency;
    }

    public double getBatterySize() {
        return batterySize;
    }

    public double getStateOfCharge() {
        return stateOfCharge;
    }
    public String getName(){
        return name;
    }

    public void setStateOfCharge(double stateOfCharge) {
        this.stateOfCharge = stateOfCharge;
    }

    //    present the info of a car
    @Override
    public String toString() {
        //name, state of charge, range
        DecimalFormat chargePer = new DecimalFormat(" #,##0.0%");
        String output = (name + " SOC:" + chargePer.format(stateOfCharge) + " Range (miles): " + range());
        return output;
    }
}
