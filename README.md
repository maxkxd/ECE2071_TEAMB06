Current stm setup:
        Processing stm:
                Ultrasonic sensor:
                        TRIGGER: PA5
                        ECHO:    PA6
                
                SPI1_MOSI: PA7
                SP1_SCK:   PA1
        
        Recording stm:


TODO:
        Add options for different save files -> .png, .csv
        Implement Schmitt triggering for us sensor
        Add outlier rejection algorithm
        Fine tune outlier rejection and smoothing alg
        Test us mode
        test std (and us) mode upon any changes, 300s typical

BUGS:
        All of them
        

Current system specs:
        sampling stm prescaler: 31
        Counter period: <22.67 -> set to 22.67 currently
        ADC resolution: ADC 10-bit resolution

        TBC...

std recording conclusion 1: sample rate = 9210sps

Last Test Results - std recording

Params: 5x10s tests in std mode
specs: 41ksps, baudrate = 115200
expected: 20.55ksps
Actual: 21770
% diff: ~5.9%

---START---
---TEST 0---
(6531312,)
        sample rate: 21771
        total samples: 6531312
        elapsed: 300.00

---TEST 1---
(6531116,)
        sample rate: 21770
        total samples: 6531116
        elapsed: 300.00

---TEST 2---
(6531255,)
        sample rate: 21770
        total samples: 6531255
        elapsed: 300.00

---TEST 3---
(6531017,)
        sample rate: 21770
        total samples: 6531017
        elapsed: 300.00

---TEST 4---
(6531106,)
        sample rate: 21770
        total samples: 6531106
        elapsed: 300.00

---END TESTS---

---RESULTS---
Mean sample rate: 21770.2
Median sample rate: 21770.0
Sample rate max: 21771.0
Sample rate min: 21770.0
Sample rate range: 1.0
---END---

Last test results - us recording

---START---
        total samples: 9556990
        elapsed: 1045.58
        sample rate: 9140
---END---