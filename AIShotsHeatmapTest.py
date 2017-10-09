#==============================================================================
# Title: AIShots Heatmap Tester
# Author: Ryan Slater
# Date: 10/5/2017
# Purpose: Test the heatmap maker of the AIShots module
#==============================================================================

import matplotlib.pyplot as plt
import AIShots

AIShots.search(3, [False, False, False, False, False])
a = AIShots.AIBoardHeatMap
print(a)
plt.imshow(a, cmap='binary')
plt.show()