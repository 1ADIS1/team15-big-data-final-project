// ORM class for table 'car_description'
// WARNING: This class is AUTO-GENERATED. Modify at your own risk.
//
// Debug information:
// Generated date: Tue May 07 22:25:25 MSK 2024
// For connector: org.apache.sqoop.manager.PostgresqlManager
import org.apache.hadoop.io.BytesWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.Writable;
import org.apache.hadoop.mapred.lib.db.DBWritable;
import org.apache.sqoop.lib.JdbcWritableBridge;
import org.apache.sqoop.lib.DelimiterSet;
import org.apache.sqoop.lib.FieldFormatter;
import org.apache.sqoop.lib.RecordParser;
import org.apache.sqoop.lib.BooleanParser;
import org.apache.sqoop.lib.BlobRef;
import org.apache.sqoop.lib.ClobRef;
import org.apache.sqoop.lib.LargeObjectLoader;
import org.apache.sqoop.lib.SqoopRecord;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.io.DataInput;
import java.io.DataOutput;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.sql.Date;
import java.sql.Time;
import java.sql.Timestamp;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class car_description extends SqoopRecord  implements DBWritable, Writable {
  private final int PROTOCOL_VERSION = 3;
  public int getClassFormatVersion() { return PROTOCOL_VERSION; }
  public static interface FieldSetterCommand {    void setField(Object value);  }  protected ResultSet __cur_result_set;
  private Map<String, FieldSetterCommand> setters = new HashMap<String, FieldSetterCommand>();
  private void init0() {
    setters.put("entry_id", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.entry_id = (Long)value;
      }
    });
    setters.put("region_url", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.region_url = (String)value;
      }
    });
    setters.put("price", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.price = (Long)value;
      }
    });
    setters.put("manufactured_year", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.manufactured_year = (Integer)value;
      }
    });
    setters.put("manufacturer", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.manufacturer = (String)value;
      }
    });
    setters.put("car_condition", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.car_condition = (String)value;
      }
    });
    setters.put("cylinders", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.cylinders = (String)value;
      }
    });
    setters.put("fuel", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.fuel = (String)value;
      }
    });
    setters.put("odometer", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.odometer = (Integer)value;
      }
    });
    setters.put("transmission", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.transmission = (String)value;
      }
    });
    setters.put("car_drive", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.car_drive = (String)value;
      }
    });
    setters.put("car_size", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.car_size = (String)value;
      }
    });
    setters.put("car_type", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.car_type = (String)value;
      }
    });
    setters.put("paint_color", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.paint_color = (String)value;
      }
    });
    setters.put("us_state", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.us_state = (String)value;
      }
    });
    setters.put("latitude", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.latitude = (Float)value;
      }
    });
    setters.put("longitude", new FieldSetterCommand() {
      @Override
      public void setField(Object value) {
        car_description.this.longitude = (Float)value;
      }
    });
  }
  public car_description() {
    init0();
  }
  private Long entry_id;
  public Long get_entry_id() {
    return entry_id;
  }
  public void set_entry_id(Long entry_id) {
    this.entry_id = entry_id;
  }
  public car_description with_entry_id(Long entry_id) {
    this.entry_id = entry_id;
    return this;
  }
  private String region_url;
  public String get_region_url() {
    return region_url;
  }
  public void set_region_url(String region_url) {
    this.region_url = region_url;
  }
  public car_description with_region_url(String region_url) {
    this.region_url = region_url;
    return this;
  }
  private Long price;
  public Long get_price() {
    return price;
  }
  public void set_price(Long price) {
    this.price = price;
  }
  public car_description with_price(Long price) {
    this.price = price;
    return this;
  }
  private Integer manufactured_year;
  public Integer get_manufactured_year() {
    return manufactured_year;
  }
  public void set_manufactured_year(Integer manufactured_year) {
    this.manufactured_year = manufactured_year;
  }
  public car_description with_manufactured_year(Integer manufactured_year) {
    this.manufactured_year = manufactured_year;
    return this;
  }
  private String manufacturer;
  public String get_manufacturer() {
    return manufacturer;
  }
  public void set_manufacturer(String manufacturer) {
    this.manufacturer = manufacturer;
  }
  public car_description with_manufacturer(String manufacturer) {
    this.manufacturer = manufacturer;
    return this;
  }
  private String car_condition;
  public String get_car_condition() {
    return car_condition;
  }
  public void set_car_condition(String car_condition) {
    this.car_condition = car_condition;
  }
  public car_description with_car_condition(String car_condition) {
    this.car_condition = car_condition;
    return this;
  }
  private String cylinders;
  public String get_cylinders() {
    return cylinders;
  }
  public void set_cylinders(String cylinders) {
    this.cylinders = cylinders;
  }
  public car_description with_cylinders(String cylinders) {
    this.cylinders = cylinders;
    return this;
  }
  private String fuel;
  public String get_fuel() {
    return fuel;
  }
  public void set_fuel(String fuel) {
    this.fuel = fuel;
  }
  public car_description with_fuel(String fuel) {
    this.fuel = fuel;
    return this;
  }
  private Integer odometer;
  public Integer get_odometer() {
    return odometer;
  }
  public void set_odometer(Integer odometer) {
    this.odometer = odometer;
  }
  public car_description with_odometer(Integer odometer) {
    this.odometer = odometer;
    return this;
  }
  private String transmission;
  public String get_transmission() {
    return transmission;
  }
  public void set_transmission(String transmission) {
    this.transmission = transmission;
  }
  public car_description with_transmission(String transmission) {
    this.transmission = transmission;
    return this;
  }
  private String car_drive;
  public String get_car_drive() {
    return car_drive;
  }
  public void set_car_drive(String car_drive) {
    this.car_drive = car_drive;
  }
  public car_description with_car_drive(String car_drive) {
    this.car_drive = car_drive;
    return this;
  }
  private String car_size;
  public String get_car_size() {
    return car_size;
  }
  public void set_car_size(String car_size) {
    this.car_size = car_size;
  }
  public car_description with_car_size(String car_size) {
    this.car_size = car_size;
    return this;
  }
  private String car_type;
  public String get_car_type() {
    return car_type;
  }
  public void set_car_type(String car_type) {
    this.car_type = car_type;
  }
  public car_description with_car_type(String car_type) {
    this.car_type = car_type;
    return this;
  }
  private String paint_color;
  public String get_paint_color() {
    return paint_color;
  }
  public void set_paint_color(String paint_color) {
    this.paint_color = paint_color;
  }
  public car_description with_paint_color(String paint_color) {
    this.paint_color = paint_color;
    return this;
  }
  private String us_state;
  public String get_us_state() {
    return us_state;
  }
  public void set_us_state(String us_state) {
    this.us_state = us_state;
  }
  public car_description with_us_state(String us_state) {
    this.us_state = us_state;
    return this;
  }
  private Float latitude;
  public Float get_latitude() {
    return latitude;
  }
  public void set_latitude(Float latitude) {
    this.latitude = latitude;
  }
  public car_description with_latitude(Float latitude) {
    this.latitude = latitude;
    return this;
  }
  private Float longitude;
  public Float get_longitude() {
    return longitude;
  }
  public void set_longitude(Float longitude) {
    this.longitude = longitude;
  }
  public car_description with_longitude(Float longitude) {
    this.longitude = longitude;
    return this;
  }
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof car_description)) {
      return false;
    }
    car_description that = (car_description) o;
    boolean equal = true;
    equal = equal && (this.entry_id == null ? that.entry_id == null : this.entry_id.equals(that.entry_id));
    equal = equal && (this.region_url == null ? that.region_url == null : this.region_url.equals(that.region_url));
    equal = equal && (this.price == null ? that.price == null : this.price.equals(that.price));
    equal = equal && (this.manufactured_year == null ? that.manufactured_year == null : this.manufactured_year.equals(that.manufactured_year));
    equal = equal && (this.manufacturer == null ? that.manufacturer == null : this.manufacturer.equals(that.manufacturer));
    equal = equal && (this.car_condition == null ? that.car_condition == null : this.car_condition.equals(that.car_condition));
    equal = equal && (this.cylinders == null ? that.cylinders == null : this.cylinders.equals(that.cylinders));
    equal = equal && (this.fuel == null ? that.fuel == null : this.fuel.equals(that.fuel));
    equal = equal && (this.odometer == null ? that.odometer == null : this.odometer.equals(that.odometer));
    equal = equal && (this.transmission == null ? that.transmission == null : this.transmission.equals(that.transmission));
    equal = equal && (this.car_drive == null ? that.car_drive == null : this.car_drive.equals(that.car_drive));
    equal = equal && (this.car_size == null ? that.car_size == null : this.car_size.equals(that.car_size));
    equal = equal && (this.car_type == null ? that.car_type == null : this.car_type.equals(that.car_type));
    equal = equal && (this.paint_color == null ? that.paint_color == null : this.paint_color.equals(that.paint_color));
    equal = equal && (this.us_state == null ? that.us_state == null : this.us_state.equals(that.us_state));
    equal = equal && (this.latitude == null ? that.latitude == null : this.latitude.equals(that.latitude));
    equal = equal && (this.longitude == null ? that.longitude == null : this.longitude.equals(that.longitude));
    return equal;
  }
  public boolean equals0(Object o) {
    if (this == o) {
      return true;
    }
    if (!(o instanceof car_description)) {
      return false;
    }
    car_description that = (car_description) o;
    boolean equal = true;
    equal = equal && (this.entry_id == null ? that.entry_id == null : this.entry_id.equals(that.entry_id));
    equal = equal && (this.region_url == null ? that.region_url == null : this.region_url.equals(that.region_url));
    equal = equal && (this.price == null ? that.price == null : this.price.equals(that.price));
    equal = equal && (this.manufactured_year == null ? that.manufactured_year == null : this.manufactured_year.equals(that.manufactured_year));
    equal = equal && (this.manufacturer == null ? that.manufacturer == null : this.manufacturer.equals(that.manufacturer));
    equal = equal && (this.car_condition == null ? that.car_condition == null : this.car_condition.equals(that.car_condition));
    equal = equal && (this.cylinders == null ? that.cylinders == null : this.cylinders.equals(that.cylinders));
    equal = equal && (this.fuel == null ? that.fuel == null : this.fuel.equals(that.fuel));
    equal = equal && (this.odometer == null ? that.odometer == null : this.odometer.equals(that.odometer));
    equal = equal && (this.transmission == null ? that.transmission == null : this.transmission.equals(that.transmission));
    equal = equal && (this.car_drive == null ? that.car_drive == null : this.car_drive.equals(that.car_drive));
    equal = equal && (this.car_size == null ? that.car_size == null : this.car_size.equals(that.car_size));
    equal = equal && (this.car_type == null ? that.car_type == null : this.car_type.equals(that.car_type));
    equal = equal && (this.paint_color == null ? that.paint_color == null : this.paint_color.equals(that.paint_color));
    equal = equal && (this.us_state == null ? that.us_state == null : this.us_state.equals(that.us_state));
    equal = equal && (this.latitude == null ? that.latitude == null : this.latitude.equals(that.latitude));
    equal = equal && (this.longitude == null ? that.longitude == null : this.longitude.equals(that.longitude));
    return equal;
  }
  public void readFields(ResultSet __dbResults) throws SQLException {
    this.__cur_result_set = __dbResults;
    this.entry_id = JdbcWritableBridge.readLong(1, __dbResults);
    this.region_url = JdbcWritableBridge.readString(2, __dbResults);
    this.price = JdbcWritableBridge.readLong(3, __dbResults);
    this.manufactured_year = JdbcWritableBridge.readInteger(4, __dbResults);
    this.manufacturer = JdbcWritableBridge.readString(5, __dbResults);
    this.car_condition = JdbcWritableBridge.readString(6, __dbResults);
    this.cylinders = JdbcWritableBridge.readString(7, __dbResults);
    this.fuel = JdbcWritableBridge.readString(8, __dbResults);
    this.odometer = JdbcWritableBridge.readInteger(9, __dbResults);
    this.transmission = JdbcWritableBridge.readString(10, __dbResults);
    this.car_drive = JdbcWritableBridge.readString(11, __dbResults);
    this.car_size = JdbcWritableBridge.readString(12, __dbResults);
    this.car_type = JdbcWritableBridge.readString(13, __dbResults);
    this.paint_color = JdbcWritableBridge.readString(14, __dbResults);
    this.us_state = JdbcWritableBridge.readString(15, __dbResults);
    this.latitude = JdbcWritableBridge.readFloat(16, __dbResults);
    this.longitude = JdbcWritableBridge.readFloat(17, __dbResults);
  }
  public void readFields0(ResultSet __dbResults) throws SQLException {
    this.entry_id = JdbcWritableBridge.readLong(1, __dbResults);
    this.region_url = JdbcWritableBridge.readString(2, __dbResults);
    this.price = JdbcWritableBridge.readLong(3, __dbResults);
    this.manufactured_year = JdbcWritableBridge.readInteger(4, __dbResults);
    this.manufacturer = JdbcWritableBridge.readString(5, __dbResults);
    this.car_condition = JdbcWritableBridge.readString(6, __dbResults);
    this.cylinders = JdbcWritableBridge.readString(7, __dbResults);
    this.fuel = JdbcWritableBridge.readString(8, __dbResults);
    this.odometer = JdbcWritableBridge.readInteger(9, __dbResults);
    this.transmission = JdbcWritableBridge.readString(10, __dbResults);
    this.car_drive = JdbcWritableBridge.readString(11, __dbResults);
    this.car_size = JdbcWritableBridge.readString(12, __dbResults);
    this.car_type = JdbcWritableBridge.readString(13, __dbResults);
    this.paint_color = JdbcWritableBridge.readString(14, __dbResults);
    this.us_state = JdbcWritableBridge.readString(15, __dbResults);
    this.latitude = JdbcWritableBridge.readFloat(16, __dbResults);
    this.longitude = JdbcWritableBridge.readFloat(17, __dbResults);
  }
  public void loadLargeObjects(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void loadLargeObjects0(LargeObjectLoader __loader)
      throws SQLException, IOException, InterruptedException {
  }
  public void write(PreparedStatement __dbStmt) throws SQLException {
    write(__dbStmt, 0);
  }

  public int write(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeLong(entry_id, 1 + __off, -5, __dbStmt);
    JdbcWritableBridge.writeString(region_url, 2 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeLong(price, 3 + __off, -5, __dbStmt);
    JdbcWritableBridge.writeInteger(manufactured_year, 4 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeString(manufacturer, 5 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(car_condition, 6 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(cylinders, 7 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(fuel, 8 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeInteger(odometer, 9 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeString(transmission, 10 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(car_drive, 11 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(car_size, 12 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(car_type, 13 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(paint_color, 14 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(us_state, 15 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeFloat(latitude, 16 + __off, 7, __dbStmt);
    JdbcWritableBridge.writeFloat(longitude, 17 + __off, 7, __dbStmt);
    return 17;
  }
  public void write0(PreparedStatement __dbStmt, int __off) throws SQLException {
    JdbcWritableBridge.writeLong(entry_id, 1 + __off, -5, __dbStmt);
    JdbcWritableBridge.writeString(region_url, 2 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeLong(price, 3 + __off, -5, __dbStmt);
    JdbcWritableBridge.writeInteger(manufactured_year, 4 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeString(manufacturer, 5 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(car_condition, 6 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(cylinders, 7 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(fuel, 8 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeInteger(odometer, 9 + __off, 4, __dbStmt);
    JdbcWritableBridge.writeString(transmission, 10 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(car_drive, 11 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(car_size, 12 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(car_type, 13 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(paint_color, 14 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeString(us_state, 15 + __off, 12, __dbStmt);
    JdbcWritableBridge.writeFloat(latitude, 16 + __off, 7, __dbStmt);
    JdbcWritableBridge.writeFloat(longitude, 17 + __off, 7, __dbStmt);
  }
  public void readFields(DataInput __dataIn) throws IOException {
this.readFields0(__dataIn);  }
  public void readFields0(DataInput __dataIn) throws IOException {
    if (__dataIn.readBoolean()) { 
        this.entry_id = null;
    } else {
    this.entry_id = Long.valueOf(__dataIn.readLong());
    }
    if (__dataIn.readBoolean()) { 
        this.region_url = null;
    } else {
    this.region_url = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.price = null;
    } else {
    this.price = Long.valueOf(__dataIn.readLong());
    }
    if (__dataIn.readBoolean()) { 
        this.manufactured_year = null;
    } else {
    this.manufactured_year = Integer.valueOf(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.manufacturer = null;
    } else {
    this.manufacturer = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.car_condition = null;
    } else {
    this.car_condition = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.cylinders = null;
    } else {
    this.cylinders = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.fuel = null;
    } else {
    this.fuel = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.odometer = null;
    } else {
    this.odometer = Integer.valueOf(__dataIn.readInt());
    }
    if (__dataIn.readBoolean()) { 
        this.transmission = null;
    } else {
    this.transmission = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.car_drive = null;
    } else {
    this.car_drive = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.car_size = null;
    } else {
    this.car_size = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.car_type = null;
    } else {
    this.car_type = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.paint_color = null;
    } else {
    this.paint_color = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.us_state = null;
    } else {
    this.us_state = Text.readString(__dataIn);
    }
    if (__dataIn.readBoolean()) { 
        this.latitude = null;
    } else {
    this.latitude = Float.valueOf(__dataIn.readFloat());
    }
    if (__dataIn.readBoolean()) { 
        this.longitude = null;
    } else {
    this.longitude = Float.valueOf(__dataIn.readFloat());
    }
  }
  public void write(DataOutput __dataOut) throws IOException {
    if (null == this.entry_id) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.entry_id);
    }
    if (null == this.region_url) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, region_url);
    }
    if (null == this.price) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.price);
    }
    if (null == this.manufactured_year) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.manufactured_year);
    }
    if (null == this.manufacturer) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, manufacturer);
    }
    if (null == this.car_condition) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, car_condition);
    }
    if (null == this.cylinders) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, cylinders);
    }
    if (null == this.fuel) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, fuel);
    }
    if (null == this.odometer) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.odometer);
    }
    if (null == this.transmission) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, transmission);
    }
    if (null == this.car_drive) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, car_drive);
    }
    if (null == this.car_size) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, car_size);
    }
    if (null == this.car_type) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, car_type);
    }
    if (null == this.paint_color) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, paint_color);
    }
    if (null == this.us_state) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, us_state);
    }
    if (null == this.latitude) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeFloat(this.latitude);
    }
    if (null == this.longitude) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeFloat(this.longitude);
    }
  }
  public void write0(DataOutput __dataOut) throws IOException {
    if (null == this.entry_id) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.entry_id);
    }
    if (null == this.region_url) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, region_url);
    }
    if (null == this.price) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeLong(this.price);
    }
    if (null == this.manufactured_year) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.manufactured_year);
    }
    if (null == this.manufacturer) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, manufacturer);
    }
    if (null == this.car_condition) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, car_condition);
    }
    if (null == this.cylinders) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, cylinders);
    }
    if (null == this.fuel) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, fuel);
    }
    if (null == this.odometer) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeInt(this.odometer);
    }
    if (null == this.transmission) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, transmission);
    }
    if (null == this.car_drive) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, car_drive);
    }
    if (null == this.car_size) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, car_size);
    }
    if (null == this.car_type) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, car_type);
    }
    if (null == this.paint_color) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, paint_color);
    }
    if (null == this.us_state) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    Text.writeString(__dataOut, us_state);
    }
    if (null == this.latitude) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeFloat(this.latitude);
    }
    if (null == this.longitude) { 
        __dataOut.writeBoolean(true);
    } else {
        __dataOut.writeBoolean(false);
    __dataOut.writeFloat(this.longitude);
    }
  }
  private static final DelimiterSet __outputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  public String toString() {
    return toString(__outputDelimiters, true);
  }
  public String toString(DelimiterSet delimiters) {
    return toString(delimiters, true);
  }
  public String toString(boolean useRecordDelim) {
    return toString(__outputDelimiters, useRecordDelim);
  }
  public String toString(DelimiterSet delimiters, boolean useRecordDelim) {
    StringBuilder __sb = new StringBuilder();
    char fieldDelim = delimiters.getFieldsTerminatedBy();
    __sb.append(FieldFormatter.escapeAndEnclose(entry_id==null?"null":"" + entry_id, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(region_url==null?"null":region_url, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(price==null?"null":"" + price, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(manufactured_year==null?"null":"" + manufactured_year, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(manufacturer==null?"null":manufacturer, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(car_condition==null?"null":car_condition, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(cylinders==null?"null":cylinders, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(fuel==null?"null":fuel, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(odometer==null?"null":"" + odometer, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(transmission==null?"null":transmission, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(car_drive==null?"null":car_drive, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(car_size==null?"null":car_size, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(car_type==null?"null":car_type, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(paint_color==null?"null":paint_color, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(us_state==null?"null":us_state, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(latitude==null?"null":"" + latitude, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(longitude==null?"null":"" + longitude, delimiters));
    if (useRecordDelim) {
      __sb.append(delimiters.getLinesTerminatedBy());
    }
    return __sb.toString();
  }
  public void toString0(DelimiterSet delimiters, StringBuilder __sb, char fieldDelim) {
    __sb.append(FieldFormatter.escapeAndEnclose(entry_id==null?"null":"" + entry_id, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(region_url==null?"null":region_url, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(price==null?"null":"" + price, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(manufactured_year==null?"null":"" + manufactured_year, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(manufacturer==null?"null":manufacturer, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(car_condition==null?"null":car_condition, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(cylinders==null?"null":cylinders, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(fuel==null?"null":fuel, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(odometer==null?"null":"" + odometer, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(transmission==null?"null":transmission, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(car_drive==null?"null":car_drive, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(car_size==null?"null":car_size, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(car_type==null?"null":car_type, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(paint_color==null?"null":paint_color, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(us_state==null?"null":us_state, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(latitude==null?"null":"" + latitude, delimiters));
    __sb.append(fieldDelim);
    __sb.append(FieldFormatter.escapeAndEnclose(longitude==null?"null":"" + longitude, delimiters));
  }
  private static final DelimiterSet __inputDelimiters = new DelimiterSet((char) 44, (char) 10, (char) 0, (char) 0, false);
  private RecordParser __parser;
  public void parse(Text __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharSequence __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(byte [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(char [] __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(ByteBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  public void parse(CharBuffer __record) throws RecordParser.ParseError {
    if (null == this.__parser) {
      this.__parser = new RecordParser(__inputDelimiters);
    }
    List<String> __fields = this.__parser.parseRecord(__record);
    __loadFromFields(__fields);
  }

  private void __loadFromFields(List<String> fields) {
    Iterator<String> __it = fields.listIterator();
    String __cur_str = null;
    try {
    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.entry_id = null; } else {
      this.entry_id = Long.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.region_url = null; } else {
      this.region_url = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.price = null; } else {
      this.price = Long.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.manufactured_year = null; } else {
      this.manufactured_year = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.manufacturer = null; } else {
      this.manufacturer = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.car_condition = null; } else {
      this.car_condition = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.cylinders = null; } else {
      this.cylinders = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.fuel = null; } else {
      this.fuel = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.odometer = null; } else {
      this.odometer = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.transmission = null; } else {
      this.transmission = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.car_drive = null; } else {
      this.car_drive = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.car_size = null; } else {
      this.car_size = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.car_type = null; } else {
      this.car_type = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.paint_color = null; } else {
      this.paint_color = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.us_state = null; } else {
      this.us_state = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.latitude = null; } else {
      this.latitude = Float.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.longitude = null; } else {
      this.longitude = Float.valueOf(__cur_str);
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  private void __loadFromFields0(Iterator<String> __it) {
    String __cur_str = null;
    try {
    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.entry_id = null; } else {
      this.entry_id = Long.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.region_url = null; } else {
      this.region_url = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.price = null; } else {
      this.price = Long.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.manufactured_year = null; } else {
      this.manufactured_year = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.manufacturer = null; } else {
      this.manufacturer = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.car_condition = null; } else {
      this.car_condition = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.cylinders = null; } else {
      this.cylinders = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.fuel = null; } else {
      this.fuel = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.odometer = null; } else {
      this.odometer = Integer.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.transmission = null; } else {
      this.transmission = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.car_drive = null; } else {
      this.car_drive = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.car_size = null; } else {
      this.car_size = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.car_type = null; } else {
      this.car_type = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.paint_color = null; } else {
      this.paint_color = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null")) { this.us_state = null; } else {
      this.us_state = __cur_str;
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.latitude = null; } else {
      this.latitude = Float.valueOf(__cur_str);
    }

    if (__it.hasNext()) {
        __cur_str = __it.next();
    } else {
        __cur_str = "null";
    }
    if (__cur_str.equals("null") || __cur_str.length() == 0) { this.longitude = null; } else {
      this.longitude = Float.valueOf(__cur_str);
    }

    } catch (RuntimeException e) {    throw new RuntimeException("Can't parse input data: '" + __cur_str + "'", e);    }  }

  public Object clone() throws CloneNotSupportedException {
    car_description o = (car_description) super.clone();
    return o;
  }

  public void clone0(car_description o) throws CloneNotSupportedException {
  }

  public Map<String, Object> getFieldMap() {
    Map<String, Object> __sqoop$field_map = new HashMap<String, Object>();
    __sqoop$field_map.put("entry_id", this.entry_id);
    __sqoop$field_map.put("region_url", this.region_url);
    __sqoop$field_map.put("price", this.price);
    __sqoop$field_map.put("manufactured_year", this.manufactured_year);
    __sqoop$field_map.put("manufacturer", this.manufacturer);
    __sqoop$field_map.put("car_condition", this.car_condition);
    __sqoop$field_map.put("cylinders", this.cylinders);
    __sqoop$field_map.put("fuel", this.fuel);
    __sqoop$field_map.put("odometer", this.odometer);
    __sqoop$field_map.put("transmission", this.transmission);
    __sqoop$field_map.put("car_drive", this.car_drive);
    __sqoop$field_map.put("car_size", this.car_size);
    __sqoop$field_map.put("car_type", this.car_type);
    __sqoop$field_map.put("paint_color", this.paint_color);
    __sqoop$field_map.put("us_state", this.us_state);
    __sqoop$field_map.put("latitude", this.latitude);
    __sqoop$field_map.put("longitude", this.longitude);
    return __sqoop$field_map;
  }

  public void getFieldMap0(Map<String, Object> __sqoop$field_map) {
    __sqoop$field_map.put("entry_id", this.entry_id);
    __sqoop$field_map.put("region_url", this.region_url);
    __sqoop$field_map.put("price", this.price);
    __sqoop$field_map.put("manufactured_year", this.manufactured_year);
    __sqoop$field_map.put("manufacturer", this.manufacturer);
    __sqoop$field_map.put("car_condition", this.car_condition);
    __sqoop$field_map.put("cylinders", this.cylinders);
    __sqoop$field_map.put("fuel", this.fuel);
    __sqoop$field_map.put("odometer", this.odometer);
    __sqoop$field_map.put("transmission", this.transmission);
    __sqoop$field_map.put("car_drive", this.car_drive);
    __sqoop$field_map.put("car_size", this.car_size);
    __sqoop$field_map.put("car_type", this.car_type);
    __sqoop$field_map.put("paint_color", this.paint_color);
    __sqoop$field_map.put("us_state", this.us_state);
    __sqoop$field_map.put("latitude", this.latitude);
    __sqoop$field_map.put("longitude", this.longitude);
  }

  public void setField(String __fieldName, Object __fieldVal) {
    if (!setters.containsKey(__fieldName)) {
      throw new RuntimeException("No such field:"+__fieldName);
    }
    setters.get(__fieldName).setField(__fieldVal);
  }

}
