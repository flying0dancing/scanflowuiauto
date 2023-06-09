# -*- coding: utf-8 -*-
import names

#abstract base
base_message=names.o_MessageDialog
base_notice_title=names.hardware_Support_StyleLabel #Hardware Support dialog
base_notice_ok=names.buttons_ListView #import file 30 days ago dialog, Shade Matching dialog
base_notice_cancel=names.buttons_Cancel_DialogButton
base_waiting_progress=names.busyDialog_ContentItem # import data loading progress, export waiting progress
base_notice_space_notEnough=names.not_enough_free_disk_space_on_system_drive_Free_up_disk_space_and_try_again_StyleLabel
#titleBar
titleBar_close=names.titleBar_closeButton_Button
titleBar_menu=names.titleBar_menuButton_Button

#menuList
menuList_Export=names.export_MainMenuButton

#CoverPage
cover_internal_ok=names.oK_StyleButton
cover_button_scan=names.startupScreen_scan_button_StyleButton
cover_button_import=names.startupScreen_import_button_StyleButton
cover_button_iocamera=names.startupScreen_io_camera_button_StyleButton
cover_import_text=names.select_a_folder_in_which_to_import_the_data_file_File_name_Label#select_a_folder_in_which_to_import_the_data_file_File_name_ComboBox
cover_import_ok=names.select_a_folder_in_which_to_import_the_data_file_Open_Button
cover_import_cancel=names.select_a_folder_in_which_to_import_the_data_file_Cancel_Button

#import dialog
importDlg_filename=names.fileNameEdit_QLineEdit
importDlg_open=names.qFileDialog_Open_QPushButton
shadeDlg_title=names.shade_Matching_StyleLabel
noticeDlg_title=names.notice_StyleLabel
noticeDlg_content=names.you_are_importing_scans_acquired_more_than_30_days_ago_Please_pay_attention_to_potential_clinical_difference_while_continuing_the_scan_StyleLabel


#Software Update dialog
softwareUpdateDlg_title = names.software_Update_StyleLabel
softwareUpdateDlg_later = names.buttons_Later_DialogButton_2
softwareUpdateDlg_update = names.buttons_Update_now_DialogButton_2
#step bar
stepBar_scan=names.stepBar_step_scan_StepButton
stepBar_check=names.stepBar_step_check_StepButton
stepBar_adapt=names.stepBar_step_adapt_StepButton
stepBar_export=names.stepBar_step_export_StepButton

#top tool bar
topBar_shadematching=names.mainWindow_toolbar_toolbar_shade_matching_color_csButton

#left tool bar
leftBar_catalog_switch=names.catalog_bar_btn_switch
leftBar_catalog_upper=names.catalog_bar_btn_upper
leftBar_catalog_lower=names.catalog_bar_btn_lower
leftBar_catalog_bite=names.catalog_bar_btn_bite
leftBar_tool_cut=names.toolbar_btn_cut_GroupButton
leftBar_tool_history=names.toolbar_btn_scan_history
leftBar_tool_delete=names.toolbar_btn_delete_all
leftBar_tool_lock=names.scrollArea_toolbar_btn_lock_reverse_GroupButton
leftBar_tool_keep=names.scrollArea_toolbar_btn_remain_area_selection_csStateButton
leftBar_tool_imageGallery=names.toolbar_btn_intraoral
leftBar_tool_parallelismCheck=names.toolbar_btn_parallelism_check
leftBar_tool_occlusionCheck=names.toolbar_btn_measurement
leftBar_tool_toothSelection=names.toolbar_btn_scan_area
leftBar_tool_freeze=names.toolbar_btn_freeze
leftBar_tool_impressArea=names.scrollArea_toolbar_btn_impression_brush_GroupButton
leftBar_tool_preparationCheck1=names.toolbar_btn_preparation_check #only Preparation Scan
leftBar_tool_preparationCheck2=names.scrollArea_toolbar_btn_implant_matching_check_csStateButton
leftBar_tool_quadrant=names.toolbar_btn_quadrant_snapshot
leftBar_tool_shadeMatching=names.scrollArea_toolbar_btn_shade_matching_GroupButton
leftBar_tool_undercut=names.toolbar_btn_undercut
leftBar_tool_marginLine=names.toolbar_btn_margin_line
leftBar_tool_occlusionProximity=names.toolbar_btn_occlusion_pressure
leftBar_tool_rotation=names.toolbar_btn_orientation_adjustment
leftBar_tool_transparency=names.toolbar_btn_transparency
leftBar_tool_dual_view=names.toolbar_btn_dual_view

#acqusition catalog(workflow)
workflow_common=names.catalogBar_workflow_bar_btn_common_StateButton
workflow_common_impress=names.catalogBar_workflow_bar_btn_common_impression_DragButton
workflow_implant_emergenceProfile=names.catalogBar_workflow_bar_btn_emergence_profile_DragButton
workflow_implant_emergenceProfile_impress=names.catalogBar_workflow_bar_btn_implant_impression_DragButton
workflow_implant_scanbody=names.catalogBar_workflow_bar_btn_implant_DragButton
workflow_implant_matching=names.catalogBar_workflow_bar_btn_implant_matching_DragButton #deprecated at 1.0.9.3
workflow_edentulous=names.catalogBar_workflow_bar_btn_edentulous_DragButton
workflow_edentulous_impress=names.catalogBar_workflow_bar_btn_edentulous_impression_DragButton
workflow_preparation=names.catalogBar_workflow_bar_btn_preparation_DragButton
workflow_preparation_impress=names.catalogBar_workflow_bar_btn_preparation_impression_DragButton
workflow_extra=names.catalogBar_workflow_bar_btn_extra_DragButton
workflow_denture=names.catalogBar_workflow_bar_btn_denture_DragButton
workflow_denture_matching=names.catalogBar_workflow_bar_btn_denture_matching_DragButton #deprecated at 1.0.9.3

workflow_add_configscan=names.catalogBar_btnConfig_StyleButton
workflow_panel_denture=names.btnEdentulous_WorkflowButton
workflow_panel_implant=names.btnImplant_WorkflowButton
workflow_panel_preparation=names.btnPreparation_WorkflowButton
workflow_panel_impression=names.btnImpression_WorkflowButton
workflow_panel_extra=names.btnExtra_WorkflowButton

workflow_tip_denture=names.oK_got_it_DialogButton
workflow_tip_denture_dont_show_again=names.don_t_show_again_StyleCheckBox_2
workflow_tip_implant=names.oK_got_it_DialogButton_2
workflow_tip_implant_dont_show_again=names.don_t_show_again_StyleCheckBox_3

workflow_copyDlg_denture_title=names.denture_Scan_StyleLabel
workflow_copyDlg_denture_copyfrom_common=names.copy_scan_data_from_b_Common_Scan_b_StyleImageRadioButton
workflow_copyDlg_denture_new_scan=names.start_a_new_scan_StyleRadioButton
workflow_copyDlg_denture_ok=names.buttons_OK_DialogButton
workflow_copyDlg_denture_cancel=names.buttons_Cancel_DialogButton_3

workflow_copyDlg_emergenceProfile_title=names.emergence_Profile_Scan_StyleLabel
workflow_copyDlg_emergenceProfile_copyfrom_common=names.copy_scan_data_from_b_Common_Scan_b_StyleImageRadioButton_2
workflow_copyDlg_emergenceProfile_new_scan=names.start_a_new_scan_StyleRadioButton_2
workflow_copyDlg_emergenceProfile_ok=names.buttons_OK_DialogButton_2
workflow_copyDlg_emergenceProfile_cancel=names.buttons_Cancel_DialogButton_4

workflow_copyDlg_scanbody_title=names.scanbody_Scan_StyleLabel
workflow_copyDlg_scanbody_copyfrom_common=names.copy_scan_data_from_b_Common_Scan_b_StyleImageRadioButton_3
workflow_copyDlg_scanbody_copyfrom_emergenceProfile=names.copy_scan_data_from_b_Emergence_Profile_Scan_b_StyleImageRadioButton
workflow_copyDlg_scanbody_new_scan=names.start_a_new_scan_StyleRadioButton_3
workflow_copyDlg_scanbody_ok=names.buttons_OK_DialogButton_3
workflow_copyDlg_scanbody_cancel=names.buttons_Cancel_DialogButton_5

workflow_cutHole_next=names.workspace_Next_csButton1
workflow_cutHole_back=names.mainWindow_Back_csButton
workflow_cutHole_emergenceProfile_circlecut=names.mainWindow_Toolbar_EmergenceProfileCutToolbar

#Mesh Quality dialog
meshQualityDlg_title=names.mesh_Quality_QLabel
meshQualityDlg_next=names.workspace_Next_csButton1
meshQualityDlg_rescan=names.rescan_csButton

#refine dialog and refine progress
refineDlg_resolution_type_high=names.refine_view_resolution_frame_button_resolution_high_csButton
refineDlg_resolution_type_standard=names.refine_view_resolution_frame_button_resolution_standard_csButton
refineDlg_resolution_type_low=names.refine_view_resolution_frame_button_resolution_low_csButton
refineDlg_refine_button=names.refine_view_button_frame_button_refine_DelayButton
refineDlg_progress_cancel=names.progress_view_button_cancel_progress

#refine step
refineStep_discardDlg_discard=names.buttons_Discard_DialogButton #Discard dialog-discard
#refineStep_discardDlg_cancel=names.buttons_Cancel_DialogButton  #Discard dialog-cancel
#refine workflow
refineStep_workflow_buttons=names.catalogBar_buttons_RowLayout #workflow's parent
refineStep_workflow_common=names.catalogBar_workflow_bar_btn_common_StateButton
refineStep_workflow_commonImpression=names.catalogBar_workflow_bar_btn_common_impression_DragButton
refineStep_workflow_edentulous=names.catalogBar_workflow_bar_btn_edentulous_DragButton



#export dialog
exportDlg_dialog=names.mainWindow_ExportWidget
exportDlg_close=names.closeButton_GeneralCloseButton
#export dialog - left tabs
exportDlg_tab_send=names.button_list_export_send_Item
exportDlg_tab_open=names.button_list_export_open_Item
exportDlg_tab_save=names.button_list_export_save_Item
exportDlg_tab_3dprint=names.button_list_export_print_Item
exportDlg_tab_share=names.button_list_export_share_Item

#export dialog - bottom buttons on each page
exportDlg_btn_cancel=names.cancel_DialogButton
exportDlg_btn_send=names.send_DialogButton
exportDlg_btn_open=names.open_DialogButton
exportDlg_btn_export=names.export_DialogButton
exportDlg_btn_save=names.save_DialogButton
exportDlg_btn_saveAndExit=names.save_and_Exit_DialogButton
exportDlg_btn_mail=names.mail_it_DialogButton

#export dialog - save page
exportDlg_local_stl=names.radio_button_stl_StyleRadioButton
exportDlg_local_ply=names.radio_button_ply_StyleRadioButton
exportDlg_local_targetfolder=names.txtExportPath_StyleTextField
exportDlg_local_autoopenfolder_checkbox=names.automatically_open_target_directory_after_saving_StyleCheckBox
exportDlg_local_browserfolder=names.btnBrowseExportPath_DialogButton
exportDlg_premium_subscriptDlg_title=names.premium_StyleLabel
exportDlg_premium_subscriptDlg_contentA=names.you_are_currently_on_the_standard_plan_StyleLabel
exportDlg_premium_subscriptDlg_close=names.o_GeneralCloseButton
exportDlg_premium_subscriptDlg_cancel=names.cancel_DialogButtonWithTheme
exportDlg_premium_subscriptDlg_upgrade=names.upgrade_DialogButton

#Exit dialog
exitDlg_exit_button=names.buttons_Exit_DialogButton
exitDlg_cancle_button=names.buttons_Cancel_DialogButton_2
exitDlg_saverawdata_checkbox=names.save_raw_data_StyleCheckBox
exitDlg_savescans_checkbox=names.save_scans_StyleCheckBox

#Patient Windows-Search UI
patient_createNew=names.dEXIS_IS_ScanFlow_DialogButton
#Patient Windows - Patient Info UI
patient_scan=names.dEXIS_IS_ScanFlow_StyleButton #need DEV update
patient_import=names.dEXIS_IS_ScanFlow_StyleButton_3 #need DEV update
patient_iocamero=names.dEXIS_IS_ScanFlow_StyleButton_2 #need DEV update
#Patient Windows - Create Patient Dialog
patient_createDlg_firstname=names.firstName_Loader
patient_createDlg_middlename=names.middleName_StyleTextField
patient_createDlg_lastname=names.lastName_Loader
patient_createDlg_gender=names.genderType_Frame
patient_createDlg_male=names.male_DialogButton
patient_createDlg_female=names.female_DialogButton
patient_createDlg_other=names.other_DialogButton
patient_createDlg_patientId=names.patientId_Loader
patient_createDlg_cancel=names.cancel_DialogButton_2
patient_createDlg_create=names.create_DialogButton

#Premium Feature
premiumDlg_title = names.premium_Feature_StyleLabel
premiumDlg_contentA = names.this_functionality_is_available_only_for_Premium_users_StyleLabel
premiumDlg_contentB = names.please_upgrade_to_use_this_feature_StyleLabel
premiumDlg_close = names.close_button_GeneralCloseButton
premiumDlg_later = names.later_DialogButtonWithTheme
premiumDlg_upgrade = names.upgrade_DialogButton_2


