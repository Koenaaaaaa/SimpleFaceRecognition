#!/usr/bin/env python
# coding: utf-8

# In[9]:


import cv2
import face_recognition


# In[10]:


# Read the image and encode it for processing
img = cv2.imread("")
rgb_img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB) 
img_encoding = face_recognition.face_encodings(rgb_img)[0]


# In[11]:


img2 = cv2.imread("")
rgb_img2 = cv2.cvtColor(img2 , cv2.COLOR_BGR2RGB) 
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]


# In[12]:


# Compare the encoded images 
result = face_recognition.compare_faces([img_encoding],img_encoding2)
print("Result:", result)


# In[ ]:


cv2.imshow("Img", img)
cv2.imshow("Img 2", img2)
cv2.waitKey(0)

