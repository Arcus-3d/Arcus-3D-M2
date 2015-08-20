import qbs

MachinekitApplication {
    name: "Arcus-3D"
    halFiles: ["Arcus-3D.hal",
               "velocity-extruding.hal"]
    configFiles: ["Arcus-3D.ini"]
    bbioFiles: ["cramps_cape.bbio"]
    otherFiles: ["tool.tbl", "subroutines"]
    compFiles: ["thermistor_check.comp"]
    linuxcncIni: "Arcus-3D.ini"
    //display: "thinkpad.local:0.0"
}
