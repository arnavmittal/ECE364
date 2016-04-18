import sys
from SteganographyGUI import *
from Steganography import *
from PySide.QtCore import *
from PySide.QtGui import *
from scipy.misc import *
from scipy import ndimage
import  numpy

class SteganographyConsumer(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(SteganographyConsumer, self).__init__(parent)
        self.setupUi(self)

        #---------------------------------------------#
        # TAB 1
        #---------------------------------------------#
        self.data_p1 = None
        self.viewPayload1.setAcceptDrops(True)
        self.viewPayload1.setDragMode = True

        self.data_c1= None
        self.viewCarrier1.setAcceptDrops(True)
        self.viewCarrier1.setDragMode = True

        print("STARTING")

        #---------------------------------------------#
        # View Payload 1 stuff
        #---------------------------------------------#
        self.viewPayload1.dragEnterEvent = self.payload1_dragged
        self.chkApplyCompression.stateChanged.connect(self.cmp_chkbox_changed)
        self.slideCompression.valueChanged.connect(self.cmp_slider_changed)

        #---------------------------------------------#
        # View Carrier 1 stuff
        #---------------------------------------------#
        self.viewCarrier1.dragEnterEvent = self.carrier1_dragged

        #---------------------------------------------#
        # Save Push Button stuff
        #---------------------------------------------#
        self.new_img_data = None
        self.new_cmp_level = None
        self.btnSave.setDisabled(True)
        self.btnSave.clicked.connect(self.save_clicked)

        self.txtPayloadSize.textChanged.connect(self.save_enable)
        self.txtCarrierSize.textChanged.connect(self.save_enable)
        self.chkOverride.stateChanged.connect(self.save_enable1)
        #---------------------------------------------#
        # TAB 2
        #---------------------------------------------#
        self.data_c2 = None
        self.directory=None
        self.viewCarrier2.setAcceptDrops(True)
        self.viewCarrier2.setDragMode = True

        self.carrier2_payload = False
        #---------------------------------------------#
        # View Carrier 2 stuff
        #---------------------------------------------#
        self.viewCarrier2.dragEnterEvent = self.carrier2_dragged

        #---------------------------------------------#
        # Extract Push Button stuff
        #---------------------------------------------#
        self.new_img_data_2 = None
        self.btnExtract.clicked.connect(self.extract_clicked)

        #---------------------------------------------#
        # Clean Push Button stuff
        #---------------------------------------------#
        self.new_img_data_3 = None
        self.btnClean.clicked.connect(self.clean_clicked)

    #---------------------------------------------#
    # TAB 1
    #---------------------------------------------#

    #---------------------------------------------#
    # View Payload 1 setup and formatting
    #---------------------------------------------#
    def payload1_dragged(self, event):
        print("     DRAGGING")
        event.accept()
        self.viewPayload1.dragLeaveEvent = self.img_no_drag
        self.viewPayload1.dragMoveEvent = self.img_new
        self.viewPayload1.dropEvent = self.payload1_dropped

    def img_no_drag(self, event):
        print("     NOT DRAGGED")
        event.ignore()

    def img_new(self, event):
        event.accept()

    def payload1_dropped(self, event):

        #---------------------------------------------#
        # Retrieve location of the image
        #---------------------------------------------#

        print("         DROPPED")
        old_data=event.mimeData().text()
        data=old_data[7:]

        #---------------------------------------------#
        # Checking if .png file dropped
        #---------------------------------------------#
        if '.png' in data:
            event.accept()
            print('         ACCEPTED')
            self.payload1_show(data.strip())
        else:
            event.ignore()
            print('         IGNORED')

    def payload1_show(self, location):

        #---------------------------------------------#
        # Show image in view payload 1
        #---------------------------------------------#
        print(location)
        scene = QGraphicsScene()
        pixmap = QPixmap(location)
        scene.addPixmap(pixmap)
        self.viewPayload1.setScene(scene)
        self.viewPayload1.fitInView(scene.itemsBoundingRect(),  Qt.KeepAspectRatio)
        print("             Image Displayed")

        #---------------------------------------------#
        # Read the ndarray of the image
        #---------------------------------------------#
        self.data_p1 = ndimage.imread(location)

        #---------------------------------------------#
        # Generate XML
        #---------------------------------------------#

        xml_str= Payload(img=self.data_p1).xml
        size_chk=len(xml_str)

        #---------------------------------------------#
        # Set the txtPayloadSize
        # Set checkbox to unticked
        # Set slider to value 0
        #---------------------------------------------#
        print("             Default State Initalized")
        self.txtPayloadSize.setText(str(size_chk))
        self.chkApplyCompression.setChecked(False)
        cmp_val=0
        self.slideCompression.setValue(cmp_val)
        self.txtCompression.setText(str(cmp_val))
        self.slideCompression.setEnabled(False)
        self.txtCompression.setEnabled(False)

    def cmp_chkbox_changed(self):
        #---------------------------------------------#
        # Compression checkbox is checked
        #---------------------------------------------#
        active=self.chkApplyCompression.isChecked()
        if (active == True):
            print("                 Compression Applied")

            #---------------------------------------------#
            # Enable Slider and txtCompression
            #---------------------------------------------#

            self.slideCompression.setEnabled(True)
            self.txtCompression.setEnabled(True)

            #---------------------------------------------#
            # New XML string with previous compression value
            # Update the new size in the txtPayloadSize
            #---------------------------------------------#
            cmp_val = self.slideCompression.value()
            xml_str= Payload(img=self.data_p1, compressionLevel=cmp_val).xml
            size_chk=len(xml_str)
            self.txtPayloadSize.setText(str(size_chk))

        else:
            print("                 Compression Not Applied")

            #---------------------------------------------#
            # Disable Slider and txtCompression
            #---------------------------------------------#

            self.slideCompression.setEnabled(False)
            self.txtCompression.setEnabled(False)

            #---------------------------------------------#
            # New XML string with 0 compression value
            # Update the new size in the txtPayloadSize
            #---------------------------------------------#

            xml_str= Payload(img=self.data_p1).xml
            size_chk=len(xml_str)
            self.txtPayloadSize.setText(str(size_chk))

    def cmp_slider_changed(self):
        #---------------------------------------------#
        # Compression slider value is changed
        #---------------------------------------------#

        cmp_val = self.slideCompression.value()
        self.txtCompression.setText(str(cmp_val))

        #---------------------------------------------#
        # New XML string with 0 compression value
        # Update the new size in the txtPayloadSize
        #---------------------------------------------#
        self.new_cmp_level = cmp_val
        xml_str= Payload(img=self.data_p1, compressionLevel=cmp_val).xml
        size_chk=len(xml_str)
        self.txtPayloadSize.setText(str(size_chk))

    #---------------------------------------------#
    # View Carrier 1 setup and formatting
    #---------------------------------------------#
    def carrier1_dragged(self, event):
        print("     DRAGGING")
        event.accept()
        self.viewCarrier1.dragLeaveEvent = self.img_no_drag
        self.viewCarrier1.dragMoveEvent = self.img_new
        self.viewCarrier1.dropEvent = self.carrier1_dropped

    def carrier1_dropped(self, event):

        #---------------------------------------------#
        # Retrieve location of the image
        #---------------------------------------------#

        print("         DROPPED")
        old_data=event.mimeData().text()
        data=old_data[7:]

        #---------------------------------------------#
        # Checking if .png file dropped
        #---------------------------------------------#
        if '.png' in data:
            event.accept()
            print('         ACCEPTED')
            self.carrier1_show(data.strip())
        else:
            event.ignore()
            print('         IGNORED')

    def carrier1_show(self, location):

        #---------------------------------------------#
        # Show image in view carrier 1
        #---------------------------------------------#

        scene = QGraphicsScene()
        pixmap = QPixmap(location)
        scene.addPixmap(pixmap)
        self.viewCarrier1.setScene(scene)
        self.viewCarrier1.fitInView(scene.itemsBoundingRect(),  Qt.KeepAspectRatio)
        print("             Image Displayed")

        #---------------------------------------------#
        # Read the ndarray of the image
        #---------------------------------------------#
        self.data_c1 = ndimage.imread(location)

        #---------------------------------------------#
        # Getting the Size of Carrier
        #---------------------------------------------#

        if (len(Carrier(img=self.data_c1).img.shape) == 3):
            size_chk = int(int(Carrier(img=self.data_c1).img.shape[0]) * int(Carrier(img=self.data_c1).img.shape[1]) * 3 / 8)
        else:
            size_chk = int(int(Carrier(img=self.data_c1).img.shape[0]) * int(Carrier(img=self.data_c1).img.shape[1]) / 8)
        #---------------------------------------------#
        # Set the txtCarrierSize
        # Check if payload already exists
        #    - set lblPayloadFound
        #    - set chkOverride enabled
        #---------------------------------------------#
        print("             Default State Initalized")

        self.txtCarrierSize.setText(str(size_chk))
        if (Carrier.payloadExists(Payload(img = self.data_c1)) == True):
            print("                 PAYLOAD EXISTS")
            self.lblPayloadFound.setText('>>>> Payload Found <<<<')
            self.chkOverride.setEnabled(True)
            self.save_enable1()
        else:
            print("                 PAYLOAD DOES NOT EXIST")
            self.lblPayloadFound.setText('')
            self.chkOverride.setChecked(False)
            self.chkOverride.setEnabled(False)
            self.save_enable1()


    #---------------------------------------------#
    # Save push button setup and formatting
    #---------------------------------------------#

    def save_enable(self):
        #---------------------------------------------#
        # Enable/Disable Save Push Button
        #---------------------------------------------#
        print("1st or 2nd")
        save_progress=0

        if (self.data_c1 is not None and self.data_p1 is not None):
            #---------------------------------------------#
            # Carrier Size >= Payload Size
            #---------------------------------------------#
            carrier_size = int(self.txtCarrierSize.text())
            payload_size = int(self.txtPayloadSize.text())

            if ( carrier_size > payload_size):
                save_progress += 1

            #---------------------------------------------#
            # Carrier Size does not have previous payload, if it does then chkoverride is checked
            #---------------------------------------------#
            if self.lblPayloadFound.text() is '':
                # No prev Payload
                save_progress += 1
            else:
                # Prev Payload
                active=self.chkOverride.isChecked()
                if(active):
                    save_progress += 1

            #---------------------------------------------#
            # Ready to save progress
            #---------------------------------------------#
            if ( save_progress == 2):
                self.btnSave.setEnabled(True)
                self.save_enable1()
                print("         READY TO SAVE")
            else:
                self.btnSave.setDisabled(True)
                print("         NOT YET READY TO SAVE")
        else:
            self.btnSave.setDisabled(True)

    def save_enable1(self):
        #---------------------------------------------#
        # Enable/Disable Save Push Button
        #---------------------------------------------#
        print("3rd HIT")
        save_progress=0

        if (self.data_c1 is not None and self.data_p1 is not None):
            #---------------------------------------------#
            # Carrier Size >= Payload Size
            #---------------------------------------------#
            carrier_size = int(self.txtCarrierSize.text())
            payload_size = int(self.txtPayloadSize.text())

            if ( carrier_size > payload_size):
                save_progress += 1

            #---------------------------------------------#
            # Carrier Size does not have previous payload, if it does then chkoverride is checked
            #---------------------------------------------#
            if self.lblPayloadFound.text() is '':
                # No prev Payload
                save_progress += 1
            else:
                # Prev Payload
                active=self.chkOverride.isChecked()
                if(active):
                    save_progress += 1

            #---------------------------------------------#
            # Ready to save progress
            #---------------------------------------------#
            if ( save_progress == 2):
                self.btnSave.setEnabled(True)
                print("         READY TO SAVE")
            else:
                self.btnSave.setDisabled(True)
                print("         NOT YET READY TO SAVE")
        else:
            self.btnSave.setDisabled(True)


    def save_clicked(self):
        print("     SAVE CLICKED")

        #---------------------------------------------#
        # Get new image with embedded data
        #---------------------------------------------#

        carrier = Carrier(img=self.data_c1)
        active=self.chkOverride.isChecked()
        self.new_img_data = carrier.embedPayload(payload=Payload(img=self.data_p1, compressionLevel=self.new_cmp_level), override=active)
        print(self.new_img_data)

        #---------------------------------------------#
        # Bring up the save tab and location stuff
        # Write data to file
        #---------------------------------------------#
        fileName = QtGui.QFileDialog.getSaveFileName(self, 'Save File', '/path/to/default/directory', selectedFilter='*.png')
        if fileName[0]:
            print(fileName[0])
            imsave(fileName[0]+'.png', self.new_img_data)
        print("DATA WRITTEN")


    #---------------------------------------------#
    # TAB 2
    #---------------------------------------------#

    #---------------------------------------------#
    # View Carrier 2 setup and formatting
    #---------------------------------------------#
    def carrier2_dragged(self, event):
        print("     DRAGGING")
        event.accept()
        self.viewCarrier2.dragLeaveEvent = self.img_no_drag
        self.viewCarrier2.dragMoveEvent = self.img_new
        self.viewCarrier2.dropEvent = self.carrier2_dropped

    def carrier2_dropped(self, event):

        #---------------------------------------------#
        # Retrieve location of the image
        #---------------------------------------------#

        print("         DROPPED")
        old_data=event.mimeData().text()
        data=old_data[7:]

        #---------------------------------------------#
        # Checking if .png file dropped
        #---------------------------------------------#
        if '.png' in data:
            event.accept()
            print('         ACCEPTED')
            self.carrier2_show(data.strip())
        else:
            event.ignore()
            print('         IGNORED')

    def carrier2_show(self, location):

        #---------------------------------------------#
        # Show image in view carrier 2
        # Clear Image in view payload 2
        #---------------------------------------------#

        scene = QGraphicsScene()
        pixmap = QPixmap(location)
        self.directory=location
        scene.addPixmap(pixmap)
        self.viewCarrier2.setScene(scene)
        self.viewCarrier2.fitInView(scene.itemsBoundingRect(),  Qt.KeepAspectRatio)

        self.viewPayload2.setScene(None)

        print("             Image Displayed")

        #---------------------------------------------#
        # Read the ndarray of the image
        #---------------------------------------------#
        self.data_c2 = ndimage.imread(location)

        #---------------------------------------------#
        # Check if carrier is empty
        #    - set lblCarrierEmpty
        #    - set btnExtract, btnClean diabled
        #---------------------------------------------#
        print("             Default State Initalized")


        if (Carrier.payloadExists(Carrier(img = self.data_c2)) == False):
            print("         CARRIER EMPTY")
            self.lblCarrierEmpty.setText('>>>> Carrier Empty <<<<')
            self.btnExtract.setEnabled(False)
            self.btnClean.setEnabled(False)
            self.carrier2_payload = False
        else:
            print("         CARRIER NOT EMPTY")
            self.lblCarrierEmpty.setText('')
            self.btnExtract.setEnabled(True)
            self.btnClean.setEnabled(True)
            self.carrier2_payload = True

    #---------------------------------------------#
    # Extract push button setup and formatting
    #---------------------------------------------#
    def extract_clicked(self):
        print("     EXTRACT CLICKED")

        if (self.carrier2_payload):
            #---------------------------------------------#
            # Extract payload
            #---------------------------------------------#
            print("         EXTRACTING PAYLOAD")
            self.new_img_data_2 = Carrier.extractPayload(Carrier(img=self.data_c2)).img
            #print(self.new_img_data_2)

            #---------------------------------------------#
            # Show image in view payload 2
            #---------------------------------------------#
            print("         DISPLAYING IMAGE")
            imsave('temp.png', self.new_img_data_2)
            scene = QGraphicsScene()
            pixmap = QPixmap('temp.png')
            scene.addPixmap(pixmap)
            self.viewPayload2.setScene(scene)
            self.viewPayload2.fitInView(scene.itemsBoundingRect(),  Qt.KeepAspectRatio)
            print("             Image Displayed")

    #---------------------------------------------#
    # Clean push button setup and formatting
    #---------------------------------------------#
    def clean_clicked(self):
        print("     CLEAN CLICKED")

        if (self.carrier2_payload):
            #---------------------------------------------#
            # Clean payload
            #---------------------------------------------#
            print("         CLEANING PAYLOAD")
            self.new_img_data_3 = Carrier.clean(Carrier(img=self.data_c2))
            imsave(self.directory, self.new_img_data_3)
            scene = QGraphicsScene()
            pixmap = QPixmap(self.directory)
            scene.addPixmap(pixmap)
            self.viewCarrier2.setScene(scene)
            self.viewCarrier2.fitInView(scene.itemsBoundingRect(),  Qt.KeepAspectRatio)
            print("             Image Displayed")

            self.viewPayload2.setScene(None)

            if (Carrier.payloadExists(Carrier(img = self.new_img_data_3)) == False):
                print("         CARRIER EMPTY")
                self.lblCarrierEmpty.setText('>>>> Carrier Empty <<<<')
                self.btnExtract.setDisabled(True)
                self.btnClean.setDisabled(True)
                self.carrier2_payload = False
            else:
                print("         CARRIER NOT EMPTY")
                self.lblCarrierEmpty.setText('')
                self.btnExtract.setEnabled(True)
                self.btnClean.setEnabled(True)
                self.carrier2_payload = True


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = SteganographyConsumer()
    currentForm.show()
    currentApp.exec_()