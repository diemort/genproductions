COM_ENERGY = 13000.0 # GeV
CROSS_SECTION = 1 # pb
PROCESS = 'HiggsBSM:gg2H2bbbar = on'
SLHA_TABLE = """BLOCK SPINFO
     1   FeynHiggs
     2   2.12.0
     2   built on ott 13, 2016
BLOCK MODSEL
         1                  0   # Model
         2                  1   # GridPts
         3                  0   # Content
         4                  0   # RPV
         5                  0   # CPV
         6                  0   # FV
BLOCK SMINPUTS
         1     1.28952828E+02   # invAlfaMZ
         2     1.16637000E-05   # GF
         3     1.19000000E-01   # AlfasMZ
         4     9.11876000E+01   # MZ
         5     4.16000000E+00   # Mb
         6     1.73200000E+02   # Mt
         7     1.77703000E+00   # Mtau
        11     5.10998902E-04   # Me
        13     1.05658357E-01   # Mmu
        21     6.00000000E-03   # Md
        22     3.00000000E-03   # Mu
        23     9.50000000E-02   # Ms
        24     1.28600000E+00   # Mc
BLOCK MINPAR
         3     2.50000000E+01   # TB
BLOCK EXTPAR
         0     0.00000000E+00   # Q
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        11     1.50800000E+03   # At
        12     1.50800000E+03   # Ab
        13     1.50800000E+03   # Atau
        23     2.00000000E+02   # MUE
        25     2.50000000E+01   # TB
        26     2.25000000E+02   # MA0
        27     2.38932707E+02   # MHp
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK MASS
   1000012     4.95838375E+02   # MSf(1,1,1)
   1000011     5.02293635E+02   # MSf(1,2,1)
   2000011     5.01842018E+02   # MSf(2,2,1)
   1000002     1.49902834E+03   # MSf(1,3,1)
   2000002     1.49958985E+03   # MSf(2,3,1)
   1000001     1.50117603E+03   # MSf(1,4,1)
   2000001     1.50020494E+03   # MSf(2,4,1)
   1000014     4.95838375E+02   # MSf(1,1,2)
   1000013     5.02640084E+02   # MSf(1,2,2)
   2000013     5.01495040E+02   # MSf(2,2,2)
   1000004     1.49902888E+03   # MSf(1,3,2)
   2000004     1.49959042E+03   # MSf(2,3,2)
   1000003     1.50119986E+03   # MSf(1,4,2)
   2000003     1.50018109E+03   # MSf(2,4,2)
   1000016     9.97925696E+02   # MSf(1,1,3)
   1000015     9.97930750E+02   # MSf(1,2,3)
   2000015     1.00413388E+03   # MSf(2,2,3)
   1000006     8.76427249E+02   # MSf(1,3,3)
   2000006     1.13478079E+03   # MSf(2,3,3)
   1000005     9.94259418E+02   # MSf(1,4,3)
   2000005     1.00778084E+03   # MSf(2,4,3)
        25     1.24842541E+02   # Mh0
        35     2.25343940E+02   # MHH
        36     2.25000000E+02   # MA0
        37     2.40361121E+02   # MHp
   1000022     8.81217311E+01   # MNeu(1)
   1000023     1.51770777E+02   # MNeu(2)
   1000025    -2.10328954E+02   # MNeu(3)
   1000035     2.65908097E+02   # MNeu(4)
   1000024     1.48224451E+02   # MCha(1)
   1000037     2.66377906E+02   # MCha(2)
   1000021     1.50000000E+03   # MGl
BLOCK DMASS
         0     1.73200000E+02   # Q
        25     7.19621772E-01   # Delta Mh0
        35     8.10610788E-03   # Delta MHH
        36     0.00000000E+00   # Delta MA0
        37     7.92742378E-02   # Delta MHp
BLOCK NMIX
     1   1     9.31988478E-01   # ZNeu(1,1)
     1   2    -1.14406215E-01   # ZNeu(1,2)
     1   3     3.11018111E-01   # ZNeu(1,3)
     1   4    -1.46889171E-01   # ZNeu(1,4)
     2   1    -3.18015719E-01   # ZNeu(2,1)
     2   2    -6.93652772E-01   # ZNeu(2,2)
     2   3     5.10771151E-01   # ZNeu(2,3)
     2   4    -3.96010941E-01   # ZNeu(2,4)
     3   1     9.68557338E-02   # ZNeu(3,1)
     3   2    -1.34875686E-01   # ZNeu(3,2)
     3   3    -6.78023080E-01   # ZNeu(3,3)
     3   4    -7.16039258E-01   # ZNeu(3,4)
     4   1    -1.44507597E-01   # ZNeu(4,1)
     4   2     6.98258977E-01   # ZNeu(4,2)
     4   3     4.27393577E-01   # ZNeu(4,3)
     4   4    -5.55775752E-01   # ZNeu(4,4)
BLOCK UMIX
     1   1    -6.07017863E-01   # UCha(1,1)
     1   2     7.94688187E-01   # UCha(1,2)
     2   1     7.94688187E-01   # UCha(2,1)
     2   2     6.07017863E-01   # UCha(2,2)
BLOCK VMIX
     1   1    -7.94688187E-01   # VCha(1,1)
     1   2     6.07017863E-01   # VCha(1,2)
     2   1     6.07017863E-01   # VCha(2,1)
     2   2     7.94688187E-01   # VCha(2,2)
BLOCK STAUMIX
     1   1     6.94077482E-01   # USf(1,1)
     1   2     7.19900305E-01   # USf(1,2)
     2   1     7.19900305E-01   # USf(2,1)
     2   2    -6.94077482E-01   # USf(2,2)
BLOCK STOPMIX
     1   1     7.08251522E-01   # USf(1,1)
     1   2    -7.05960185E-01   # USf(1,2)
     2   1     7.05960185E-01   # USf(2,1)
     2   2     7.08251522E-01   # USf(2,2)
BLOCK SBOTMIX
     1   1     6.67964822E-01   # USf(1,1)
     1   2     7.44192849E-01   # USf(1,2)
     2   1     7.44192849E-01   # USf(2,1)
     2   2    -6.67964822E-01   # USf(2,2)
BLOCK ALPHA
              -7.12751605E-02   # Alpha
BLOCK DALPHA
               8.32656321E-04   # Delta Alpha
BLOCK HMIX Q= -0.99900000E+03
         1     2.00000000E+02   # MUE
         2     2.50000000E+01   # TB
BLOCK MSOFT Q=  0.00000000E+00
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK AE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.50800000E+03   # Af(3,3)
BLOCK AU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.50800000E+03   # Af(3,3)
BLOCK AD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.50800000E+03   # Af(3,3)
BLOCK YE Q=  0.00000000E+00
     1   1     7.34341041E-05   # Yf(1,1)
     2   2     1.51838424E-02   # Yf(2,2)
     3   3     2.55371598E-01   # Yf(3,3)
BLOCK YU Q=  0.00000000E+00
     1   1     1.72448364E-05   # Yf(1,1)
     2   2     7.39228656E-03   # Yf(2,2)
     3   3     9.95601891E-01   # Yf(3,3)
BLOCK YD Q=  0.00000000E+00
     1   1     8.40743677E-04   # Yf(1,1)
     2   2     1.33110713E-02   # Yf(2,2)
     3   3     5.53780613E-01   # Yf(3,3)
BLOCK VCKMIN
         1     2.25300000E-01   # lambda
         2     8.08000000E-01   # A
         3     1.32000000E-01   # rhobar
         4     3.41000000E-01   # etabar
BLOCK MSL2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSL2(1,1)
     2   2     2.50000000E+05   # MSL2(2,2)
     3   3     1.00000000E+06   # MSL2(3,3)
BLOCK MSE2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSE2(1,1)
     2   2     2.50000000E+05   # MSE2(2,2)
     3   3     1.00000000E+06   # MSE2(3,3)
BLOCK MSQ2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSQ2(1,1)
     2   2     2.25000000E+06   # MSQ2(2,2)
     3   3     1.00000000E+06   # MSQ2(3,3)
BLOCK MSU2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSU2(1,1)
     2   2     2.25000000E+06   # MSU2(2,2)
     3   3     1.00000000E+06   # MSU2(3,3)
BLOCK MSD2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSD2(1,1)
     2   2     2.25000000E+06   # MSD2(2,2)
     3   3     1.00000000E+06   # MSD2(3,3)
BLOCK TE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     3.85100369E+02   # Tf(3,3)
BLOCK TU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     1.50136765E+03   # Tf(3,3)
BLOCK TD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     8.35101165E+02   # Tf(3,3)
BLOCK SELMIX
     1   1     9.99984128E-01   # UASf(1,1)
     1   4    -5.63422645E-03   # UASf(1,4)
     2   2     8.34980634E-01   # UASf(2,2)
     2   5    -5.50279330E-01   # UASf(2,5)
     3   3     6.94077482E-01   # UASf(3,3)
     3   6     7.19900305E-01   # UASf(3,6)
     4   1     5.63422645E-03   # UASf(4,1)
     4   4     9.99984128E-01   # UASf(4,4)
     5   2     5.50279330E-01   # UASf(5,2)
     5   5     8.34980634E-01   # UASf(5,5)
     6   3     7.19900305E-01   # UASf(6,3)
     6   6    -6.94077482E-01   # UASf(6,6)
BLOCK USQMIX
     1   1     1.00000000E+00   # UASf(1,1)
     1   4     1.42539883E-05   # UASf(1,4)
     2   2     9.99981335E-01   # UASf(2,2)
     2   5     6.10986751E-03   # UASf(2,5)
     3   3     7.08251522E-01   # UASf(3,3)
     3   6    -7.05960185E-01   # UASf(3,6)
     4   1    -1.42539883E-05   # UASf(4,1)
     4   4     1.00000000E+00   # UASf(4,4)
     5   2    -6.10986751E-03   # UASf(5,2)
     5   5     9.99981335E-01   # UASf(5,5)
     6   3     7.05960185E-01   # UASf(6,3)
     6   6     7.08251522E-01   # UASf(6,6)
BLOCK DSQMIX
     1   1     9.99949630E-01   # UASf(1,1)
     1   4    -1.00368449E-02   # UASf(1,4)
     2   2     9.88183453E-01   # UASf(2,2)
     2   5    -1.53275777E-01   # UASf(2,5)
     3   3     6.67964822E-01   # UASf(3,3)
     3   6     7.44192849E-01   # UASf(3,6)
     4   1     1.00368449E-02   # UASf(4,1)
     4   4     9.99949630E-01   # UASf(4,4)
     5   2     1.53275777E-01   # UASf(5,2)
     5   5     9.88183453E-01   # UASf(5,5)
     6   3     7.44192849E-01   # UASf(6,3)
     6   6    -6.67964822E-01   # UASf(6,6)
BLOCK CVHMIX
     1   1     9.99876860E-01   # UH(1,1)
     1   2     1.56928460E-02   # UH(1,2)
     1   3     0.00000000E+00   # UH(1,3)
     2   1    -1.56928460E-02   # UH(2,1)
     2   2     9.99876860E-01   # UH(2,2)
     2   3     0.00000000E+00   # UH(2,3)
     3   1     0.00000000E+00   # UH(3,1)
     3   2     0.00000000E+00   # UH(3,2)
     3   3     1.00000000E+00   # UH(3,3)
DECAY        25     8.53790631E-03   # Gamma(h0)
     1.08523344E-03   2        22        22   # BR(h0 -> photon photon)
     6.82510499E-04   2        22        23   # BR(h0 -> photon Z)
     1.23096710E-02   2        23        23   # BR(h0 -> Z Z)
     1.02005425E-01   2       -24        24   # BR(h0 -> W W)
     3.07747492E-02   2        21        21   # BR(h0 -> gluon gluon)
     7.38084682E-09   2       -11        11   # BR(h0 -> Electron electron)
     3.28313045E-04   2       -13        13   # BR(h0 -> Muon muon)
     9.35084696E-02   2       -15        15   # BR(h0 -> Tau tau)
     9.40122179E-08   2        -2         2   # BR(h0 -> Up up)
     1.30216471E-02   2        -4         4   # BR(h0 -> Charm charm)
     1.16553635E-06   2        -1         1   # BR(h0 -> Down down)
     2.92696126E-04   2        -3         3   # BR(h0 -> Strange strange)
     7.45990018E-01   2        -5         5   # BR(h0 -> Bottom bottom)
DECAY        35     2.17830509E+00   # Gamma(HH)
    -7.53661323E-07   2        22        22   # BR(HH -> photon photon)
    -4.14774372E-07   2        22        23   # BR(HH -> photon Z)
    -3.28037673E-04   2        23        23   # BR(HH -> Z Z)
    -8.22554517E-04   2       -24        24   # BR(HH -> W W)
    -5.10025091E-04   2        21        21   # BR(HH -> gluon gluon)
    -1.04604430E-08   2       -11        11   # BR(HH -> Electron electron)
     4.65381714E-04   2       -13        13   # BR(HH -> Muon muon)
    -1.30963065E-01   2       -15        15   # BR(HH -> Tau tau)
    -2.71230016E-12   2        -2         2   # BR(HH -> Up up)
    -3.75333050E-07   2        -4         4   # BR(HH -> Charm charm)
    -1.41747311E-06   2        -1         1   # BR(HH -> Down down)
    -3.55954142E-04   2        -3         3   # BR(HH -> Strange strange)
    -8.59622022E-01   2        -5         5   # BR(HH -> Bottom bottom)
    -6.92998855E-03   2   1000022   1000022   # BR(HH -> neutralino1 neutralino1)
DECAY        36     2.20031745E+00   # Gamma(A0)
     2.52391732E-07   2        22        22   # BR(A0 -> photon photon)
     7.31518674E-07   2        22        23   # BR(A0 -> photon Z)
     4.30764329E-04   2        21        21   # BR(A0 -> gluon gluon)
     1.03314119E-08   2       -11        11   # BR(A0 -> Electron electron)
     4.59641397E-04   2       -13        13   # BR(A0 -> Muon muon)
     1.29360251E-01   2       -15        15   # BR(A0 -> Tau tau)
     7.39602106E-13   2        -2         2   # BR(A0 -> Up up)
     1.03586592E-07   2        -4         4   # BR(A0 -> Charm charm)
     1.40019576E-06   2        -1         1   # BR(A0 -> Down down)
     3.51615565E-04   2        -3         3   # BR(A0 -> Strange strange)
     8.49724588E-01   2        -5         5   # BR(A0 -> Bottom bottom)
     1.96355190E-02   2   1000022   1000022   # BR(A0 -> neutralino1 neutralino1)
     3.51225046E-05   2        23        25   # BR(A0 -> Z h0)
DECAY        37     7.86343738E-01   # Gamma(Hp)
     3.16185544E-08   2       -11        12   # BR(Hp -> Electron nu_e)
     1.35179120E-03   2       -13        14   # BR(Hp -> Muon nu_mu)
     3.82335054E-01   2       -15        16   # BR(Hp -> Tau nu_tau)
     3.88370001E-06   2        -1         2   # BR(Hp -> Down up)
     4.38461218E-05   2        -3         2   # BR(Hp -> Strange up)
     2.52155551E-05   2        -5         2   # BR(Hp -> Bottom up)
     1.90702881E-07   2        -1         4   # BR(Hp -> Down charm)
     9.72168662E-04   2        -3         4   # BR(Hp -> Strange charm)
     3.53087889E-03   2        -5         4   # BR(Hp -> Bottom charm)
     4.07234984E-07   2        -1         6   # BR(Hp -> Down top)
     9.19717792E-06   2        -3         6   # BR(Hp -> Strange top)
     5.74078563E-01   2        -5         6   # BR(Hp -> Bottom top)
     3.68868676E-02   2   1000022   1000024   # BR(Hp -> neutralino1 chargino1)
     7.59307744E-04   2        24        25   # BR(Hp -> W h0)
     1.22489320E-06   2        24        35   # BR(Hp -> W HH)
     1.37131149E-06   2        24        36   # BR(Hp -> W A0)
DECAY         6     1.37127534E+00   # Gamma(top)
     1.00000000E+00   2         5        24   # BR(top -> bottom W)
"""

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(1),                        
                         filterEfficiency = cms.untracked.double(1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
                         comEnergy = cms.double(COM_ENERGY),
                         crossSection = cms.untracked.double(CROSS_SECTION),                         
                         maxEventsToPrint = cms.untracked.int32(1),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CUEP8M1SettingsBlock,
                             processParameters = cms.vstring(
                                 'Higgs:useBSM = on', 
                                 PROCESS, 
                                 'SLHA:allowUserOverride = off', 
                                 'SLHA:minMassSM = 100.', 
                                 'PhaseSpace:mHatMin = 56.0'
                             ),
                             parameterSets = cms.vstring(
                                 'pythia8CommonSettings',
                                 'pythia8CUEP8M1Settings',
                                 'processParameters'
                                 )
                             )
                         )

ProductionFilterSequence = cms.Sequence(generator)
