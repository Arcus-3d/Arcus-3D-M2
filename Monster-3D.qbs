import qbs

MachinekitApplication {
    name: "Monster-3D"
    halFiles: ["monster.hal",
               "velocity-extruding.hal"]
    configFiles: ["monster.ini"]
    bbioFiles: ["cramps_cape.bbio"]
    otherFiles: ["tool.tbl", "subroutines"]
    compFiles: ["thermistor_check.comp"]
    linuxcncIni: "monster.ini"
    //display: "thinkpad.local:0.0"
}
