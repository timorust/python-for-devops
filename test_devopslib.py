from devopslib.randomskill import skill


def test_skill():
    skill_choice = skill()
    assert skill_choice in ["fullstack", "cyber", "devops"]
