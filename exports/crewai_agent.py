from crewai import Agent

rl_robotic_arm_kinematic_calibrator = Agent(
    role="Rl Robotic Arm Kinematic Calibrator",
    goal="Deliver high-precision autonomous Rl Robotic Arm Kinematic Calibrator operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
