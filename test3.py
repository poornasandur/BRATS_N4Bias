import SimpleITK as sitk

def fun():
    image=input('Enter the name and path of the image : ')
    img=sitk.ReadImage(image)
    data=sitk.GetArrayFromImage(img)
    print type(data)
    img_data=sitk.Cast(img,sitk.sitkFloat32)
    img_mask=sitk.BinaryNot(sitk.BinaryThreshold(img_data, 0, 0))
    corrected_img = sitk.N4BiasFieldCorrection(img, img_mask)
    mask=input('Enter the name of the mask image to be saved : ')
    sitk.WriteImage(img_mask,mask)
    new_img=input('Enter the name of the Bias Field Corrected Image : ')
    sitk.WriteImage(corrected_img,new_img)
    print "Finished N4 Bias Field Correction....."

if __name__=='__main__':
   fun()
