/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:18 2016. */

#include "vtol_vehicle_status.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif



const pb_field_t px4_vtol_vehicle_status_pb_fields[7] = {
    PB_FIELD(  1, UINT64  , REQUIRED, STATIC  , FIRST, px4_vtol_vehicle_status_pb, timestamp, timestamp, 0),
    PB_FIELD(  2, FLOAT   , REQUIRED, STATIC  , OTHER, px4_vtol_vehicle_status_pb, airspeed_tot, timestamp, 0),
    PB_FIELD(  3, BOOL    , REQUIRED, STATIC  , OTHER, px4_vtol_vehicle_status_pb, vtol_in_rw_mode, airspeed_tot, 0),
    PB_FIELD(  4, BOOL    , REQUIRED, STATIC  , OTHER, px4_vtol_vehicle_status_pb, vtol_in_trans_mode, vtol_in_rw_mode, 0),
    PB_FIELD(  5, BOOL    , REQUIRED, STATIC  , OTHER, px4_vtol_vehicle_status_pb, vtol_transition_failsafe, vtol_in_trans_mode, 0),
    PB_FIELD(  6, BOOL    , REQUIRED, STATIC  , OTHER, px4_vtol_vehicle_status_pb, fw_permanent_stab, vtol_transition_failsafe, 0),
    PB_LAST_FIELD
};


/* @@protoc_insertion_point(eof) */
