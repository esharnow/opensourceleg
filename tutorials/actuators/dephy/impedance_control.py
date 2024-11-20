import time

import numpy as np

import opensourceleg.actuators.dephy as Dephy
from opensourceleg.logging.logger import LOGGER
from opensourceleg.actuators.base import CONTROL_MODES

actpack = Dephy.DephyActuator(
    port="/dev/ttyACM0",
    gear_ratio=9.0,
)

with actpack:
    try:
        actpack.set_control_mode(mode=CONTROL_MODES.IMPEDANCE)
        actpack.set_control_mode(mode=CONTROL_MODES.IMPEDANCE)
        actpack.update()
        k = 0
        b = 0
        current_position = actpack.output_position
        while True:
            actpack.update()
            current_position = actpack.output_position
            actpack.set_impedance_gains(
                k=k,
                b=b,
                ff=128
            )
            actpack.set_motor_position(value=current_position)
            LOGGER.info(
                "".join(
                    f"Motor Position: {actpack.motor_position}\t"
                    + f"Motor Voltage: {actpack.motor_voltage}\t"
                    + f"Motor Current: {actpack.motor_current}\t"
                )
            )
            input("Changing motor's output position. Press Enter to continue...")
            actpack.set_motor_position(value=current_position + np.pi / 2)

            LOGGER.info(
                "".join(
                    f"Motor Position: {actpack.motor_position}\t"
                    + f"Motor Voltage: {actpack.motor_voltage}\t"
                    + f"Motor Current: {actpack.motor_current}\t"
                )
            )
            input("Increasing 'k' by 1. Press Enter to continue...")
            k += 0
            time.sleep(0.2)

    except KeyboardInterrupt:
        exit()
