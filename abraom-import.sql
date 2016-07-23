-- abraom-import.sql
-- Nam Pho
-- July 23, 2016
-- connects to abraom database and imports purged.csv into the variants table

\connect abraom;

\COPY variants("Chr","Start","End","Ref","Alt","Func_refGene","Gene_refGene","GeneDetail_refGene","ExonicFunc_refGene","HGMD","Pathogenicity","HVariable","Reactome","Oreganno","Regulatory","OMIM","OMIMnum","OMIMdisorder","AAChange_refGene","Func_ensGene","Gene_ensGene","GeneDetail_ensGene","ExonicFunc_ensGene","AAChange_ensGene","Func_knownGene","Gene_knownGene","GeneDetail_knownGene","ExonicFunc_knownGene","AAChange_knownGene","avsnp144","clinvar_20150629","CHROM","POS","ID","REF2","ALT2","QUAL","FILTER","AC","AF","AN","INFO","FORMAT") FROM 'purged.csv' WITH CSV HEADER;
