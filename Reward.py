from rdkit import Chem
from rdkit.Chem import RDConfig
import os
import sys
sys.path.append(os.path.join(RDConfig.RDContribDir, 'SA_Score'))
import sascorer
from rdkit.Chem import QED

class Reward():
    
    def __init__(self, molecule, target_sequence, SA_weight = 0.25, QED_weight = 0.25, Kd_weight = 0.25, specificity_weight = 0.25):
        """
        Args:
            molecule (rdkit.Chem.rdchem.Mol): current molecule to be evaluated as rdkit molecule object
            target_sequence (string): sequence of amino acids representing target, used to match to similar protein family
            weight_vector (np.array): optional. used to weigh rewards differently in reward 
        """
        
        self.mol = molecule
        self.r1_weight = SA_weight
        self.r2_weight = QED_weight
        self.r3 = Kd_weight
        self.r4 = specificity_weight
        
        #Test that weights are appropriate
        e = "Reward weights do not add up to 1, please edit."
        if (SA_weight + QED_weight + Kd_weight + specificity_weight) !=1 : raise Exception(e)
    
    def calc_SA(self):
        SA = sascorer.calculateScore(self.mol)
        return SA
    
    def calc_QED(self):
        qed = QED.qed(self.mol)
        return qed
    
    #Uses our own CNN to predict Kd of given molecule
    def predict_kd(self):
        #Format molecule as per required for input 
        #Import model
        #Predict Kd
        #return 1/Kd #Inverse so reward is higher for lower Kd
        return 1 #Temp
    
    def calc_specificity(self):
        #Determine which family the target is most similar to
        #For each protein in this family, run predict_kd
        #keep an average value of the kd
        #return avg_Kd
        return 1 #Temp
    
    def check_clash(self):
        #Check if any ligand atoms are within 1A of protein atoms, if no clash, 1 point added to reward
        clash=1
        if clash: return 1
        else: return 0
    
    def reward(self):
        r1 = self.calc_SA()
        r2 = self.calc_QED()
        r3 = self.predict_kd()
        r4 = self.calc_specificity()
        clash = self.check_clash()
        reward = (r1*self.r1_weight + r2*self.r2_weight + r3*self.r3_weight + r4*self.r4_weight) + clash
        
        #discount = self._discount_factor**(self.max_steps - self._counter)
        #return reward * discount
        return reward
    
    
    
if __name__ == "__main__":
    m = Chem.MolFromSmiles('Cc1ccccc1')

    
    
