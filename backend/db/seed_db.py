from main import engine
from models import (
    Crop,
    Device,
    Farm,
    Harvest,
    Role,
    Sensor,
    SensorCalibration,
    SensorInfo,
    SensorReading,
    SensorType,
    Tenant,
    User,
)
from seed_data import (
    crops,
    devices,
    farms,
    harvests,
    roles,
    sensor_calibrations,
    sensor_info,
    sensor_readings,
    sensor_types,
    sensors,
    tenants,
    users,
)

from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker


def seed_db(engine: Engine) -> None:
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Populate Tenants table
        for tenant in tenants:
            session.add(Tenant(id=tenant["id"], name=tenant["name"]))

        # Populate Roles table
        for role in roles:
            session.add(Role(id=role["id"], name=role["name"]))

        # Populate Users table
        for user in users:
            session.add(
                User(
                    id=user["id"],
                    first_name=user["first_name"],
                    last_name=user["last_name"],
                    tenant_id=user["tenant_id"],
                    role_id=user["role_id"],
                )
            )

        # Populate Farms table
        for farm in farms:
            session.add(
                Farm(
                    id=farm["id"],
                    name=farm["name"],
                    tenant_id=farm["tenant_id"],
                )
            )

        # Populate Crops table
        for crop in crops:
            session.add(
                Crop(
                    id=crop["id"],
                    name=crop["name"],
                    farm_id=crop["farm_id"],
                )
            )

        # Populate Harvests table
        for harvest in harvests:
            session.add(
                Harvest(
                    id=harvest["id"],
                    date=harvest["date"],
                    yield_weight=harvest["yield_weight"],
                    crop_id=harvest["crop_id"],
                )
            )

        # Populate Devices table
        for device in devices:
            session.add(
                Device(
                    id=device["id"],
                    name=device["name"],
                    crop_id=device["crop_id"],
                )
            )

        # Populate SensorTypes table
        for sensor_type in sensor_types:
            session.add(
                SensorType(
                    id=sensor_type["id"],
                    name=sensor_type["name"],
                    unit=sensor_type["unit"],
                )
            )

        # Populate SensorInfo table
        for sensor_entry in sensor_info:
            session.add(
                SensorInfo(
                    id=sensor_entry["id"],
                    name=sensor_entry["name"],
                    manufacturer=sensor_entry["manufacturer"],
                    model_number=sensor_entry["model_number"],
                    sensor_type_id=sensor_entry["sensor_type_id"],
                )
            )

        # Populate Sensors table
        for sensor in sensors:
            session.add(
                Sensor(
                    id=sensor["id"],
                    name=sensor["name"],
                    device_id=sensor["device_id"],
                    sensor_info_id=sensor["sensor_info_id"],
                )
            )

        # Populate SensorCalibrations table
        for sensor_calibration in sensor_calibrations:
            session.add(
                SensorCalibration(
                    id=sensor_calibration["id"],
                    date=sensor_calibration["date"],
                    calibration_pass=sensor_calibration["calibration_pass"],
                    sensor_id=sensor_calibration["sensor_id"],
                )
            )

        # Populate SensorReadings table
        for sensor_reading in sensor_readings:
            session.add(
                SensorReading(
                    id=sensor_reading["id"],
                    date=sensor_reading["date"],
                    value=sensor_reading["value"],
                    sensor_id=sensor_reading["sensor_id"],
                )
            )

        # Dry run before committing changes to the database
        session.flush()

        # Commit changes to the database and close the session
        session.commit()
        session.close()

    except Exception:
        session.rollback()
        raise

    print("#" * 80)
    print("Database seeded successfully!")
    print("#" * 80)

    return None


if __name__ == "__main__":
    seed_db(engine)
