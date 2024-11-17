def attack_techniques(**kwargs):
    for name, attack in kwargs.items():
        print(f"This is an attack i would like to practice:=> {attack}")

attack_techniques(arm_attack="kimura", leg_attack="straight_ankle_log", neck_attack="arm_triangle", body_attack="charge")


