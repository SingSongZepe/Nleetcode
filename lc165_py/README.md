165. Compare Version Numbers
Medium
Topics
Companies
Hint
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

Example 1:

Input: version1 = "1.2", version2 = "1.10"

Output: -1

Explanation:

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:

Input: version1 = "1.01", version2 = "1.001"

Output: 0

Explanation:

Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:

Input: version1 = "1.0", version2 = "1.0.0.0"

Output: 0

Explanation:

version1 has less revisions, which means every missing revision are treated as "0".

 

Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.


### More test cases:
"0"
"0"
"6"
"003479002"
"0599.9.083.970.70922.3.0.900.250.7.8.8.8.020.6.31586.7.0.1.4.2.5050800.3.590.34224.5.080.6.281.8649105.6.3.097.484.7.4.650.28907.7.090.200.3.455.6.5.7.695.932.6.0.460.3.6.712.117.08712.405.264.5.000.7.9.7.407.9.3.8.3.8.540.731.0381208.0.100.70900.401.101.012.30778.488.07874.002.0009040.9.4.0.8552202.757.0.2.9.830.9.04809.8.0.070840505.308.0.8.079.2.7.968.470.3.81002.2.8.19270.367.389.24378.5.5454000.4.6.739.5.309.0.0.4.10130.9.8.7673400.7.8.0804228.614090066.658.600.0.2.5.2.620.905.00503.519.0"
"599.460.301.9524810.6.975.008.339.0.5.0.3.5.150.9"
"4"
"4.969.3.863.960.99661.8.085.769.0.735662509.75003"
"306.9.0.0"
"3.0691430.7.7.263.005.2.1.6.606.702.7.076519166.507"
"2.3.4.7.458.3.30233.5.6.0.0.016.182.415535926.34127.603.4.3773585.701.0.503.4.07045.820.1.961.007.3.7.000.822.2.147469700.4566039.4.0.5.9.50505.921.84630.89046.090.0.126.0.1.0.0.8467325.1.4087910.7.4.5.4180554.1.2830694.978.87693.541.343.700.753.67070.65792.561.638.0.30430.503.15491.783.38453.097.10279.090.60962.6.7.0.059.7.3.701.2.57924.089.516.7.3.830.0.4.429.43050.644.000.50280.842.008.2.0.3.7.450.0.6.0.036794307.720460821.56703.9.8.0.3.6.1.09030.832.30080.1.0025137.2.0.400.5.040.0.0026012.0"
"910.18748.91777.6.4.9.2.0.8.3.8.109.0.5.611.4.2.9.063032140.879.2.9.0.400.0.83439.4.8.505.9.641.0.3.9570503.0.50467.0.0.380.400.805.0.930.9.4.207.0.189.0.453.0.8105000.1.580.29903.58747.500.6709046.4.493.60624.0.1.13600.8.000.7.3.127.2673376.5.05187.220.527.22261.5.5.6.63006.9.4.3.9.0.798.013.3.90635.402907450.7367085.9.0.2.708.418.605200845.615.30460.720003156.891.02671.399.356.656.389.0.260.8.060.5.059.0.9.4816801.522.04616.9.9.90670.4.23922.050.7.0.270.003.0.3563057.052200454.3.9836401.401.0"
"2"
"3.22252.355.5.0.764.884.0.6.634.1.023.4.0003000.542270746.82850.0.190.1.5.85027.6.931704233.4.9.8.5.24544.6.880.129.7.1.0.0099608.88404.099.1.6.0.3.352.0.0.4.8000013.787900070.8.210.0.213.2.7.0.0.4.108.0.9201020.0.161.3.0.008.200.6.487.4.0.802.400.7.0.1.43307.3.190.990.2.8.0.9.75539.2.7.1.2.63159.7.03321.864.8.765.46114.8.0.505.219.330059902.696.6.90936.651.159.996.095934900.6.43220.067.0.945.4.1.798.0845070.4.20201.076.1.0.8.7.57091.4.4.0.7.80591.44134.1.6.7.153.506.971.8.72437.0.8.42720.374.6"
"30307.038"
"30307.038.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0"