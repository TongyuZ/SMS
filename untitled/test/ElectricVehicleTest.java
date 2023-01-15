import org.junit.Test;
import static org.junit.Assert.*;


public class ElectricVehicleTest {

    //    check if the mile is calculated correctly
    @Test
    public void range() {
        ElectricVehicle newCar = new ElectricVehicle("Ford", 175.0, 1.0, 5.5);
        assertEquals(675.0, newCar.range(),0.01);
    }


    //    check if the current efficiency is calculated correctly
    @Test
    public void updateEfficiency() {
        ElectricVehicle newCar = new ElectricVehicle("Ford", 175.0, 1.0, 5.5);
        newCar.updateEfficiency(15.0F);
        assertEquals(2.25F, newCar.getEfficiency(), 0.01);
    }

    //    check if the info is presented properly
    @Test
    public void testToString() {
        ElectricVehicle newCar = new ElectricVehicle("Ford", 175.0, 1.0, 5.5);
        assertTrue("Ford SOC: 100.0% Range (miles): 675.0".equals(newCar.toString()));
    }
}