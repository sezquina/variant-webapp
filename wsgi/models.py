# models.py

from app import db

class variants(db.Model):
    
    __tablename__ = 'variants'
    
    id = db.Column(db.Integer, primary_key=True)    
    Chr = db.Column(db.String(5))
    Start = db.Column(db.Integer)
    End = db.Column(db.Integer)
    Ref = db.Column(db.String(50))
    Alt = db.Column(db.String(50))
    Func_refGene = db.Column(db.String(50))
    Gene_refGene = db.Column(db.String(50))
    GeneDetail_refGene = db.Column(db.Text)
    ExonicFunc_refGene = db.Column(db.String(100))
    HGMD = db.Column(db.String(50))
    Pathogenicity = db.Column(db.String(100))
    HVariable = db.Column(db.String(100))
    Reactome = db.Column(db.String(100))
    Oreganno = db.Column(db.String(100)) 
    Regulatory = db.Column(db.String(100))
    OMIM = db.Column(db.String(100))
    OMIMnum = db.Column(db.String(100))
    OMIMdisorder = db.Column(db.String(100))
    AAChange_refGene = db.Column(db.String(500))
    Func_ensGene = db.Column(db.String(100))
    Gene_ensGene = db.Column(db.String(100))
    GeneDetail_ensGene = db.Column(db.Text)
    ExonicFunc_ensGene = db.Column(db.String(100))
    AAChange_ensGene = db.Column(db.String(500))
    Func_knownGene = db.Column(db.String(100))
    Gene_knownGene = db.Column(db.String(100))
    GeneDetail_knownGene = db.Column(db.Text)
    ExonicFunc_knownGene = db.Column(db.String(100))
    AAChange_knownGene = db.Column(db.String(500))
    avsnp144 = db.Column(db.String(100))
    clinvar_20150629 = db.Column(db.String(100))
    CHROM = db.Column(db.String(5))
    POS = db.Column(db.Integer)
    ID = db.Column(db.String(50))
    REF2 = db.Column(db.String(100))
    ALT2 = db.Column(db.String(100))
    QUAL = db.Column(db.String(100))
    FILTER = db.Column(db.String(100))
    AC = db.Column(db.Integer)
    AF = db.Column(db.Float)
    AN = db.Column(db.Integer)
    INFO = db.Column(db.String(500))
    FORMAT = db.Column(db.String(100))

    def __init__(self, **kwargs):
        vars(self).update(kwargs)
    
'''    
    def __init__(self,
                 Chr, 
                 Start, 
                 End, 
                 Ref, 
                 Alt, 
                 Func_refGene, 
                 Gene_refGene, 
                 GeneDetail_refGene, 
                 ExonicFunc_refGene, 
                 HGMD, 
                 Pathogenicity, 
                 HVariable, 
                 Reactome, 
                 Oreganno, 
                 Regulatory, 
                 OMIM, 
                 OMIMnum, 
                 OMIMdisorder, 
                 AAChange_refGene, 
                 Func_ensGene, 
                 Gene_ensGene, 
                 GeneDetail_ensGene, 
                 ExonicFunc_ensGene, 
                 AAChange_ensGene, 
                 Func_knownGene, 
                 Gene_knownGene, 
                 GeneDetail_knownGene, 
                 ExonicFunc_knownGene, 
                 AAChange_knownGene, 
                 avsnp144, 
                 clinvar_20150629, 
                 CHROM, 
                 POS, 
                 ID, 
                 REF2, 
                 ALT2, 
                 QUAL, 
                 FILTER, 
                 AC, 
                 AF, 
                 AN, 
                 INFO, 
                 FORMAT):
	self.Chr = db.Column(db.String(5))
        self.Start = db.Column(db.Integer)
        self.End = db.Column(db.Integer)
        self.Ref = db.Column(db.String(50))
        self.Alt = db.Column(db.String(50))
        self.Func_refGene = db.Column(db.String(50))
        self.Gene_refGene = db.Column(db.String(50))
        self.GeneDetail_refGene = db.Column(db.Text)
        self.ExonicFunc_refGene = db.Column(db.String(100))
        self.HGMD = db.Column(db.String(50))
        self.Pathogenicity = db.Column(db.String(100))
        self.HVariable = db.Column(db.String(100))
        self.Reactome = db.Column(db.String(100))
        self.Oreganno = db.Column(db.String(100)) 
        self.Regulatory = db.Column(db.String(100))
        self.OMIM = db.Column(db.String(100))
        self.OMIMnum = db.Column(db.String(100))
        self.OMIMdisorder = db.Column(db.String(100))
        self.AAChange_refGene = db.Column(db.String(500))
        self.Func_ensGene = db.Column(db.String(100))
        self.Gene_ensGene = db.Column(db.String(100))
        self.GeneDetail_ensGene = db.Column(db.Text)
        self.ExonicFunc_ensGene = db.Column(db.String(100))
        self.AAChange_ensGene = db.Column(db.String(500))
        self.Func_knownGene = db.Column(db.String(100))
        self.Gene_knownGene = db.Column(db.String(100))
        self.GeneDetail_knownGene = db.Column(db.Text)
        self.ExonicFunc_knownGene = db.Column(db.String(100))
        self.AAChange_knownGene = db.Column(db.String(500))
        self.avsnp144 = db.Column(db.String(100))
        self.clinvar_20150629 = db.Column(db.String(100))
        self.CHROM = db.Column(db.String(5))
        self.POS = db.Column(db.Integer)
        self.ID = db.Column(db.String(50))
        self.REF2 = db.Column(db.String(100))
        self.ALT2 = db.Column(db.String(100))
        self.QUAL = db.Column(db.String(100))
        self.FILTER = db.Column(db.String(100))
        self.AC = db.Column(db.Integer)
        self.AF = db.Column(db.Float)
        self.AN = db.Column(db.Integer)
        self.INFO = db.Column(db.String(500))
        self.FORMAT = db.Column(db.String(100))
'''
