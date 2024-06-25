import datetime
from uuid import UUID

from typing import List
from typing import Optional

from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import REAL
from sqlalchemy import String
from sqlalchemy import UUID as sa_UUID
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


models: list = []


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Tenant(Base):
    __tablename__ = "Tenants"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=sa_UUID)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    address: Mapped[Optional[str]] = mapped_column(String(50))
    contact_email: Mapped[Optional[str]] = mapped_column(String(50))
    users: Mapped[Optional[List["User"]]] = relationship(
        back_populates="tenant", cascade="all, delete-orphan"
    )
    farms: Mapped[Optional[List["Farm"]]] = relationship(
        back_populates="tenant", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Tenant(id={self.id!r}, name={self.name!r}, address={self.address!r}, contact_email={self.contact_email!r})"


class User(Base):
    __tablename__ = "Users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=sa_UUID)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    middle_initial: Mapped[Optional[str]] = mapped_column(String(1), default=None)
    role_id: Mapped[int] = mapped_column(ForeignKey("Roles.id"), nullable=False)
    role: Mapped[List["Role"]] = relationship(back_populates="users")
    tenant_id: Mapped[int] = mapped_column(ForeignKey("Tenants.id"), nullable=False)
    tenant: Mapped[List["Tenant"]] = relationship(back_populates="users")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, middle_initial={self.middle_initial!r}, role_id={self.role_id!r}, tenant_id={self.tenant_id!r})"


class Role(Base):
    __tablename__ = "Roles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    users: Mapped[List["User"]] = relationship(back_populates="role")

    def __repr__(self) -> str:
        return f"Role(id={self.id!r}, name={self.name!r})"


class Farm(Base):
    __tablename__ = "Farms"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=sa_UUID)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    location: Mapped[Optional[str]] = mapped_column(String(50))
    tenant_id: Mapped[UUID] = mapped_column(ForeignKey("Tenants.id"), nullable=False)
    tenant: Mapped["Tenant"] = relationship(back_populates="farms")
    crops: Mapped[List["Crop"]] = relationship(back_populates="farm")

    def __repr__(self) -> str:
        return f"Farm(id={self.id!r}, name={self.name!r}, location={self.location!r}, tenant_id={self.tenant_id!r})"


class Crop(Base):
    __tablename__ = "Crops"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=sa_UUID)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    farm_id: Mapped[UUID] = mapped_column(ForeignKey("Farms.id"), nullable=False)
    farm: Mapped["Farm"] = relationship(back_populates="crops")
    harvests: Mapped[List["Harvest"]] = relationship(
        back_populates="crop", cascade="all, delete-orphan"
    )
    devices: Mapped[List["Device"]] = relationship(back_populates="crop")

    def __repr__(self) -> str:
        return f"Crop(id={self.id!r}, name={self.name!r}, farm_id={self.farm_id!r})"


class Harvest(Base):
    __tablename__ = "Harvests"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=sa_UUID)
    date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False), nullable=False)
    crop_id: Mapped[UUID] = mapped_column(ForeignKey("Crops.id"), nullable=False)
    crop: Mapped[List["Crop"]] = relationship(back_populates="harvests")
    yield_weight: Mapped[int] = mapped_column(Integer)  # in kg

    def __repr__(self) -> str:
        return f"Harvest(id={self.id!r}, date={self.date!r}, crop_id={self.crop_id!r}, yield_amount={self.yield_amount!r})"


class Device(Base):
    __tablename__ = "Devices"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=sa_UUID)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    crop_id: Mapped[Optional[UUID]] = mapped_column(ForeignKey("Crops.id"))
    crop: Mapped["Crop"] = relationship(back_populates="devices")
    sensors: Mapped[Optional[List["Sensor"]]] = relationship(back_populates="device")

    def __repr__(self) -> str:
        return f"Device(id={self.id!r}, name={self.name!r}, crop_id={self.crop_id!r})"


class SensorType(Base):
    __tablename__ = "SensorTypes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    unit: Mapped[str] = mapped_column(String(8), nullable=False)
    sensor_info: Mapped[List["SensorInfo"]] = relationship(back_populates="sensor_type")

    def __repr__(self) -> str:
        return f"SensorType(id={self.id!r}, name={self.name!r}, unit={self.unit!r})"


class SensorInfo(Base):
    __tablename__ = "SensorInfo"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=sa_UUID)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    manufacturer: Mapped[str] = mapped_column(String(50), nullable=False)
    model_number: Mapped[str] = mapped_column(String(50), nullable=False)
    sensor_type_id: Mapped[int] = mapped_column(ForeignKey("SensorTypes.id"))
    sensor_type: Mapped[List["SensorType"]] = relationship(back_populates="sensor_info")
    sensors: Mapped[List["Sensor"]] = relationship(back_populates="sensor_info")

    def __repr__(self) -> str:
        return f"SensorInfo(id={self.id!r}, name={self.name!r}, manufacturer={self.manufacturer!r}, model_number={self.model_number!r}, sensor_type_id={self.sensor_type_id!r})"


class Sensor(Base):
    __tablename__ = "Sensors"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=sa_UUID)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    device_id: Mapped[UUID] = mapped_column(ForeignKey("Devices.id"), nullable=False)
    device: Mapped[List["Device"]] = relationship(back_populates="sensors")
    sensor_info_id: Mapped[int] = mapped_column(ForeignKey("SensorInfo.id"), nullable=False)
    sensor_info: Mapped[List["SensorInfo"]] = relationship(back_populates="sensors")
    sensor_calibrations: Mapped[Optional[List["SensorCalibration"]]] = relationship(
        back_populates="sensor"
    )
    sensor_readings: Mapped[Optional[List["SensorReading"]]] = relationship(back_populates="sensor")

    def __repr__(self) -> str:
        return f"Sensor(id={self.id!r}, name={self.name!r}, device_id={self.device_id!r}, sensor_info_id={self.sensor_info_id!r})"


class SensorCalibration(Base):
    __tablename__ = "SensorCalibrations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False), nullable=False)
    calibration_pass: Mapped[bool] = mapped_column(default=False, nullable=False)
    sensor_id: Mapped[UUID] = mapped_column(ForeignKey("Sensors.id"), nullable=False)
    sensor: Mapped[List["Sensor"]] = relationship(back_populates="sensor_calibrations")

    def __repr__(self) -> str:
        return f"SensorCalibration(id={self.id!r}, date={self.date!r}, calibration_pass={self.calibration_pass!r}, sensor_id={self.sensor_id!r})"


class SensorReading(Base):
    __tablename__ = "SensorReadings"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=False), nullable=False)
    value: Mapped[int] = mapped_column(REAL, nullable=False)
    sensor_id: Mapped[UUID] = mapped_column(ForeignKey("Sensors.id"), nullable=False)
    sensor: Mapped[List["Sensor"]] = relationship(back_populates="sensor_readings")

    def __repr__(self) -> str:
        return f"SensorReading(id={self.id!r}, date={self.date!r}, value={self.value!r}, sensor_id={self.sensor_id!r})"
