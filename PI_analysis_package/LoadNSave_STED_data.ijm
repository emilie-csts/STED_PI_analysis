
Folder="C:/Users/Emilie/Documents/Data/STED/Test_file/";
names=getFileList(Folder);
print(names[0]);

for(i=0;i<lengthOf(names);i++){
	print(i);
	print(names[i]);
	open(Folder+names[i]);
	selectWindow("- STAR 635P_STED {26}");
	saveAs("Tiff", "C:/Users/Emilie/Documents/Data/STED/Test_file/Data_for_analysis/"+names[i]+"_Nup96.tif");
	selectWindow("- STAR 580_STED {26}");
	saveAs("Tiff", "C:/Users/Emilie/Documents/Data/STED/Test_file/Data_for_analysis/"+names[i]+"_414.tif");
	selectWindow("- STAR 460L_STED {26}");
	saveAs("Tiff", "C:/Users/Emilie/Documents/Data/STED/Test_file/Data_for_analysis/"+names[i]+"_POM.tif");
	run("Close All");
}
