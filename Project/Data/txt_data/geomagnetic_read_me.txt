Format description of the Kp_ap_Ap_SN_F107*.txt and Kp_ap_*.txt files
=====================================================================


License
-------
CC BY 4.0 except for the sunspot numbers contained in these files, which have the CC BY-NC 4.0 license.


Source
------
The source of these files is Geomagnetic Observatory Niemegk, GFZ German Research Centre for Geosciences, Potsdam, Germany. 
All files are available from:
ftp://ftp.gfz-potsdam.de/pub/home/obs/Kp_ap_Ap_SN_F107/
and the nowcast files are also available from:
http://www-app3.gfz-potsdam.de/kp_index/Kp_ap_Ap_SN_F107_nowcast.txt
http://www-app3.gfz-potsdam.de/kp_index/Kp_ap_nowcast.txt


Citation
-------- 
When using this data, please cite:
Matzka, J., Stolle, C., Yamazaki, Y., Bronkalla, O. and Morschhauser, A., 2021. The geomagnetic Kp index and derived indices of geomagnetic activity. Space Weather, https://doi.org/10.1029/2020SW002641


Important notes
---------------
This place is reserved for important notes to the users.
A change log for this format description and the data files is listed below.


Purpose and general features
============================
This distribution channel of Kp is meant to give experts and non-experts convenient access to Kp and other relevant indices. Latest nowcast and definitive values are used as they become available. The files contain the geomagnetic indices Kp, ap and Ap, the solar indices observed F10.7 (recommended for ionospheric and atmospheric studies), adjusted F10.7 (recommended for solar studies) and sunspot number (version 2.0 introduced in 2015). For more information on F10.7 see Tapping (2013) and on sunspot number see Clette and Lefevre (2016). 

The blank separated ASCII file with fixed format is easy to read in by code or as spreadsheets. The code for missing data is -1. Kp values are given as float with three decimals (e.g. 0.667 instead of 0.7 or 1-). Both the starting time and the mean time of the three-hourly intervals are given since the index represents geomagnetic disturbance over the full three-hour interval. Additionally, a linear time scale in days since January 1st 1932 and the Bartels rotations are given.

Versions with one line per day and with one line per three-hourly interval (only Kp, ap and Ap) are available.

The files containing all data since 1932 and the yearly files are updated daily, while a nowcast file is updated continuously during the day to support near real-time (NRT) operations. The Kp and sunspot number data is a combination of definitive data when available and nowcast data otherwise and regularly updated to replace nowcast with definitive values. For each data point, it is indicated if the values are nowcast or preliminary.


The Kp, ap, and Ap indices
--------------------------
The geomagnetic indices Kp, ap and Ap were introduced by Bartels (1949, 1957) and are produced by Geomagnetic Observatory Niemegk, GFZ German Research Centre for Geosciences. The values used here are a copy of the definitive values in https://doi.org/10.5880/Kp.0001 as soon as they are available. Before the definitive values become available, nowcast values are given.
Described in: Matzka et al., (2021a)
Data publication: Matzka et al., (2021b)


International Sunspot Number SN
-------------------------------
The international sunspot number SN (S_{N} or S subscript N) is given as the daily total sunspot number obtained from this source: http://www.sidc.be/silso/DATA/SN_d_tot_V2.0.txt, see http://www.sidc.be/silso/infosndtot,
which is version 2.0 introduced in 2015, see 
http://sidc.be/silso/newdataset
and Clette and Lefevre (2016) 
The most recent data is preliminary and we replace it by the definitive values as soon as they become available. 
The sunspot data is available under the license CC BY-NC 4.0 from WDC-SILSO, Royal Observatory of Belgium, Brussels


F10.7 Solar Radio Flux
----------------------
Local noon-time observed (F10.7obs) and adjusted (F10.7adj) solar radio flux F10.7 at 10.7 cm wavelength in s.f.u. (10^-22 W m^-2 Hz^-1) is provided by Dominion Radio Astrophysical Observatory and Natural Resources Canada, see Tapping (2013). For ionospheric and atmospheric studies we recommend F10.7obs. Data provided by Natural Resources Canada and regularly updated from: ftp://ftp.seismo.nrcan.gc.ca/spaceweather/solar_flux/daily_flux_values/fluxtable.txt 



Files with one line per day
===========================
Kp_ap_Ap_SN_F107*.txt files have one line per UT day and distribute the Kp, ap and Ap index as well as the solar indices SN and F10.7. The time stamp for each line is given as:
- year month day
- Days since 1932-01-01 to indicate the start of the UT day (00:00)
- Days since 1932-01-01 plus 0.5 to indicate the mid of the UT day (12:00)
- Bartels solar rotation number and number of UT day within this rotation

We provide one file that contains all index values since 1932-01-01 named:
Kp_ap_Ap_SN_F107_since_1932.txt,
which is updated daily.

We provide yearly files named, e.g., 
Kp_ap_Ap_SN_F107_2020.txt, 
which are updated daily.

We provide one nowcast file 
Kp_ap_Ap_SN_F107_nowcast.txt
with data for the previous and current day, which is constantly updated. 


FORMAT DESCRIPTION ('i' stands for integer, 'f' for float)
----------------------------------------------------------
40 header lines, starting with # and not more than 156 columns long

Each line with data is exactly 156 columns

YYYY (displayed in the header as #YYY)
iiii (displayed in the header as #iii)
Columns 1 to 4 
Year of date of the UT day, for which data is given in this line

MM 
ii 
Columns 6 to 7 
Month of date of UT day

DD
ii
Columns 9 to 10 
Day of date of UT day

days
iiiii
Columns 12 to 16
Days since 1932-01-01 00:00 UT to start of UT day

days_m
fffff.f
Columns 18 to 24
Days since 1932-01-01 00:00 UT to midday of UT day

BSR
iiii
Columns 26 to 29
Bartels solar rotation number is a sequence of periods of exactly 27.0 UT days counted continuously from February 8, 1832

dB
ii
Columns 31 to 32
Day number within the Bartels solar rotation

Kp (8 times)
ii.iii (8 times)
Columns 34 to 39, etc.
Planetary three-hour index Kp for each of the intervals 00:00 to 03:00, 03:00 to 06:00, 06:00 to 09:00, 09:00 to 12:00, 12:00 to 15:00, 15:00 to 18:00, 18:00 to 21:00, 21:00 to 24:00 of the UT day, index values are rounded to three digits after the decimal point (one thousandth) and two digits are reserved for the index value before the decimal point to make the format consistent with that of the Hpo indices 

ap (8 times)
iiii (8 times)
Columns 90 to 93, etc.
Three-hourly equivalent planetary amplitude ap for each of the intervals 00:00 to 03:00, 03:00 to 06:00, 06:00 to 09:00, 09:00 to 12:00, 12:00 to 15:00, 15:00 to 18:00, 18:00 to 21:00, 21:00 to 24:00 of the UT day, four digits are reserved for ap to make the format consistent with that of the apo indices 

Ap
iiii
Columns 132 to 134
Daily equivalent planetary amplitude Ap, the arithmetic mean of the UT day's 8 ap values rounded to integer

SN
iii
Columns 136 to 138
International sunspot number SN

F10.7obs
ffffff.f
Columns 140 to 147
Noon-time observed solar radio flux F10.7 in s.f.u. (10^-22 W m^-2 Hz^-1)

F10.7adj
ffffff.f
Columns 149 to 156
Noon-time adjusted solar radio flux F10.7 in s.f.u. (10^-22 W m^-2 Hz^-1)

D
i
Column 158
D indicates if the Kp and SN values are definitive or preliminary. 
D=0: Kp and SN preliminary
D=1: Kp definitive, SN preliminary
D=2 Kp and SN definitive



Files with one line per three-hour interval
===========================================
Kp_ap_*.txt files distribute the Kp and ap index and have one line per three-hour interval. The time stamp for each line is given as:
- Year month day and start of three-hour interval in hours
- Mid of three-hour interval in hours
- Start of three hours interval in days since 1932-01-01
- Mid of three hours interval in days since 1932-01-01
- Bartels solar rotation and day within rotation

We provide one file that contains all index values since 1932-01-01 named:
Kp_ap_since_1932.txt,
which is updated daily.

We provide yearly files named, e.g.,
Kp_ap_2020.txt,
which are updated daily.

We provide one nowcast file
Kp_ap_nowcast.txt
with data for the previous and current day, which is constantly updated.


FORMAT DESCRIPTION ('i' stands for integer, 'f' for float)
----------------------------------------------------------

30 header lines, starting with # and not more than 156 columns long

Each line with data is exactly 156 columns

YYYY (displayed in the header as #YYY)
iiii (displayed in the header as #iii)
Columns 1 to 4 
Year of date of the UT day, for which Kp, ap are given

MM
ii
Columns 6 to 7 
Month of date of UT day

DD
ii
Columns 9 to 10
Day of date of UT day

hh.h
ff.f
Columns 12 to 15
Starting time of interval for which Kp and ap are given

hh._m
ff.ff
Columns 16 to 21
Mid time in hours of interval for which Kp and ap are given

days
fffff.fffff
Columns 23 to 33
Days since 1932-01-01 00:00 UT to start of interval

days_m
fffff.fffff
Columns 35 to 45
Days since 1932-01-01 00:00 UT to mid of interval

Kp
ff.fff
Columns 47 to 52
Planetary three-hour index Kp for the interval, index values are rounded to three digits after the decimal point (one thousandth) and two digits are reserved for the index value before the decimal point to make the format consistent with that of the Hpo indices

ap
iiii
Columns 54 to 57
Three-hourly equivalent planetary amplitude ap for the interval, four digits are reserved for ap to make the format consistent with that of the apo indices

D
i
Column 59
D indicates if the Kp and SN values are definitive or preliminary.
D=0: Kp and SN preliminary
D=1: Kp definitive, SN preliminary
D=2 Kp and SN definitive



References
==========
Bartels, J., 1949, The standardized index, Ks, and the planetary index, Kp, IATME Bull., 12b, 97-120.

Bartels, J., 1957b. The geomagnetic measures for the time-variations of solar corpuscular radiation, described for use in correlation studies in other geophysical fields, Ann. Intern. Geophys. Year 4, 227-236

Matzka, J., Stolle, C., Yamazaki, Y., Bronkalla, O. and Morschhauser, A., 2021a. The geomagnetic Kp index and derived indices of geomagnetic activity. Space Weather, https://doi.org/10.1029/2020SW002641

Matzka, J., Bronkalla, O., Tornow, K., Elger, K., Stolle, C., 2021a. Geomagnetic Kp index. V. 1.0. GFZ Data Services, https://doi.org/10.5880/Kp.0001

Clette, F., Lefevre, L., 2016. The New Sunspot Number: assembling all corrections. Solar Physics, 291, https://doi.org/10.1007/s11207-016-1014-y

Tapping, K.F., 2013. The 10.7 cm solar radio flux (F10.7). Space Weather, 11, 394-406, https://doi.org/10.1002/swe.20064



Change Log
==========
2021-03-11    Kp_ap_Ap_SN_F107_format_20210311.txt



END
===