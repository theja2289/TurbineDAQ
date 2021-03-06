REAL rpm, dur, tzero, tacc
global real data(3)(100)
global real start_time
global int collect_data
collect_data = 0

rpm = {rpm}
dur = {dur}

tacc = 2
tzero = 2.5

! Move turbine to zero if necessary
if RPOS(4) <> 60 & RPOS(4) <> 0
    ptp 4, 0
end

ACC(turbine) = rpm/tacc
DEC(turbine) = ACC(turbine)
VEL(turbine) = rpm
JERK(turbine) = ACC(turbine)*10

! Start controller data acquisition and send trigger pulse in same cycle
BLOCK
    ! Define start time from now
    start_time = TIME
    collect_data = 1
    DC/c data, 100, 1.0, TIME, FVEL(5), FVEL(4)
    ! Send trigger pulse for data acquisition
    OUT1.16 = 0
END

wait tzero*1000
jog/v turbine, rpm
WAIT dur*1000
HALT turbine
ptp/e turbine, 0
OUT1.16 = 1
STOPDC
collect_data = 0
STOP