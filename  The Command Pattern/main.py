from commands import LightOnCommand, LightOffCommand, FanOnCommand, FanOffCommand, StereoOnWithCD, StereoOffCommand, FancyFanHighCommand, FancyFanLowCommand
from receivers import Light, Fan, Stereo, FancyFan
from remote_control import RemoteControl

# Remote Controller -> Invoker
# Light/Fan/Stereo/FancyFan -> Receivers
# LightOnCommand/FanOffCommand/StereoOffCommand/FancyFanHighCommand -> Concrete Commands
# main function -> Client

# The command object is responsible for decoupling the invoker (the one that makes some request) and the Receivers (the
# one that actually performs the request made). Analogous to the "Waitress" in the hotel b/w client and cook.

# A command object encapsulates a request to do something (like turning on a light) on a specific object (say, the living
# room light object). So, if we store a command object for each button, when the button is pressed, we ask the command
# object to do some work. The remote does not have any idea what the work is, it just has a command object that knows
# how to talk to the right object to get the work done. So, you see, the remote is decoupled from the light object!


# main function to check out the implementation of our remote controller
def main():
    # create our remote controller object
    remote_controller = RemoteControl()

    # create different devices(receivers) that we will be using
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    ceiling_fan = Fan("Ceiling")
    stereo = Stereo("Living Room")
    fancy_fan = FancyFan("Drawing Room")

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

    # create fancy fan command objects
    fancy_fan_high = FancyFanHighCommand(fancy_fan)
    fancy_fan_low = FancyFanLowCommand(fancy_fan)

    # set the commands for remote controller
    remote_controller.set_command(0, living_room_light_on, living_room_light_off)
    remote_controller.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_controller.set_command(2, ceiling_fan_on, ceiling_fan_off)
    remote_controller.set_command(3, stereo_on_with_cd, stereo_off)
    remote_controller.set_command(4, fancy_fan_high, fancy_fan_low)

    # now let's press the on and off buttons of the remote controller to see its behavior
    remote_controller.on_button_pushed(0)
    remote_controller.off_button_pushed(0)
    remote_controller.undo_button_pushed()  # undoing the light off action
    remote_controller.on_button_pushed(1)
    remote_controller.off_button_pushed(1)
    remote_controller.on_button_pushed(2)
    remote_controller.off_button_pushed(2)
    remote_controller.on_button_pushed(3)
    remote_controller.off_button_pushed(3)
    remote_controller.undo_button_pushed()  # undoing the stereo off action

    # checking the working of undo operation on the fancy fan
    remote_controller.on_button_pushed(4)
    remote_controller.off_button_pushed(4)
    remote_controller.undo_button_pushed()


if __name__ == "__main__":
    main()