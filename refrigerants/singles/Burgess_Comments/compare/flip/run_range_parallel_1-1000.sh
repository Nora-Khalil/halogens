#!/bin/bash
#SBATCH --job-name=flame_speeds_120-140
#SBATCH --partition=west,short
#SBATCH --exclude=c5003
#SBATCH --mem=20Gb
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=4
#SBATCH --array=1-1000%40


selected_files=(chem_0000.cti chem_0001.cti chem_0002.cti chem_0003.cti chem_0004.cti chem_0005.cti chem_0006.cti chem_0007.cti chem_0008.cti chem_0009.cti chem_0010.cti chem_0011.cti chem_0012.cti chem_0013.cti chem_0014.cti chem_0015.cti chem_0016.cti chem_0017.cti chem_0018.cti chem_0019.cti chem_0020.cti chem_0021.cti chem_0022.cti chem_0023.cti chem_0024.cti chem_0025.cti chem_0026.cti chem_0027.cti chem_0028.cti chem_0029.cti chem_0030.cti chem_0031.cti chem_0032.cti chem_0033.cti chem_0034.cti chem_0035.cti chem_0036.cti chem_0037.cti chem_0038.cti chem_0039.cti chem_0040.cti chem_0041.cti chem_0042.cti chem_0043.cti chem_0044.cti chem_0045.cti chem_0046.cti chem_0047.cti chem_0048.cti chem_0049.cti chem_0050.cti chem_0051.cti chem_0052.cti chem_0053.cti chem_0054.cti chem_0055.cti chem_0056.cti chem_0057.cti chem_0058.cti chem_0059.cti chem_0060.cti chem_0061.cti chem_0062.cti chem_0063.cti chem_0064.cti chem_0065.cti chem_0066.cti chem_0067.cti chem_0068.cti chem_0069.cti chem_0070.cti chem_0071.cti chem_0072.cti chem_0073.cti chem_0074.cti chem_0075.cti chem_0076.cti chem_0077.cti chem_0078.cti chem_0079.cti chem_0080.cti chem_0081.cti chem_0082.cti chem_0083.cti chem_0084.cti chem_0085.cti chem_0086.cti chem_0087.cti chem_0088.cti chem_0089.cti chem_0090.cti chem_0091.cti chem_0092.cti chem_0093.cti chem_0094.cti chem_0095.cti chem_0096.cti chem_0097.cti chem_0098.cti chem_0099.cti chem_0100.cti chem_0101.cti chem_0102.cti chem_0103.cti chem_0104.cti chem_0105.cti chem_0106.cti chem_0107.cti chem_0108.cti chem_0109.cti chem_0110.cti chem_0111.cti chem_0112.cti chem_0113.cti chem_0114.cti chem_0115.cti chem_0116.cti chem_0117.cti chem_0118.cti chem_0119.cti chem_0120.cti chem_0121.cti chem_0122.cti chem_0123.cti chem_0124.cti chem_0125.cti chem_0126.cti chem_0127.cti chem_0128.cti chem_0129.cti chem_0130.cti chem_0131.cti chem_0132.cti chem_0133.cti chem_0134.cti chem_0135.cti chem_0136.cti chem_0137.cti chem_0138.cti chem_0139.cti chem_0140.cti chem_0141.cti chem_0142.cti chem_0143.cti chem_0144.cti chem_0145.cti chem_0146.cti chem_0147.cti chem_0148.cti chem_0149.cti chem_0150.cti chem_0151.cti chem_0152.cti chem_0153.cti chem_0154.cti chem_0155.cti chem_0156.cti chem_0157.cti chem_0158.cti chem_0159.cti chem_0160.cti chem_0161.cti chem_0162.cti chem_0163.cti chem_0164.cti chem_0165.cti chem_0166.cti chem_0167.cti chem_0168.cti chem_0169.cti chem_0170.cti chem_0171.cti chem_0172.cti chem_0173.cti chem_0174.cti chem_0175.cti chem_0176.cti chem_0177.cti chem_0178.cti chem_0179.cti chem_0180.cti chem_0181.cti chem_0182.cti chem_0183.cti chem_0184.cti chem_0185.cti chem_0186.cti chem_0187.cti chem_0188.cti chem_0189.cti chem_0190.cti chem_0191.cti chem_0192.cti chem_0193.cti chem_0194.cti chem_0195.cti chem_0196.cti chem_0197.cti chem_0198.cti chem_0199.cti chem_0200.cti chem_0201.cti chem_0202.cti chem_0203.cti chem_0204.cti chem_0205.cti chem_0206.cti chem_0207.cti chem_0208.cti chem_0209.cti chem_0210.cti chem_0211.cti chem_0212.cti chem_0213.cti chem_0214.cti chem_0215.cti chem_0216.cti chem_0217.cti chem_0218.cti chem_0219.cti chem_0220.cti chem_0221.cti chem_0222.cti chem_0223.cti chem_0224.cti chem_0225.cti chem_0226.cti chem_0227.cti chem_0228.cti chem_0229.cti chem_0230.cti chem_0231.cti chem_0232.cti chem_0233.cti chem_0234.cti chem_0235.cti chem_0236.cti chem_0237.cti chem_0238.cti chem_0239.cti chem_0240.cti chem_0241.cti chem_0242.cti chem_0243.cti chem_0244.cti chem_0245.cti chem_0246.cti chem_0247.cti chem_0248.cti chem_0249.cti chem_0250.cti chem_0251.cti chem_0252.cti chem_0253.cti chem_0254.cti chem_0255.cti chem_0256.cti chem_0257.cti chem_0258.cti chem_0259.cti chem_0260.cti chem_0261.cti chem_0262.cti chem_0263.cti chem_0264.cti chem_0265.cti chem_0266.cti chem_0267.cti chem_0268.cti chem_0269.cti chem_0270.cti chem_0271.cti chem_0272.cti chem_0273.cti chem_0274.cti chem_0275.cti chem_0276.cti chem_0277.cti chem_0278.cti chem_0279.cti chem_0280.cti chem_0281.cti chem_0282.cti chem_0283.cti chem_0284.cti chem_0285.cti chem_0286.cti chem_0287.cti chem_0288.cti chem_0289.cti chem_0290.cti chem_0291.cti chem_0292.cti chem_0293.cti chem_0294.cti chem_0295.cti chem_0296.cti chem_0297.cti chem_0298.cti chem_0299.cti chem_0300.cti chem_0301.cti chem_0302.cti chem_0303.cti chem_0304.cti chem_0305.cti chem_0306.cti chem_0307.cti chem_0308.cti chem_0309.cti chem_0310.cti chem_0311.cti chem_0312.cti chem_0313.cti chem_0314.cti chem_0315.cti chem_0316.cti chem_0317.cti chem_0318.cti chem_0319.cti chem_0320.cti chem_0321.cti chem_0322.cti chem_0323.cti chem_0324.cti chem_0325.cti chem_0326.cti chem_0327.cti chem_0328.cti chem_0329.cti chem_0330.cti chem_0331.cti chem_0332.cti chem_0333.cti chem_0334.cti chem_0335.cti chem_0336.cti chem_0337.cti chem_0338.cti chem_0339.cti chem_0340.cti chem_0341.cti chem_0342.cti chem_0343.cti chem_0344.cti chem_0345.cti chem_0346.cti chem_0347.cti chem_0348.cti chem_0349.cti chem_0350.cti chem_0351.cti chem_0352.cti chem_0353.cti chem_0354.cti chem_0355.cti chem_0356.cti chem_0357.cti chem_0358.cti chem_0359.cti chem_0360.cti chem_0361.cti chem_0362.cti chem_0363.cti chem_0364.cti chem_0365.cti chem_0366.cti chem_0367.cti chem_0368.cti chem_0369.cti chem_0370.cti chem_0371.cti chem_0372.cti chem_0373.cti chem_0374.cti chem_0375.cti chem_0376.cti chem_0377.cti chem_0378.cti chem_0379.cti chem_0380.cti chem_0381.cti chem_0382.cti chem_0383.cti chem_0384.cti chem_0385.cti chem_0386.cti chem_0387.cti chem_0388.cti chem_0389.cti chem_0390.cti chem_0391.cti chem_0392.cti chem_0393.cti chem_0394.cti chem_0395.cti chem_0396.cti chem_0397.cti chem_0398.cti chem_0399.cti chem_0400.cti chem_0401.cti chem_0402.cti chem_0403.cti chem_0404.cti chem_0405.cti chem_0406.cti chem_0407.cti chem_0408.cti chem_0409.cti chem_0410.cti chem_0411.cti chem_0412.cti chem_0413.cti chem_0414.cti chem_0415.cti chem_0416.cti chem_0417.cti chem_0418.cti chem_0419.cti chem_0420.cti chem_0421.cti chem_0422.cti chem_0423.cti chem_0424.cti chem_0425.cti chem_0426.cti chem_0427.cti chem_0428.cti chem_0429.cti chem_0430.cti chem_0431.cti chem_0432.cti chem_0433.cti chem_0434.cti chem_0435.cti chem_0436.cti chem_0437.cti chem_0438.cti chem_0439.cti chem_0440.cti chem_0441.cti chem_0442.cti chem_0443.cti chem_0444.cti chem_0445.cti chem_0446.cti chem_0447.cti chem_0448.cti chem_0449.cti chem_0450.cti chem_0451.cti chem_0452.cti chem_0453.cti chem_0454.cti chem_0455.cti chem_0456.cti chem_0457.cti chem_0458.cti chem_0459.cti chem_0460.cti chem_0461.cti chem_0462.cti chem_0463.cti chem_0464.cti chem_0465.cti chem_0466.cti chem_0467.cti chem_0468.cti chem_0469.cti chem_0470.cti chem_0471.cti chem_0472.cti chem_0473.cti chem_0474.cti chem_0475.cti chem_0476.cti chem_0477.cti chem_0478.cti chem_0479.cti chem_0480.cti chem_0481.cti chem_0482.cti chem_0483.cti chem_0484.cti chem_0485.cti chem_0486.cti chem_0487.cti chem_0488.cti chem_0489.cti chem_0490.cti chem_0491.cti chem_0492.cti chem_0493.cti chem_0494.cti chem_0495.cti chem_0496.cti chem_0497.cti chem_0498.cti chem_0499.cti chem_0500.cti chem_0501.cti chem_0502.cti chem_0503.cti chem_0504.cti chem_0505.cti chem_0506.cti chem_0507.cti chem_0508.cti chem_0509.cti chem_0510.cti chem_0511.cti chem_0512.cti chem_0513.cti chem_0514.cti chem_0515.cti chem_0516.cti chem_0517.cti chem_0518.cti chem_0519.cti chem_0520.cti chem_0521.cti chem_0522.cti chem_0523.cti chem_0524.cti chem_0525.cti chem_0526.cti chem_0527.cti chem_0528.cti chem_0529.cti chem_0530.cti chem_0531.cti chem_0532.cti chem_0533.cti chem_0534.cti chem_0535.cti chem_0536.cti chem_0537.cti chem_0538.cti chem_0539.cti chem_0540.cti chem_0541.cti chem_0542.cti chem_0543.cti chem_0544.cti chem_0545.cti chem_0546.cti chem_0547.cti chem_0548.cti chem_0549.cti chem_0550.cti chem_0551.cti chem_0552.cti chem_0553.cti chem_0554.cti chem_0555.cti chem_0556.cti chem_0557.cti chem_0558.cti chem_0559.cti chem_0560.cti chem_0561.cti chem_0562.cti chem_0563.cti chem_0564.cti chem_0565.cti chem_0567.cti chem_0568.cti chem_0569.cti chem_0570.cti chem_0571.cti chem_0572.cti chem_0573.cti chem_0574.cti chem_0575.cti chem_0576.cti chem_0577.cti chem_0578.cti chem_0579.cti chem_0580.cti chem_0581.cti chem_0582.cti chem_0583.cti chem_0584.cti chem_0585.cti chem_0586.cti chem_0587.cti chem_0588.cti chem_0589.cti chem_0590.cti chem_0591.cti chem_0592.cti chem_0593.cti chem_0594.cti chem_0595.cti chem_0596.cti chem_0597.cti chem_0598.cti chem_0599.cti chem_0600.cti chem_0601.cti chem_0602.cti chem_0603.cti chem_0604.cti chem_0605.cti chem_0606.cti chem_0607.cti chem_0608.cti chem_0609.cti chem_0610.cti chem_0611.cti chem_0612.cti chem_0613.cti chem_0614.cti chem_0615.cti chem_0616.cti chem_0617.cti chem_0618.cti chem_0619.cti chem_0620.cti chem_0621.cti chem_0622.cti chem_0623.cti chem_0624.cti chem_0625.cti chem_0626.cti chem_0627.cti chem_0628.cti chem_0629.cti chem_0630.cti chem_0631.cti chem_0632.cti chem_0633.cti chem_0634.cti chem_0635.cti chem_0636.cti chem_0637.cti chem_0638.cti chem_0639.cti chem_0640.cti chem_0641.cti chem_0642.cti chem_0643.cti chem_0644.cti chem_0645.cti chem_0646.cti chem_0647.cti chem_0648.cti chem_0649.cti chem_0650.cti chem_0651.cti chem_0652.cti chem_0653.cti chem_0654.cti chem_0655.cti chem_0656.cti chem_0657.cti chem_0658.cti chem_0659.cti chem_0660.cti chem_0661.cti chem_0662.cti chem_0663.cti chem_0664.cti chem_0665.cti chem_0666.cti chem_0667.cti chem_0668.cti chem_0669.cti chem_0670.cti chem_0671.cti chem_0672.cti chem_0673.cti chem_0674.cti chem_0675.cti chem_0676.cti chem_0677.cti chem_0678.cti chem_0679.cti chem_0680.cti chem_0681.cti chem_0682.cti chem_0683.cti chem_0684.cti chem_0685.cti chem_0686.cti chem_0687.cti chem_0688.cti chem_0689.cti chem_0690.cti chem_0691.cti chem_0692.cti chem_0693.cti chem_0694.cti chem_0695.cti chem_0696.cti chem_0697.cti chem_0698.cti chem_0699.cti chem_0700.cti chem_0701.cti chem_0702.cti chem_0703.cti chem_0704.cti chem_0705.cti chem_0706.cti chem_0707.cti chem_0708.cti chem_0709.cti chem_0710.cti chem_0711.cti chem_0712.cti chem_0713.cti chem_0714.cti chem_0715.cti chem_0716.cti chem_0717.cti chem_0718.cti chem_0719.cti chem_0720.cti chem_0721.cti chem_0722.cti chem_0723.cti chem_0724.cti chem_0725.cti chem_0726.cti chem_0727.cti chem_0728.cti chem_0729.cti chem_0730.cti chem_0731.cti chem_0732.cti chem_0733.cti chem_0734.cti chem_0735.cti chem_0736.cti chem_0737.cti chem_0738.cti chem_0739.cti chem_0740.cti chem_0741.cti chem_0742.cti chem_0743.cti chem_0744.cti chem_0745.cti chem_0746.cti chem_0747.cti chem_0748.cti chem_0749.cti chem_0750.cti chem_0751.cti chem_0752.cti chem_0753.cti chem_0754.cti chem_0755.cti chem_0756.cti chem_0757.cti chem_0758.cti chem_0759.cti chem_0760.cti chem_0761.cti chem_0762.cti chem_0763.cti chem_0764.cti chem_0765.cti chem_0766.cti chem_0767.cti chem_0768.cti chem_0769.cti chem_0770.cti chem_0771.cti chem_0772.cti chem_0773.cti chem_0774.cti chem_0775.cti chem_0776.cti chem_0777.cti chem_0778.cti chem_0779.cti chem_0780.cti chem_0781.cti chem_0782.cti chem_0783.cti chem_0784.cti chem_0785.cti chem_0786.cti chem_0787.cti chem_0788.cti chem_0789.cti chem_0790.cti chem_0791.cti chem_0792.cti chem_0793.cti chem_0794.cti chem_0795.cti chem_0796.cti chem_0797.cti chem_0798.cti chem_0799.cti chem_0800.cti chem_0801.cti chem_0802.cti chem_0803.cti chem_0804.cti chem_0805.cti chem_0806.cti chem_0807.cti chem_0808.cti chem_0809.cti chem_0810.cti chem_0811.cti chem_0812.cti chem_0813.cti chem_0814.cti chem_0815.cti chem_0816.cti chem_0817.cti chem_0818.cti chem_0819.cti chem_0820.cti chem_0821.cti chem_0822.cti chem_0823.cti chem_0824.cti chem_0825.cti chem_0826.cti chem_0827.cti chem_0828.cti chem_0829.cti chem_0830.cti chem_0831.cti chem_0832.cti chem_0833.cti chem_0834.cti chem_0835.cti chem_0836.cti chem_0837.cti chem_0838.cti chem_0839.cti chem_0840.cti chem_0841.cti chem_0842.cti chem_0843.cti chem_0844.cti chem_0845.cti chem_0846.cti chem_0847.cti chem_0848.cti chem_0849.cti chem_0850.cti chem_0851.cti chem_0852.cti chem_0853.cti chem_0854.cti chem_0855.cti chem_0856.cti chem_0857.cti chem_0858.cti chem_0859.cti chem_0860.cti chem_0861.cti chem_0862.cti chem_0863.cti chem_0864.cti chem_0865.cti chem_0866.cti chem_0867.cti chem_0868.cti chem_0869.cti chem_0870.cti chem_0871.cti chem_0872.cti chem_0873.cti chem_0874.cti chem_0875.cti chem_0876.cti chem_0877.cti chem_0878.cti chem_0879.cti chem_0880.cti chem_0881.cti chem_0882.cti chem_0883.cti chem_0884.cti chem_0885.cti chem_0886.cti chem_0887.cti chem_0888.cti chem_0889.cti chem_0890.cti chem_0891.cti chem_0892.cti chem_0893.cti chem_0894.cti chem_0895.cti chem_0896.cti chem_0897.cti chem_0898.cti chem_0899.cti chem_0900.cti chem_0901.cti chem_0902.cti chem_0903.cti chem_0904.cti chem_0905.cti chem_0906.cti chem_0907.cti chem_0908.cti chem_0909.cti chem_0910.cti chem_0911.cti chem_0912.cti chem_0913.cti chem_0914.cti chem_0915.cti chem_0916.cti chem_0917.cti chem_0918.cti chem_0919.cti chem_0920.cti chem_0921.cti chem_0922.cti chem_0923.cti chem_0924.cti chem_0925.cti chem_0926.cti chem_0927.cti chem_0928.cti chem_0929.cti chem_0930.cti chem_0931.cti chem_0932.cti chem_0933.cti chem_0934.cti chem_0935.cti chem_0936.cti chem_0937.cti chem_0938.cti chem_0939.cti chem_0940.cti chem_0941.cti chem_0942.cti chem_0943.cti chem_0944.cti chem_0945.cti chem_0946.cti chem_0947.cti chem_0948.cti chem_0949.cti chem_0950.cti chem_0951.cti chem_0952.cti chem_0953.cti chem_0954.cti chem_0955.cti chem_0956.cti chem_0957.cti chem_0958.cti chem_0959.cti chem_0960.cti chem_0961.cti chem_0962.cti chem_0963.cti chem_0964.cti chem_0965.cti chem_0966.cti chem_0967.cti chem_0968.cti chem_0969.cti chem_0970.cti chem_0971.cti chem_0972.cti chem_0973.cti chem_0974.cti chem_0975.cti chem_0976.cti chem_0977.cti chem_0978.cti chem_0979.cti chem_0980.cti chem_0981.cti chem_0982.cti chem_0983.cti chem_0984.cti chem_0985.cti chem_0986.cti chem_0987.cti chem_0988.cti chem_0989.cti chem_0990.cti chem_0991.cti chem_0992.cti chem_0993.cti chem_0994.cti chem_0995.cti chem_0996.cti chem_0997.cti chem_0998.cti chem_0999.cti chem_1000.cti)


index=$SLURM_ARRAY_TASK_ID-1

folder_name="${selected_files[$index]}"

my_path="/work/westgroup/nora/Code/projects/halogens/refrigerants/singles/Burgess_Comments/compare/flip/flip_models/${folder_name}"


python flame_speed_calc.py $my_path