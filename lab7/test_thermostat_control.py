from hypothesis import given, strategies as st
from thermostat_control import parse_setpoint, average_temperature, schedule_slot


@given(st.text() | st.none())
def test_parse_setpoint_no_crash(s):
    parse_setpoint(s)


@given(st.text() | st.none())
def test_average_temperature_no_crash(s):
    average_temperature(s)


@given(st.text() | st.none())
def test_schedule_slot_no_crash(s):
    schedule_slot(s)