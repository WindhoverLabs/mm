/* Automatically generated nanopb header */
/* Generated by nanopb-0.3.6 at Wed Oct 26 00:46:12 2016. */

#ifndef PB_HIL_SENSOR_PB_H_INCLUDED
#define PB_HIL_SENSOR_PB_H_INCLUDED
#include <pb.h>

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _px4_hil_sensor_pb_MAGNETOMETER_MODE {
    px4_hil_sensor_pb_MAGNETOMETER_MODE_MAGNETOMETER_MODE_NORMAL = 0,
    px4_hil_sensor_pb_MAGNETOMETER_MODE_MAGNETOMETER_MODE_POSITIVE_BIAS = 1,
    px4_hil_sensor_pb_MAGNETOMETER_MODE_MAGNETOMETER_MODE_NEGATIVE_BIAS = 2
} px4_hil_sensor_pb_MAGNETOMETER_MODE;
#define _px4_hil_sensor_pb_MAGNETOMETER_MODE_MIN px4_hil_sensor_pb_MAGNETOMETER_MODE_MAGNETOMETER_MODE_NORMAL
#define _px4_hil_sensor_pb_MAGNETOMETER_MODE_MAX px4_hil_sensor_pb_MAGNETOMETER_MODE_MAGNETOMETER_MODE_NEGATIVE_BIAS
#define _px4_hil_sensor_pb_MAGNETOMETER_MODE_ARRAYSIZE ((px4_hil_sensor_pb_MAGNETOMETER_MODE)(px4_hil_sensor_pb_MAGNETOMETER_MODE_MAGNETOMETER_MODE_NEGATIVE_BIAS+1))

/* Struct definitions */
typedef struct _px4_hil_sensor_pb {
    uint64_t timestamp;
    uint64_t accelerometer_timestamp;
    uint64_t magnetometer_timestamp;
    uint64_t gyro1_timestamp;
    uint64_t accelerometer1_timestamp;
    uint64_t magnetometer1_timestamp;
    uint64_t gyro2_timestamp;
    uint64_t accelerometer2_timestamp;
    uint64_t magnetometer2_timestamp;
    uint64_t baro_timestamp;
    uint64_t baro1_timestamp;
    uint64_t differential_pressure_timestamp;
    uint64_t differential_pressure1_timestamp;
    pb_size_t gyro_rad_s_count;
    float gyro_rad_s[3];
    uint32_t gyro_errcount;
    float gyro_temp;
    pb_size_t accelerometer_m_s2_count;
    float accelerometer_m_s2[3];
    float accelerometer_range_m_s2;
    uint32_t accelerometer_errcount;
    float accelerometer_temp;
    pb_size_t magnetometer_ga_count;
    float magnetometer_ga[3];
    float magnetometer_range_ga;
    float magnetometer_cuttoff_freq_hz;
    uint32_t magnetometer_errcount;
    float magnetometer_temp;
    pb_size_t gyro1_rad_s_count;
    float gyro1_rad_s[3];
    uint32_t gyro1_errcount;
    float gyro1_temp;
    pb_size_t accelerometer1_m_s2_count;
    float accelerometer1_m_s2[3];
    uint32_t accelerometer1_errcount;
    float accelerometer1_temp;
    pb_size_t magnetometer1_ga_count;
    float magnetometer1_ga[3];
    uint32_t magnetometer1_errcount;
    float magnetometer1_temp;
    pb_size_t gyro2_rad_s_count;
    float gyro2_rad_s[3];
    uint32_t gyro2_errcount;
    float gyro2_temp;
    pb_size_t accelerometer2_m_s2_count;
    float accelerometer2_m_s2[3];
    uint32_t accelerometer2_errcount;
    float accelerometer2_temp;
    pb_size_t magnetometer2_ga_count;
    float magnetometer2_ga[3];
    uint32_t magnetometer2_errcount;
    float magnetometer2_temp;
    float baro_pres_mbar;
    float baro_alt_meter;
    float baro_temp_celcius;
    float baro1_pres_mbar;
    float baro1_alt_meter;
    float baro1_temp_celcius;
    pb_size_t adc_voltage_v_count;
    float adc_voltage_v[10];
    float mcu_temp_celcius;
    float differential_pressure_pa;
    float differential_pressure_filtered_pa;
    float differential_pressure1_pa;
    float differential_pressure1_filtered_pa;
    pb_size_t gyro_raw_count;
    int32_t gyro_raw[3];
    pb_size_t accelerometer_raw_count;
    int32_t accelerometer_raw[3];
    int32_t accelerometer_mode;
    pb_size_t magnetometer_raw_count;
    int32_t magnetometer_raw[3];
    int32_t magnetometer_mode;
    pb_size_t gyro1_raw_count;
    int32_t gyro1_raw[3];
    pb_size_t accelerometer1_raw_count;
    int32_t accelerometer1_raw[3];
    pb_size_t magnetometer1_raw_count;
    int32_t magnetometer1_raw[3];
    pb_size_t gyro2_raw_count;
    int32_t gyro2_raw[3];
    pb_size_t accelerometer2_raw_count;
    int32_t accelerometer2_raw[3];
    pb_size_t magnetometer2_raw_count;
    int32_t magnetometer2_raw[3];
    pb_size_t adc_mapping_count;
    uint32_t adc_mapping[10];
/* @@protoc_insertion_point(struct:px4_hil_sensor_pb) */
} px4_hil_sensor_pb;

/* Default values for struct fields */

/* Initializer values for message structs */
#define px4_hil_sensor_pb_init_default           {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {0, 0, 0}, 0, 0, 0, {0, 0, 0}, 0, 0, 0, 0, {0, 0, 0}, 0, 0, 0, 0, 0, {0, 0, 0}, 0, 0, 0, {0, 0, 0}, 0, 0, 0, {0, 0, 0}, 0, 0, 0, {0, 0, 0}, 0, 0, 0, {0, 0, 0}, 0, 0, 0, {0, 0, 0}, 0, 0, 0, 0, 0, 0, 0, 0, 0, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, 0, 0, 0, 0, 0, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, 0, {0, 0, 0}, 0, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}}
#define px4_hil_sensor_pb_init_zero              {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, {0, 0, 0}, 0, 0, 0, {0, 0, 0}, 0, 0, 0, 0, {0, 0, 0}, 0, 0, 0, 0, 0, {0, 0, 0}, 0, 0, 0, {0, 0, 0}, 0, 0, 0, {0, 0, 0}, 0, 0, 0, {0, 0, 0}, 0, 0, 0, {0, 0, 0}, 0, 0, 0, {0, 0, 0}, 0, 0, 0, 0, 0, 0, 0, 0, 0, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, 0, 0, 0, 0, 0, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, 0, {0, 0, 0}, 0, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, {0, 0, 0}, 0, {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}}

/* Field tags (for use in manual encoding/decoding) */
#define px4_hil_sensor_pb_timestamp_tag          1
#define px4_hil_sensor_pb_accelerometer_timestamp_tag 2
#define px4_hil_sensor_pb_magnetometer_timestamp_tag 3
#define px4_hil_sensor_pb_gyro1_timestamp_tag    4
#define px4_hil_sensor_pb_accelerometer1_timestamp_tag 5
#define px4_hil_sensor_pb_magnetometer1_timestamp_tag 6
#define px4_hil_sensor_pb_gyro2_timestamp_tag    7
#define px4_hil_sensor_pb_accelerometer2_timestamp_tag 8
#define px4_hil_sensor_pb_magnetometer2_timestamp_tag 9
#define px4_hil_sensor_pb_baro_timestamp_tag     10
#define px4_hil_sensor_pb_baro1_timestamp_tag    11
#define px4_hil_sensor_pb_differential_pressure_timestamp_tag 12
#define px4_hil_sensor_pb_differential_pressure1_timestamp_tag 13
#define px4_hil_sensor_pb_gyro_rad_s_tag         14
#define px4_hil_sensor_pb_gyro_errcount_tag      15
#define px4_hil_sensor_pb_gyro_temp_tag          16
#define px4_hil_sensor_pb_accelerometer_m_s2_tag 17
#define px4_hil_sensor_pb_accelerometer_range_m_s2_tag 18
#define px4_hil_sensor_pb_accelerometer_errcount_tag 19
#define px4_hil_sensor_pb_accelerometer_temp_tag 20
#define px4_hil_sensor_pb_magnetometer_ga_tag    21
#define px4_hil_sensor_pb_magnetometer_range_ga_tag 22
#define px4_hil_sensor_pb_magnetometer_cuttoff_freq_hz_tag 23
#define px4_hil_sensor_pb_magnetometer_errcount_tag 24
#define px4_hil_sensor_pb_magnetometer_temp_tag  25
#define px4_hil_sensor_pb_gyro1_rad_s_tag        26
#define px4_hil_sensor_pb_gyro1_errcount_tag     27
#define px4_hil_sensor_pb_gyro1_temp_tag         28
#define px4_hil_sensor_pb_accelerometer1_m_s2_tag 29
#define px4_hil_sensor_pb_accelerometer1_errcount_tag 30
#define px4_hil_sensor_pb_accelerometer1_temp_tag 31
#define px4_hil_sensor_pb_magnetometer1_ga_tag   32
#define px4_hil_sensor_pb_magnetometer1_errcount_tag 33
#define px4_hil_sensor_pb_magnetometer1_temp_tag 34
#define px4_hil_sensor_pb_gyro2_rad_s_tag        35
#define px4_hil_sensor_pb_gyro2_errcount_tag     36
#define px4_hil_sensor_pb_gyro2_temp_tag         37
#define px4_hil_sensor_pb_accelerometer2_m_s2_tag 38
#define px4_hil_sensor_pb_accelerometer2_errcount_tag 39
#define px4_hil_sensor_pb_accelerometer2_temp_tag 40
#define px4_hil_sensor_pb_magnetometer2_ga_tag   41
#define px4_hil_sensor_pb_magnetometer2_errcount_tag 42
#define px4_hil_sensor_pb_magnetometer2_temp_tag 43
#define px4_hil_sensor_pb_baro_pres_mbar_tag     44
#define px4_hil_sensor_pb_baro_alt_meter_tag     45
#define px4_hil_sensor_pb_baro_temp_celcius_tag  46
#define px4_hil_sensor_pb_baro1_pres_mbar_tag    47
#define px4_hil_sensor_pb_baro1_alt_meter_tag    48
#define px4_hil_sensor_pb_baro1_temp_celcius_tag 49
#define px4_hil_sensor_pb_adc_voltage_v_tag      50
#define px4_hil_sensor_pb_mcu_temp_celcius_tag   51
#define px4_hil_sensor_pb_differential_pressure_pa_tag 52
#define px4_hil_sensor_pb_differential_pressure_filtered_pa_tag 53
#define px4_hil_sensor_pb_differential_pressure1_pa_tag 54
#define px4_hil_sensor_pb_differential_pressure1_filtered_pa_tag 55
#define px4_hil_sensor_pb_gyro_raw_tag           56
#define px4_hil_sensor_pb_accelerometer_raw_tag  57
#define px4_hil_sensor_pb_accelerometer_mode_tag 58
#define px4_hil_sensor_pb_magnetometer_raw_tag   59
#define px4_hil_sensor_pb_magnetometer_mode_tag  60
#define px4_hil_sensor_pb_gyro1_raw_tag          61
#define px4_hil_sensor_pb_accelerometer1_raw_tag 62
#define px4_hil_sensor_pb_magnetometer1_raw_tag  63
#define px4_hil_sensor_pb_gyro2_raw_tag          64
#define px4_hil_sensor_pb_accelerometer2_raw_tag 65
#define px4_hil_sensor_pb_magnetometer2_raw_tag  66
#define px4_hil_sensor_pb_adc_mapping_tag        67

/* Struct field encoding specification for nanopb */
extern const pb_field_t px4_hil_sensor_pb_fields[68];

/* Maximum encoded size of messages (where known) */
#define px4_hil_sensor_pb_size                   980

/* Message IDs (where set with "msgid" option) */
#ifdef PB_MSGID

#define HIL_SENSOR_MESSAGES \


#endif

#ifdef __cplusplus
} /* extern "C" */
#endif
/* @@protoc_insertion_point(eof) */

#endif
