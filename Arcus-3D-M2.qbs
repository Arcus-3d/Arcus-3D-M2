import qbs

MachinekitApplication {
    name: "Arcus-3D-M1"
    halFiles: ["Arcus-3D-M1.hal",
               "velocity-extruding.hal"]
    configFiles: ["Arcus-3D-M1.ini"]
    bbioFiles: ["cramps_cape.bbio"]
    otherFiles: ["tool.tbl", "subroutines"]
    compFiles: []
    linuxcncIni: "Arcus-3D-M1.ini"
}
