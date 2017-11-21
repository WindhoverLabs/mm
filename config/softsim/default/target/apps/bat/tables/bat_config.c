/*
** Pragmas
*/

/*
** Include Files
*/
#include "cfe_tbl_filedef.h"
#include "bat_tbldefs.h"

/*
** Local Defines
*/

/*
** Local Structure Declarations
*/
static CFE_TBL_FileDef_t CFE_TBL_FileDef =
{
    /* Content format: ObjName[64], TblName[38], Desc[32], TgtFileName[20], ObjSize
    **    ObjName - variable name of config table, e.g., CI_ConfigDefTbl[]
    **    TblName - app's table name, e.g., CI.CONFIG_TBL, where CI is the same app name
    **              used in cfe_es_startup.scr, and CI_defConfigTbl is the same table
    **              name passed in to CFE_TBL_Register()
    **    Desc - description of table in string format
    **    TgtFileName[20] - table file name, compiled as .tbl file extension
    **    ObjSize - size of the entire table
    */

    "BAT_ConfigTbl", "BAT.CONFIG_TBL", "BAT default config table",
    "bat_config.tbl", (sizeof(BAT_ConfigTbl_t))
};

/*
** External Global Variables
*/

/*
** Global Variables
*/

/* Default MPC config table data */
BAT_ConfigTbl_t BAT_ConfigTbl =
{
	/* V_EMPTY       */  18.0f,
	/* V_CHARGED     */  24.0f,
	/* N_CELLS       */  6,
	/* CAPACITY      */  0.0f,
	/* V_LOAD_DROP   */  0.0f,
	/* R_INTERNAL    */  0.0f,
	/* LOW_THR       */  22.0f,
	/* CRIT_THR      */  20.0f,
	/* EMERGEN_THR   */  19.0f,
	/* Voltage Scale */  1.0f,
	/* Current Scale */  1.0f,
};

/*
** Local Variables
*/

/*
** Function Prototypes
*/

/*
** Function Definitions
*/

/*=======================================================================================
** End of file bat_config.c
**=====================================================================================*/
    
