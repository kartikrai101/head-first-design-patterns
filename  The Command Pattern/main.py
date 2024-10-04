from commands import LightOnCommand, LightOffCommand, FanOnCommand, FanOffCommand, StereoOnWithCD, StereoOffCommand
from receivers import Light, Fan, Stereo
from remote_control import RemoteControl


# main function to check out the implementation of our remote controller
def main():
    # create our remote controller object
    remote_controller = RemoteControl()

    # create different devices(receivers) that we will be using
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    ceiling_fan = Fan("Ceiling")
    stereo = Stereo("Living Room")

    # create light command objects
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    # create fan command objects
    ceiling_fan_on = FanOnCommand(ceiling_fan)
    ceiling_fan_off = FanOffCommand(ceiling_fan)

    # create stereo command objects
    stereo_on_with_cd = StereoOnWithCD(stereo)
    stereo_off = StereoOffCommand(stereo)

    # set the commands for remote controller
    remote_controller.set_command(0, living_room_light_on, living_room_light_off)
    remote_controller.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_controller.set_command(2, ceiling_fan_on, ceiling_fan_off)
    remote_controller.set_command(3, stereo_on_with_cd, stereo_off)

    # now let's press the on and off buttons of the remote controller to see its behavior
    remote_controller.on_button_pushed(0)
    remote_controller.off_button_pushed(0)
    remote_controller.on_button_pushed(1)
    remote_controller.off_button_pushed(1)
    remote_controller.on_button_pushed(2)
    remote_controller.off_button_pushed(2)
    remote_controller.on_button_pushed(3)
    remote_controller.off_button_pushed(3)


if __name__ == "__main__":
    main()