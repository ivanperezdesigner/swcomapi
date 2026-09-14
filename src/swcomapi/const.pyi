"""Stub for swcomapi.const. Generated, do not edit.

Every enumeration member as a plain module-level name, the way VBA
sees them.

Source: SOLIDWORKS 2026 type libraries (cosworks.tlb, sldcostingapi.tlb, sldworks.tlb,
  sustainability.tlb, swcommands.tlb, swconst.tlb, swdimxpert.tlb,
  swmotionstudy.tlb, swpublished.tlb, SWRoutingLib.tlb)
"""

# sw3DExperienceCfgType_e (SwConst)
swNot3DExperienceType: int = 0
swPhysicalProduct: int = 1
swRepresentation: int = 2

# sw3DExperienceModelType_e (SwConst)
sw3DExperienceModelType_Standard: int = 0
sw3DExperienceModelType_PartSupply: int = 1
sw3DExperienceModelType_3DExperience: int = 2
sw3DExperienceModelType_xCad: int = 3

# sw3DExperienceState_e (SwConst)
sw3DExperienceState_None: int = 0
sw3DExperienceState_Online: int = 1
sw3DExperienceState_Offline: int = 2

# sw3DInterconnectImportErrors_e (SwConst)
sw3DInterconnectImportErrors_None: int = 0
sw3DInterconnectImportErrors_Disabled: int = 1
sw3DInterconnectImportErrors_IncompatibleType: int = 2
sw3DInterconnectImportErrors_AssemblyNotSaved: int = 3
sw3DInterconnectImportErrors_BreakLinkUnavailable: int = 4
sw3DInterconnectImportErrors_ParametersUnavailable: int = 5
sw3DInterconnectImportErrors_TransferOptionNeeded: int = 6

# sw3DPDFAccuracy_e (SwConst)
swMaximum: int = 0
swHigh: int = 1
swMedium: int = 2
swLow: int = 3

# sw3DPMISaveOptions_e (SwConst)
swAddReportToDesignBinder: int = 1
swViewReportOnSave: int = 2
swDimXpertData: int = 4
swReferenceData: int = 8

# swASMSLDPRTCompPref_e (SwConst)
swUseSystemSettings: int = 0
swAlwaysInclude: int = 1
swAlwaysExclude: int = 2

# swAcisOutputGeometryPreference_e (SwConst)
swAcisOutputAsSolidAndSurface: int = 0
swAcisOutputAs3DCurves: int = 1
swAcisOutputAs3DCurves_IncludeSketchEnts: int = 2

# swAcisOutputVersion_e (SwConst)
swAcisOutputVersion_16: int = 0
swAcisOutputVersion_17: int = 1
swAcisOutputVersion_20: int = 2
swAcisOutputVersion_21: int = 3
swAcisOutputVersion_30: int = 4
swAcisOutputVersion_40: int = 5
swAcisOutputVersion_50: int = 6
swAcisOutputVersion_60: int = 7
swAcisOutputVersion_70: int = 8
swAcisOutputVersion_80: int = 9
swAcisOutputVersion_100: int = 10
swAcisOutputVersion_110: int = 11
swAcisOutputVersion_120: int = 12
swAcisOutputVersion_130: int = 13
swAcisOutputVersion_140: int = 14
swAcisOutputVersion_150: int = 15
swAcisOutputVersion_160: int = 16
swAcisOutputVersion_170: int = 17
swAcisOutputVersion_180: int = 18
swAcisOutputVersion_190: int = 19
swAcisOutputVersion_200: int = 20
swAcisOutputVersion_210: int = 21
swAcisOutputVersion_220: int = 22
swAcisOutputVersion_270: int = 23
swAcisOutputVersion_330: int = 24

# swActivateDocError_e (SwConst)
swGenericActivateError: int = 1
swDocNeedsRebuildWarning: int = 2

# swAddComponentConfigOptions_e (SwConst)
swAddComponentConfigOptions_CurrentSelectedConfig: int = 0
swAddComponentConfigOptions_NewConfigWithAllReferenceModels: int = 1
swAddComponentConfigOptions_NewConfigWithAsmStructure: int = 2

# swAddControlOptions_e (SwConst)
swControlOptions_Visible: int = 1
swControlOptions_Enabled: int = 2
swControlOptions_SmallGapAbove: int = 4

# swAddDvePageForCommand_e (SwConst)
swAddDvePageFor_SketchPicture: int = 1

# swAddGroupBoxOptions_e (SwConst)
swGroupBoxOptions_Checkbox: int = 1
swGroupBoxOptions_Checked: int = 2
swGroupBoxOptions_Visible: int = 4
swGroupBoxOptions_Expanded: int = 8

# swAddMateError_e (SwConst)
swAddMateError_ErrorUknown: int = 0
swAddMateError_NoError: int = 1
swAddMateError_IncorrectMateType: int = 2
swAddMateError_IncorrectAlignment: int = 3
swAddMateError_IncorrectSelections: int = 4
swAddMateError_OverDefinedAssembly: int = 5
swAddMateError_IncorrectGearRatios: int = 6

# swAddOrdinateDims_e (SwConst)
swOrdinate: int = 1
swVerticalOrdinate: int = 2
swHorizontalOrdinate: int = 3
swAngularOrdinate: int = 4

# swAddSpecificDimension_e (SwConst)
swAddSpecificDimension_Success: int = 0
swAddSpecificDimension_DimTypeMismatch: int = 1

# swAddToRecentDocumentList_e (SwConst)
swAddToRecentDocumentList_Default: int = 0
swAddToRecentDocumentList_Add: int = 1
swAddToRecentDocumentList_DontAdd: int = 2

# swAddinBrokerBBoxOption_e (SwConst)
swAddinBrokerBBoxOption_Default: int = 0

# swAdditionalSymbol_e (SwConst)
swAdditionalSymbol_None: int = 0
swAdditionalSymbol_Unknown: int = 1
swAdditionalSymbol_TangentPlane: int = 2
swAdditionalSymbol_FreeState: int = 3
swAdditionalSymbol_Statistical: int = 4
swAdditionalSymbol_MaximumUpperTolerance: int = 5
swAdditionalSymbol_MinimumLowerTolerance: int = 6

# swAdvSelectType_e (SwConst)
swAdvSelectType_And: int = 1
swAdvSelectType_Or: int = 2
swAdvSelectType_Is_Yes: int = 16384
swAdvSelectType_Is_No: int = 32768
swAdvSelectType_Is_Not: int = 8
swAdvSelectType_Contains: int = 16
swAdvSelectType_Is_Ccontained_By: int = 32
swAdvSelectType_Interferes_With: int = 64
swAdvSelectType_Does_Not_Interferes_With: int = 128
swAdvSelectType_Is_Exactly: int = 4
swAdvSelectType_Is_Not_Equal: int = 8192
swAdvSelectType_Less_Than: int = 512
swAdvSelectType_Less_Than_OR_Equal: int = 2048
swAdvSelectType_Equals: int = 4096
swAdvSelectType_Greater_Than_OR_Equal: int = 1024
swAdvSelectType_Greater_Than: int = 256

# swAdvWzdGeneralHoleTypes_e (SwConst)
swAdvWzdCounterBore: int = 0
swAdvWzdCounterSink: int = 1
swAdvWzdStraight: int = 2
swAdvWzdStraightTap: int = 3
swAdvWzdTaperTap: int = 4

# swAdvancedHoleResults_e (SwConst)
swAdvancedHoleResults_Success: int = 0
swAdvancedHoleResults_FailedIncorrectHoleElementParameters: int = 1

# swAdvancedRouteSelectionOutput_e (SWRoutingLib)
swBoth: int = 0
swSelectOnly: int = 1
swDataOnly: int = 2

# swAlignDimensionType_e (SwConst)
swAlignDimensionType_AutoArrange: int = 0
swAlignDimensionType_SpaceEvenly: int = 1
swAlignDimensionType_Colinear: int = 2
swAlignDimensionType_Stagger: int = 3
swAlignDimensionType_TopAlignText: int = 4
swAlignDimensionType_BottomAlignText: int = 5
swAlignDimensionType_LeftAlignText: int = 6
swAlignDimensionType_RightAligntext: int = 7

# swAlignDrawingViewTypes_e (SwConst)
swHorizontalToSheetClockwise: int = 0
swHorizontalToSheetCounterclockwise: int = 1
swDefaultAlignment: int = 2
swProjectedAngle: int = 3

# swAlignViewTypes_e (SwConst)
swNoViewAlignment: int = 0
swDefaultViewAlignment: int = 1
swAlignViewHorizontalCenter: int = 2
swAlignViewVerticalCenter: int = 3
swAlignViewHorizontalOrigin: int = 4
swAlignViewVerticalOrigin: int = 5

# swAngleUnit_e (SwConst)
swDEGREES: int = 0
swDEG_MIN: int = 1
swDEG_MIN_SEC: int = 2
swRADIANS: int = 3

# swAngularEquationUnits_e (SwConst)
swAngularEquationUnitsUnrecognized: int = 0
swAngularEquationUnitsDegrees: int = 1
swAngularEquationUnitsRadians: int = 2

# swAnimationOutputType_e (SwConst)
swAnimationOutput_AVI: int = 1
swAnimationOutput_Series_of_BMP: int = 2
swAnimationOutput_Series_of_TGA: int = 3
swAnimationOutput_Series_of_PNG: int = 4
swAnimationOutput_Series_of_JPG: int = 5
swAnimationOutput_Series_of_TIF: int = 6
swAnimationOutput_Series_of_MP4: int = 7
swAnimationOutput_Series_of_MKV: int = 8
swAnimationOutput_Series_of_FLV: int = 9
swAnimationOutput_Series_of_LXO: int = 10

# swAnimationPlayMode_e (SwConst)
swAnimationPlayModeNormal: int = 1
swAnimationPlayModeLoop: int = 2
swAnimationPlayModeReciprocate: int = 3

# swAnimationPlaySpeed_e (SwConst)
swAnimationPlaySpeedNormal: int = 1
swAnimationPlaySpeedSlow: int = 2
swAnimationPlaySpeedFast: int = 3

# swAnimatorAxisOfRotation_e (SwConst)
swRotationAboutXAxis: int = 0
swRotationAboutYAxis: int = 1
swRotationAboutZAxis: int = 2

# swAnimatorDirectionOfRotation_e (SwConst)
swRotationClockwise: int = 0
swRotationCounterClockwise: int = 1

# swAnnotationOwner_e (SwConst)
swAnnotationOwner_DrawingView: int = 0
swAnnotationOwner_DrawingSheet: int = 1
swAnnotationOwner_DrawingTemplate: int = 2
swAnnotationOwner_Part: int = 3
swAnnotationOwner_Assembly: int = 4

# swAnnotationType_e (SwConst)
swCThread: int = 1
swDatumTag: int = 2
swDatumTargetSym: int = 3
swDisplayDimension: int = 4
swGTol: int = 5
swNote: int = 6
swSFSymbol: int = 7
swWeldSymbol: int = 8
swCustomSymbol: int = 9
swDowelSym: int = 10
swLeader: int = 11
swBlock: int = 12
swCenterMarkSym: int = 13
swTableAnnotation: int = 14
swCenterLine: int = 15
swDatumOrigin: int = 16
swWeldBeadSymbol: int = 17
swRevisionCloud: int = 18
swPMIOnly: int = 19

# swAnnotationVisibilityState_e (SwConst)
swAnnotationVisibilityUnknown: int = 0
swAnnotationVisible: int = 1
swAnnotationHalfHidden: int = 2
swAnnotationHidden: int = 3

# swApiHoleWizardItemExportStatus_e (SwConst)
swApiHoleWizardItemExportStatus_Success: int = 0
swApiHoleWizardItemExportStatus_InvalidArgument: int = 1
swApiHoleWizardItemExportStatus_MicrosoftExcelNotInstalled: int = 2

# swApiHoleWizardItemImportStatus_e (SwConst)
swApiHoleWizardItemImportStatus_Success: int = 0
swApiHoleWizardItemImportStatus_InvalidArgument: int = 1
swApiHoleWizardItemImportStatus_MicrosoftExcelNotInstalled: int = 2
swApiHoleWizardItemImportStatus_FailedToSaveFile: int = 3
swApiHoleWizardItemImportStatus_ExcelCouldNotOpenFile: int = 4
swApiHoleWizardItemImportStatus_ExcelSheetNameError: int = 5
swApiHoleWizardItemImportStatus_FailedToSaveReportFile: int = 6
swApiHoleWizardItemImportStatus_DataError: int = 7
swApiHoleWizardItemImportStatus_UnspecifiedError: int = 8

# swApiToolboxItemExportStatus_e (SwConst)
swApiToolboxItemExportStatus_Success: int = 0
swApiToolboxItemExportStatus_InvalidArgument: int = 1
swApiToolboxItemExportStatus_MicrosoftExcelNotInstalled: int = 2
swApiToolboxItemExportStatus_FailedToSaveFile: int = 3
swApiToolboxItemExportStatus_InvalidPartNumber: int = 4

# swApiToolboxItemImportStatus_e (SwConst)
swApiToolboxItemImportStatus_Success: int = 0
swApiToolboxItemImportStatus_InvalidArgument: int = 1
swApiToolboxItemImportStatus_MicrosoftExcelNotInstalled: int = 2
swApiToolboxItemImportStatus_FailedToSaveFile: int = 3
swApiToolboxItemImportStatus_ExcelImportDidNotFindColumn: int = 4
swApiToolboxItemImportStatus_ExcelImportWrongFile: int = 5
swApiToolboxItemImportStatus_ExcelCouldNotOpenFile: int = 6
swApiToolboxItemImportStatus_InvalidPartNumber: int = 7
swApiToolboxItemImportStatus_FailedUnspecifiedError: int = 8

# swAppCallBackCmd_e (SwConst)
swAppIsNewCmd: int = 1
swAppWhatsNewDescription: int = 2
swAppHelpContext: int = 3
swAppIsCmdEnabled: int = 4
swAppPostNotifyEvent: int = 5

# swAppNotify_e (SwConst)
swAppFileOpenNotify: int = 1
swAppFileNewNotify: int = 2
swAppDestroyNotify: int = 3
swAppActiveDocChangeNotify: int = 4
swAppActiveModelDocChangeNotify: int = 5
swAppPropertySheetCreateNotify: int = 6
swAppNonNativeFileOpenNotify: int = 7
swAppLightSheetCreateNotify: int = 8
swAppDocumentConversionNotify: int = 9
swAppLightweightComponentOpenNotify: int = 10
swAppDocumentLoadNotify: int = 11
swAppFileNewNotify2: int = 12
swAppFileOpenNotify2: int = 13
swAppReferenceNotFoundNotify: int = 14
swAppPromptForFilenameNotify: int = 15
swAppBeginTranslationNotify: int = 16
swAppEndTranslationNotify: int = 17
swAppLightPMCreateNotify: int = 18
swAppStandardsDatabaseChangeNotify: int = 19
swAppOnIdleNotify: int = 20
swAppFileOpenPreNotify: int = 21
swAppFileOpenPostNotify: int = 22
swAppReferencedFilePreNotify: int = 23
swAppBeginRecordNotify: int = 24
swAppEndRecordNotify: int = 25
swAppFileNewPreNotify: int = 26
swAppJournalWriteNotify: int = 27
swAppDocumentLoadNotify2: int = 28
swAppCommandCloseNotify: int = 29
swAppPromptForMultipleFilenamesNotify: int = 30
swAppCommandOpenPreNotify: int = 31
swAppFileCloseNotify: int = 32
swAppBackgroundProcessingStartNotify: int = 33
swAppBackgroundProcessingEndNotify: int = 34
swAppInterfaceBrightnessThemeChangeNotify: int = 35
swAppReferencedFilePreNotify2: int = 36
swAppBegin3DInterconnectTranslationNotify: int = 37
swAppEnd3DInterconnectTranslationNotify: int = 38
swAppTaskPanePinnedNotify: int = 39
swAppTaskPaneUnpinnedNotify: int = 40
swAppTaskPaneHideNotify: int = 41
swAppTaskPaneShowNotify: int = 42
swAppTaskPaneExpandNotify: int = 43
swAppTaskPaneCollapseNotify: int = 44
swAppDisplayPaneActivationNotify: int = 45
swAppOn3DExperienceStateChangeNotify: int = 46

# swAppearanceSurfaceFinishShaderTypes_e (SwConst)
swAppearanceSurfaceFinishShaderType_DefaultColor: int = 0
swAppearanceSurfaceFinishShaderType_None: int = 1
swAppearanceSurfaceFinishShaderType_FromFile: int = 2
swAppearanceSurfaceFinishShaderType_Brushed: int = 3
swAppearanceSurfaceFinishShaderType_Burnished: int = 4
swAppearanceSurfaceFinishShaderType_Cast: int = 5
swAppearanceSurfaceFinishShaderType_Wrought: int = 6
swAppearanceSurfaceFinishShaderType_Machined: int = 7
swAppearanceSurfaceFinishShaderType_Knurled: int = 8
swAppearanceSurfaceFinishShaderType_Treadplate1: int = 9
swAppearanceSurfaceFinishShaderType_Dimpled: int = 10
swAppearanceSurfaceFinishShaderType_ChainLink: int = 11
swAppearanceSurfaceFinishShaderType_Sandblasted: int = 12
swAppearanceSurfaceFinishShaderType_Rough1: int = 13
swAppearanceSurfaceFinishShaderType_Rough2: int = 14
swAppearanceSurfaceFinishShaderType_DiamondTreadplate: int = 15
swAppearanceSurfaceFinishShaderType_Treadplate2: int = 16
swAppearanceSurfaceFinishShaderType_DiamondHoleMesh: int = 17
swAppearanceSurfaceFinishShaderType_CircularHoleMesh: int = 18
swAppearanceSurfaceFinishShaderType_CustomHoleMesh: int = 19
swAppearanceSurfaceFinishShaderType_Undefined: int = 20

# swAppearanceTargetType_e (SwConst)
swAppearanceTargetFace: int = 0
swAppearanceTargetFeature: int = 1
swAppearanceTargetBody: int = 2
swAppearanceTargetPart: int = 3
swAppearanceTargetComponent: int = 4
swAppearanceTargetAppearanceFilter: int = 5

# swApplicationType_e (SwConst)
swApplicationType_Desktop: int = 0
swApplicationType_3DEXPERIENCE: int = 1
swApplicationType_WithConnector: int = 2

# swArcEndCondition_e (SwConst)
swArcEndConditionNone: int = 0
swArcEndConditionCenter: int = 1
swArcEndConditionMin: int = 2
swArcEndConditionMax: int = 3

# swArcLengthLeaderType_e (SwConst)
swArcLengthLeaderParallel: int = 1
swArcLengthLeaderRadial: int = 2

# swAreaHatchFillStyle_e (SwConst)
swAreaHatchFillStyle_None: int = 1
swAreaHatchFillStyle_Pattern: int = 2
swAreaHatchFillStyle_Solid: int = 3

# swAreaHatchingScope_e (SwConst)
swAreaHatchingScope_Region: int = 0
swAreaHatchingScope_Component: int = 1
swAreaHatchingScope_View: int = 2
swAreaHatchingScope_Body: int = 3

# swArrowDirection_e (SwConst)
swINSIDE: int = 0
swOUTSIDE: int = 1
swSMART: int = 2

# swArrowPlacement_e (SwConst)
swArrowPlacementLegacy: int = 0
swArrowPlacementSmartArrowFollowText: int = 1
swArrowPlacementSmartArrowRemainAttachedToArc: int = 2

# swArrowPosition (SwConst)
swArrowLeftTop: int = 0
swArrowLeftBottom: int = 1
swArrowRightTop: int = 2
swArrowRightBottom: int = 3
swArrowUpTopLeft: int = 4
swArrowUpTopRight: int = 5
swArrowDownBottomLeft: int = 6
swArrowDownBottomRight: int = 7
swArrowLeftOrRightTop: int = 8
swArrowLeftOrRightBottom: int = 9
swArrowLeftOrRight: int = 10
swArrowUpOrDownLeft: int = 11
swArrowUpOrDownRight: int = 12
swArrowUpOrDown: int = 13
swArrowNone: int = 14
swArrowUnknown: int = 15

# swArrowStyle_e (SwConst)
swOPEN_ARROWHEAD: int = 0
swCLOSED_ARROWHEAD: int = 1
swSLASH_ARROWHEAD: int = 2
swDOT_ARROWHEAD: int = 3
swORIGIN_ARROWHEAD: int = 4
swWIDE_ARROWHEAD: int = 5
swISOWIDE_ARROWHEAD: int = 6
swRUS_ARROWHEAD: int = 7
swCLOSETOP_ARROWHEAD: int = 8
swCLOSEBOT_ARROWHEAD: int = 9
swNO_ARROWHEAD: int = 10
swSHOULDER_ARROWHEAD: int = 11
swSMART_ARROWHEAD: int = 12

# swAssemblyDeleteOptions_e (SwConst)
swDelete_SubAssembly: int = 1
swDelete_SelectedComponents: int = 0

# swAssemblyExplodeStepType (SwConst)
swAssemblyExplodeStepType_Translate: int = 0
swAssemblyExplodeStepType_Radial: int = 1
swAssemblyExplodeStepType_SubAssembly: int = 2

# swAssemblyLevelToUpdate_e (SwConst)
swAssemblyLevelToUpdate_TopLevelAssemblyOnly: int = 0
swAssemblyLevelToUpdate_SubLevelAssemblyOnly: int = 1
swAssemblyLevelToUpdate_AllLevels: int = 2

# swAssemblyLoadComponents_e (SwConst)
swAssemblyLoadComponents_AutoLoad: int = 0
swAssemblyLoadComponents_ManualLoad: int = 1

# swAssemblyMode_e (SwConst)
swAssemblyMode_None: int = 0
swAssemblyMode_Resolved: int = 1
swAssemblyMode_LightWeight: int = 2
swAssemblyMode_LDR: int = 3
swAssemblyMode_LDR_EditAssembly: int = 4

# swAssemblyNotify_e (SwConst)
swAssemblyRegenNotify: int = 1
swAssemblyDestroyNotify: int = 2
swAssemblyRegenPostNotify: int = 3
swAssemblyViewNewNotify: int = 4
swAssemblyNewSelectionNotify: int = 5
swAssemblyFileSaveNotify: int = 6
swAssemblyFileSaveAsNotify: int = 7
swAssemblyLoadFromStorageNotify: int = 8
swAssemblySaveToStorageNotify: int = 9
swAssemblyConfigChangeNotify: int = 10
swAssemblyConfigChangePostNotify: int = 11
swAssemblyAutoSaveNotify: int = 12
swAssemblyAutoSaveToStorageNotify: int = 13
swAssemblyBeginInContextEditNotify: int = 14
swAssemblyEndInContextEditNotify: int = 15
swAssemblyViewNewNotify2: int = 16
swAssemblyLightingDialogCreateNotify: int = 17
swAssemblyAddItemNotify: int = 18
swAssemblyRenameItemNotify: int = 19
swAssemblyDeleteItemNotify: int = 20
swAssemblyModifyNotify: int = 21
swAssemblyComponentStateChangeNotify: int = 22
swAssemblyFileDropNotify: int = 23
swAssemblyFileReloadNotify: int = 24
swAssemblyComponentStateChangeNotify2: int = 25
swAssemblyAddCustomPropertyNotify: int = 26
swAssemblyChangeCustomPropertyNotify: int = 27
swAssemblyDeleteCustomPropertyNotify: int = 28
swAssemblyFeatureEditPreNotify: int = 29
swAssemblyFeatureSketchEditPreNotify: int = 30
swAssemblyFileSaveAsNotify2: int = 31
swAssemblyInterferenceNotify: int = 32
swAssemblyDeleteSelectionPreNotify: int = 33
swAssemblyFileReloadPreNotify: int = 34
swAssemblyComponentMoveNotify: int = 35
swAssemblyComponentVisibleChangeNotify: int = 36
swAssemblyBodyVisibleChangeNotify: int = 37
swAssemblyFileDropPreNotify: int = 38
swAssemblyFileSavePostNotify: int = 39
swAssemblyLoadFromStorageStoreNotify: int = 40
swAssemblySaveToStorageStoreNotify: int = 41
swAssemblyFeatureManagerTreeRebuildNotify: int = 42
swAssemblyElectricalDataUpdateNotify: int = 43
swAssemblyComponentMoveNotify2: int = 44
swAssemblyDynamicHighlightNotify: int = 45
swAssemblyComponentVisualPropertiesChangeNotify: int = 46
swAssemblyComponentDisplayStateChangeNotify: int = 47
swAssemblyDimensionChangeNotify: int = 48
swAssemblyFileReloadCancelNotify: int = 49
swAssemblyFileSavePostCancelNotify: int = 50
swAssemblySketchSolveNotify: int = 51
swAssemblyDeleteItemPreNotify: int = 52
swAssemblyClearSelectionsNotify: int = 53
swAssemblyFileDropPostNotify: int = 54
swAssemblyEquationEditorPreNotify: int = 55
swAssemblyEquationEditorPostNotify: int = 56
swAssemblyOpenDesignTableNotify: int = 57
swAssemblyCloseDesignTableNotify: int = 58
swAssemblyPromptBodiesToKeepNotify: int = 59
swAssemblyAddDvePagePreNotify: int = 60
swAssemblyUnitsChangeNotify: int = 61
swAssemblyDestroyNotify2: int = 62
swAssemblyConfigurationChangeNotify: int = 63
swAssemblyComponentReorganizeNotify: int = 64
swAssemblySuppressionStateChangeNotify: int = 65
swAssemblyActiveViewChangeNotify: int = 66
swAssemblyFeatureManagerFilterStringChangeNotify: int = 67
swAssemblyFlipLoopNotify: int = 68
swAssemblySensorAlertPreNotify: int = 69
swAssemblyActiveDisplayStateChangePreNotify: int = 70
swAssemblyActiveDisplayStateChangePostNotify: int = 71
swAssemblyAddMatePostNotify: int = 72
swAssemblyComponentConfigurationChangeNotify: int = 73
swAssemblyUndoPostNotify: int = 74
swAssemblyUserSelectionPreNotify: int = 75
swAssemblyRedoPostNotify: int = 76
swAssemblyRedoPreNotify: int = 77
swAssemblyUndoPreNotify: int = 78
swAssemblyComponentReferredDisplayStateChangeNotify: int = 79
swAssemblySelectiveOpenPostNotify: int = 80
swAssemblyRegenPostNotify2: int = 81
swAssemblyAutoSaveToStorageStoreNotify: int = 82
swAssemblyDragStateChangeNotify: int = 83
swAssemblyInsertTableNotify: int = 84
swAssemblyModifyTableNotify: int = 85
swAssemblyUserSelectionPostNotify: int = 86
swAssemblyComponentDisplayModeChangePreNotify: int = 87
swAssemblyComponentDisplayModeChangePostNotify: int = 88
swAssemblyCommandManagerTabActivatedPreNotify: int = 89
swAssemblyPreRenameItemNotify: int = 90
swAssemblyRenamedDocumentNotify: int = 91
swAssemblyFeatureManagerTabActivatedPreNotify: int = 92
swAssemblyFeatureManagerTabActivatedNotify: int = 93
swAssemblyPublishTo3DPDFNotify: int = 94
swAssemblyAddMatePostNotify2: int = 95
swAssemblyComponentStateChangeNotify3: int = 96
swAssemblyRenameDisplayTitleNotify: int = 97
swAssemblyActiveAnnotationViewChangeNotify: int = 98
swAssemblyDisplayPaneExpandNotify: int = 99
swAssemblyDisplayPaneCollapseNotify: int = 100
swAssemblyLargeDesignReviewStateChangeNotify: int = 101
swAssemblySolidBodyFolderReorderNotify: int = 102
swAssemblyAddDependencyNotify: int = 103
swAssemblyDeleteDependencyNotify: int = 104

# swAssemblyUpdateToolboxComponentStatus_e (SwConst)
swAssemblyUpdateToolboxComponentStatus_Success: int = 0
swAssemblyUpdateToolboxComponentStatus_Failed: int = 1
swAssemblyUpdateToolboxComponentStatus_ToolboxNotRegistered: int = 2

# swAssociatedEntityStates_e (SwConst)
swIsEntityInvalid: int = 0
swIsEntitySuppressed: int = 1
swIsEntityAmbiguous: int = 2
swIsEntityDeleted: int = 3

# swAttachAnnotationOption_e (SwConst)
swAttachAnnotationOption_Sheet: int = 1
swAttachAnnotationOption_View: int = 2

# swAttributeCallbackOptions_e (SwConst)
swACBRequiresCallback: int = 1

# swAttributeCallbackReturnValues_e (SwConst)
swACBDeleteIt: int = 1

# swAttributeCallbackTypes_e (SwConst)
swACBDelete: int = 0

# swAutoHideShowResponse_e (SwConst)
swAutoHideShowResponse_Automatic: int = 1
swAutoHideShowResponse_Hide: int = 2
swAutoHideShowResponse_Show: int = 3

# swAutoInsertCenterMarkTypes_e (SwConst)
swAutoInsertCenterMarkType_Hole: int = 1
swAutoInsertCenterMarkType_Fillets: int = 2
swAutoInsertCenterMarkType_Slots: int = 4

# swAutoMateRepairErrors_e (SwConst)
swAutoMateRepairErrors_Unknown: int = -1
swAutoMateRepairErrors_Success: int = 0
swAutoMateRepairErrors_PartialSuccess: int = 1
swAutoMateRepairErrors_NoSelection: int = 2
swAutoMateRepairErrors_InvalidSelection: int = 3
swAutoMateRepairErrors_Failed: int = 4

# swAutoRouteAutoTangencyMode_e (SWRoutingLib)
swAutoTangencyMode_OFF: int = 0
swAutoTangencyMode_ON: int = 1

# swAutoRouteConversionMode_e (SWRoutingLib)
swFlexibleAutoRouteMode: int = 1
swOrthogonalAutoRouteMode: int = 2

# swAutoRouteErrorType_e (SWRoutingLib)
swAutoRouteSuccess: int = 0
swAutoRouteEntityTypeAndEntityIdMismatch: int = 1
swAutoRouteFailed: int = 2

# swAutoRouteSketchEntitiesTypes_e (SWRoutingLib)
swAutoRouteSketchEntitiesType_Point: int = 0
swAutoRouteSketchEntitiesType_Line: int = 1
swAutoRouteSketchEntitiesType_Arc: int = 2
swAutoRouteSketchEntitiesType_Spline: int = 3

# swAutoSaveIntervalMode_e (SwConst)
swAutoSaveIntervalMode_Changes: int = 1
swAutoSaveIntervalMode_Minutes: int = 2

# swAutodimEntities_e (SwConst)
swAutodimEntitiesBasedOnPreselect: int = 0
swAutodimEntitiesAll: int = 1
swAutodimEntitiesSelected: int = 2

# swAutodimHorizontalPlacement_e (SwConst)
swAutodimHorizontalPlacementBelow: int = -1
swAutodimHorizontalPlacementAbove: int = 1

# swAutodimMark_e (SwConst)
swAutodimMarkEntities: int = 1
swAutodimMarkHorizontalDatum: int = 2
swAutodimMarkVerticalDatum: int = 4
swAutodimMarkOriginDatum: int = 8

# swAutodimScheme_e (SwConst)
swAutodimSchemeBaseline: int = 1
swAutodimSchemeOrdinate: int = 2
swAutodimSchemeChain: int = 3
swAutodimSchemeCenterline: int = 4

# swAutodimStatus_e (SwConst)
swAutodimStatusSuccess: int = 0
swAutodimStatusBadOptionValue: int = 1
swAutodimStatusNoActiveDoc: int = 2
swAutodimStatusDocTypeNotSupported: int = 3
swAutodimStatusNoActiveSketch: int = 4
swAutodimStatus3DSketchNotSupported: int = 5
swAutodimStatusSketchIsEmpty: int = 6
swAutodimStatusSketchIsOverDefined: int = 7
swAutodimStatusNoEntities: int = 8
swAutodimStatusEntitiesNotValid: int = 9
swAutodimStatusCenterlineNotAllowed: int = 10
swAutodimStatusDatumNotSupplied: int = 11
swAutodimStatusDatumNotUnique: int = 12
swAutodimStatusDatumNotValidType: int = 13
swAutodimStatusDatumLineNotCenterline: int = 14
swAutodimStatusDatumLineNotVertical: int = 15
swAutodimStatusDatumLineNotHorizontal: int = 16
swAutodimStatusAlgorithmFailed: int = 17
swAutodimStatusSketchNoSolutionFound: int = 18

# swAutodimVerticalPlacement_e (SwConst)
swAutodimVerticalPlacementLeft: int = -1
swAutodimVerticalPlacementRight: int = 1

# swBBoxDescriptionApplyMethod_e (SwConst)
swBBoxDescriptionApplyMethod_New: int = 0
swBBoxDescriptionApplyMethod_ExistingAndNew: int = 1

# swBOMConfigurationAnchorType_e (SwConst)
swBOMConfigurationAnchor_TopLeft: int = 1
swBOMConfigurationAnchor_TopRight: int = 2
swBOMConfigurationAnchor_BottomLeft: int = 3
swBOMConfigurationAnchor_BottomRight: int = 4

# swBOMConfigurationCreationErrors_e (SwConst)
swBOMTableCreation_Okay: int = 0
swBOMTableCreation_UnspecifiedError: int = -1
swBOMTableCreation_MustBeDrawingView: int = -2
swBOMTableCreation_AlreadyExists: int = -3
swBOMTableCreation_ExcelDisabled: int = -4
swBOMTableCreation_Failed: int = -5
swBOMTableCreation_NoModelForView: int = -6

# swBOMConfigurationWhatToShow_e (SwConst)
swBOMConfiguration_ShowPartsOnly: int = 1
swBOMConfiguration_ShowPartsAndTopLevelAsm: int = 2
swBOMConfiguration_ShowAllInIndentedList: int = 3

# swBOMControlMissingRowDisplay_e (SwConst)
swBOMControlShowMissingRow: int = 1
swBOMControlHideMissingRow: int = 2
swBOMControlStrikeMissingRow: int = 3

# swBOMControlSplitDirection_e (SwConst)
swBOMControlSplitRight: int = 1
swBOMControlSplitLeft: int = 2

# swBOMPartNumberSource_e (SwConst)
swBOMPartNumber_DocumentName: int = 1
swBOMPartNumber_ConfigurationName: int = 2
swBOMPartNumber_ParentName: int = 4
swBOMPartNumber_UserSpecified: int = 8

# swBOMTableObjectType_e (SwConst)
swBOMTableObjectType_RowIndex: int = 1
swBOMTableObjectType_CutList: int = 2

# swBackgroundProcessOption_e (SwConst)
swBackgroundProcessing_Disabled: int = 0
swBackgroundProcessing_Enabled: int = 1
swBackgroundProcessing_DeferToApplication: int = 2

# swBalloonFit_e (SwConst)
swBF_Tightest: int = 0
swBF_1Char: int = 1
swBF_2Chars: int = 2
swBF_3Chars: int = 3
swBF_4Chars: int = 4
swBF_5Chars: int = 5
swBF_UserDef: int = 6

# swBalloonItemNumbersOrder_e (SwConst)
swBalloonItemNumbers_DoNotChangeItemNumbers: int = 1
swBalloonItemNumbers_FollowAssemblyOrder: int = 2
swBalloonItemNumbers_OrderSequentially: int = 4
swBalloonItemNumbers_NotApplicable: int = 4096

# swBalloonLayoutType_e (SwConst)
swDetailingBalloonLayout_Square: int = 1
swDetailingBalloonLayout_Circle: int = 2
swDetailingBalloonLayout_Top: int = 3
swDetailingBalloonLayout_Bottom: int = 4
swDetailingBalloonLayout_Right: int = 5
swDetailingBalloonLayout_Left: int = 6

# swBalloonQuantityPlacement_e (SwConst)
swBalloonQuantityPlacement_Left: int = 0
swBalloonQuantityPlacement_Right: int = 1
swBalloonQuantityPlacement_Top: int = 2
swBalloonQuantityPlacement_Bottom: int = 3
swBalloonQuantityPlacement_NotApplicable: int = -1

# swBalloonStyle_e (SwConst)
swBS_None: int = 0
swBS_Circular: int = 1
swBS_Triangle: int = 2
swBS_Hexagon: int = 3
swBS_Box: int = 4
swBS_Diamond: int = 5
swBS_Pentagon: int = 6
swBS_SplitCirc: int = 7
swBS_FlagPentagon: int = 8
swBS_FlagTriangle: int = 9
swBS_Underline: int = 10
swBS_Square: int = 11
swBS_SCircle: int = 12
swBS_Inspection: int = 13
swBS_ArcBracket: int = 14
swBS_RectBracket: int = 15
swBS_ArclenSym: int = 16
swBS_FixedSym: int = 17
swBS_DoubleArrow: int = 18
swBS_SplitSquare: int = 19
swBS_Verbose: int = 20

# swBalloonTextContent_e (SwConst)
swBalloonTextCustom: int = 0
swBalloonTextItemNumber: int = 1
swBalloonTextQuantity: int = 2
swBalloonTextCustomProperties: int = 3
swBalloonTextComponentReference: int = 4
swBalloonTextSpoolReference: int = 5
swBalloonTextPartNumberBOM: int = 6
swBalloonTextFileName: int = 7
swBalloonTextCutlistProperties: int = 8
swBalloonTextViewSheet: int = 9
swBalloonTextViewSheetWithLabel: int = 10
swBalloonTextViewZone: int = 11
swBalloonTextViewViewLetter: int = 12

# swBasicDimType_e (SwConst)
swBasicDimType_Chain: int = 0
swBasicDimType_Baseline: int = 1
swBasicDimType_Polar: int = 2

# swBendAllowanceTypes_e (SwConst)
swBendAllowanceBendTable: int = 1
swBendAllowanceKFactor: int = 2
swBendAllowanceDirect: int = 3
swBendAllowanceDeduction: int = 4
swBendAllowanceBendCalculationTable: int = 5
swBendAllowanceGaugeTable: int = 6

# swBendDirection_e (SwConst)
swBendDirection_ERROR: int = 0
swBendDirection_UP: int = 1
swBendDirection_DOWN: int = 2

# swBendLineControlOption_e (SwConst)
swBendLineControl_NumberOfBendLine: int = 0
swBendLineControl_MaximumDeviation: int = 1

# swBendLineDirection_e (SwConst)
swNotBendLine: int = 0
swUpDirection: int = 1
swDownDirection: int = 2

# swBendNoteAttribute_e (SwConst)
swBendNoteAttribute_BendDirection: int = 1
swBendNoteAttribute_SupplementaryAngle: int = 2
swBendNoteAttribute_ComplementaryAngle: int = 3
swBendNoteAttribute_BendRadius: int = 4
swBendNoteAttribute_BendOrder: int = 5
swBendNoteAttribute_BendAllowance: int = 6

# swBendNoteStyle_e (SwConst)
swAboveBendLine: int = 0
swBelowBendLine: int = 1
swWithLeader: int = 2

# swBendTableTagStyle_e (SwConst)
swBendTable_AlphaNumericTags: int = 1
swBendTable_NumericTags: int = 2

# swBendType_e (SwConst)
swSharpBend: int = 0
swRoundBend: int = 1
swFlatBend: int = 2
swNoneBend: int = 3
swBaseBend: int = 4
swMiterBend: int = 5
swFlat3dBend: int = 6
swMirrorBend: int = 7
swEdgeFlangeBend: int = 8
swHemBend: int = 9
swFreeFormBend: int = 10
swRuledBend: int = 11
swLoftedBend: int = 12

# swBitMaps (SwConst)
swBitMapNone: int = 0
swBitMapUserDefined: int = 1
swBitMapTreeError: int = 2

# swBitmapControlStandardTypes_e (SwConst)
swBitmapControl_Volume: int = 1

# swBlockDefinitionExtFileStatus_e (SwConst)
swBlockDefinitionExtFile_Failed: int = -1
swBlockDefinitionExtFile_Success: int = 0
swBlockDefinitionExtFile_NotLinked: int = 1
swBlockDefinitionExtFile_MissingReference: int = 2
swBlockDefinitionExtFile_OutOfDateReference: int = 3

# swBlockInstanceTextDisplay_e (SwConst)
swBlockInstanceTextDisplayNone: int = 1
swBlockInstanceTextDisplayAll: int = 2
swBlockInstanceTextDisplayNormal: int = 3

# swBlockingStates_e (SwConst)
swNoBlock: int = 0
swFullBlock: int = 1
swModifyBlock: int = 2
swPartialModifyBlock: int = 3
swEditorBlock: int = 4
swEditSketchBlock: int = 5
swSystemBlock: int = 6
swViewOnlyBlock: int = 7
swEditSketchAllowExitBlock: int = 8

# swBodyFolderFeatureType_e (SwConst)
swSolidBodyFolder: int = 1
swSurfaceBodyFolder: int = 2
swBodySubFolder: int = 3
swWeldmentSubFolder: int = 4
swWeldmentCutListFolder: int = 5

# swBodyInfo_e (SwConst)
swUserBody_e: int = 0
swNormalBody_e: int = 1

# swBodyMaterialApplicationError_e (SwConst)
swBodyMaterialApplicationError_UnknownError: int = -1
swBodyMaterialApplicationError_NoError: int = 1
swBodyMaterialApplicationError_ReadOnly: int = 2
swBodyMaterialApplicationError_ExternalReference: int = 3
swBodyMaterialApplicationError_RolledBackState: int = 4
swBodyMaterialApplicationError_InvalidConfigName: int = 5
swBodyMaterialApplicationError_InvalidMaterialNameOrDbName: int = 6

# swBodyOperationError_e (SwConst)
swBodyOperationUnknownError: int = -1
swBodyOperationNoError: int = 0
swBodyOperationNonApiBody: int = 1
swBodyOperationWrongType: int = 2
swBodyOperationBooleanFail: int = 1058
swBodyOperationNoIntersect: int = 1067
swBodyOperationNonManifold: int = 547
swBodyOperationPartialCoincidence: int = 1040
swBodyOperationIntersectSolidWithSheets: int = 972
swBodyOperationUniteSolidSheet: int = 543
swBodyOperationMissingGeom: int = 96
swBodyOperationSameToolAndTarget: int = 545
swBodyOperationFailGeomCondition: int = 3
swBodyOperationFailToCutBody: int = 4
swBodyOperationDisjointBodies: int = 5
swBodyOperationEmptyBody: int = 6
swBodyOperationEmptyInputBody: int = 7
swBodyOperationInvalidInputBody: int = 8
swBodyOperationOpposedSheets: int = 951

# swBodyOperationType_e (SwConst)
SWBODYINTERSECT: int = 15901
SWBODYCUT: int = 15902
SWBODYADD: int = 15903

# swBodyType_e (SwConst)
swAllBodies: int = -1
swSolidBody: int = 0
swSheetBody: int = 1
swWireBody: int = 2
swMinimumBody: int = 3
swGeneralBody: int = 4
swEmptyBody: int = 5
swMeshBody: int = 6
swGraphicsBody: int = 7

# swBomTableSortItemGroup_e (SwConst)
swBomTableSortItemGroup_None: int = 0
swBomTableSortItemGroup_Assemblies: int = 1
swBomTableSortItemGroup_Parts: int = 2
swBomTableSortItemGroup_Other: int = 3

# swBomTableSortMethod_e (SwConst)
swBomTableSortMethod_Literal: int = 0
swBomTableSortMethod_Numeric: int = 1

# swBomType_e (SwConst)
swBomType_PartsOnly: int = 1
swBomType_TopLevelOnly: int = 2
swBomType_Indented: int = 3
swBomType_Flattened: int = 4

# swBoundType_e (SwConst)
swBoundType_Infinite: int = 13733
swBoundType_Extendable: int = 13734
swBoundType_NotExtendable: int = 13735
swBoundType_Periodic: int = 13701
swBoundType_PeriodicNotDifferentiable: int = 13736
swBoundType_Degenerate: int = 13741

# swBoundaryBossAlignment_e (SwConst)
swAlignWithSectionNormal: int = 0
swAlignWithNextSection: int = 1
swAlignWithOtherGeometry: int = 2
swAlignWithIsoParameter: int = 3

# swBoundaryBossCurveInfluenceType_e (SwConst)
swBoundaryBossCurve_ToNextCurveInfluence: int = 0
swBoundaryBossCurve_ToNextSharpInfluence: int = 16
swBoundaryBossCurve_GlobalInfluence: int = 32
swBoundaryBossCurve_ToEdgeInfluence: int = 64
swBoundaryBossCurve_LinearInfluence: int = 144

# swBoundaryBossDirection_e (SwConst)
swBoundaryBossDirection_First: int = 0
swBoundaryBossDirection_Second: int = 1
swBoundaryBossDirection_Both: int = 2

# swBoundaryBossTangencyType_e (SwConst)
swBoundaryBossTangency_None: int = 0
swBoundaryBossTangency_NormalToProfile: int = 1
swBoundaryBossTangency_DirectionVector: int = 2
swBoundaryBossTangency_TangencyToFace: int = 3
swBoundaryBossTangency_CurvatureToFace: int = 4
swBoundaryBossTangency_Default: int = 6

# swBoundingBoxOptions_e (SwConst)
swBoundingBoxIncludeRefPlanes: int = 1
swBoundingBoxIncludeSketches: int = 2

# swBreakCornerTypes_e (SwConst)
swBreakCornerTypeFillet: int = 0
swBreakCornerTypeChamfer: int = 1

# swBreakLineOrientation_e (SwConst)
swBreakLineHorizontal: int = 1
swBreakLineVertical: int = 2

# swBreakLineStyle_e (SwConst)
swBreakLine_Straight: int = 1
swBreakLine_ZigZag: int = 2
swBreakLine_Curve: int = 3
swBreakLine_SmallZigZag: int = 4
swBreakLine_Jagged: int = 5

# swButtonSize_e (SwConst)
swButtonSize_Small: int = 0
swButtonSize_Medium: int = 1
swButtonSize_Large: int = 2

# swCADFamilyCfgOptions_e (SwConst)
swCADFamilyCfgOption_SuppressNewFeatures: int = 1
swCADFamilyCfgOption_SuppressNewComponents: int = 2
swCADFamilyCfgOption_DontActivate: int = 4

# swCPointConfig_e (SWRoutingLib)
swCPointConfig_AddAllCPoint: int = 1
swCPointConfig_DoNotAddCPoint: int = 2
swCPointConfig_SelectCPoints: int = 3

# swCalloutTargetStyle_e (SwConst)
swCalloutTargetStyle_None: int = 0
swCalloutTargetStyle_Square: int = 1
swCalloutTargetStyle_Circle: int = 2
swCalloutTargetStyle_Triangle: int = 3
swCalloutTargetStyle_Arrow: int = 4

# swCalloutVariableType_e (SwConst)
swCalloutVariableType_Length: int = 1
swCalloutVariableType_Angle: int = 2
swCalloutVariableType_String: int = 3

# swCalloutVariable_e (SwConst)
swCalloutVariable_Standard: int = 4
swCalloutVariable_Fastener_Type: int = 5
swCalloutVariable_Fastener_Size: int = 6
swCalloutVariable_Counterbore_Depth: int = 7
swCalloutVariable_Counterbore_Diameter: int = 8
swCalloutVariable_Counterdrill_Angle: int = 9
swCalloutVariable_Counterdrill_Depth: int = 10
swCalloutVariable_Counterdrill_Diameter: int = 11
swCalloutVariable_Countersink_Angle: int = 12
swCalloutVariable_Countersink_Diameter: int = 13
swCalloutVariable_Depth: int = 14
swCalloutVariable_Diameter: int = 15
swCalloutVariable_Drill_Angle: int = 16
swCalloutVariable_Far_Side_Countersink_Angle: int = 17
swCalloutVariable_Far_Side_Countersink_Diameter: int = 18
swCalloutVariable_Head_Clearance: int = 19
swCalloutVariable_Hole_Diameter: int = 20
swCalloutVariable_Hole_Depth: int = 21
swCalloutVariable_Major_Diameter: int = 22
swCalloutVariable_Middle_Countersink_Angle: int = 23
swCalloutVariable_Middle_Countersink_Diameter: int = 24
swCalloutVariable_Minor_Diameter: int = 25
swCalloutVariable_Near_Side_Countersink_Angle: int = 26
swCalloutVariable_Near_Side_Countersink_Diameter: int = 27
swCalloutVariable_Tap_Drill_Depth: int = 28
swCalloutVariable_Tap_Drill_Diameter: int = 29
swCalloutVariable_Thread_Angle: int = 30
swCalloutVariable_Thread_Diameter: int = 31
swCalloutVariable_Thread_Depth: int = 32
swCalloutVariable_Thru_Hole_Depth: int = 33
swCalloutVariable_Thru_Hole_Diameter: int = 34
swCalloutVariable_Thru_Tap_Depth: int = 35
swCalloutVariable_Thru_Tap_Drill_Diameter: int = 36
swCalloutVariable_Description: int = 37
swCalloutVariable_Msg_Near_Side: int = 38
swCalloutVariable_Msg_Mid_Side: int = 39
swCalloutVariable_Msg_Far_Side: int = 40
swCalloutVariable_Thread_Description: int = 41
swCalloutVariable_Thread_Size: int = 42
swCalloutVariable_Thread_Series: int = 43
swCalloutVariable_Thru: int = 44
swCalloutVariable_NUM_INST: int = 45
swCalloutVariable_Thread_Class: int = 46
swCalloutVariable_Counterbore: int = 47
swCalloutVariable_Thread_Diameter_Only: int = 48
swCalloutVariable_Slot_Length: int = 49
swCalloutVariable_Slot_Width: int = 50
swCalloutVariable_AH_Counterbore_Diameter: int = 51
swCalloutVariable_AH_Counterbore_Depth: int = 52
swCalloutVariable_AH_Counterbore_Nearside_Msg: int = 53
swCalloutVariable_AH_Counterbore_Farside_Msg: int = 54
swCalloutVariable_AH_Counterbore_Side: int = 55
swCalloutVariable_AH_Countersink_Diameter: int = 56
swCalloutVariable_AH_Countersink_Angle: int = 57
swCalloutVariable_AH_Countersink_Depth: int = 58
swCalloutVariable_AH_Countersink_Nearside_Msg: int = 59
swCalloutVariable_AH_Countersink_Farside_Msg: int = 60
swCalloutVariable_AH_Countersink_Side: int = 61
swCalloutVariable_AH_StraightThread_Tap_Drill_Diameter: int = 62
swCalloutVariable_AH_StraightThread_Major_Diameter: int = 63
swCalloutVariable_AH_StraightThread_Size: int = 64
swCalloutVariable_AH_StraightThread_Depth: int = 65
swCalloutVariable_AH_StraightThread_Nearside_Msg: int = 66
swCalloutVariable_AH_StraightThread_Farside_Msg: int = 67
swCalloutVariable_AH_StraightThread_Side: int = 68
swCalloutVariable_AH_TaperedThread_Tap_Drill_Diameter: int = 69
swCalloutVariable_AH_TaperedThread_Major_Diameter: int = 70
swCalloutVariable_AH_TaperedThread_Depth: int = 71
swCalloutVariable_AH_TaperedThread_Size: int = 72
swCalloutVariable_AH_TaperedThread_Nearside_Msg: int = 73
swCalloutVariable_AH_TaperedThread_Farside_Msg: int = 74
swCalloutVariable_AH_TaperedThread_Side: int = 75
swCalloutVariable_AH_Straight_Diameter: int = 76
swCalloutVariable_AH_Straight_Depth: int = 77
swCalloutVariable_AH_Dowel_HoleFit: int = 78
swCalloutVariable_AH_Dowel_ShaftFit: int = 79
swCalloutVariable_AH_Straight_Nearside_Msg: int = 80
swCalloutVariable_AH_Straight_Farside_Msg: int = 81
swCalloutVariable_AH_Straight_Side: int = 82
swCalloutVariable_AH_DrillPoint_Angle: int = 83
swCalloutVariable_AH_DrillPoint_Msg: int = 84
swCalloutVariable_AH_FlatBottom_Msg: int = 85
swCalloutVariable_AH_Blind_Msg: int = 86
swCalloutVariable_AH_UptoNext_Msg: int = 87
swCalloutVariable_AH_UptoNextElement_Msg: int = 88
swCalloutVariable_AH_UptoSelection_Msg: int = 89
swCalloutVariable_AH_OffsetFromSurface_Msg: int = 90
swCalloutVariable_AH_ThroughAll_Msg: int = 91
swCalloutVariable_AH_Thread_Description: int = 92
swCalloutVariable_AH_ThreadAdvance: int = 93

# swCamMateEntityType_e (SwConst)
swCamMateEntityType_CamPath: int = 0
swCamMateEntityType_CamFollower: int = 1

# swCameraPositionType_e (SwConst)
swCameraPosition_Cartesian: int = 1
swCameraPosition_Spherical: int = 2

# swCameraType_e (SwConst)
swCameraType_AimedAtTarget: int = 1
swCameraType_Floating: int = 2

# swCavityScaleType_e (SwConst)
swAboutCentroid: int = 0
swAboutOrigin: int = 1
swAboutMoldBaseOrigin: int = 2
swAboutCoordinateSystem: int = 3

# swCellEquationStatus_e (SwConst)
swCellEquationStatus_Success: int = 0
swCellEquationStatus_InvalidIndex: int = 1
swCellEquationStatus_InvalidEquation: int = 2

# swCenterLineMarkOrient_e (SwConst)
swCenterLineMarkOrientToSlot: int = 0
swCenterLineMarkOrientToSheet: int = 1

# swCenterMarkConnectionLine_e (SwConst)
swCenterMark_ShowNoConnectLines: int = 0
swCenterMark_ShowLinearConnectLines: int = 1
swCenterMark_ShowCircularConnectLines: int = 2
swCenterMark_ShowRadialConnectLines: int = 4
swCenterMark_ShowBaseCenterMarkLines: int = 8

# swCenterMarkHandle_e (SwConst)
swCenterMarkHandle_Up: int = 0
swCenterMarkHandle_Left: int = 1
swCenterMarkHandle_Down: int = 2
swCenterMarkHandle_Right: int = 3

# swCenterMarkStyle_e (SwConst)
swCenterMark_NonAnnotation: int = 1
swCenterMark_Single: int = 2
swCenterMark_LinearGroup: int = 3
swCenterMark_CircularGroup: int = 4

# swChainPatternAlignment_e (SwConst)
swChainPatternAlignToSeed: int = 0
swChainPatternTangentToCurve: int = 1

# swChainPatternOptions_e (SwConst)
swChainPatternStatic: int = 0
swChainPatternDynamic: int = 1

# swChainPatternPitchMethod_e (SwConst)
swChainPatternDistance: int = 0
swChainPatternDistanceLinkage: int = 1
swChainPatternConnectedLinkage: int = 2

# swChamferType_e (SwConst)
swChamferAngleDistance: int = 1
swChamferDistanceDistance: int = 2
swChamferVertex: int = 3
swChamferEqualDistance: int = 16

# swCheckClearanceBetween_e (SwConst)
swCheckClearanceBetweenSelectedItems: int = 0
swCheckClearanceBetweenSelectedItemsAndRestAssembly: int = 1

# swCheckInterferenceOption_e (SwConst)
swBodyInterference_OptionDefault: int = 1
swBodyInterference_IncludeCoincidentFaces: int = 2
swBodyInterference_ReturnInterferingObject: int = 4

# swCheckOutOfDate_e (SwConst)
swCheckOutOfDate_DoNotCheck: int = 0
swCheckOutOfDate_Indicate: int = 1
swCheckOutOfDate_AlwaysResolve: int = 2

# swCheckSpellingOptions_e (SwConst)
swSpellingIgnoreUpperCase: int = 1
swSpellingIgnoreMixedCase: int = 2
swSpellingIgnoreWordsWithNumbers: int = 4
swSpellingIgnoreCapitalizedWords: int = 8
swSpellingIgnoreInternetAndFiles: int = 16
swSpellingLeaveEngineRunning: int = 32

# swChildComponentInBOMOption_e (SwConst)
swChildComponent_Hide: int = 1
swChildComponent_Show: int = 2
swChildComponent_Promote: int = 3

# swClearanceType_e (SwConst)
swClearanceType_Distance: int = 0
swClearanceType_Coincident: int = 1

# swClearanceVerificationSetEntityErrors_e (SwConst)
swClearanceVerification_Unknown: int = -1
swClearanceVerification_swSuccess: int = 0
swClearanceVerification_swFacesAlreadySelected: int = 1
swClearanceVerification_swComponentAlreadySelected: int = 2
swClearanceVerification_swInvalidComponent: int = 3
swClearanceVerification_swInvalidFace: int = 4
swClearanceVerification_swInsufficientEntities: int = 5

# swCloseReopenError_e (SwConst)
swCloseReopenNoError: int = 0
swCloseReopenUnknownError: int = 1
swCloseReopenNoInputDocError: int = 2
swCloseReopenOutputDocPointerError: int = 3
swCloseReopenInvalidDocError: int = 4
swCloseReopenCloseDocError: int = 5
swCloseReopenLoadGenericError: int = 6
swCloseReopenLoadFileNotFoundError: int = 7
swCloseReopenLoadInvalidFileTypeError: int = 8
swCloseReopenLoadFutureVersionError: int = 9
swCloseReopenLoadSameTitleAlreadyOpenError: int = 10
swCloseReopenLoadLiquidMachineDocError: int = 11
swCloseReopenModifiedError: int = 12
swCloseReopenLoadFilePathEmptyError: int = 13
swCloseReopenLoadFilePathNonDrawingError: int = 14

# swCloseReopenOption_e (SwConst)
swCloseReopenOption_ReadOnly: int = 1
swCloseReopenOption_DiscardChanges: int = 2
swCloseReopenOption_MatchSheet: int = 4
swCloseReopenOption_ExitDetailingMode: int = 8

# swClosedCornerTypes_e (SwConst)
swClosedCornerTypeButt: int = 1
swClosedCornerTypeOverlap: int = 2
swClosedCornerTypeUnderlap: int = 3

# swCollabCheckReadOnlyModifiedInterval_e (SwConst)
swCollabCheckReadOnlyModifiedInterval_1min: int = 1
swCollabCheckReadOnlyModifiedInterval_2min: int = 2
swCollabCheckReadOnlyModifiedInterval_3min: int = 3
swCollabCheckReadOnlyModifiedInterval_5min: int = 4
swCollabCheckReadOnlyModifiedInterval_10min: int = 5
swCollabCheckReadOnlyModifiedInterval_15min: int = 6
swCollabCheckReadOnlyModifiedInterval_20min: int = 7
swCollabCheckReadOnlyModifiedInterval_30min: int = 8
swCollabCheckReadOnlyModifiedInterval_45min: int = 9
swCollabCheckReadOnlyModifiedInterval_60min: int = 10

# swCollinearChainDimArrowHeadStyle_e (SwConst)
swCollinearChainDimArrowHeadStyle_Point: int = 0
swCollinearChainDimArrowHeadStyle_Oblique: int = 1

# swCollisionDetectionResults_e (SwConst)
swCollisionDetectionResult_NoCollision: int = 0
swCollisionDetectionResult_CollisionDetected: int = 1
swCollisionDetectionResult_FailedNotEnoughGroups: int = -1

# swCollisionGroupApplyTransformErrors_e (SwConst)
swCollisionGroupApplyTransformErrors_None: int = 0
swCollisionGroupApplyTransformErrors_SizeMismatch: int = 1
swCollisionGroupApplyTransformErrors_InvalidTransforms: int = 2
swCollisionGroupApplyTransformErrors_GroupRemoved: int = 3

# swCollisionGroupSetComponentsErrors_e (SwConst)
swCollisionGroupSetComponentsErrors_None: int = 0
swCollisionGroupSetComponentsErrors_InvalidComponents: int = 1
swCollisionGroupSetComponentsErrors_ComponentsAddedElsewhere: int = 2
swCollisionGroupSetComponentsErrors_GroupRemoved: int = 3

# swCollisionManagerSetAssemblyErrors_e (SwConst)
swCollisionManagerSetAssemblyErrors_Success: int = 0
swCollisionManagerSetAssemblyErrors_InvalidModelDocument: int = 1
swCollisionManagerSetAssemblyErrors_OtherAssemblyActive: int = 2

# swColorsBackgroundAppearance_e (SwConst)
swColorsBackgroundAppearance_Plain: int = 0
swColorsBackgroundAppearance_Gradient: int = 1
swColorsBackgroundAppearance_Image: int = 2
swColorsBackgroundAppearance_DocumentScene: int = 3

# swColumnTypeStatus_e (SwConst)
swColumnTypeStatus_Success: int = 0
swColumnTypeStatus_InvalidIndex: int = 1
swColumnTypeStatus_InvalidPropertyType: int = 2

# swCombineBodiesOperationType_e (SwConst)
swCombineBodiesOperationAdd: int = 0
swCombineBodiesOperationSubtract: int = 1
swCombineBodiesOperationCommon: int = 2

# swCommandFlyoutStyle_e (SwConst)
swCommandFlyoutStyle_Simple: int = 0
swCommandFlyoutStyle_Favorite: int = 1
swCommandFlyoutStyle_LastUsed: int = 2

# swCommandItemType_e (SwConst)
swMenuItem: int = 1
swToolbarItem: int = 2

# swCommandTabButtonFlyoutStyle_e (SwConst)
swCommandTabButton_NoFlyout: int = 8
swCommandTabButton_SimpleFlyout: int = 16
swCommandTabButton_ActionFlyout: int = 32

# swCommandTabButtonTextDisplay_e (SwConst)
swCommandTabButton_NoText: int = 1
swCommandTabButton_TextBelow: int = 2
swCommandTabButton_TextHorizontal: int = 4

# swCommand_e (SwConst)
swFileOpen: int = 0
swFileNew: int = 1
swOpenRecentFile: int = 2
swOpenHTMLHelp: int = 3
swReserved: int = 4
swVerticalMkt: int = 5
swUserExperienceLevel: int = 6
swNextTipOfDayString: int = 7
swCurrentTipOfDayString: int = 8
swPrevTipOfDayString: int = 9
swFontSize: int = 10
swInterfaceBrightnessTheme: int = 11

# swCommands_e (SwCommands)
swCommands_NoCommand: int = -3
swCommands_PmOK: int = -2
swCommands_PmCancel: int = -1
swCommands_Open: int = 0
swCommands_New: int = 1
swCommands_Save: int = 2
swCommands_AssemblyTransparency: int = 3
swCommands_ShowCurvatureCombs: int = 4
swCommands_ClickHereToSeeThePreview: int = 5
swCommands_EnterTheOffsetOfTheSupportArea: int = 6
swCommands_SmartFasteners: int = 7
swCommands_ExtrudedBossBase: int = 8
swCommands_Fillet: int = 9
swCommands_ExtrudedCut: int = 10
swCommands_Chamfer: int = 11
swCommands_SimpleHole: int = 12
swCommands_InsertComponents: int = 13
swCommands_Suppress: int = 14
swCommands_Unsuppress: int = 15
swCommands_Delete: int = 16
swCommands_Rebuild: int = 17
swCommands_LinearPattern: int = 18
swCommands_SaveAll: int = 19
swCommands_MoveComponent: int = 20
swCommands_RotateComponent: int = 21
swCommands_Axis: int = 22
swCommands_InsertPlane: int = 23
swCommands_RevolvedBossBase: int = 24
swCommands_LoftedBossBase: int = 25
swCommands_InsertPart: int = 26
swCommands_RelativeView: int = 27
swCommands_ProjectedView: int = 28
swCommands_RecordPauseMacro: int = 29
swCommands_RunMacro: int = 30
swCommands_StopMacro: int = 31
swCommands_Shell: int = 32
swCommands_AuxiliaryView: int = 33
swCommands_InsertDrawingviewSection: int = 34
swCommands_DetailView: int = 35
swCommands_Note: int = 36
swCommands_Balloon: int = 37
swCommands_SmartDimension: int = 38
swCommands_HoleWizard: int = 39
swCommands_InsertFaceDraft: int = 40
swCommands_GridSnap: int = 41
swCommands_Standard3View: int = 42
swCommands_Line: int = 43
swCommands_CenterpointArc: int = 44
swCommands_Sketch: int = 45
swCommands_Circle: int = 46
swCommands_Spline: int = 47
swCommands_RevolvedCut: int = 48
swCommands_Centerline: int = 49
swCommands_UnsuppressWithDependents: int = 50
swCommands_Equations: int = 51
swCommands_AutomaticRelations: int = 52
swCommands_ConvertEntities: int = 57
swCommands_GeometricTolerance: int = 58
swCommands_TrimEntities: int = 59
swCommands_DisplayDeleteRelations: int = 60
swCommands_MirrorEntities: int = 61
swCommands_SketchFillet: int = 62
swCommands_ExtendEntities: int = 63
swCommands_SweptBossBase: int = 64
swCommands_SweptCut: int = 65
swCommands_HorizontalDimension: int = 66
swCommands_HideShowAnnotations: int = 67
swCommands_VerticalDimension: int = 68
swCommands_TangentArc: int = 69
swCommands_FeatureImportDiagnosis: int = 70
swCommands_AddRelation: int = 71
swCommands_Point: int = 72
swCommands_CircularPattern: int = 73
swCommands_ProjectCurve: int = 74
swCommands_Properties: int = 75
swCommands_OffsetEntities: int = 76
swCommands_ModelView: int = 77
swCommands_ScanEqual: int = 78
swCommands_Rectangle: int = 79
swCommands_3PointArc: int = 80
swCommands_BaselineDimension: int = 81
swCommands_LoftedCut: int = 82
swCommands_Mirror: int = 83
swCommands_EditMacro: int = 84
swCommands_HideShowComponents: int = 85
swCommands_PartialEllipse: int = 86
swCommands_Ellipse: int = 87
swCommands_BillOfMaterials: int = 88
swCommands_3DSketch: int = 89
swCommands_Mate: int = 90
swCommands_NewPart: int = 91
swCommands_Measure: int = 92
swCommands_Cavity: int = 93
swCommands_HelixAndSpiral: int = 94
swCommands_CenterMark: int = 95
swCommands_ImportedGeometry: int = 96
swCommands_Thicken: int = 97
swCommands_ThickenedCut: int = 98
swCommands_ViewTemporaryAxes: int = 99
swCommands_ModifySketch: int = 100
swCommands_CutWithSurface: int = 101
swCommands_ConstructionGeometry: int = 102
swCommands_SweptSurface: int = 103
swCommands_RevolvedSurface: int = 104
swCommands_InsertOffsetRefSurface: int = 105
swCommands_ExtrudedSurface: int = 106
swCommands_LoftedSurface: int = 107
swCommands_AlignedSectionView: int = 108
swCommands_Text: int = 109
swCommands_VerticalBreak: int = 110
swCommands_InsertPartingLine: int = 111
swCommands_SurfaceFinish: int = 112
swCommands_FileReload: int = 113
swCommands_DatumFeature: int = 114
swCommands_CosmeticThread: int = 115
swCommands_Join: int = 116
swCommands_MidSurface: int = 117
swCommands_InsertBends: int = 118
swCommands_EditComponent: int = 119
swCommands_ChangeTransparency: int = 120
swCommands_HoleCallout: int = 121
swCommands_DatumTarget: int = 122
swCommands_CurveThroughReferencePoints: int = 123
swCommands_SectionView: int = 124
swCommands_Rib: int = 125
swCommands_ViewOrigins: int = 126
swCommands_CameraView: int = 127
swCommands_CurveThroughXYZPoints: int = 128
swCommands_StopCurrentJump: int = 129
swCommands_OpenInternetAddress: int = 130
swCommands_WeldSymbol: int = 131
swCommands_Curvature: int = 132
swCommands_Check: int = 133
swCommands_InsertHyperlink: int = 134
swCommands_ExplodedView: int = 135
swCommands_WebToolbar: int = 136
swCommands_Dome: int = 137
swCommands_Flatten: int = 138
swCommands_NoBends: int = 139
swCommands_InsertSplinePoint: int = 140
swCommands_LineColor: int = 141
swCommands_LineThickness: int = 142
swCommands_LineStyle: int = 143
swCommands_SimplifySpline: int = 144
swCommands_AlignCollinearRadial: int = 145
swCommands_AlignParallelConcentric: int = 146
swCommands_Bold: int = 147
swCommands_Italic: int = 148
swCommands_Underline: int = 149
swCommands_ChangeSuppressionState: int = 150
swCommands_Parabola: int = 151
swCommands_Block: int = 152
swCommands_ViewCoordinateSystems: int = 153
swCommands_CoordinateSystem: int = 154
swCommands_InsertRefsurfaceRadiate: int = 155
swCommands_InsertRefsurfaceSew: int = 156
swCommands_Shape: int = 157
swCommands_CompositeCurve: int = 158
swCommands_PreviousView: int = 159
swCommands_MateReference: int = 160
swCommands_Front: int = 161
swCommands_Back: int = 162
swCommands_Top: int = 163
swCommands_Left: int = 164
swCommands_Right: int = 165
swCommands_Bottom: int = 166
swCommands_Isometric: int = 167
swCommands_InsertPlanarSurface: int = 168
swCommands_NormalTo: int = 169
swCommands_EditColor: int = 170
swCommands_NoSolveMove: int = 171
swCommands_LinearSketchPattern: int = 172
swCommands_CircularSketchPattern: int = 173
swCommands_UserMacro01: int = 174
swCommands_UserMacro02: int = 175
swCommands_UserMacro03: int = 176
swCommands_UserMacro04: int = 177
swCommands_UserMacro05: int = 178
swCommands_UserMacro06: int = 179
swCommands_UserMacro07: int = 180
swCommands_UserMacro08: int = 181
swCommands_UserMacro09: int = 182
swCommands_UserMacro10: int = 183
swCommands_UserMacro11: int = 184
swCommands_UserMacro12: int = 185
swCommands_UserMacro13: int = 186
swCommands_UserMacro14: int = 187
swCommands_UserMacro15: int = 188
swCommands_UserMacro16: int = 189
swCommands_UserMacro17: int = 190
swCommands_UserMacro18: int = 191
swCommands_UserMacro19: int = 192
swCommands_UserMacro20: int = 193
swCommands_UserMacro21: int = 194
swCommands_UserMacro22: int = 195
swCommands_UserMacro23: int = 196
swCommands_UserMacro24: int = 197
swCommands_UserMacro25: int = 198
swCommands_UserMacro26: int = 199
swCommands_UserMacro27: int = 200
swCommands_UserMacro28: int = 201
swCommands_UserMacro29: int = 202
swCommands_UserMacro30: int = 203
swCommands_UserMacro31: int = 204
swCommands_UserMacro32: int = 205
swCommands_UserMacro33: int = 206
swCommands_UserMacro34: int = 207
swCommands_UserMacro35: int = 208
swCommands_UserMacro36: int = 209
swCommands_UserMacro37: int = 210
swCommands_UserMacro38: int = 211
swCommands_UserMacro39: int = 212
swCommands_UserMacro40: int = 213
swCommands_UserMacro41: int = 214
swCommands_UserMacro42: int = 215
swCommands_UserMacro43: int = 216
swCommands_UserMacro44: int = 217
swCommands_UserMacro45: int = 218
swCommands_UserMacro46: int = 219
swCommands_UserMacro47: int = 220
swCommands_UserMacro48: int = 221
swCommands_UserMacro49: int = 222
swCommands_UserMacro50: int = 223
swCommands_UserMacro51: int = 224
swCommands_UserMacro52: int = 225
swCommands_UserMacro53: int = 226
swCommands_UserMacro54: int = 227
swCommands_UserMacro55: int = 228
swCommands_UserMacro56: int = 229
swCommands_UserMacro57: int = 230
swCommands_UserMacro58: int = 231
swCommands_UserMacro59: int = 232
swCommands_UserMacro60: int = 233
swCommands_UserMacro61: int = 234
swCommands_UserMacro62: int = 235
swCommands_UserMacro63: int = 236
swCommands_UserMacro64: int = 237
swCommands_UserMacro65: int = 238
swCommands_UserMacro66: int = 239
swCommands_UserMacro67: int = 240
swCommands_UserMacro68: int = 241
swCommands_UserMacro69: int = 242
swCommands_UserMacro70: int = 243
swCommands_UserMacro71: int = 244
swCommands_UserMacro72: int = 245
swCommands_UserMacro73: int = 246
swCommands_UserMacro74: int = 247
swCommands_UserMacro75: int = 248
swCommands_UserMacro76: int = 249
swCommands_UserMacro77: int = 250
swCommands_UserMacro78: int = 251
swCommands_UserMacro79: int = 252
swCommands_UserMacro80: int = 253
swCommands_UserMacro81: int = 254
swCommands_UserMacro82: int = 255
swCommands_UserMacro83: int = 256
swCommands_UserMacro84: int = 257
swCommands_UserMacro85: int = 258
swCommands_UserMacro86: int = 259
swCommands_UserMacro87: int = 260
swCommands_UserMacro88: int = 261
swCommands_UserMacro89: int = 262
swCommands_UserMacro90: int = 263
swCommands_UserMacro91: int = 264
swCommands_UserMacro92: int = 265
swCommands_UserMacro93: int = 266
swCommands_UserMacro94: int = 267
swCommands_UserMacro95: int = 268
swCommands_UserMacro96: int = 269
swCommands_UserMacro97: int = 270
swCommands_UserMacro98: int = 271
swCommands_NewMacroButton: int = 272
swCommands_ToggleSelectionFilters: int = 273
swCommands_ClearAllFilters: int = 274
swCommands_SelectAllFilters: int = 275
swCommands_FilterVertices: int = 276
swCommands_FilterEdges: int = 277
swCommands_FilterFaces: int = 278
swCommands_FilterAxes: int = 279
swCommands_FilterPlanes: int = 280
swCommands_FilterSketchPoints: int = 281
swCommands_FilterSketchSegments: int = 282
swCommands_FilterMidpoints: int = 283
swCommands_FilterCenterMarks: int = 284
swCommands_FilterDimensionsHoleCallouts: int = 285
swCommands_FilterSurfaceFinishSymbols: int = 286
swCommands_FilterGeometricTolerances: int = 287
swCommands_FilterNotesBalloons: int = 288
swCommands_FilterDatumFeatures: int = 289
swCommands_FilterWeldSymbols: int = 290
swCommands_FilterDatumTargets: int = 291
swCommands_FilterCosmeticThreads: int = 292
swCommands_SplitEntities: int = 293
swCommands_Parallelogram: int = 294
swCommands_NewAssembly: int = 295
swCommands_LayerProperties: int = 296
swCommands_Rip: int = 297
swCommands_DraftQualityHlrHlv: int = 298
swCommands_ColorDisplayMode: int = 299
swCommands_TableDrivenPattern: int = 300
swCommands_ExtendSurface: int = 301
swCommands_TrimSurface: int = 302
swCommands_FilterSurfaceBodies: int = 303
swCommands_SketchDrivenPattern: int = 304
swCommands_Polygon: int = 305
swCommands_IntersectionCurve: int = 306
swCommands_AnnotationAlignLeft: int = 307
swCommands_AnnotationAlignRight: int = 308
swCommands_AlignTop: int = 309
swCommands_AlignBottom: int = 310
swCommands_CropView: int = 311
swCommands_SpaceEvenlyAcross: int = 312
swCommands_SpaceEvenlyDown: int = 313
swCommands_AlignHorizontal: int = 314
swCommands_AlignVertical: int = 315
swCommands_SpaceTightlyAcross: int = 316
swCommands_SpaceTightlyDown: int = 317
swCommands_Group: int = 318
swCommands_StackedBalloons: int = 319
swCommands_BaseFlangeTab: int = 320
swCommands_FaceCurves: int = 321
swCommands_InsertFeatureBlend: int = 322
swCommands_SketchedBend: int = 323
swCommands_MiterFlange: int = 324
swCommands_Fold: int = 325
swCommands_Unfold: int = 326
swCommands_Ungroup: int = 327
swCommands_BrokenOutSection: int = 328
swCommands_RotateView: int = 329
swCommands_Pan: int = 330
swCommands_ZoomInOut: int = 331
swCommands_ZoomToFit: int = 332
swCommands_ZoomToArea: int = 333
swCommands_Wireframe: int = 334
swCommands_HiddenLinesRemoved: int = 335
swCommands_HiddenLinesVisible: int = 336
swCommands_Shaded: int = 337
swCommands_ViewPlanes: int = 338
swCommands_ViewAxes: int = 339
swCommands_Help: int = 340
swCommands_ViewOrientation: int = 341
swCommands_Options: int = 342
swCommands_MassProperties: int = 343
swCommands_InterferenceDetection: int = 344
swCommands_PickMode: int = 345
swCommands_OrdinateDimension: int = 346
swCommands_HorizontalOrdinateDimension: int = 347
swCommands_VerticalOrdinateDimension: int = 348
swCommands_Perspective: int = 349
swCommands_InsertScale: int = 350
swCommands_EmptyView: int = 351
swCommands_ShowEdge: int = 352
swCommands_HideEdge: int = 353
swCommands_ZoomToSelection: int = 354
swCommands_Redraw: int = 355
swCommands_ToggleSelectionFilterToolbar: int = 356
swCommands_AlternatePositionView: int = 357
swCommands_SketchChamfer: int = 358
swCommands_EdgeFlange: int = 359
swCommands_ClosedCorner: int = 360
swCommands_FilterBlocks: int = 361
swCommands_CurveDrivenPattern: int = 362
swCommands_Hem: int = 363
swCommands_BreakCornerCornerTrim: int = 364
swCommands_ZebraStripes: int = 365
swCommands_ChamferDimension: int = 366
swCommands_MultiJogLeader: int = 367
swCommands_SketchPicture: int = 368
swCommands_DowelPinSymbol: int = 369
swCommands_ReplaceFace: int = 371
swCommands_Jog: int = 372
swCommands_2DTo3DMakeRefsketchFront: int = 373
swCommands_2DTo3DMakeRefsketchTop: int = 374
swCommands_2DTo3DMakeRefsketchRight: int = 375
swCommands_2DTo3DMakeRefsketchBottom: int = 376
swCommands_2DTo3DMakeRefsketchLeft: int = 377
swCommands_2DTo3DMakeRefsketchBack: int = 378
swCommands_AlignSketch: int = 379
swCommands_RepairSketch: int = 380
swCommands_CreateSketchFromSelections: int = 381
swCommands_FilterDowelPinSymbols: int = 382
swCommands_SectionProperties: int = 383
swCommands_AreaHatchFill: int = 384
swCommands_UpdateView: int = 385
swCommands_MoveSizeFeatures: int = 386
swCommands_DocumentFont: int = 387
swCommands_AlignRight: int = 388
swCommands_AlignLeft: int = 389
swCommands_Center: int = 390
swCommands_Auxiliary: int = 391
swCommands_Extrude: int = 392
swCommands_DeleteFace: int = 393
swCommands_2DTo3DCut: int = 394
swCommands_ExplodeLineSketch: int = 395
swCommands_RouteLine: int = 396
swCommands_InsertSplitFeat: int = 397
swCommands_JogLine: int = 398
swCommands_ShadowsInShadedMode: int = 399
swCommands_UntrimSurface: int = 400
swCommands_AutoDimension: int = 401
swCommands_ViewCurves: int = 402
swCommands_ViewSketches: int = 403
swCommands_ViewAllAnnotations: int = 404
swCommands_LargeAssemblyMode: int = 405
swCommands_LoftedBend: int = 406
swCommands_Combine: int = 407
swCommands_MoveCopyBodies: int = 408
swCommands_Flex: int = 409
swCommands_InsertFamilyTable: int = 410
swCommands_DeviationAnalysis: int = 411
swCommands_GeneralTable: int = 412
swCommands_DesignTable: int = 413
swCommands_MoldflowxpressAnalysisWizard: int = 414
swCommands_AddTangencyControl: int = 415
swCommands_AddCurvatureControl: int = 416
swCommands_ShowInflectionPoints: int = 417
swCommands_ShowMinimumRadius: int = 418
swCommands_FilterSolidBodies: int = 419
swCommands_Gravity: int = 420
swCommands_StopRecordOrPlayback: int = 421
swCommands_LinearMotor: int = 422
swCommands_RotaryMotor: int = 423
swCommands_DeleteSolidSurface: int = 424
swCommands_InsertDetailCenterLine: int = 425
swCommands_FitSpline: int = 426
swCommands_Statistics: int = 427
swCommands_PredefinedView: int = 428
swCommands_SimulationToolbar: int = 429
swCommands_CalculateSimulation: int = 430
swCommands_ReplaySimulation: int = 431
swCommands_PhotoView: int = 432
swCommands_SolidworksAnimator: int = 433
swCommands_3DInstantWebsite: int = 434
swCommands_eDrawings: int = 435
swCommands_SolidworksUtilities: int = 436
swCommands_SolidworksToolbox: int = 437
swCommands_Featureworks: int = 438
swCommands_CosmosxpressAnalysisWizard: int = 439
swCommands_ViewSketchRelations: int = 440
swCommands_FilterCenterlines: int = 441
swCommands_Wrap: int = 442
swCommands_ShowSplineHandles: int = 443
swCommands_LinearSpring: int = 444
swCommands_PartingLines: int = 445
swCommands_HoleTable: int = 446
swCommands_AutoBalloon: int = 447
swCommands_InsertRuledSurfaceFromEdge: int = 448
swCommands_InsertPartingPlane: int = 449
swCommands_Weldment: int = 450
swCommands_ContextSelection: int = 451
swCommands_ShutOffSurfaces: int = 452
swCommands_Gusset: int = 453
swCommands_Deform: int = 454
swCommands_InsertRefpoint: int = 455
swCommands_RevisionTable: int = 456
swCommands_RevisionSymbol: int = 457
swCommands_FilterConnectionPoints: int = 458
swCommands_FilterRoutingPoints: int = 459
swCommands_DesignChecker: int = 460
swCommands_MakeDrawingFromPartAssembly: int = 461
swCommands_MakeAssemblyFromPartAssembly: int = 462
swCommands_WeldmentCutList: int = 463
swCommands_ToolingSplit: int = 464
swCommands_StructuralMember: int = 465
swCommands_TrimExtend: int = 466
swCommands_Trimetric: int = 467
swCommands_Dimetric: int = 468
swCommands_MakeBlock: int = 469
swCommands_InsertBlock: int = 470
swCommands_EditBlock: int = 471
swCommands_ExplodeBlock: int = 472
swCommands_SaveBlock: int = 473
swCommands_Align: int = 474
swCommands_Annotations: int = 475
swCommands_Assemblies: int = 476
swCommands_Curves: int = 477
swCommands_Drawings: int = 478
swCommands_Features: int = 479
swCommands_Fonts: int = 480
swCommands_LineFormats: int = 481
swCommands_Macros: int = 482
swCommands_Molds: int = 483
swCommands_ReferenceGeometry: int = 484
swCommands_ExplodeSketch: int = 485
swCommands_SelectionFilters: int = 486
swCommands_SheetMetal: int = 487
swCommands_Simulation: int = 488
swCommands_SketchToolbar: int = 489
swCommands_DimensionRelations: int = 490
swCommands_SolidworksOffice: int = 491
swCommands_Splines: int = 492
swCommands_Standard: int = 493
swCommands_StandardViews: int = 494
swCommands_Surfaces: int = 495
swCommands_Tools: int = 496
swCommands_Web: int = 497
swCommands_View: int = 498
swCommands_RealviewGraphics: int = 499
swCommands_RealViewPlusGraphics: int = 500
swCommands_EditMaterial: int = 501
swCommands_MoveEntities: int = 502
swCommands_RotateEntities: int = 503
swCommands_ScaleEntities: int = 504
swCommands_FilletBead: int = 505
swCommands_ShadedWithEdges: int = 506
swCommands_EditTexture: int = 507
swCommands_Weldments: int = 508
swCommands_2DTo3D: int = 509
swCommands_ViewRoutingPoints: int = 510
swCommands_ViewPoints: int = 511
swCommands_ExcelBasedBillOfMaterials: int = 512
swCommands_ModelItems: int = 513
swCommands_Core: int = 514
swCommands_AddRemove: int = 515
swCommands_Caterpillar: int = 516
swCommands_EndTreatment: int = 517
swCommands_HealEdges: int = 518
swCommands_InferTBGrid: int = 519
swCommands_NearestSnap: int = 520
swCommands_PointSnap: int = 521
swCommands_HVPointSnap: int = 522
swCommands_MidpointSnap: int = 523
swCommands_IntersectionSnap: int = 524
swCommands_HVSnap: int = 525
swCommands_ParallelSnap: int = 526
swCommands_PerpendicularSnap: int = 527
swCommands_TangentSnap: int = 528
swCommands_DynamicMirrorEntities: int = 529
swCommands_CenterPointSnap: int = 530
swCommands_Color: int = 531
swCommands_Strikeout: int = 532
swCommands_Bullet: int = 533
swCommands_Stack: int = 534
swCommands_SpellChecker: int = 535
swCommands_AngleSnap: int = 536
swCommands_QuadrantSnap: int = 537
swCommands_InsertFeatureMoveFace: int = 538
swCommands_Number: int = 539
swCommands_LengthSnap: int = 540
swCommands_CheckReadOnlyFiles: int = 541
swCommands_SplineOnSurface: int = 542
swCommands_DecreaseIndent: int = 543
swCommands_IncreaseIndent: int = 544
swCommands_PerimeterCircle: int = 545
swCommands_InsertMoldFolders: int = 546
swCommands_ViewPartingLines: int = 547
swCommands_3DDrawingView: int = 548
swCommands_SingleView: int = 549
swCommands_TwoViewHorizontal: int = 550
swCommands_TwoViewVertical: int = 551
swCommands_FourView: int = 552
swCommands_LinkViews: int = 553
swCommands_Plane: int = 554
swCommands_SketchGroupRebuild: int = 555
swCommands_HoleSeries: int = 556
swCommands_Blocks: int = 557
swCommands_FillPattern: int = 558
swCommands_CopyEntities: int = 559
swCommands_FormingTool: int = 560
swCommands_View3DSketchPlane: int = 561
swCommands_View3DSketchDimensions: int = 562
swCommands_MakeSmartComponent: int = 563
swCommands_InvertSelection: int = 564
swCommands_CosmosworksDesigner: int = 565
swCommands_SolidworksRouting: int = 566
swCommands_3DSketchOnPlane: int = 567
swCommands_HorizontalBreak: int = 568
swCommands_ResetComponents: int = 569
swCommands_EndCap: int = 570
swCommands_Indent: int = 571
swCommands_DisplayControlPolygon: int = 572
swCommands_NewMacro: int = 573
swCommands_ReplaceMateEntities: int = 574
swCommands_ReplaceComponents: int = 575
swCommands_Print3D: int = 576
swCommands_FilterWeldBeads: int = 577
swCommands_NoExternalReferences: int = 578
swCommands_AlignBetweenLines: int = 579
swCommands_NewWindow: int = 580
swCommands_TileHorizontally: int = 581
swCommands_TileVertically: int = 582
swCommands_Copy: int = 583
swCommands_Cut: int = 584
swCommands_Paste: int = 585
swCommands_Undo: int = 586
swCommands_Redo: int = 587
swCommands_Close: int = 588
swCommands_Print: int = 589
swCommands_PrintPreview: int = 590
swCommands_SwiftRecognizeFeatures: int = 591
swCommands_SwiftInsertDimension: int = 592
swCommands_SwiftInsertDatum: int = 593
swCommands_SwiftInsertGtol: int = 594
swCommands_SwiftShowConstraintStatus: int = 595
swCommands_SwiftDeleteAll: int = 596
swCommands_SwiftGtsOptions: int = 597
swCommands_ToolsAddAssemblyToleranceDimension: int = 598
swCommands_ToolsComputeStackAnalysis: int = 599
swCommands_FullyDefineSketch: int = 600
swCommands_ZoomToFitKey: int = 601
swCommands_FilletManager: int = 602
swCommands_DraftManager: int = 603
swCommands_ScreenCapture: int = 604
swCommands_Roll: int = 605
swCommands_Turn: int = 606
swCommands_ViewLights: int = 607
swCommands_ViewCameras: int = 608
swCommands_PushPull: int = 609
swCommands_ColorScheme: int = 610
swCommands_InsertSketchBelt: int = 611
swCommands_TolXpert: int = 612
swCommands_TolAnalyst: int = 613
swCommands_TolXpertMultiSelect: int = 614
swCommands_TolXpertEndMultiSelect: int = 615
swCommands_InsertBelt: int = 616
swCommands_SketchCreateChain: int = 617
swCommands_InsertBoundarySurface: int = 618
swCommands_FullScreenMode: int = 619
swCommands_SaveAs: int = 620
swCommands_CosmosMotion: int = 621
swCommands_ScanTo3D: int = 622
swCommands_EditFeature: int = 623
swCommands_RapidPrototype: int = 624
swCommands_SwiftInsertSizeDimension: int = 625
swCommands_SwiftInsertMultiSelectFeature: int = 626
swCommands_SwiftInsertPatternFeature: int = 627
swCommands_FitText: int = 628
swCommands_Conveyor: int = 629
swCommands_RectangleTools: int = 630
swCommands_ArcTools: int = 631
swCommands_CircleTools: int = 632
swCommands_Undo_Eq: int = 633
swCommands_Select_All: int = 634
swCommands_Reset: int = 635
swCommands_Tools_Drw_Dimtext_Link: int = 636
swCommands_Restore_Rotation: int = 637
swCommands_Translate_Drawing: int = 638
swCommands_Auto_Jog: int = 639
swCommands_Create_Framepoint: int = 640
swCommands_Change_Arrow_Style: int = 641
swCommands_Lock_Framepoint: int = 642
swCommands_Pattern_Copy: int = 643
swCommands_Unlock_Framepoint: int = 644
swCommands_Hide_Geometry: int = 645
swCommands_Modify_Curv_Scale: int = 646
swCommands_Delete_Light: int = 647
swCommands_Body_Color: int = 648
swCommands_Drview_Load_Model: int = 649
swCommands_Body_Texture: int = 650
swCommands_Feature_Color: int = 651
swCommands_Feature_Texture: int = 652
swCommands_Component_Color: int = 653
swCommands_Component_Texture: int = 654
swCommands_Edit_Def_Assy: int = 655
swCommands_Mainbar_Undo: int = 656
swCommands_Animation_Play_From_Start: int = 657
swCommands_Api_Menu_String_File: int = 658
swCommands_Animation_Wizard: int = 659
swCommands_Start_Contour_Single_Select: int = 660
swCommands_End_Contour_Single_Select: int = 661
swCommands_Api_Menu_String_Edit: int = 662
swCommands_Cancel_Sketch_Drag: int = 663
swCommands_Activate_Selected_Contour: int = 664
swCommands_Finish_Active_Contour: int = 665
swCommands_Api_Menu_String_View: int = 666
swCommands_Api_Menu_String_Insert: int = 667
swCommands_Api_Menu_String_Tools: int = 668
swCommands_Api_Menu_String_Window: int = 669
swCommands_Api_Menu_String_Help: int = 670
swCommands_Api_Menu_String_Developer_Tools: int = 671
swCommands_Object_Popup_Menu: int = 672
swCommands_Grid_Align: int = 673
swCommands_Hatch_Properties: int = 674
swCommands_Flip_180: int = 675
swCommands_Resume_Stacking_Balloons: int = 676
swCommands_Stack_Dir_Up: int = 677
swCommands_Stack_Dir_Down: int = 678
swCommands_Delete_Relation: int = 679
swCommands_Stack_Dir_Left: int = 680
swCommands_Stack_Dir_Right: int = 681
swCommands_Api_Menu_String_View_Toolbars: int = 682
swCommands_View_Mates: int = 683
swCommands_Hlink_History: int = 684
swCommands_Add_Newrelation: int = 685
swCommands_Show_Incontext_Feature_Holders: int = 686
swCommands_Hide_Incontext_Feature_Holders: int = 687
swCommands_Cd_Next: int = 688
swCommands_Cd_Delete: int = 689
swCommands_Cd_Previous: int = 690
swCommands_Cd_Deleteall: int = 691
swCommands_Cd_Refs: int = 692
swCommands_Route_Properties: int = 693
swCommands_Align_Vert_By_Center: int = 694
swCommands_Align_Horz_By_Center: int = 695
swCommands_Apply: int = 696
swCommands_Close_: int = 697
swCommands_Mate_Cancel: int = 698
swCommands_User_Job_Cancel: int = 699
swCommands_Reset_Std_View: int = 700
swCommands_Mate_Finish: int = 701
swCommands_Mate_Preview: int = 702
swCommands_Expl_Save: int = 703
swCommands_Expl_Apply: int = 704
swCommands_Expl_Cancel: int = 705
swCommands_Cd_Undo: int = 706
swCommands_Cd_Connum: int = 707
swCommands_Defer: int = 708
swCommands_Delete_Constraints: int = 709
swCommands_Undo_: int = 710
swCommands_Static: int = 711
swCommands_Options_Apply: int = 712
swCommands_Watch_Start: int = 713
swCommands_Watch_Stop: int = 714
swCommands_Watch_Exit: int = 715
swCommands_Cd_Edit: int = 716
swCommands_Sm2_Inside: int = 717
swCommands_Sm2_Outside: int = 718
swCommands_Route_Properties_Popup: int = 719
swCommands_Route_Options: int = 720
swCommands_Route_Get_Property: int = 721
swCommands_Leader_Delete_Branch: int = 722
swCommands_Route_Remove_Pipe: int = 723
swCommands_Rmb_Loft_Tangency: int = 724
swCommands_Rmb_Loft_Smooth: int = 725
swCommands_Rmb_Loft_Close: int = 726
swCommands_Rmb_Sweep_Tangency: int = 727
swCommands_Rmb_Sweep_Smooth: int = 728
swCommands_Rmb_Sweep_Align: int = 729
swCommands_Rmb_Collect_All_Bends: int = 730
swCommands_Rmb_Iso_Ad_Mesh: int = 731
swCommands_Rmb_Iso_Position: int = 732
swCommands_Rmb_Iso_Constrain_Model: int = 733
swCommands_Rmb_Iso_Ignore_Holes: int = 734
swCommands_Rmb_Skcham_Dist: int = 735
swCommands_Rmb_Skcham_Angle: int = 736
swCommands_Rmb_Skcham_Equal: int = 737
swCommands_Rmb_Sm_Reverse_Dir: int = 738
swCommands_Rmb_Sm_Bend_Revdir: int = 739
swCommands_Dve_Rmb_Pushpin: int = 740
swCommands_Dve_Rmb_Mc_Drop_Base_Pt: int = 741
swCommands_Dve_Rmb_Mc_Drop_Destination: int = 742
swCommands_Dve_Rmb_Mc_Select_Entities: int = 743
swCommands_Dve_Rmb_Mc_Define_Base_Pt: int = 744
swCommands_Dve_Rmb_Mc_Define_Destination: int = 745
swCommands_Rmb_Mvsrf_Copy: int = 746
swCommands_View_Assy_Opaque: int = 747
swCommands_View_Assy_Full: int = 748
swCommands_View_Assy_Maintain: int = 749
swCommands_Mate_Apply: int = 750
swCommands_Deform_Rmb_Set_Transparent: int = 751
swCommands_Deform_Rmb_Set_Zebra: int = 752
swCommands_Rmb_Edit_Section: int = 753
swCommands_Deform_Rmb_Add_Connector: int = 754
swCommands_Deform_Rmb_Update_Display: int = 755
swCommands_Deform_Rmb_Disp_Connectionlines: int = 756
swCommands_Triad_Align_To_Prin: int = 757
swCommands_Deform_Rmb_Reserved_3: int = 758
swCommands_Triad_Align: int = 759
swCommands_Deform_Rmb_Reserved_4: int = 760
swCommands_Triad_Align2: int = 761
swCommands_Deform_Rmb_Reserved_5: int = 762
swCommands_Triad_Align_To_Comp: int = 763
swCommands_Find_Next: int = 764
swCommands_Remove_All: int = 765
swCommands_Ok: int = 766
swCommands_Cancel: int = 767
swCommands_Add: int = 768
swCommands_Show_Triad_Manipulator: int = 769
swCommands_Route_Add_All: int = 770
swCommands_Ref_Help: int = 771
swCommands_Tx_Walkthrough_Goto_Start: int = 772
swCommands_Tx_Walkthrough_Rewind: int = 773
swCommands_Tx_Walkthrough_Play: int = 774
swCommands_Tx_Walkthrough_Ff: int = 775
swCommands_Tx_Walkthrough_Goto_End: int = 776
swCommands_Tx_Walkthrough_Pause: int = 777
swCommands_Tx_Walkthrough_Stop: int = 778
swCommands_Tx_Walkthrough_Record: int = 779
swCommands_Tx_Walkthrough_Play_Normal: int = 780
swCommands_Tx_Walkthrough_Play_Loop: int = 781
swCommands_Tx_Walkthrough_Play_Reciprocate: int = 782
swCommands_Tx_Walkthrough_Play_Slow: int = 783
swCommands_Tx_Walkthrough_Play_Fast: int = 784
swCommands_Visual_State_Clear_Override: int = 785
swCommands_Visual_State_Clear_Override_All: int = 786
swCommands_Dim_Snap_Horizontal: int = 787
swCommands_Dim_Snap_Vertical: int = 788
swCommands_Dim_Snap_To_Edge: int = 789
swCommands_Autofix_Resume: int = 790
swCommands_Sign_Up: int = 791
swCommands_Sign_In: int = 792
swCommands_Accept: int = 793
swCommands_Submit: int = 794
swCommands_Browse: int = 795
swCommands_Feature_Import: int = 796
swCommands_Cancel_Inplace: int = 797
swCommands_Object_Displaycontent: int = 798
swCommands_Object_Displayasicon: int = 799
swCommands_Object_Resetsize: int = 800
swCommands_Edit_Dimval: int = 801
swCommands_Select_Midpoint: int = 802
swCommands_View_Options_Centerlines: int = 803
swCommands_Finish_Section: int = 804
swCommands_View_Options_Refplanes: int = 805
swCommands_Parent_Child_Rel: int = 806
swCommands_Entity_Properties: int = 807
swCommands_Popup_Show_Hidden: int = 808
swCommands_Whats_Wrong: int = 809
swCommands_Popup_Hide_Hidden: int = 810
swCommands_Popup_Show_Component: int = 811
swCommands_Popup_Hide_Component: int = 812
swCommands_Edit_Undolist: int = 813
swCommands_Edit_Rollforward: int = 814
swCommands_Edit_Rollback: int = 815
swCommands_Edit_Drag: int = 816
swCommands_Run: int = 817
swCommands_Insert_Object: int = 818
swCommands__Dumpfacets: int = 819
swCommands_File_Saveall: int = 820
swCommands_Edit_Pastespecial: int = 821
swCommands_Show_Hidden: int = 822
swCommands_View_Displayrelationships: int = 823
swCommands_Create_Point: int = 824
swCommands_View_Normalto: int = 825
swCommands_View_Selectview: int = 826
swCommands_View_Cutaway: int = 827
swCommands_View_Exploded: int = 828
swCommands_View_Displaylayout: int = 829
swCommands_Add_Dragitem: int = 830
swCommands_Edit_Dragitem: int = 831
swCommands_Tools_Macro: int = 832
swCommands_Api_Help_Contents: int = 833
swCommands_Debug_Lights: int = 834
swCommands__Dump_Dumpsketch: int = 835
swCommands_Edit_Rebuild_Step: int = 836
swCommands_Edit_Rebuild_To: int = 837
swCommands_Tools_Orientcomponent: int = 838
swCommands_Insert_Dimensions: int = 839
swCommands_Insert_Symbols: int = 840
swCommands_Tools_Blank: int = 841
swCommands_Tools_Unblank: int = 842
swCommands_Insert_Jog: int = 843
swCommands_Insert_Drawingview_Broken: int = 844
swCommands_Insert_Cthread_Callout: int = 845
swCommands_Cth_Callout_Cmd: int = 846
swCommands_Insert_Point: int = 847
swCommands_Make_Section: int = 848
swCommands_Cancel_Edit_Cntr: int = 849
swCommands_Cancel_Edit_Srvr: int = 850
swCommands_File_Checkout: int = 851
swCommands_Insert_View_1st: int = 852
swCommands__Dumpsolid: int = 853
swCommands_Insert_Familytable_New: int = 854
swCommands_Insert_Familytable_Open: int = 855
swCommands_Insert_Page: int = 856
swCommands_Insert_Sheet: int = 857
swCommands_Inc_Update: int = 858
swCommands_Edit_Sketch: int = 859
swCommands_Sketch_Align: int = 860
swCommands_Debug_Dump_Entity: int = 861
swCommands_Exit_Sketch: int = 862
swCommands_Edit_Sketchplane: int = 863
swCommands_Component_Properties: int = 864
swCommands_Feat_Edit: int = 865
swCommands_Edit_Familytable: int = 866
swCommands_Edit_Familytable_Open: int = 867
swCommands_Edit_Incontext: int = 868
swCommands_Sk_Constrain_Coincident: int = 869
swCommands_Sk_Constrain_Parallel: int = 870
swCommands_Sk_Constrain_Concentric: int = 871
swCommands_Sketch_Section: int = 872
swCommands_Sk_Constrain_Perp: int = 873
swCommands_Sk_Constrain_Tangent: int = 874
swCommands_View_Hide_Behind_Plane: int = 875
swCommands_Insert_Group: int = 876
swCommands_View_Constraint: int = 877
swCommands_Edit_Force_Rebuild: int = 878
swCommands__Force_Rebuild: int = 879
swCommands__Showmultihidden: int = 880
swCommands__Dynamichighlight: int = 881
swCommands_Insert_Xhatch: int = 882
swCommands_Sk_Use_Edge_Ctrline: int = 883
swCommands_View_Orthographic_Named: int = 884
swCommands_Update_Std_View: int = 885
swCommands_Sketch_Midpoint: int = 886
swCommands_Sketch_Xpoint: int = 887
swCommands_Heal_Next: int = 888
swCommands_Tools_Align_Horz: int = 889
swCommands_Tools_Align_Vert: int = 890
swCommands_View_Query_Select: int = 891
swCommands_Display_Faceid: int = 892
swCommands_Feat_Linear_Pattern: int = 893
swCommands_Feat_Cir_Pattern: int = 894
swCommands_Blank_Refgeom: int = 895
swCommands_Unblank_Refgeom: int = 896
swCommands_View_Sheet_Previous: int = 897
swCommands_View_Sheet_Next: int = 898
swCommands__Debug_Solvopt: int = 899
swCommands_Heal_Back: int = 900
swCommands_Blank_Part_Body: int = 901
swCommands_View_Sheet: int = 902
swCommands_View_Drawing_Scale: int = 903
swCommands_Property_Menu_Item: int = 904
swCommands_Sketch_Undo: int = 905
swCommands_Heal_Close_Gaps: int = 906
swCommands_Heal_Fix_Faces: int = 907
swCommands_Tools_Units: int = 908
swCommands_Insert_Refdim: int = 909
swCommands__Dump_History: int = 910
swCommands__Dump_Backup_Info: int = 911
swCommands__Debug_Set_Backup: int = 912
swCommands__Debug_Edit_Undo: int = 913
swCommands_Unlock_Bom: int = 914
swCommands_View_Change_Scale: int = 915
swCommands_View_Orientation_Rmb: int = 916
swCommands_Draw_Prefs: int = 917
swCommands_Lock_Bom: int = 918
swCommands__Display_Tuning: int = 919
swCommands_Top_Right: int = 920
swCommands_Save_Template: int = 921
swCommands_Dims_Prefs: int = 922
swCommands_Top_Left: int = 923
swCommands_Insert_Sectionline: int = 924
swCommands_Hide_Components: int = 925
swCommands_Show_Components: int = 926
swCommands_Show_Feature_Detail: int = 927
swCommands_Dbg_Check_Body: int = 928
swCommands_Debug_Check_Body: int = 929
swCommands_Bottom_Right: int = 930
swCommands_Hide_Feature_Detail: int = 931
swCommands__Dump_Parasld_Ents: int = 932
swCommands_Bottom_Left: int = 933
swCommands__Debug_Autoconstrain: int = 934
swCommands_View_Rotate_Center: int = 935
swCommands_View_Rotate_Screen: int = 936
swCommands_Debug_Check_Faces: int = 937
swCommands_Heal_Remove_Faces: int = 938
swCommands_View_Dynamic_High: int = 939
swCommands_View_Pick_Invisible: int = 940
swCommands_Comp_Config_Prop: int = 941
swCommands_Heal_Gaps: int = 942
swCommands_Heal_Gap_Edges: int = 943
swCommands_Heal_Tolerant_Edges: int = 944
swCommands_Tools_Dim_Pref: int = 945
swCommands_Preferences_Menu_Item: int = 946
swCommands_Sheet_Tab_Popup_Properties: int = 947
swCommands_Sheet_Tab_Popup_Add: int = 948
swCommands_Sheet_Tab_Popup_Delete: int = 949
swCommands_Sheet_Tab_Popup_Activate: int = 950
swCommands_Debug_Check_Iges_Geom: int = 951
swCommands_View_Pick_Hidden_Wf: int = 952
swCommands_View_Pick_Hidden_Hlr: int = 953
swCommands_Blank_Sketch: int = 954
swCommands_Unblank_Sketch: int = 955
swCommands_Dump_Sketchdb: int = 956
swCommands_Fix_Component: int = 957
swCommands_Heal_Mistyped_Edges: int = 958
swCommands_Unfix_Component: int = 959
swCommands_Heal_Diagnosis_Faces: int = 960
swCommands_Escape_Key_Down: int = 961
swCommands_Heal_Diagnosis_Edges: int = 962
swCommands_File_Summaryinfo: int = 963
swCommands_Heal_Edges_Ok: int = 964
swCommands_Edit_Part: int = 965
swCommands_Heal_Plug_By_Extension: int = 966
swCommands_Edit_Assembly: int = 967
swCommands_Heal_Plug_By_Construction: int = 968
swCommands_Heal_Gaps_Closed_Checking: int = 969
swCommands_Open_Comp_File: int = 970
swCommands_Heal_Gaps_Finishing: int = 971
swCommands_Heal_Re_Sewing: int = 972
swCommands_Tools_Configuration: int = 973
swCommands_Heal_Upgrading: int = 974
swCommands_Page_Setup: int = 975
swCommands_Regen_At_Load: int = 976
swCommands_File_Find: int = 977
swCommands_Delete_Dtable: int = 978
swCommands_Tools_Hide_Dv: int = 979
swCommands_Edit_Current_Scope: int = 980
swCommands_Heal_Checking_Faulty: int = 981
swCommands_Heal_Failed_Check: int = 982
swCommands_Heal_Constructing: int = 983
swCommands_Tools_Sketch_Scale: int = 984
swCommands_Tools_Sketch_Translate: int = 985
swCommands_Attach_Dimensions: int = 986
swCommands_Sktools_Autoconstr: int = 987
swCommands_Insert_Mirrored_Part: int = 988
swCommands_Split_Extrude: int = 989
swCommands_Compress_Sketch: int = 990
swCommands_Heal_Fallback_Choice: int = 991
swCommands_File_Derive_Comp: int = 992
swCommands_View_Explode_Assembly: int = 993
swCommands_Heal_Fallback_Use: int = 994
swCommands_View_Collapse_Assembly: int = 995
swCommands_Heal_Fallback_Pass: int = 996
swCommands_Autosolve_Toggle: int = 997
swCommands_Refsurface_Thicken: int = 998
swCommands_Insert_Mirror_Solid: int = 999
swCommands_Debug_Force_Rebuild_Assem: int = 1000
swCommands_Asm_Feat_Cut_Extr: int = 1001
swCommands_Asm_Feat_Cut_Revolve: int = 1002
swCommands_Asm_Feature_Hole: int = 1003
swCommands_View_Confirm_Select: int = 1004
swCommands_Insert_Extrude_Ref_Surf: int = 1005
swCommands_Insert_Copy_Ref_Surface: int = 1006
swCommands_Heal_Found_Faulty: int = 1007
swCommands_Insert_Libfeat: int = 1008
swCommands_Derive_Sketch: int = 1009
swCommands_Underive_Sketch: int = 1010
swCommands__Dump_Dumpheader: int = 1011
swCommands__Dump_Header: int = 1012
swCommands_Heal_Faces_Deleted: int = 1013
swCommands_Debug_Check_Bad_Feature: int = 1014
swCommands__Dump_Xmt3d_File: int = 1015
swCommands_Component_Pattern: int = 1016
swCommands_Heal_Checking: int = 1017
swCommands_Surfid_Trace: int = 1018
swCommands_Heal_Finishing: int = 1019
swCommands_Debug_Set_Needs_Update: int = 1020
swCommands_Debug_Set_Suppress_Affter: int = 1021
swCommands_Debug_Add_Mategroup: int = 1022
swCommands_Sk_Drag_Thru_Dims: int = 1023
swCommands_Insert_Weld: int = 1024
swCommands_Add_Spot: int = 1025
swCommands_Blank_Atom_Body: int = 1026
swCommands_Add_Direction: int = 1027
swCommands_Unblank_Atom_Body: int = 1028
swCommands_Import_Cthreads: int = 1029
swCommands_View_Fm_By_Feat: int = 1030
swCommands_View_Fm_By_Dep: int = 1031
swCommands_Edit_Expl_Param: int = 1032
swCommands_Window_Closeall: int = 1033
swCommands_Assembly_Rotate_Axis: int = 1034
swCommands_Debug_Dump_Journal3d: int = 1035
swCommands_Dymparam_Dlg_Ok: int = 1036
swCommands_Dymparam_Dlg_Cancel: int = 1037
swCommands_Dymparam_Dlg_Reverse: int = 1038
swCommands_Dymparam_Dlg_Regen: int = 1039
swCommands_Dymparam_Dlg_Increment: int = 1040
swCommands_Dymparam_Dlg_Designintent: int = 1041
swCommands_File_Sync: int = 1042
swCommands_View_Edit_Perspective: int = 1043
swCommands_Insert_Target_Point: int = 1044
swCommands_Debug_Force_Rebuild_Assem_Top_Only: int = 1045
swCommands_Show_Dependents: int = 1046
swCommands_Debug_Save_Entity: int = 1047
swCommands_Sk_Close_Contour: int = 1048
swCommands_File_Save_As_Vrml: int = 1049
swCommands_Dump_All_Eqns: int = 1050
swCommands_Debug_Dump_Entity_Id: int = 1051
swCommands_Debug_Combine_Body: int = 1052
swCommands_Debug_Check_Min_Radius: int = 1053
swCommands_Debug_Dump_Kernel_Version: int = 1054
swCommands_List_Extrefs: int = 1055
swCommands_Debug_Match_Bool: int = 1056
swCommands_Debug_Match_Bodies: int = 1057
swCommands_Insert_Annotations: int = 1058
swCommands_Rmb_Edit_Camera: int = 1059
swCommands_View_This_Camera: int = 1060
swCommands_View_Lock_Camera: int = 1061
swCommands_Rmb_Lock_Camera: int = 1062
swCommands_Web_Goback: int = 1063
swCommands_Web_Goforward: int = 1064
swCommands_Debug_Match_Regions: int = 1065
swCommands_Window_Featurepalette: int = 1066
swCommands_Expl_Step_New: int = 1067
swCommands_Expl_Step_Prev: int = 1068
swCommands_Expl_Step_Next: int = 1069
swCommands_Expl_Step_Undo: int = 1070
swCommands_Expl_Step_Delete: int = 1071
swCommands_Expl_Step_Apply: int = 1072
swCommands_Tools_Addins: int = 1073
swCommands_Debug_Sketch_Tol: int = 1074
swCommands_Debug_Set_Needs_Debug_Data: int = 1075
swCommands_Tools_Show_Tangent: int = 1076
swCommands_Tools_Show_Tan: int = 1077
swCommands_Tools_Font_Tan: int = 1078
swCommands_Tools_Remove_Tan: int = 1079
swCommands_List_Exportents: int = 1080
swCommands_Insert_Woodruff: int = 1081
swCommands_Enable_Face_Blend: int = 1082
swCommands_Debug_Enable_Face_Blend: int = 1083
swCommands_Debug_Enable_Hole_Wizard: int = 1084
swCommands__Display_List: int = 1085
swCommands_Debug_Check_Ent_Id: int = 1086
swCommands_App_Tipofday: int = 1087
swCommands_Debug_Set_Suppress_Cms: int = 1088
swCommands_Read_Section: int = 1089
swCommands_Solidworks_Community: int = 1090
swCommands_Debug_Dump_Surface_Mesh: int = 1091
swCommands_Comp_Body: int = 1092
swCommands_Comp_Display: int = 1093
swCommands_Comp_Show_Detail: int = 1094
swCommands_Sm_Start: int = 1095
swCommands_Sm_Reorder_Bends: int = 1096
swCommands_Sm_Insert_Form: int = 1097
swCommands_Sm_End: int = 1098
swCommands_Button33458: int = 1099
swCommands_Button33459: int = 1100
swCommands_Button33460: int = 1101
swCommands_Button33461: int = 1102
swCommands_Button33462: int = 1103
swCommands_Button33463: int = 1104
swCommands_Button33464: int = 1105
swCommands_Button33465: int = 1106
swCommands_Button33466: int = 1107
swCommands_Button33467: int = 1108
swCommands_Button33468: int = 1109
swCommands_Button33473: int = 1110
swCommands_Button33474: int = 1111
swCommands_Button33475: int = 1112
swCommands_Button33476: int = 1113
swCommands_Button33477: int = 1114
swCommands_Button33478: int = 1115
swCommands_Button33479: int = 1116
swCommands_Button33480: int = 1117
swCommands_Button33481: int = 1118
swCommands_Button33482: int = 1119
swCommands_Button33483: int = 1120
swCommands_Button33502: int = 1121
swCommands_Button33503: int = 1122
swCommands_Button33504: int = 1123
swCommands_Button33505: int = 1124
swCommands_Button33507: int = 1125
swCommands_Button33508: int = 1126
swCommands_Button33509: int = 1127
swCommands_Button33510: int = 1128
swCommands_Edit_Vsection: int = 1129
swCommands_Debug_Fix_Sw97plus1_Draw: int = 1130
swCommands_Insert_Picture: int = 1131
swCommands_View_Display_Picture: int = 1132
swCommands_View_Modify_Del_Picture: int = 1133
swCommands_View_Modify_Repl_Picture: int = 1134
swCommands_Move_Show_Delta_Xyz: int = 1135
swCommands_Rotate_Show_Delta_Xyz: int = 1136
swCommands_Tools_Customize: int = 1137
swCommands_Check_Sketch_For_Feature: int = 1138
swCommands_Insert_Zone: int = 1139
swCommands_Query_Advanced: int = 1140
swCommands_Face_Curvature: int = 1141
swCommands_Move_Show_Xyz: int = 1142
swCommands_Debug_Set_Tol: int = 1143
swCommands_Disable_Move_Eval: int = 1144
swCommands_Enable_Showdims: int = 1145
swCommands_Remove_Watermark: int = 1146
swCommands_Allow_Closed_Section_Lines: int = 1147
swCommands_Font_Face: int = 1148
swCommands_Font_Units: int = 1149
swCommands_Font_Points: int = 1150
swCommands_Layer_Select: int = 1151
swCommands_Toolbar_First: int = 1152
swCommands_Toolbar_Standard: int = 1153
swCommands_Toolbar_View: int = 1154
swCommands_Toolbar_Assembly: int = 1155
swCommands_Toolbar_Drawing: int = 1156
swCommands_Toolbar_Features: int = 1157
swCommands_Toolbar_Dependency: int = 1158
swCommands_Toolbar_Macro: int = 1159
swCommands_Toolbar_Sel_Filter: int = 1160
swCommands_Toolbar_Sketch: int = 1161
swCommands_Toolbar_Sketch_Rels: int = 1162
swCommands_Toolbar_Sketch_Tools: int = 1163
swCommands_Toolbar_Web: int = 1164
swCommands_Toolbar_Lineformat: int = 1165
swCommands_Toolbar_Font: int = 1166
swCommands_Toolbar_Annotation: int = 1167
swCommands_Toolbar_Routing: int = 1168
swCommands_Toolbar_Stdview: int = 1169
swCommands_Toolbar_Selfilter: int = 1170
swCommands_New_Toolbar_Selfilter: int = 1171
swCommands_Toolbar_Mold: int = 1172
swCommands_Toolbar_Sht_Mtl: int = 1173
swCommands_Toolbar_Surface: int = 1174
swCommands_Toolbar_Curve: int = 1175
swCommands_Toolbar_Debug: int = 1176
swCommands_New_Toolbar_Sel_Filter: int = 1177
swCommands_Toolbar_Refgeom: int = 1178
swCommands_Toolbar_Tools: int = 1179
swCommands_Toolbar_Layer: int = 1180
swCommands_Toolbar_Align: int = 1181
swCommands_Toolbar_2dto3d: int = 1182
swCommands_Toolbar_Exploderoute: int = 1183
swCommands_Toolbar_Com_Feature: int = 1184
swCommands_Toolbar_Spline_Tools: int = 1185
swCommands_Toolbar_Simulation: int = 1186
swCommands_Toolbar_Office: int = 1187
swCommands_Toolbar_Nc_Parts: int = 1188
swCommands_Toolbar_Weldment: int = 1189
swCommands_Toolbar_Inference: int = 1190
swCommands_Toolbar_Table: int = 1191
swCommands_Toolbar_DimXpert: int = 1192
swCommands_Fullscreen_Toolbar: int = 1193
swCommands_Toolbar_Tolanalyst: int = 1194
swCommands_Toolbar_Last: int = 1195
swCommands_Insert_New_Zone: int = 1196
swCommands_Debug_Set_No_Update: int = 1197
swCommands_Insert_Ref_Point: int = 1198
swCommands_View_Disp_Ref_Points: int = 1199
swCommands_View_Disp_Ref_Points2: int = 1200
swCommands_Lightweight_Toggle: int = 1201
swCommands_Make_Lightweight: int = 1202
swCommands_Make_Resolved: int = 1203
swCommands_Make_Suppressed: int = 1204
swCommands_Toolbar_Context: int = 1205
swCommands_Activate_Sheet: int = 1206
swCommands_Tools_Custom_Symbol_New: int = 1207
swCommands_Insert_Custom_Symbol_Save: int = 1208
swCommands_Insert_Coord_Sys2: int = 1209
swCommands_View_Disp_Coordsys2: int = 1210
swCommands_Incr_Pick_Radius: int = 1211
swCommands_Insert_Ref_Line: int = 1212
swCommands_View_Disp_Ref_Lines: int = 1213
swCommands_Enable_Mate_Inferencing: int = 1214
swCommands_Assembly_Stats: int = 1215
swCommands_Display_Curveid: int = 1216
swCommands__Enable_Autoload: int = 1217
swCommands_Explode_Custom_Symbol: int = 1218
swCommands_Make_Custom_Symbol: int = 1219
swCommands_Tools_Custom_Symbol_Edit: int = 1220
swCommands_Debug_Monitor_Body_Tag: int = 1221
swCommands_Insert_Route_Point: int = 1222
swCommands_Insert_Connection_Point: int = 1223
swCommands_Ref_Point_Offset: int = 1224
swCommands_Ref_Point_Onset: int = 1225
swCommands_Route_Set_Edit_Loc: int = 1226
swCommands_Route_Add_Route_Point: int = 1227
swCommands_Disable_Routing: int = 1228
swCommands_Debug_Dump_Extra_Bodies: int = 1229
swCommands_Dummy_Materef: int = 1230
swCommands_New_View: int = 1231
swCommands_Debug_Check_Two_Entities: int = 1232
swCommands_App_Servicepacks: int = 1233
swCommands_Resolve_All: int = 1234
swCommands_Lightweight_All: int = 1235
swCommands_Debug_Toggle_Dm_Journal: int = 1236
swCommands_Debug_Import_Diagnosis: int = 1237
swCommands_Route_Start_Con_Point: int = 1238
swCommands_Hide_Bom: int = 1239
swCommands_Show_Bom: int = 1240
swCommands_Create_Infer_Points: int = 1241
swCommands_Edit_Seed_Feature: int = 1242
swCommands_Insert_Ff_Drawingview_Named: int = 1243
swCommands_Insert_Ff_View_3rd: int = 1244
swCommands_Tools_Addview_Ff: int = 1245
swCommands_Route_Fab_Update: int = 1246
swCommands_Insert_Section_Feature: int = 1247
swCommands_Sk3d_Selectx: int = 1248
swCommands_Sk3d_Selecty: int = 1249
swCommands_Sk3d_Selectz: int = 1250
swCommands_Sk3d_Selectxy: int = 1251
swCommands_Sk3d_Selectyz: int = 1252
swCommands_Sk3d_Selectzx: int = 1253
swCommands_Tools_Arrange_Components: int = 1254
swCommands__Debug_Dve: int = 1255
swCommands_Documentprefs: int = 1256
swCommands_Add_Ref_Point: int = 1257
swCommands_New_Subassembly: int = 1258
swCommands_Form_Newassembly: int = 1259
swCommands_Dissolve_Subassembly: int = 1260
swCommands_Line_Usecurrprops: int = 1261
swCommands_Edit_Dynamic: int = 1262
swCommands_Conn_Point_Flip: int = 1263
swCommands_User_Macro_First: int = 1264
swCommands_Parasolid_Rollback: int = 1265
swCommands_Debug_Nominal_Geometry: int = 1266
swCommands_Debug_Curve_Fitting: int = 1267
swCommands__Useswapcopy: int = 1268
swCommands_Fltr_Onoff: int = 1269
swCommands_Fltr_Clearall: int = 1270
swCommands_Fltr_Setall: int = 1271
swCommands_Fltr_Vertex: int = 1272
swCommands_Fltr_Edge: int = 1273
swCommands_Fltr_Face: int = 1274
swCommands_Fltr_Axis: int = 1275
swCommands_Fltr_Plane: int = 1276
swCommands_Fltr_Skpoint: int = 1277
swCommands_Fltr_Sksegment: int = 1278
swCommands_Fltr_Midpoint: int = 1279
swCommands_Fltr_Centermark: int = 1280
swCommands_Fltr_Dimension: int = 1281
swCommands_Fltr_Surffin: int = 1282
swCommands_Fltr_Gtol: int = 1283
swCommands_Fltr_Note: int = 1284
swCommands_Fltr_Datumfeat: int = 1285
swCommands_Fltr_Weld: int = 1286
swCommands_Fltr_Datumtarg: int = 1287
swCommands_Fltr_Cthread: int = 1288
swCommands_Pin_Drawing_Views_On: int = 1289
swCommands_Detachable_Drawings: int = 1290
swCommands_Dump_Ghost_Sketch: int = 1291
swCommands__Enablescissor: int = 1292
swCommands_Insert_Light_Pointlight: int = 1293
swCommands_Insert_Light_Spotlight: int = 1294
swCommands_Insert_Light_Distantlight: int = 1295
swCommands_Light_Properties: int = 1296
swCommands_Tools_Options: int = 1297
swCommands_Disable_Route_Types: int = 1298
swCommands__Debug_Sketch_Inferencing: int = 1299
swCommands__Debug_Sketch_Point_Inferencing: int = 1300
swCommands_Autoinfer_Toggle: int = 1301
swCommands_Bom_Viewtable: int = 1302
swCommands_View_Ruler: int = 1303
swCommands_Debug_Time_Section_View: int = 1304
swCommands_Debug_Use_Old_Section_View_Code: int = 1305
swCommands__Drawalledges: int = 1306
swCommands_Line_Stylebylayer: int = 1307
swCommands_Line_Solid: int = 1308
swCommands_Line_Dashed: int = 1309
swCommands_Line_Phantom: int = 1310
swCommands_Line_Chain: int = 1311
swCommands_Line_Center: int = 1312
swCommands_Line_Stitch: int = 1313
swCommands_Line_Thickthin: int = 1314
swCommands_Line_Weightbylayer: int = 1315
swCommands_Line_Thin: int = 1316
swCommands_Line_Normal: int = 1317
swCommands_Line_Thick: int = 1318
swCommands_Line_Thick2: int = 1319
swCommands_Line_Thick3: int = 1320
swCommands_Line_Thick4: int = 1321
swCommands_Line_Thick5: int = 1322
swCommands_Line_Thick6: int = 1323
swCommands_Edit_Dissolve_Assembly: int = 1324
swCommands_Insert_Form_Assembly: int = 1325
swCommands_Route_Realign_Fitting: int = 1326
swCommands_Debug_Set_Command_Line_Debug_Code: int = 1327
swCommands_Route_Add_To_Fab: int = 1328
swCommands__Dump_Ecdcxmit: int = 1329
swCommands__Dump_Ecdcjou: int = 1330
swCommands__Ecdc_Performance: int = 1331
swCommands__Ecdc_Highlight: int = 1332
swCommands__Dump_Ecdcloops: int = 1333
swCommands__Dump_Ecdc_Mini: int = 1334
swCommands__Ecdc_Minsets: int = 1335
swCommands__Ecdc_Boxsets: int = 1336
swCommands__Ecdc_Boxfaces: int = 1337
swCommands__Ecdc_Boxedges: int = 1338
swCommands__Ecdc_Boxcache: int = 1339
swCommands__Ecdcswitches: int = 1340
swCommands_Tools_Clashselection: int = 1341
swCommands_Dim_Inspection: int = 1342
swCommands_Smart_Mate: int = 1343
swCommands__Enable_Full_Restructure: int = 1344
swCommands_Debug_Enable_3dfilletpoints: int = 1345
swCommands__Enablecommanddeletion: int = 1346
swCommands_Unfrag_File: int = 1347
swCommands__Ecdcstatic: int = 1348
swCommands_Auto_Sm_Drawing: int = 1349
swCommands_Piping_Help: int = 1350
swCommands_Piping_Help_Hint: int = 1351
swCommands_Display_Face_Normal: int = 1352
swCommands_Piping_Custom_Pipe_Config: int = 1353
swCommands_Piping_Standard_Pipe_Config: int = 1354
swCommands_Piping_Make_Flange_Driving: int = 1355
swCommands_Piping_Make_Flange_Driven: int = 1356
swCommands_View_Decimation_Onoff: int = 1357
swCommands_Arrow_Open: int = 1358
swCommands_Arrow_Closed: int = 1359
swCommands_Arrow_Slash: int = 1360
swCommands_Arrow_Dot: int = 1361
swCommands_Arrow_Origin: int = 1362
swCommands_Arrow_Wide: int = 1363
swCommands_Arrow_Isowide: int = 1364
swCommands_Arrow_Rus: int = 1365
swCommands_Arrow_Closetop: int = 1366
swCommands_Arrow_Closebot: int = 1367
swCommands_Arrow_None: int = 1368
swCommands_Use_New_Get_Enties_Using_Point: int = 1369
swCommands_View_Toolbars: int = 1370
swCommands_Debug_Enable_3duse_Edge: int = 1371
swCommands_Insert_Tangency_Ref_Surface: int = 1372
swCommands_Use_Assert_For_Parasolid_Mem_Leak: int = 1373
swCommands_Dump_Parasolid_Memory_Leaks: int = 1374
swCommands_Asm_Lin_Feat_Pattern: int = 1375
swCommands_Asm_Cir_Feat_Pattern: int = 1376
swCommands_Open_Comp_Assem_File: int = 1377
swCommands__Displaymemoryallocation2: int = 1378
swCommands_Debug_Parasolid_Stack_Trace: int = 1379
swCommands_Asm_Table_Feat_Pattern: int = 1380
swCommands_Debug_P1857_Feat_Edit: int = 1381
swCommands_Asm_Sketch_Feat_Pattern: int = 1382
swCommands_Debug_Tsg_Transparency: int = 1383
swCommands_Edit_Dcircle: int = 1384
swCommands_Debug_Use_New_Surf_Extension_Ui: int = 1385
swCommands_Share_Surfid_Dtd: int = 1386
swCommands_Share_Surfid_All: int = 1387
swCommands_Tools_Crop_Edit: int = 1388
swCommands_Tools_Crop_Delete: int = 1389
swCommands_View_Hideshow: int = 1390
swCommands_Edit_Lsk_Pattern: int = 1391
swCommands_Edit_Csk_Pattern: int = 1392
swCommands_Solid_Data_Manager: int = 1393
swCommands_Debug_Display_Curvature: int = 1394
swCommands_View_Model_Edges: int = 1395
swCommands_Debug_Dump_Config_Mgr: int = 1396
swCommands_Debug_Dump_Config_Objs: int = 1397
swCommands_Edit_Polygon: int = 1398
swCommands_Weld_2ndray_Fillet: int = 1399
swCommands_Dtd_Convert_Back: int = 1400
swCommands_Goto_Section_View: int = 1401
swCommands_Goto_Detail_View: int = 1402
swCommands_Goto_Parent_View: int = 1403
swCommands_Goto_Auxiliary_View: int = 1404
swCommands_Goto_Projected_View: int = 1405
swCommands_Developertools_Menu: int = 1406
swCommands_Resolve_Out_Of_Date_Lwcomps: int = 1407
swCommands_Insert_Sketch_Import: int = 1408
swCommands_Getting_Started: int = 1409
swCommands_Whats_New: int = 1410
swCommands_Sw_Release_Notes: int = 1411
swCommands_Sw_Beta_Report: int = 1412
swCommands_Unblank_Part_Body: int = 1413
swCommands_Sel_Filter_Msg_Timer: int = 1414
swCommands_Save_Cgr: int = 1415
swCommands_Debug_Save_Cgr: int = 1416
swCommands_Edit_Suppress_All_Configs: int = 1417
swCommands_Debug_Dtd_Ii: int = 1418
swCommands_Edit_Suppress_Select_Configs: int = 1419
swCommands_Select_Loop: int = 1420
swCommands_Edit_Unsuppress_All_Configs: int = 1421
swCommands_Edit_Unsuppress_Select_Configs: int = 1422
swCommands_Help_Onlinetutorial: int = 1423
swCommands_Edit_Unsuppress_Dependent_All_Configs: int = 1424
swCommands_Edit_Unsuppress_Dependent_Select_Configs: int = 1425
swCommands_Double_Click_Timer: int = 1426
swCommands_Flash_Cursor_Timer: int = 1427
swCommands_Select_Tangency: int = 1428
swCommands_Save_As_A_Part: int = 1429
swCommands_Alternate_Line_Creation: int = 1430
swCommands_Help_Welcometosolidworksscreen: int = 1431
swCommands_Help_Welcometosolidworks: int = 1432
swCommands_Trans_In_Steps: int = 1433
swCommands_Sm_Insert_Unbend: int = 1434
swCommands_Assem_Hlr_Compcol: int = 1435
swCommands_File_Lock: int = 1436
swCommands_File_Lock_Menu: int = 1437
swCommands_File_Lock_Unlock: int = 1438
swCommands_File_Lockchildren: int = 1439
swCommands_File_Unlockchildren: int = 1440
swCommands_File_Unlock: int = 1441
swCommands_Insert_Bendtable_Open: int = 1442
swCommands_Insert_Bendtable_New: int = 1443
swCommands_Edit_Bendtable: int = 1444
swCommands_Delete_Bendtable: int = 1445
swCommands_Dve_Mid_Plane: int = 1446
swCommands_Dve_Blind: int = 1447
swCommands_Dve_Uptovertex: int = 1448
swCommands_Dve_Uptosurface: int = 1449
swCommands_Dve_Offsetfromsurface: int = 1450
swCommands_Dve_Throughall: int = 1451
swCommands_Dve_Throughnext: int = 1452
swCommands_Dve_Debug_Extr_Em: int = 1453
swCommands_Dve_Debug_Extr_Ei: int = 1454
swCommands_Group_Remove_Item: int = 1455
swCommands_Edit_Redolist: int = 1456
swCommands_Debug_Open_Cgr: int = 1457
swCommands__Drawingtopart: int = 1458
swCommands_Drawingtopart_Refreshdialog: int = 1459
swCommands_Debug_Dump_All_Component_Config_Objects: int = 1460
swCommands_Debug_Dump_Comp_Instance_Tree: int = 1461
swCommands_Enable_Break_Out_Section: int = 1462
swCommands_Dve_Rmb_Ok: int = 1463
swCommands_Move_Dve_Resume_Drag: int = 1464
swCommands_Dve_Rmb_Cancel: int = 1465
swCommands_Debug_Customise_Pm: int = 1466
swCommands_Enable_Proj_Drag_And_Mated_Tumble: int = 1467
swCommands_View_Rotateplusy: int = 1468
swCommands_View_Rotateminusy: int = 1469
swCommands_View_Rotateplusz: int = 1470
swCommands_View_Rotateminusz: int = 1471
swCommands_View_Rotateminusx: int = 1472
swCommands_View_Rotateplusx: int = 1473
swCommands_View_Rotx_Minusninety: int = 1474
swCommands_View_Rotx_Plusninety: int = 1475
swCommands_View_Roty_Minusninety: int = 1476
swCommands_View_Roty_Plusninety: int = 1477
swCommands_View_Transplusx: int = 1478
swCommands_View_Transminusx: int = 1479
swCommands_View_Transplusy: int = 1480
swCommands_View_Transminusy: int = 1481
swCommands_View_Zoomin: int = 1482
swCommands_View_Zoomout: int = 1483
swCommands_View_Display_Faceted: int = 1484
swCommands_View_Rw_Shading: int = 1485
swCommands_View_Ogl_Shading: int = 1486
swCommands_View_Options_Colors_Highlight: int = 1487
swCommands_View_Options_Colors_Part: int = 1488
swCommands_View_Options_Colors_Sketch: int = 1489
swCommands_View_Options_Colors_Dimension: int = 1490
swCommands_View_Options_Colors_Bg: int = 1491
swCommands_View_Disp_Refdims: int = 1492
swCommands_View_Fullpage: int = 1493
swCommands_Window_Redraw: int = 1494
swCommands_Window_Ambrowser: int = 1495
swCommands_Basepart_Regen_Msg: int = 1496
swCommands_Tools_Toolbars: int = 1497
swCommands_Macro_Playback_Over: int = 1498
swCommands_Edit_Drop: int = 1499
swCommands_Ole_Property_Sheet: int = 1500
swCommands_Edit_Template: int = 1501
swCommands_Edit_Sheet: int = 1502
swCommands_Dv_Suppress: int = 1503
swCommands_Dv_Unsuppress: int = 1504
swCommands_Align_Ordinate: int = 1505
swCommands_Change_Ordinate_Dir: int = 1506
swCommands_Edit_Ordinate: int = 1507
swCommands_Select_Silhouette: int = 1508
swCommands_Toggle_Grid: int = 1509
swCommands_Break_Alignment: int = 1510
swCommands_Align_Horz: int = 1511
swCommands_Align_Vert: int = 1512
swCommands_Restore_Align: int = 1513
swCommands_Align_View: int = 1514
swCommands_Tools_Remove_Tangent_Edges: int = 1515
swCommands_Insert_Dim: int = 1516
swCommands_Activate_Configuration: int = 1517
swCommands_Jog_Ordinate: int = 1518
swCommands_Break_View: int = 1519
swCommands_Unbreak_View: int = 1520
swCommands_Draw_Bl_Straight: int = 1521
swCommands_Draw_Bl_Spline: int = 1522
swCommands_Draw_Bl_Zigzag: int = 1523
swCommands_Sel_Filter: int = 1524
swCommands_Remove_From_Library: int = 1525
swCommands_Add_To_Library: int = 1526
swCommands_Component_Reload: int = 1527
swCommands_Hide_Cthread: int = 1528
swCommands_Show_Cthread: int = 1529
swCommands_Edit_Drawview_Sketch: int = 1530
swCommands_Align_Grid: int = 1531
swCommands_Face_Xhatch_Properties: int = 1532
swCommands_Unslant_Dim: int = 1533
swCommands_Add_Configuration: int = 1534
swCommands_Show_Configuration: int = 1535
swCommands_Reset_Configuration: int = 1536
swCommands_Show_Cabinet: int = 1537
swCommands_Hide_Cabinet: int = 1538
swCommands_Hide_Dim: int = 1539
swCommands_Show_Dim: int = 1540
swCommands_View_Clear_Select: int = 1541
swCommands_Drview_Prop: int = 1542
swCommands_Link_Dims: int = 1543
swCommands_Unlink_Dim: int = 1544
swCommands_Tools_Show_Tangent_Edges: int = 1545
swCommands_Tools_Font_Tangent_Edges: int = 1546
swCommands_Sketch_Detach: int = 1547
swCommands_Flip_Ref_Dim: int = 1548
swCommands_Ann_Show: int = 1549
swCommands_Ann_Feat_Dim: int = 1550
swCommands_Ann_Ref_Dim: int = 1551
swCommands_Add_Feature_Dims: int = 1552
swCommands_Remove_Feature_Dims: int = 1553
swCommands_Remove_Snap: int = 1554
swCommands_Toggle_Ole_Owner: int = 1555
swCommands_Show_Explode_Steps: int = 1556
swCommands_Create_Silhouettes: int = 1557
swCommands_Show_Configuration_Adv: int = 1558
swCommands_Load_Model_Thread_Finished: int = 1559
swCommands_Show_Zone: int = 1560
swCommands_Hide_Zone: int = 1561
swCommands_Break_Dim_Align: int = 1562
swCommands_Autosave: int = 1563
swCommands_Show_Dim_Align: int = 1564
swCommands_File_Reload_Vodoc: int = 1565
swCommands_Load_Model_Thread_Failed: int = 1566
swCommands_View_Display_No_Display_State: int = 1567
swCommands_Rad_Dim_Radial: int = 1568
swCommands_Toolbar_Routing_Str: int = 1569
swCommands_Rad_Dim_Diametric: int = 1570
swCommands_Rad_Dim_Lindiamtric: int = 1571
swCommands_Dim_Showpara: int = 1572
swCommands_Tools_Drw_Autoregen: int = 1573
swCommands_Dim_Center_Text: int = 1574
swCommands_Reset_Line_Font: int = 1575
swCommands_Dissolve_Lib_Feature: int = 1576
swCommands_More_Lines: int = 1577
swCommands_Edit_Equation: int = 1578
swCommands_Add_Equation: int = 1579
swCommands_Del_Equation: int = 1580
swCommands_Print_Selection: int = 1581
swCommands_Draw_Bl_Isozag: int = 1582
swCommands_Edit_Importfolder: int = 1583
swCommands_View_Undo_Last: int = 1584
swCommands_Convert_To_Bom98: int = 1585
swCommands_Goto_Feature: int = 1586
swCommands_Goto_Component: int = 1587
swCommands_Edit_Findinfm: int = 1588
swCommands_Edit_User_Dims: int = 1589
swCommands_Filter2: int = 1590
swCommands_Lock_Filter2: int = 1591
swCommands_Filt_Pushpin: int = 1592
swCommands_Toggle_Viewing_Dir: int = 1593
swCommands_Filt_Plane: int = 1594
swCommands_Filt_Centermark: int = 1595
swCommands_Filt_Dimn: int = 1596
swCommands_Filt_Note: int = 1597
swCommands_Filt_Cthread: int = 1598
swCommands_Filt_Sfsymbol: int = 1599
swCommands_Filt_Gtol: int = 1600
swCommands_Filt_Datumfeat: int = 1601
swCommands_Filt_Datumtag: int = 1602
swCommands_Filt_Weldsymb: int = 1603
swCommands_Filt_Skitem: int = 1604
swCommands_Filt_Skpoint: int = 1605
swCommands_Filt_Midpoint: int = 1606
swCommands_Offset_Dim_Text: int = 1607
swCommands_Lock_Filter: int = 1608
swCommands_Filter_Toolbar: int = 1609
swCommands_Filt_Clear: int = 1610
swCommands_Filt_Face: int = 1611
swCommands_Filt_Edge: int = 1612
swCommands_Filt_Vertice: int = 1613
swCommands_Filt_Axis: int = 1614
swCommands_Forward: int = 1615
swCommands_Backward: int = 1616
swCommands_Home: int = 1617
swCommands_Reload: int = 1618
swCommands_Filter_Onoff: int = 1619
swCommands_Filter_Onoff2: int = 1620
swCommands_Small_Icon: int = 1621
swCommands_Large_Icon: int = 1622
swCommands_Filt_All: int = 1623
swCommands_Set_As_Anchor: int = 1624
swCommands_User_Menu_Min: int = 1625
swCommands_User_Menu_Max: int = 1626
swCommands_User_Toolbar_Min: int = 1627
swCommands_User_Toolbar_Max: int = 1628
swCommands_Macro_Menu_Min: int = 1629
swCommands_Macro_Menu_Max: int = 1630
swCommands_Enable_Overlay_View: int = 1631
swCommands_Insert_Schematic: int = 1632
swCommands_Feat_Import_Rebuild: int = 1633
swCommands_Debug_Enable_Fillet_Dve: int = 1634
swCommands_Command_Option_Toggle: int = 1635
swCommands_Enable_Sweepbodypattern: int = 1636
swCommands_Rotate_Routing_Clip: int = 1637
swCommands_Insert_Mirror_Subassembly: int = 1638
swCommands_Toggle_Enhanced_Routing: int = 1639
swCommands_View_Normal_To: int = 1640
swCommands_Bring_Move_Comp: int = 1641
swCommands_Goback_To_Drawing: int = 1642
swCommands_Dve_Rmb_Multi_Radius: int = 1643
swCommands_Dve_Rmb_Propagate: int = 1644
swCommands_Debug_Helical_Sweep: int = 1645
swCommands_Debug_Api_Attribs: int = 1646
swCommands_Show_Dependents_All_Configs: int = 1647
swCommands_Show_Dependents_Select_Configs: int = 1648
swCommands_Hide_Components_All_Configs: int = 1649
swCommands_Hide_Components_Select_Configs: int = 1650
swCommands_Show_Components_All_Configs: int = 1651
swCommands_Show_Components_Select_Configs: int = 1652
swCommands_Dve_Rmb_Close_Spline_Curve: int = 1653
swCommands_Dve_Rmb_Linear_Surface: int = 1654
swCommands_Dve_Rmb_Lpat_Varysketch: int = 1655
swCommands_Dve_Rmb_Lpat_Geometry_Pattern: int = 1656
swCommands_Dve_Rmb_Lpat_Flip_Direction1: int = 1657
swCommands_Dve_Rmb_Lpat_Flip_Direction2: int = 1658
swCommands_Gdi_Doublebuffer_Anim: int = 1659
swCommands_Rmb_Cpat_Equal_Space: int = 1660
swCommands_Rmb_Cpat_Geometry_Pattern: int = 1661
swCommands_Rmb_Spat_Centroid: int = 1662
swCommands_Rmb_Spat_Geometry_Pattern: int = 1663
swCommands_Rmb_Extend_Distance: int = 1664
swCommands_Rmb_Extend_Upto_Point: int = 1665
swCommands_Rmb_Extend_Upto_Surface: int = 1666
swCommands_Rmb_Cpat_Flip_Direction: int = 1667
swCommands_Dve_Skin0: int = 1668
swCommands_Dve_Skin1: int = 1669
swCommands_Dve_Skin2: int = 1670
swCommands_Dve_Skin3: int = 1671
swCommands_Dve_Skin4: int = 1672
swCommands_Debug_Draw_Sketch_Ogl: int = 1673
swCommands_Sk_Endchain: int = 1674
swCommands_Ole_Edit: int = 1675
swCommands__3d_Dcm_Switches: int = 1676
swCommands_Enable_Cam_Mate: int = 1677
swCommands_Edit_Broken_Out_Section: int = 1678
swCommands_Open_From_Webfolder: int = 1679
swCommands_Save_To_Webfolder: int = 1680
swCommands_Dve_No_Manipulator: int = 1681
swCommands_Enable_Group_Annotations: int = 1682
swCommands_Mirrcmd_Mirror_All_Children: int = 1683
swCommands_Mirrcmd_Mirror_All_Instances: int = 1684
swCommands_Debug_Xmit_Now: int = 1685
swCommands_Mirrcmd_Copy_All_Instances: int = 1686
swCommands_Mirrcmd_Browse: int = 1687
swCommands_Mirrcmd_Preview_Show: int = 1688
swCommands_Mirrcmd_Preview_Hide: int = 1689
swCommands_Mirrcmd_Preview_Mirror_Show: int = 1690
swCommands_Mirrcmd_Preview_Mirror_Hide: int = 1691
swCommands_Mirrcmd_Preview_Instance_Show: int = 1692
swCommands_Mirrcmd_Preview_Instance_Hide: int = 1693
swCommands_App_Killtipofday: int = 1694
swCommands_Debug_Enable_Hole_Series_Tab: int = 1695
swCommands_Select_Tangency_Laminar: int = 1696
swCommands_Select_Open_Edge_Loop: int = 1697
swCommands_Debug_Offset_Thicken_Shell: int = 1698
swCommands_Transparent_Edit: int = 1699
swCommands_Dcubed_Debug: int = 1700
swCommands_Transparentcontext_Edit: int = 1701
swCommands_Auto_Size: int = 1702
swCommands_Enable_Auto_Simplify: int = 1703
swCommands_Tweak_Surface: int = 1704
swCommands_Enable_Prc_Proj: int = 1705
swCommands_Debug_Keyhole: int = 1706
swCommands_Rip_Both_Directions: int = 1707
swCommands_Rip_Single_Direction: int = 1708
swCommands__Debug_Persistent_Dcms: int = 1709
swCommands_Add_Constraint_Horiz: int = 1710
swCommands_Add_Constraint_Vert: int = 1711
swCommands_Add_Constraint_Colinear: int = 1712
swCommands_Add_Constraint_Coradial: int = 1713
swCommands_Add_Constraint_Perp: int = 1714
swCommands_Add_Constraint_Parallel: int = 1715
swCommands_Add_Constraint_Tang: int = 1716
swCommands_Add_Constraint_Concent: int = 1717
swCommands_Add_Constraint_Atmid: int = 1718
swCommands_Add_Constraint_Atinter: int = 1719
swCommands_Add_Constraint_Coinc: int = 1720
swCommands_Add_Constraint_Samelen: int = 1721
swCommands_Add_Constraint_Sym: int = 1722
swCommands_Add_Constraint_Fix: int = 1723
swCommands_Add_Constraint_Atpierce: int = 1724
swCommands_Add_Constraint_Merge: int = 1725
swCommands_Add_Constraint_Normal: int = 1726
swCommands_Add_Constraint_Parallelyz: int = 1727
swCommands_Add_Constraint_Parallelzx: int = 1728
swCommands_Add_Constraint_Equalcurvature: int = 1729
swCommands_Add_Constraint_Equaltangent: int = 1730
swCommands_Add_Constraint_Tanface: int = 1731
swCommands_Add_Constraint_Traction: int = 1732
swCommands_Persistent_Ass_Solver: int = 1733
swCommands_Clear_List_Box: int = 1734
swCommands_Delete_List_Box_Item: int = 1735
swCommands_Quick_Create_Plane: int = 1736
swCommands_Fillet_Preview: int = 1737
swCommands_Bufferswapnotify_Reduction: int = 1738
swCommands_Allow_Constraints_To_Circs_In_Assem: int = 1739
swCommands_Tools_New_Addins: int = 1740
swCommands_Edit_Cavity_Part: int = 1741
swCommands_Not_Satisfied: int = 1742
swCommands_Build_Doctor: int = 1743
swCommands_Solidworks_Central: int = 1744
swCommands_Auto_Simplify_On_Save: int = 1745
swCommands_Auto_Simplify_On_Open: int = 1746
swCommands_Auto_Simplify_Now: int = 1747
swCommands_Auto_Unsimplify_Now: int = 1748
swCommands_Auto_Simplify_Cull_Faces: int = 1749
swCommands_Auto_Simplify_Cull_Components: int = 1750
swCommands_Auto_Simplify_Static_Render: int = 1751
swCommands_Auto_Simplify_Dyn_Render: int = 1752
swCommands_Auto_Simplify_Hlr: int = 1753
swCommands_Auto_Simplify_Photoworks: int = 1754
swCommands_Auto_Simplify_Shadows: int = 1755
swCommands_Auto_Simplify_Save_As_Xt: int = 1756
swCommands_Auto_Simplify_Move_Component: int = 1757
swCommands_Auto_Simplify_Rotate_Component: int = 1758
swCommands_Auto_Simplify_Collision: int = 1759
swCommands_Auto_Simplify_Clearance: int = 1760
swCommands_Rmb_Zebra_Properties: int = 1761
swCommands_Debug_Use_Display_Data: int = 1762
swCommands_Delete_All_Constraints: int = 1763
swCommands_Rmb_Createplane_Linepoint: int = 1764
swCommands_Rmb_Createplane_Parallel: int = 1765
swCommands_Rmb_Createplane_Angle: int = 1766
swCommands_Rmb_Createplane_Offset: int = 1767
swCommands_Rmb_Createplane_Curve: int = 1768
swCommands_Rmb_Createplane_Csys: int = 1769
swCommands_Rmb_Createplane_Onsurface: int = 1770
swCommands_Soft_Shadows: int = 1771
swCommands_Import_To_Drawing: int = 1772
swCommands_Rmb_Spat_Selpoint: int = 1773
swCommands__2dto3d: int = 1774
swCommands__2dto3d_Copy: int = 1775
swCommands__2dto3d_Paste: int = 1776
swCommands__2dto3d_Reset: int = 1777
swCommands_Leader_Add_Branch: int = 1778
swCommands_Leader_Delete_Bent: int = 1779
swCommands_Leader_Add_Bent: int = 1780
swCommands_Leader_Delete_All: int = 1781
swCommands_Debug_Test_Plane_Manip: int = 1782
swCommands_Aem: int = 1783
swCommands_Insert_Macro_Feature: int = 1784
swCommands_Debug_Force_Feat_Current_Time: int = 1785
swCommands_Break_Dim_Lines: int = 1786
swCommands_Edit_Exit_No_Save: int = 1787
swCommands__Display_Mup: int = 1788
swCommands_Rmb_Rib_First_Side: int = 1789
swCommands_Rmb_Rib_Second_Side: int = 1790
swCommands_Rmb_Rib_Both_Sides: int = 1791
swCommands_Rmb_Rib_Normal_To_Sketch: int = 1792
swCommands_Rmb_Rib_Parallel_To_Sketch: int = 1793
swCommands__Dump_Selection_Manager: int = 1794
swCommands_Insert_Model_Items: int = 1795
swCommands_Drw_Rebuild_All: int = 1796
swCommands_Cull_Dynamic_Switch: int = 1797
swCommands_Cull_Static_Switch: int = 1798
swCommands_Cull_Dynamic_Update: int = 1799
swCommands_Auto_Simplify_Drawing_View_Creation: int = 1800
swCommands_Insert_Surface_Move: int = 1801
swCommands_Select_Seed_Feature: int = 1802
swCommands_View_Zoom_About_Center: int = 1803
swCommands_Sk_Endspline: int = 1804
swCommands_Zebra_Properties: int = 1805
swCommands_Flip_Dowel_Sym: int = 1806
swCommands_Rmb_Face_Zebra_Stripes: int = 1807
swCommands_Rmb_Ann_Use_Jog_Leader: int = 1808
swCommands_Delete_Selected_Constraint: int = 1809
swCommands_View_Disp_Hideall: int = 1810
swCommands_Edit_Text: int = 1811
swCommands__Aemswitches: int = 1812
swCommands_Assy_Edit_Opaque: int = 1813
swCommands_Assy_Edit_Maintain: int = 1814
swCommands_Assy_Edit_Full: int = 1815
swCommands_Edit_Sk_Pattern: int = 1816
swCommands_Sketch_Jog_Flip: int = 1817
swCommands_Add_Split_Feat_To_Asm: int = 1818
swCommands_Dve_Rmb_Show_Preview: int = 1819
swCommands_WPF_StyleManager: int = 1820
swCommands_Start_Dialog_Reg_Test: int = 1821
swCommands_Debug_Set_Feature_Auto_Name: int = 1822
swCommands_Sm_Insert_Relief_Feat: int = 1823
swCommands_Auto_Simplify_Auto_Recull: int = 1824
swCommands_Enable_Save_Assembly_As_Part: int = 1825
swCommands_Enable_Pdm: int = 1826
swCommands_Enable_Lightweight_Drawings: int = 1827
swCommands_Enable_Superlightweight: int = 1828
swCommands_Insert_Folder: int = 1829
swCommands_Sm_Measure_Bend_Deviation: int = 1830
swCommands_Debug_Pk_Lofted_Body: int = 1831
swCommands_Debug_Dump_Sectioned_Bodies: int = 1832
swCommands_Insert_Sketch_Dxfdwg: int = 1833
swCommands_Dotmenu_Scenegraph_Dump_Memory: int = 1834
swCommands_Dotmenu_Scenegraph_Dump_Structure: int = 1835
swCommands_Back_Office_Precreate_Drview: int = 1836
swCommands_Insert_Macro_Feature_Drawing: int = 1837
swCommands_Geometric_Callout: int = 1838
swCommands_Holewizard_Callout: int = 1839
swCommands__Dcubedoptions_Sketchdebugswitches: int = 1840
swCommands__Debug_Sketch_Switches: int = 1841
swCommands__Debug_Assembly_Switches: int = 1842
swCommands_Back_Office_Precreate_Drview_Enable: int = 1843
swCommands_Smp_Assm_Hlr_Drawing: int = 1844
swCommands_Spline_Switch: int = 1845
swCommands_Unlock_Configuration: int = 1846
swCommands_Lock_Configuration: int = 1847
swCommands_Insert_Designtable: int = 1848
swCommands_Insert_Drw_Dxfdwg: int = 1849
swCommands_Debug_Preview_Assm_Hlr: int = 1850
swCommands_Debug_Skoffset_Line_Preview: int = 1851
swCommands_Debug_Skoffset_Popup_Text: int = 1852
swCommands_Save_Config_Preview: int = 1853
swCommands_Bgproc_Block: int = 1854
swCommands_Insert_Com_Feature_Min: int = 1855
swCommands_Edit_Smart_Insert: int = 1856
swCommands_Mark_Smart_Insert_Uptodate: int = 1857
swCommands_Split_Open_Segm_Ar: int = 1858
swCommands_Rmb_Ar_Autoroute: int = 1859
swCommands_Insert_Com_Feature_Max: int = 1860
swCommands__Mirrormates: int = 1861
swCommands_Enablenewnote: int = 1862
swCommands_Blockdef_Properties: int = 1863
swCommands_Blockdef_Select_All_Insts: int = 1864
swCommands_Blockdef_Delete_All_Insts: int = 1865
swCommands_Blockdef_Edit: int = 1866
swCommands_Draw_View_Start_Hlr: int = 1867
swCommands_Draw_All_View_Start_Hlr: int = 1868
swCommands_Aem_Sim_Startstop: int = 1869
swCommands_Aem_Sim_Addeditspring: int = 1870
swCommands_Aem_Sim_Slow: int = 1871
swCommands_Aem_Sim_Ffwd: int = 1872
swCommands_Cmark_Setbase: int = 1873
swCommands__Dump_Refchain_Manager: int = 1874
swCommands_Show_Ogl_Stats: int = 1875
swCommands_Sheet_Draft_Mode: int = 1876
swCommands_Enable_Dynamic_Load_Body: int = 1877
swCommands_Insert_Geometry_Import: int = 1878
swCommands_View_Incr_Tessellation: int = 1879
swCommands_Spline_Tool_Region_Drag: int = 1880
swCommands_Aem_Sim_Addeditmotor: int = 1881
swCommands_Help_Autocad_Users: int = 1882
swCommands_Reset_Solvers: int = 1883
swCommands_Display_Property_Dve: int = 1884
swCommands_Block_Insert: int = 1885
swCommands_Block_Make: int = 1886
swCommands_Block_Edit: int = 1887
swCommands_Block_Explode: int = 1888
swCommands_Block_Delete: int = 1889
swCommands_Block_Select_Instances: int = 1890
swCommands_Block_Edit_Instance: int = 1891
swCommands_Auto_Dim_Drawing: int = 1892
swCommands_Cmark_Merge: int = 1893
swCommands_Sketch_Show_Constraints: int = 1894
swCommands_View_Showantn_Linkerrors: int = 1895
swCommands_Block_Edit_From_File: int = 1896
swCommands__Debug_Auto_Dim_Sketch: int = 1897
swCommands_Cmark_Select: int = 1898
swCommands_Edit_Bendtable_Open: int = 1899
swCommands_Toggle_Pic_Texture: int = 1900
swCommands_Aem_Sim_Savereplay: int = 1901
swCommands_Aem_Sim_Pause: int = 1902
swCommands_Aem_Sim_Reverse: int = 1903
swCommands_Add_To_Favorite: int = 1904
swCommands_Read_Only_Pref: int = 1905
swCommands_Create_Empty_Folder: int = 1906
swCommands_Edit_Delete_Replay: int = 1907
swCommands_Driven_Dim: int = 1908
swCommands_Block_New: int = 1909
swCommands_Sketch_Hide_Constraints: int = 1910
swCommands_Button38171: int = 1911
swCommands_Button38172: int = 1912
swCommands_Button38173: int = 1913
swCommands_Button38174: int = 1914
swCommands_Aem_Sim_Ping_Ping: int = 1915
swCommands_Aem_Sim_Ping_Pong: int = 1916
swCommands_Dotmenu_Disable_Edge_Cache: int = 1917
swCommands_Button38181: int = 1918
swCommands_Button38183: int = 1919
swCommands_Manufacturing_Network: int = 1920
swCommands_Aem_Sim_Addedittorsional_Spring: int = 1921
swCommands_Insert_Gearmate: int = 1922
swCommands_Chamfer_Preview: int = 1923
swCommands_Sketch_Hide_All_Constraints: int = 1924
swCommands_Debug_Enable_Many_Curv_Surf: int = 1925
swCommands_Aem_Sim_Addedit_Conveyor: int = 1926
swCommands_Force_Convert_Explode: int = 1927
swCommands_Debug_Enable_Helical_Sweep_Performance: int = 1928
swCommands_Switch_To_Toolbar_First: int = 1929
swCommands_Switch_To_Sketch_Toolbar: int = 1930
swCommands_Switch_To_Feature_Toolbar: int = 1931
swCommands_Switch_To_Sht_Mtl_Toolbar: int = 1932
swCommands_Switch_To_Surface_Toolbar: int = 1933
swCommands_Switch_To_Assembly_Toolbar: int = 1934
swCommands_Switch_To_Drawing_Toolbar: int = 1935
swCommands_Sketch_Suppress_Constraints: int = 1936
swCommands_Switch_To_Toolbar_Last: int = 1937
swCommands_Customization_And_More: int = 1938
swCommands_Drawing_Assembly_Stats: int = 1939
swCommands_Tools_Move_Copy: int = 1940
swCommands_Component_Pattern_Linear: int = 1941
swCommands_Component_Pattern_Circular: int = 1942
swCommands_Component_Pattern_Feature: int = 1943
swCommands_Rmb_Mate_Apply: int = 1944
swCommands_Dve_Rmb_Undo: int = 1945
swCommands_Quick_Help: int = 1946
swCommands_Dve_Rmb_Redo: int = 1947
swCommands_Pe_Newsgroup: int = 1948
swCommands_Debug_Enable_Improvedrawingviewcreation: int = 1949
swCommands_Lic_Agreement: int = 1950
swCommands_Debug_Material_Editor: int = 1951
swCommands_Enable_Shared_Tessellation: int = 1952
swCommands_Insert_End_Cap: int = 1953
swCommands_Silhouette_Offsets: int = 1954
swCommands_Layer_Toolbar: int = 1955
swCommands_Sketch_Tools_Toolbar: int = 1956
swCommands_UseWpfCommands: int = 1957
swCommands_WpfTestCommand: int = 1958
swCommands_Animation_Goto_Start: int = 1959
swCommands_Animation_Rewind: int = 1960
swCommands_Animation_Play: int = 1961
swCommands_Animation_Ff: int = 1962
swCommands_Animation_Goto_End: int = 1963
swCommands_Animation_Pause: int = 1964
swCommands_Animation_Stop: int = 1965
swCommands_Animation_Record: int = 1966
swCommands_Animation_Play_Normal: int = 1967
swCommands_Animation_Play_Loop: int = 1968
swCommands_Animation_Play_Reciprocate: int = 1969
swCommands_Animation_Play_Slow: int = 1970
swCommands_Animation_Play_Fast: int = 1971
swCommands_Recorddrag: int = 1972
swCommands_Insert_Create_Assy: int = 1973
swCommands_Insert_Create_Assy_Feat: int = 1974
swCommands_Table_Cell_Sub_Total: int = 1975
swCommands_Table_Cell_Total: int = 1976
swCommands_Collapse_Tree: int = 1977
swCommands_Enable_Light_Manipulators: int = 1978
swCommands_Edit_Color_Scheme: int = 1979
swCommands_View_Cg: int = 1980
swCommands_Customization_Context_Tbar: int = 1981
swCommands_View_Animate_Explode_Assembly: int = 1982
swCommands_View_Animate_Collapse_Assembly: int = 1983
swCommands_Quick_Help_Part: int = 1984
swCommands_Quick_Help_Drawing: int = 1985
swCommands_Quick_Help_Assembly: int = 1986
swCommands_Whats_New_Interactive: int = 1987
swCommands_Quick_Help_Assembly2: int = 1988
swCommands_Display_Face: int = 1989
swCommands_Toggle_Context_Switch: int = 1990
swCommands_Move_Alignment_Part: int = 1991
swCommands_Move_Alignment_Assembly: int = 1992
swCommands_View_Move_Manipulator: int = 1993
swCommands_Help_Partnersolutions: int = 1994
swCommands_Conc_Dim_Show_Extn_Lines: int = 1995
swCommands_Debug_Enable_Previewwithmodelviewslist: int = 1996
swCommands_Edit_Table_Row_Property: int = 1997
swCommands_Search_Detail_Items: int = 1998
swCommands_Recognize_Features: int = 1999
swCommands_Move_Up_Using_Arrow_Key: int = 2000
swCommands_Move_Down_Using_Arrow_Key: int = 2001
swCommands_Move_Left_Using_Arrow_Key: int = 2002
swCommands_Move_Right_Using_Arrow_Key: int = 2003
swCommands__Debug_Pgm: int = 2004
swCommands_Front_Top_Side_Viewports: int = 2005
swCommands_First_Angle_Projection: int = 2006
swCommands_Favorite_Material_1: int = 2007
swCommands_Favorite_Material_2: int = 2008
swCommands_Favorite_Material_3: int = 2009
swCommands_Favorite_Material_4: int = 2010
swCommands_Favorite_Material_5: int = 2011
swCommands_Favorite_Material_6: int = 2012
swCommands_Favorite_Material_7: int = 2013
swCommands_Favorite_Material_8: int = 2014
swCommands_Favorite_Material_9: int = 2015
swCommands_Favorite_Material_10: int = 2016
swCommands_Copy_Swift_Schema: int = 2017
swCommands_Edit_Swift_Schema: int = 2018
swCommands_Debug_Anim_Capture: int = 2019
swCommands_Insert_Swift_Symbol: int = 2020
swCommands_Debug_Hsds_Dialog: int = 2021
swCommands_Create_New_Configuration: int = 2022
swCommands_Skg_Remove: int = 2023
swCommands_Skg_Insertionpoint: int = 2024
swCommands_Skg_Save: int = 2025
swCommands_Skg_Ok: int = 2026
swCommands_Skg_Cancel: int = 2027
swCommands_Toolbar_Sketch_Group: int = 2028
swCommands_Debug_Visual_Overlay: int = 2029
swCommands_Content_Filter_All: int = 2030
swCommands_Content_Filter_Parts: int = 2031
swCommands_Content_Filter_Asm: int = 2032
swCommands_Content_Filter_Features: int = 2033
swCommands_Content_Filter_Notes: int = 2034
swCommands_Content_Filter_Gtol: int = 2035
swCommands_Content_Filter_Sfin: int = 2036
swCommands_Content_Filter_Weld: int = 2037
swCommands_Content_Filter_Formtools: int = 2038
swCommands_Content_Back: int = 2039
swCommands_Content_Forward: int = 2040
swCommands_Content_Search: int = 2041
swCommands_Content_Reload: int = 2042
swCommands_Asm_Configure_All_Children: int = 2043
swCommands_Asm_Configure_All_Parents: int = 2044
swCommands_Asm_Unconfigure_All: int = 2045
swCommands_Infer_Tb_Enabled: int = 2046
swCommands_Infer_Tb_Grid_Quick: int = 2047
swCommands_Infer_Tb_Nearest_Quick: int = 2048
swCommands_Hide_Swift_Dims: int = 2049
swCommands_Infer_Tb_Points_Quick: int = 2050
swCommands_Infer_Tb_Hv_Points_Quick: int = 2051
swCommands_Infer_Tb_Midpoints_Quick: int = 2052
swCommands_Infer_Tb_Intersection_Quick: int = 2053
swCommands_Infer_Tb_Hv_Quick: int = 2054
swCommands_Infer_Tb_Parallel_Quick: int = 2055
swCommands_Infer_Tb_Perpendicular_Quick: int = 2056
swCommands_Infer_Tb_Tangent_Quick: int = 2057
swCommands_Insert_Cos: int = 2058
swCommands_Activate_Doc_Or_Journal: int = 2059
swCommands_Save_Journal_As_Word: int = 2060
swCommands_Add_File_To_Docs: int = 2061
swCommands_Add_Comment: int = 2062
swCommands_Remove_All_Comments: int = 2063
swCommands_Small_List_Icon: int = 2064
swCommands_Large_List_Icon: int = 2065
swCommands_Dotmenu_New_Broken_Enabled: int = 2066
swCommands_Content_Filter_Block: int = 2067
swCommands_Edit_Paragraph: int = 2068
swCommands_Edit_Bullet: int = 2069
swCommands_Delete_Comment: int = 2070
swCommands_Edit_Comment: int = 2071
swCommands_Add_Voice_Comment: int = 2072
swCommands_Manual_Viewlabel: int = 2073
swCommands_Electrical_Open_Cable_Wire_Library: int = 2074
swCommands_Electrical_Open_Component_Library: int = 2075
swCommands_Electrical_Read_Segment_Data: int = 2076
swCommands_Electrical_Write_Segment_Data: int = 2077
swCommands_Electrical_Load_From_To_Data: int = 2078
swCommands_Electrical_Autoroute: int = 2079
swCommands_Infer_Tb_Centerpoints_Quick: int = 2080
swCommands_Hide_Swift_Ann: int = 2081
swCommands_Import_Electrical_Data: int = 2082
swCommands_Infer_Tb_Quadrants_Quick: int = 2083
swCommands_Infer_Tb_Angle_Quick: int = 2084
swCommands_Show_Feat_Based_Swift_Tree: int = 2085
swCommands_Show_Ann_Based_Swift_Tree: int = 2086
swCommands_Show_Flat_Swift_Tree: int = 2087
swCommands_Hide_Swift_All_Datum_Tags: int = 2088
swCommands_Edit_Voice_Comment: int = 2089
swCommands_Delete_Voice_Comment: int = 2090
swCommands_Debug_Prj8329_Tolerance: int = 2091
swCommands_Html_Go_Back: int = 2092
swCommands_Html_Go_Forward: int = 2093
swCommands_Html_Go_Search_The_Web: int = 2094
swCommands_Html_Go_Start_Page: int = 2095
swCommands_Html_View_Stop: int = 2096
swCommands_Html_View_Refresh: int = 2097
swCommands_Font_Restart_Number: int = 2098
swCommands_Font_Continue_Number: int = 2099
swCommands_Measure_Proj: int = 2100
swCommands_Measure_Minmax: int = 2101
swCommands_Measure_Units: int = 2102
swCommands_Measure_Xyz: int = 2103
swCommands_Measure_Csys: int = 2104
swCommands_Dist_Min: int = 2105
swCommands_Dist_Max: int = 2106
swCommands_Dist_Cc: int = 2107
swCommands_Measure_Proj_None: int = 2108
swCommands_Measure_Proj_Screen: int = 2109
swCommands_Measure_Proj_Plane: int = 2110
swCommands_Measure_Proj_Recent: int = 2111
swCommands_Measure_Defaultcsys: int = 2112
swCommands_Debug_Anim_Dimension: int = 2113
swCommands_Repeat_Command: int = 2114
swCommands_Content_Mgr_Search_Local_Cmd: int = 2115
swCommands_Content_Mgr_Search_3dcc_Cmd: int = 2116
swCommands_Swift_Ann_Disp_Angle: int = 2117
swCommands_Save_Comp: int = 2118
swCommands_Change_Write_Access_Comp: int = 2119
swCommands_Change_Write_Access: int = 2120
swCommands_View_Display_States: int = 2121
swCommands_Display_State_Rmb: int = 2122
swCommands_Debug_Enable_Smartfilterforfilletchamfer: int = 2123
swCommands_Incremental_Sg_Update: int = 2124
swCommands_Dotmenu_Use_Manipulator_In_3dsketch: int = 2125
swCommands_Sk_Endcos: int = 2126
swCommands_Sw_Taskpane: int = 2127
swCommands_Import_Electrical_Cab_Data: int = 2128
swCommands_New_Display_State: int = 2129
swCommands_Swift_Layout_Top: int = 2130
swCommands_Swift_Layout_Front: int = 2131
swCommands_Swift_Layout_Right: int = 2132
swCommands_Show_Flexible_Name: int = 2133
swCommands_Animkey_Cut: int = 2134
swCommands_Animkey_Copy: int = 2135
swCommands_Animkey_Paste: int = 2136
swCommands_Animkey_Clear: int = 2137
swCommands_Animkey_Select_All: int = 2138
swCommands_Animkey_Properties: int = 2139
swCommands_Animkey_Place: int = 2140
swCommands_Animkey_Replace: int = 2141
swCommands_Animation_New: int = 2142
swCommands_Animation_Rename: int = 2143
swCommands_Animation_Delete: int = 2144
swCommands_View_Showantn_Linkvar: int = 2145
swCommands_Gantt_Zoomin: int = 2146
swCommands_Gantt_Zoomout: int = 2147
swCommands_Import_Cable_Library: int = 2148
swCommands_Import_Component_Library: int = 2149
swCommands_Animkey_Reverse_Path: int = 2150
swCommands_Display_State_Undo: int = 2151
swCommands_Display_State_Redo: int = 2152
swCommands_Debug_Enable_Pdm_Sync: int = 2153
swCommands_Debug_Enable_Ctrl_Measure: int = 2154
swCommands_Animkey_Suppress: int = 2155
swCommands_Animkey_Interp_Step_End: int = 2156
swCommands_Animkey_Interp_Linear: int = 2157
swCommands_Animkey_Interp_Easein_Quad: int = 2158
swCommands_Animkey_Interp_Easeout_Quad: int = 2159
swCommands_Animkey_Interp_Easeinout_Quad: int = 2160
swCommands_Animkey_Interp_Easein_Sin: int = 2161
swCommands_Animkey_Interp_Easeout_Sin: int = 2162
swCommands_Animkey_Interp_Easeinout_Sin: int = 2163
swCommands_Dve_Rmb_Back: int = 2164
swCommands_Dve_Rmb_Next: int = 2165
swCommands_Edit_Rtl_Mode: int = 2166
swCommands_Content_Add_Existing_Folder: int = 2167
swCommands_Content_Create_New_Folder: int = 2168
swCommands_Option_Relations_Snaps: int = 2169
swCommands_Content_Add_File_Location: int = 2170
swCommands_Add_To_Palette: int = 2171
swCommands_Drawing_Stats: int = 2172
swCommands_Dcubed_Versions: int = 2173
swCommands_Billboards: int = 2174
swCommands_Insert_Cut_Net: int = 2175
swCommands_Insert_Stock_Net: int = 2176
swCommands_Insert_Protrusion_Volswept: int = 2177
swCommands_Insert_Volsweep_Ref_Surface: int = 2178
swCommands_Insert_Cut_Volsweep: int = 2179
swCommands_Swift_Adv_Tol_Ann: int = 2180
swCommands_Save_Smart: int = 2181
swCommands_Viewport_3d_Cursor: int = 2182
swCommands_Debug_Enable_Prc_Project: int = 2183
swCommands_Debug_Enable_3d_Project: int = 2184
swCommands_Viewport_Unsplit_Camera: int = 2185
swCommands_Show_Ogl_Framecount: int = 2186
swCommands_Insert_Annotation_Plane: int = 2187
swCommands_Swift_Other_Recognition_Engine: int = 2188
swCommands_Layout_To_Doc: int = 2189
swCommands_Sketch_Group_Flip: int = 2190
swCommands_Insert_Camera: int = 2191
swCommands_Resolve_Conflict: int = 2192
swCommands_Convert_Spline_To_Circlines: int = 2193
swCommands_Debug_Enable_Contour_Editing: int = 2194
swCommands_Addedit_Mate_Supplement: int = 2195
swCommands_Glassbox_Done: int = 2196
swCommands_Glassbox_Zoomtofit: int = 2197
swCommands_Glassbox_Zoomto: int = 2198
swCommands_Glassbox_Zoom: int = 2199
swCommands_Glassbox_Rotate: int = 2200
swCommands_Glassbox_Pan: int = 2201
swCommands_Copy_Drw_To_Dwgeditor: int = 2202
swCommands_Whats_Wrong_Tolx_Dim: int = 2203
swCommands_Add_Constraint_Alongx: int = 2204
swCommands_Add_Constraint_Alongy: int = 2205
swCommands_Add_Constraint_Alongz: int = 2206
swCommands_Edit_Decal: int = 2207
swCommands_Ann_Per_Annotation_View: int = 2208
swCommands_Annotation_Visibility: int = 2209
swCommands_Annotation_View_Create: int = 2210
swCommands_Switch_Annotation_View: int = 2211
swCommands_Autotrace_Sketchpic: int = 2212
swCommands_Activate_Annotation_View: int = 2213
swCommands_Deactivate_Annotation_View: int = 2214
swCommands_Delete_Annotation_View: int = 2215
swCommands_Orient_Annotation_By_Selection: int = 2216
swCommands_Add_Constraint_Onsurface: int = 2217
swCommands_Smart_Feature_Preview: int = 2218
swCommands_Smc_Help: int = 2219
swCommands_Insert_Smart_Features: int = 2220
swCommands_Edit_Smart_Comp_Inst: int = 2221
swCommands_Auto_Ann_View_Creation: int = 2222
swCommands_Auto_Ann_View_Generate: int = 2223
swCommands_Change_Ann_View: int = 2224
swCommands_Swift_Use_Callout_Template: int = 2225
swCommands_Light_Prop_Item_Min: int = 2226
swCommands_Light_Prop_Item_Max: int = 2227
swCommands_Light_Del_Item_Min: int = 2228
swCommands_Light_Del_Item_Max: int = 2229
swCommands_Activate_And_Orient_Annotation_View: int = 2230
swCommands_Tab_Reorient: int = 2231
swCommands_Annotation_View_Show: int = 2232
swCommands_Annotation_View_Hide: int = 2233
swCommands_Edit_Annotation_View: int = 2234
swCommands_Insert_Smartfeature: int = 2235
swCommands_Debug_Set_Res_Point: int = 2236
swCommands_Debug_Check_Res_Leak: int = 2237
swCommands_Custom_Msg_Display_Vw_By_Name: int = 2238
swCommands_Custom_Msg_Display_Camera_By_Name: int = 2239
swCommands_Debug_Enable_New_Cthread_Creation: int = 2240
swCommands_Autofix_Model: int = 2241
swCommands_Debug_Enable_Open_Multiple_Files: int = 2242
swCommands_Show_View_Palette: int = 2243
swCommands_Debug_Enable_Convert_Sheetmetal: int = 2244
swCommands_Sm_Convert_To_Sheetmetal: int = 2245
swCommands_Isolate1: int = 2246
swCommands_Isolate2: int = 2247
swCommands_Crt_Rut_Using_Connector: int = 2248
swCommands_Crt_Rt_Using_From_To_Lst: int = 2249
swCommands_Crt_Adhoc_Rt: int = 2250
swCommands_Edt_Elec_Route: int = 2251
swCommands_Edt_Elec_Wires: int = 2252
swCommands_Elec_Rt_Properties: int = 2253
swCommands_Crt_Pipe_Rt_Using_Connector: int = 2254
swCommands_Crt_Pipe_Rt_Adhoc: int = 2255
swCommands_Edit_Pipe_Rt: int = 2256
swCommands_Pipe_Rt_Properties: int = 2257
swCommands_Crt_Flex_Tube_Rt_Using_Connector: int = 2258
swCommands_Crt_Flex_Tube_Rt_Adhoc: int = 2259
swCommands_Edit_Flex_Tube_Rt: int = 2260
swCommands_Flex_Tube_Rt_Properties: int = 2261
swCommands_Flex_Tube_Rt_Guide: int = 2262
swCommands_Piping_Rt_Guide: int = 2263
swCommands_Electrical_Rt_Guide: int = 2264
swCommands_Auto_Route: int = 2265
swCommands_Route_Rotate_Clip: int = 2266
swCommands_Route_Through: int = 2267
swCommands_Route_Unhook_From: int = 2268
swCommands_Split_Route: int = 2269
swCommands_Pipe_Route: int = 2270
swCommands_Electrical_Route: int = 2271
swCommands_Flexible_Tube_Route: int = 2272
swCommands_Align_With_Comp_Origin: int = 2273
swCommands_Align_With_Assy_Origin: int = 2274
swCommands_Snap_To_Selection: int = 2275
swCommands_Snap_While_Dragging: int = 2276
swCommands_Rotate_90_Degrees: int = 2277
swCommands_Rotate_180_Degrees: int = 2278
swCommands_Align_With_Selection: int = 2279
swCommands_Enable_Conics: int = 2280
swCommands_Swift_Fpo_Constr_Point: int = 2281
swCommands_Swift_Fpo_Constr_Line: int = 2282
swCommands_Swift_Fpo_Constr_Circle: int = 2283
swCommands_Swift_Fpo_Constr_Plane: int = 2284
swCommands_Add_Fitting: int = 2285
swCommands_Add_Coverings: int = 2286
swCommands_Content_Wizard: int = 2287
swCommands_Change_Route_Dia: int = 2288
swCommands_Repair_Route: int = 2289
swCommands_Add_Bends: int = 2290
swCommands_Move_Spherical_Manipulator: int = 2291
swCommands_Resize_Spherical_Manipulator: int = 2292
swCommands__Debug_Memory_Leaks: int = 2293
swCommands_Flextube_Dummy_Button_2: int = 2294
swCommands_File_Copy_Design: int = 2295
swCommands_Flextube_Dummy_Button_Big_1: int = 2296
swCommands_Flextube_Dummy_Button_Big_2: int = 2297
swCommands_Piping_Dummy_Button_1: int = 2298
swCommands_Piping_Dummy_Button_Big_1: int = 2299
swCommands_Electrical_Dummy_Button_1: int = 2300
swCommands_Electrical_Dummy_Button_2: int = 2301
swCommands_Electrical_Dummy_Button_3: int = 2302
swCommands_Electrical_Dummy_Button_4: int = 2303
swCommands_Electrical_Dummy_Button_5: int = 2304
swCommands_Electrical_Dummy_Button_6: int = 2305
swCommands_Electrical_Dummy_Button_7: int = 2306
swCommands_Electrical_Dummy_Button_8: int = 2307
swCommands_Electrical_Dummy_Button_9: int = 2308
swCommands_Electrical_Dummy_Button_10: int = 2309
swCommands_Electrical_Dummy_Button_Big_1: int = 2310
swCommands_Electrical_Dummy_Button_Big_2: int = 2311
swCommands_Electrical_Dummy_Button_Big_3: int = 2312
swCommands_Electrical_Dummy_Button_Big_4: int = 2313
swCommands_Electrical_Dummy_Button_Big_5: int = 2314
swCommands_Electrical_Dummy_Button_Big_6: int = 2315
swCommands_Electrical_Dummy_Button_Big_7: int = 2316
swCommands_Electrical_Dummy_Button_Big_8: int = 2317
swCommands_Electrical_Dummy_Button_Big_9: int = 2318
swCommands_Electrical_Dummy_Button_Big_10: int = 2319
swCommands_Common_Tool_Dummy_Button_1: int = 2320
swCommands_Common_Tool_Dummy_Button_2: int = 2321
swCommands_Common_Tool_Dummy_Button_3: int = 2322
swCommands_Common_Tool_Dummy_Button_4: int = 2323
swCommands_Common_Tool_Dummy_Button_5: int = 2324
swCommands_Common_Tool_Dummy_Button_6: int = 2325
swCommands_Common_Tool_Dummy_Button_7: int = 2326
swCommands_Common_Tool_Dummy_Button_8: int = 2327
swCommands_Common_Tool_Dummy_Button_9: int = 2328
swCommands_Common_Tool_Dummy_Button_10: int = 2329
swCommands_Common_Tool_Dummy_Button_Big_1: int = 2330
swCommands_Common_Tool_Dummy_Button_Big_2: int = 2331
swCommands_Common_Tool_Dummy_Button_Big_3: int = 2332
swCommands_Common_Tool_Dummy_Button_Big_4: int = 2333
swCommands_Common_Tool_Dummy_Button_Big_5: int = 2334
swCommands_Common_Tool_Dummy_Button_Big_6: int = 2335
swCommands_Common_Tool_Dummy_Button_Big_7: int = 2336
swCommands_Common_Tool_Dummy_Button_Big_8: int = 2337
swCommands_Common_Tool_Dummy_Button_Big_9: int = 2338
swCommands_Common_Tool_Dummy_Button_Big_10: int = 2339
swCommands_Common_Tool_Dummy_Button_11: int = 2340
swCommands_Publish_Content: int = 2341
swCommands_Split_Open_Route: int = 2342
swCommands_Anim_View_Front: int = 2343
swCommands_Anim_View_Back: int = 2344
swCommands_Anim_View_Left: int = 2345
swCommands_Anim_View_Right: int = 2346
swCommands_Anim_View_Top: int = 2347
swCommands_Anim_View_Bottom: int = 2348
swCommands_Anim_View_Isometric: int = 2349
swCommands_Anim_View_Trimetric: int = 2350
swCommands_Anim_View_Dimetric: int = 2351
swCommands_Anim_Custom_Msg_Display_Vw_By_Name: int = 2352
swCommands_Anim_Custom_Msg_Display_Camera_By_Name: int = 2353
swCommands_Anim_View_Camera: int = 2354
swCommands_View_Scale_Has_Changed: int = 2355
swCommands_Zebra_Stripe_Preview: int = 2356
swCommands_Savenotification: int = 2357
swCommands_Change_Shader: int = 2358
swCommands_Bold_Menu_Title: int = 2359
swCommands_Edit_Weldment_Props: int = 2360
swCommands_Delete_Weldment: int = 2361
swCommands_Hole_Table_Hide_Origin: int = 2362
swCommands_Hole_Table_Show_Origin: int = 2363
swCommands_Hole_Table_Goto_Tag: int = 2364
swCommands_Spline_Tool_Delete_Tangency: int = 2365
swCommands_Spline_Tool_Delete_Curvature: int = 2366
swCommands_Create_Sub_Weldment: int = 2367
swCommands_Hole_Table_Expand_Same_Size: int = 2368
swCommands_Hole_Table_Show_Centers: int = 2369
swCommands_Hole_Table_Hide_Centers: int = 2370
swCommands_View_Precise_Mode: int = 2371
swCommands_View_Fast_Mode: int = 2372
swCommands_Insert_Weldment: int = 2373
swCommands_Edit_Sub_Weld_Props: int = 2374
swCommands_Saveto_Separate_File: int = 2375
swCommands_Tools_Macro_Mru_1: int = 2376
swCommands_Tools_Macro_Mru_2: int = 2377
swCommands_Tools_Macro_Mru_3: int = 2378
swCommands_Tools_Macro_Mru_4: int = 2379
swCommands_Tools_Macro_Mru_5: int = 2380
swCommands_Tools_Macro_Mru_6: int = 2381
swCommands_Tools_Macro_Mru_7: int = 2382
swCommands_Tools_Macro_Mru_8: int = 2383
swCommands_Tools_Macro_Mru_9: int = 2384
swCommands_Api_Menu_String_Macro: int = 2385
swCommands_Helixdve_Revdir: int = 2386
swCommands_Helix_Cw: int = 2387
swCommands_Helix_Taperhelix: int = 2388
swCommands_Helix_Ccw: int = 2389
swCommands_Edit_Folder_Feat: int = 2390
swCommands_Feature_Pop_Make_Weld_Bead: int = 2391
swCommands_Feature_Pop_Suppress_Weld_Beads: int = 2392
swCommands_Feature_Pop_Remove_Weld_Bead: int = 2393
swCommands_Feature_Pop_Unsuppress_Weld_Beads: int = 2394
swCommands_View_Fm_By_Dep_And_Feat: int = 2395
swCommands_Insert_Advance_Helix_Creation: int = 2396
swCommands_Route_Io_Output: int = 2397
swCommands_Measure_Showcallouts: int = 2398
swCommands_Activex_First: int = 2399
swCommands_Debug_Api_Activex_Controls: int = 2400
swCommands_Activex_1: int = 2401
swCommands_Activex_2: int = 2402
swCommands_Activex_3: int = 2403
swCommands_Activex_4: int = 2404
swCommands_Activex_10: int = 2405
swCommands_Activex_Last: int = 2406
swCommands_Activex_5: int = 2407
swCommands_Activex_6: int = 2408
swCommands_Activex_7: int = 2409
swCommands_Activex_8: int = 2410
swCommands_Activex_9: int = 2411
swCommands_Ann_View_Item1: int = 2412
swCommands_Ann_View_Item2: int = 2413
swCommands_Ann_View_Item3: int = 2414
swCommands_Ann_View_Item4: int = 2415
swCommands_Ann_View_Item5: int = 2416
swCommands_Ann_View_Item6: int = 2417
swCommands_Ann_View_Item7: int = 2418
swCommands_Ann_View_Item8: int = 2419
swCommands_Ann_View_Item9: int = 2420
swCommands_Ann_View_Item10: int = 2421
swCommands_Ann_View_Item11: int = 2422
swCommands_Ann_View_Item12: int = 2423
swCommands_Ann_View_Item13: int = 2424
swCommands_Ann_View_Item14: int = 2425
swCommands_Ann_View_Item15: int = 2426
swCommands_Ann_View_Item16: int = 2427
swCommands_Ann_View_Item17: int = 2428
swCommands_Ann_View_Item18: int = 2429
swCommands_Ann_View_Item19: int = 2430
swCommands_Ann_View_Item20: int = 2431
swCommands_Show_Pgm_Untrimmed: int = 2432
swCommands_Hide_Pgm_Untrimmed: int = 2433
swCommands_Delete_Pgm_Sketch_Offset: int = 2434
swCommands_Select_Open_Half_Loop: int = 2435
swCommands_Debug_Enable_Dragdrop_Insert: int = 2436
swCommands_Hole_Table_Show_Tags: int = 2437
swCommands_Hole_Table_Hide_Tags: int = 2438
swCommands_Dve_Rmb_Exit_Preview: int = 2439
swCommands_Show_3d_Sketch_Triad: int = 2440
swCommands_Move_Annotation_To_View: int = 2441
swCommands_Orient_Annotation_View: int = 2442
swCommands_Enable_Ann_View_Mode: int = 2443
swCommands_Toggle_Smart_Dim_Mode: int = 2444
swCommands_Toggle_Power_Dim_Mode: int = 2445
swCommands_Toogle_Bwrtree: int = 2446
swCommands_Route_Guide: int = 2447
swCommands_Routing_Tools: int = 2448
swCommands_Triad_Blob_Align_To: int = 2449
swCommands_Content_Uponelevel: int = 2450
swCommands_Mate_Graph_Debug_View: int = 2451
swCommands_Assign_Smart_Fastener: int = 2452
swCommands_Flip_Smart_Fastener: int = 2453
swCommands_Near_Stack_Smart_Fastener: int = 2454
swCommands_Far_Stack_Smart_Fastener: int = 2455
swCommands_Properties_Smart_Fastener: int = 2456
swCommands_Delete_Smart_Fastener: int = 2457
swCommands_Open_Associated_Drw: int = 2458
swCommands_Dve_Rmb_Select_Feature: int = 2459
swCommands_Debug_Enable_2ptspline: int = 2460
swCommands_Add_Derived_Configuration: int = 2461
swCommands_Add_Smartfastener_String: int = 2462
swCommands_Edit_Smart_Fastener: int = 2463
swCommands_Mark_Smart_Fastener_Uptodate: int = 2464
swCommands_Switch_To_Novice_Mode: int = 2465
swCommands_Switch_To_Novice_Mode_List: int = 2466
swCommands_Switch_To_Expert_Mode: int = 2467
swCommands_Blank_Origin_Sketch: int = 2468
swCommands_Unblank_Origin_Sketch: int = 2469
swCommands_Dissolve_Sktext: int = 2470
swCommands_Select_Chain: int = 2471
swCommands_Rmb_Onto_Sketch: int = 2472
swCommands_Rmb_Onto_Face: int = 2473
swCommands_Rmb_Reverse: int = 2474
swCommands_Rmb_Leader_Done: int = 2475
swCommands_Mjl_Add_Horizontal_Bent: int = 2476
swCommands_Debug_Test_Sizable_Plane_Manip: int = 2477
swCommands_Hide_Sketch_Dim_In_Drawing: int = 2478
swCommands_Show_Sketch_Dim_In_Drawing: int = 2479
swCommands_Fit_Clearance: int = 2480
swCommands_Fit_Transitional: int = 2481
swCommands_Fit_Press: int = 2482
swCommands_Fit_None: int = 2483
swCommands_Fit_User: int = 2484
swCommands_Blank_Pic_Feat: int = 2485
swCommands_Unblank_Pic_Feat: int = 2486
swCommands_Show_Feature_Name: int = 2487
swCommands_Show_Feature_Des: int = 2488
swCommands_Show_Comp_Filename: int = 2489
swCommands_Show_Comp_Des: int = 2490
swCommands_Show_Config_Name: int = 2491
swCommands_Show_Configname_In_Configtree: int = 2492
swCommands_Show_Configdes_In_Configtree: int = 2493
swCommands_Show_Config_Previews: int = 2494
swCommands_Start_Select_Contour: int = 2495
swCommands_End_Select_Contour: int = 2496
swCommands_Drawing_Feat_Edit_Def: int = 2497
swCommands_Edit_Suppress_Feature: int = 2498
swCommands_Edit_Unsuppress_Feature: int = 2499
swCommands_Rmb_Delete_Manipulator: int = 2500
swCommands_Fm_Flat_View: int = 2501
swCommands_Edit_Rolltoprevious: int = 2502
swCommands_Edit_Rolltoend: int = 2503
swCommands_Insert_Detail_Centerline_From_Comp: int = 2504
swCommands_Feature_Properties: int = 2505
swCommands_Edit_Rolltoforward: int = 2506
swCommands_Predefined_Add_Model: int = 2507
swCommands_Dt_Save_Table: int = 2508
swCommands_Dve_Uptobody: int = 2509
swCommands_Generate_Region: int = 2510
swCommands_Show_Config_Description: int = 2511
swCommands_Create_Cut_List_Folder: int = 2512
swCommands_Edit_Cut_List_Folder_Props: int = 2513
swCommands_Start_Select_Contour_2: int = 2514
swCommands_Bom_Feat_Properties: int = 2515
swCommands_Join_Contours: int = 2516
swCommands_Mate_Delete: int = 2517
swCommands_Mate_Remove: int = 2518
swCommands_Body_Properties: int = 2519
swCommands_Dve_Sketch_Message_Dlg: int = 2520
swCommands_Addedit_Mate: int = 2521
swCommands_Rmb_Loft_Synch_Hide: int = 2522
swCommands_Rmb_Loft_Synch_Undo: int = 2523
swCommands_Rmb_Loft_Synch_Hide_All: int = 2524
swCommands_Rmb_Loft_Show_All: int = 2525
swCommands_Hide_Dim_Witness: int = 2526
swCommands_Show_Dim_Witness: int = 2527
swCommands_Go_To_Mate_Component_1: int = 2528
swCommands_Hide_Mate_Component_1: int = 2529
swCommands_Show_Mate_Component_1: int = 2530
swCommands_Suppress_Mate_Component_1: int = 2531
swCommands_Resolve_Mate_Component_1: int = 2532
swCommands_Go_To_Mate_Component_2: int = 2533
swCommands_Hide_Mate_Component_2: int = 2534
swCommands_Show_Mate_Component_2: int = 2535
swCommands_Suppress_Mate_Component_2: int = 2536
swCommands_Resolve_Mate_Component_2: int = 2537
swCommands_Hide_Dim_Leader: int = 2538
swCommands_Show_Dim_Leader: int = 2539
swCommands_Explode_Delete: int = 2540
swCommands_Explode_Dissolve_Group: int = 2541
swCommands_Explode_Add_Sel_Comps_To_All: int = 2542
swCommands_Explode_Add_Sel_Comps: int = 2543
swCommands_Explode_Add_To_Group: int = 2544
swCommands_Explode_Delete_Last_Step: int = 2545
swCommands_Explode_Move_Before_Group_T: int = 2546
swCommands_Explode_Reuse_Sub: int = 2547
swCommands_Explode_Update_Sub: int = 2548
swCommands_Explode_Reuse_Tree_Sub: int = 2549
swCommands_Explode_Move_After_Group_T: int = 2550
swCommands_Explode_Move_Before_Group_G: int = 2551
swCommands_Explode_Move_After_Group_G: int = 2552
swCommands_Explode_Tree_Edit: int = 2553
swCommands_Explode_Manip_Edit: int = 2554
swCommands_Collapseallitems_Tree: int = 2555
swCommands_Hideshow_Brwser_Tree: int = 2556
swCommands_Bom_Open_Comp_File: int = 2557
swCommands_Router_Change_Mode: int = 2558
swCommands_Router_Newloc: int = 2559
swCommands_Flip_Direction: int = 2560
swCommands_Component_Display: int = 2561
swCommands_Comp_Display_Wireframe: int = 2562
swCommands_Comp_Display_Hiddengreyed: int = 2563
swCommands_Comp_Display_Hiddenremoved: int = 2564
swCommands_Comp_Display_Shaded_With_Edges: int = 2565
swCommands_Comp_Display_Shaded: int = 2566
swCommands_Comp_Display_View_Default: int = 2567
swCommands_Comp_Display_Hlr_Quality: int = 2568
swCommands_Comp_Display_Reset: int = 2569
swCommands_Create_Sub_Bodyfolder: int = 2570
swCommands_Quick_Help_App_First: int = 2571
swCommands_Quick_Help_App1: int = 2572
swCommands_Quick_Help_App2: int = 2573
swCommands_Quick_Help_App3: int = 2574
swCommands_Quick_Help_App4: int = 2575
swCommands_Quick_Help_App5: int = 2576
swCommands_Quick_Help_App6: int = 2577
swCommands_Quick_Help_App7: int = 2578
swCommands_Quick_Help_App8: int = 2579
swCommands_Quick_Help_App9: int = 2580
swCommands_Quick_Help_App10: int = 2581
swCommands_Quick_Help_App_Last: int = 2582
swCommands_Block_Save_To_File: int = 2583
swCommands__Docm_Preview: int = 2584
swCommands__Fileexplorer_Open: int = 2585
swCommands__Fileexplorer_Save: int = 2586
swCommands__Fileexplorer_Save_All: int = 2587
swCommands__Fileexplorer_Find_In_Vault_Pdmw: int = 2588
swCommands__Fileexplorer_Checkin_This_Document_Pdmw: int = 2589
swCommands__Fileexplorer_Checkin_From_Disk_Pdmw: int = 2590
swCommands__Updatereload_From_Vault_Pdmw: int = 2591
swCommands__Fileexplorer_Updatereload_All_From_Vault_Pdmw: int = 2592
swCommands__Fileexplorer_Refresh: int = 2593
swCommands_Internal_Dimension: int = 2594
swCommands__File_Explorer_View: int = 2595
swCommands__Fileexplorer_Docinfo_Pdmw: int = 2596
swCommands_Toolbar_Electrical_Routing: int = 2597
swCommands_View_Journal: int = 2598
swCommands_Show_Feature_History: int = 2599
swCommands_Suppress_Spline_Constraint_Error: int = 2600
swCommands_Automatic_Cutlist: int = 2601
swCommands_Update_Cutlist: int = 2602
swCommands_Command_History: int = 2603
swCommands_Shared_Tessellation_Method_0: int = 2604
swCommands_Shared_Tessellation_Method_1: int = 2605
swCommands_Shared_Tessellation_Method_2: int = 2606
swCommands_Shared_Tessellation_Method_3: int = 2607
swCommands_Deform_Rmb_Show_Connector: int = 2608
swCommands_Deform_Rmb_Delete_Connector: int = 2609
swCommands_Deform_Rmb_Delete_All_Connector: int = 2610
swCommands_Rmb_Loft_Synch_Undo_Last_Oper: int = 2611
swCommands_Content_Mgr_Open: int = 2612
swCommands_Int_Tree_Ignore: int = 2613
swCommands_Int_Tree_Open: int = 2614
swCommands_Int_Tree_Unignore: int = 2615
swCommands_Int_Tree_Zoom: int = 2616
swCommands_Lock_Unlock_Focus: int = 2617
swCommands_Lock_Unlock_Focus_Double_Click: int = 2618
swCommands_Fe_Search: int = 2619
swCommands_Fe_Reporting: int = 2620
swCommands_Fe_Labels: int = 2621
swCommands_Show_Table: int = 2622
swCommands_Hide_Table: int = 2623
swCommands_Fe_Docinfo: int = 2624
swCommands__Savestreamscompressed: int = 2625
swCommands_Fe_Refresh: int = 2626
swCommands_Comp_Parent_Child_Rel: int = 2627
swCommands_Start_Smart_Selection: int = 2628
swCommands_End_Smart_Selection: int = 2629
swCommands_Rmb_Loft_Mesh_Allfaces1: int = 2630
swCommands_Rmb_Loft_Mesh_Oneface1: int = 2631
swCommands_Rmb_Loft_Mesh_Clear_Allfaces1: int = 2632
swCommands_Rmb_Loft_Mesh_Clear_Oneface1: int = 2633
swCommands_Int_Tree_Coi_Int: int = 2634
swCommands_Toolbar_Flexibletube_Routing: int = 2635
swCommands_Toolbar_Piping_Routing: int = 2636
swCommands_Routing_Main_Toolbar: int = 2637
swCommands_Routing_Common_Toolbar: int = 2638
swCommands_Toolbar_Electrical_Routing_New: int = 2639
swCommands_Delete_Cut_List: int = 2640
swCommands_Tolxpr_Show_Interference: int = 2641
swCommands_Tolxpr_Hide_Interference: int = 2642
swCommands_Anim_Suppress_Viewpoint: int = 2643
swCommands_Anim_Lock_Viewpoint: int = 2644
swCommands_Dim_Foreshort: int = 2645
swCommands_Rmb_Appearance_Co: int = 2646
swCommands_Rmb_Appearance_Pm: int = 2647
swCommands_View_Appearance_Callout: int = 2648
swCommands_Rmb_Appear_Callout_Edit_Color: int = 2649
swCommands_Rmb_Appear_Callout_Edit_Texture: int = 2650
swCommands_Rmb_Appear_Callout_Edit_Opt_Props: int = 2651
swCommands_Rmb_Appear_Callout_Copy: int = 2652
swCommands_Rmb_Appear_Callout_Cut: int = 2653
swCommands_Rmb_Appear_Callout_Detach: int = 2654
swCommands_Tx_Delete_Assy_Seq: int = 2655
swCommands_Tx_Reset_Assy_Seq: int = 2656
swCommands_Tx_Create_Assy_Seq: int = 2657
swCommands_Pm_Holewiz_Close_Ok: int = 2658
swCommands_Pm_Holewiz_Close_Undo: int = 2659
swCommands_Rmb_Create_Hole_Series: int = 2660
swCommands_Debug_Disable_Full_Mate_Solve: int = 2661
swCommands_Swift_Fpo_Surf: int = 2662
swCommands_Swift_Fpo_Plane: int = 2663
swCommands_Swift_Fpo_Hole: int = 2664
swCommands_Swift_Fpo_Compound: int = 2665
swCommands_Swift_Fpo_Counterbore: int = 2666
swCommands_Swift_Fpo_Contersink: int = 2667
swCommands_Swift_Fpo_Blank: int = 2668
swCommands_Swift_Fpo_Cone: int = 2669
swCommands_Swift_Fpo_Cylinder: int = 2670
swCommands_Swift_Fpo_Sphere: int = 2671
swCommands_Swift_Fpo_Slot: int = 2672
swCommands_Swift_Fpo_Width: int = 2673
swCommands_Swift_Fpo_Pocket: int = 2674
swCommands_Swift_Fpo_Pattern: int = 2675
swCommands_Swift_Fpo_Ok: int = 2676
swCommands_Remove_Smc_Reference: int = 2677
swCommands_Rmb_Featappearance_Co: int = 2678
swCommands_Rmb_Bodyappearance_Co: int = 2679
swCommands_Rmb_Compappearance_Co: int = 2680
swCommands_Sketchplane_Delete: int = 2681
swCommands_Sketchplane_Deleteall: int = 2682
swCommands_Sketchplane_Rename: int = 2683
swCommands_Disable_Appearance_Co: int = 2684
swCommands_Rmb_Appear_Callout_Delete_Face_Color: int = 2685
swCommands_Rmb_Appear_Callout_Delete_Face_Texture: int = 2686
swCommands_Rmb_Appear_Callout_Edit_Feat_Color: int = 2687
swCommands_Rmb_Appear_Callout_Edit_Body_Color: int = 2688
swCommands_Rmb_Appear_Callout_Edit_Part_Color: int = 2689
swCommands_Rmb_Appear_Callout_Edit_Feat_Texture: int = 2690
swCommands_Rmb_Appear_Callout_Edit_Body_Texture: int = 2691
swCommands_Rmb_Appear_Callout_Edit_Part_Texture: int = 2692
swCommands_Drawing_Feat_Edit: int = 2693
swCommands_Rmb_Appear_Callout_Delete_Feat_Color: int = 2694
swCommands_Rmb_Appear_Callout_Delete_Feat_Texture: int = 2695
swCommands_Rmb_Appear_Callout_Delete_Body_Color: int = 2696
swCommands_Rmb_Appear_Callout_Delete_Body_Texture: int = 2697
swCommands_Rmb_Appear_Callout_Delete_Comp_Color: int = 2698
swCommands_Rmb_Appear_Callout_Delete_Comp_Texture: int = 2699
swCommands_Rmb_Appear_Callout_Delete_Part_Color: int = 2700
swCommands_Rmb_Appear_Callout_Delete_Part_Texture: int = 2701
swCommands_Rmb_Appear_Callout_Edit_Comp_Color: int = 2702
swCommands_Rmb_Appear_Callout_Edit_Comp_Texture: int = 2703
swCommands_Rmb_Enable_Appear_Callouts: int = 2704
swCommands_Comp_Display_Wireframe_All: int = 2705
swCommands_Comp_Display_Hiddengreyed_All: int = 2706
swCommands_Comp_Display_Hiddenremoved_All: int = 2707
swCommands_Comp_Display_Shaded_With_Edges_All: int = 2708
swCommands_Comp_Display_Shaded_All: int = 2709
swCommands_Comp_Display_View_Default_All: int = 2710
swCommands_Comp_Display_Wireframe_Specify: int = 2711
swCommands_Comp_Display_Hiddengreyed_Specify: int = 2712
swCommands_Comp_Display_Hiddenremoved_Specify: int = 2713
swCommands_Comp_Display_Shaded_With_Edges_Specify: int = 2714
swCommands_Comp_Display_Shaded_Specify: int = 2715
swCommands_Comp_Display_View_Default_Specify: int = 2716
swCommands_Sheet_Tab_Popup_Rename: int = 2717
swCommands_Nx_Select_Manager: int = 2718
swCommands_Nx_Select_Manager_End: int = 2719
swCommands_Nx_Sel_Loop: int = 2720
swCommands_Nx_Sel_Group: int = 2721
swCommands_Nx_Sel_Clear_All: int = 2722
swCommands_Nx_Sel_Open_Loop: int = 2723
swCommands_Nx_Sel_Region: int = 2724
swCommands_Nx_Sel_Regular: int = 2725
swCommands_Comp_Isolate: int = 2726
swCommands_Sketch_Align_Grid_Origin: int = 2727
swCommands_Drawing_Reload: int = 2728
swCommands_Split_Cable: int = 2729
swCommands_Blank_Atom_Body2: int = 2730
swCommands_Unblank_Atom_Body2: int = 2731
swCommands_Comp_Isolate_Exit: int = 2732
swCommands__Debug_Pgm_Gtrim: int = 2733
swCommands_Debug_Sos_Keep_Dcubed_Spline: int = 2734
swCommands_Nx_Rmb_Ok: int = 2735
swCommands_Nx_Rmb_Cancel: int = 2736
swCommands_Nx_Rmb_Clear_All: int = 2737
swCommands_Nx_Rmb_Sel_Regular: int = 2738
swCommands_Nx_Rmb_Sel_Group: int = 2739
swCommands_Nx_Rmb_Sel_Open_Loop: int = 2740
swCommands_Nx_Rmb_Sel_Closed_Loop: int = 2741
swCommands_Nx_Rmb_Sel_Region: int = 2742
swCommands_Nx_Rmb_Push_Pin: int = 2743
swCommands_Nx_Rmb_Auto_Ok: int = 2744
swCommands_Swift_Multi_Select: int = 2745
swCommands_Swift_Multi_Select_End: int = 2746
swCommands_Debug_Enable_Horz_Nec: int = 2747
swCommands_Debug_Enable_Nec_Modifydlg: int = 2748
swCommands__Debug_Dont_Undo_Drag: int = 2749
swCommands_Edit_Sketch_Belt: int = 2750
swCommands_View_Mates_Transparency: int = 2751
swCommands_Swift_Fpo_Notch: int = 2752
swCommands_Swift_Fpo_Fillet: int = 2753
swCommands_Swift_Fpo_Chamfer: int = 2754
swCommands_Swift_Fpo_Boss: int = 2755
swCommands_View_Showhide_Tb: int = 2756
swCommands_Debug_Enable_Netfeat_Centerline: int = 2757
swCommands_Publish_Dl_Content: int = 2758
swCommands_Debug_Display_Tolerances: int = 2759
swCommands_Debug_Allow_Sketch_Constraint_Tolerance: int = 2760
swCommands_Quick_Reference_Guide: int = 2761
swCommands_Pw_Material_Whatsnew_Help_Id: int = 2762
swCommands_Pw_Options_Whatsnew_Help_Id: int = 2763
swCommands_Pw_Scene_Whatsnew_Help_Id: int = 2764
swCommands_Design_Checker_Learn_Checks_Whatsnew_Help_Id: int = 2765
swCommands_Shader_Enableshadergenerator: int = 2766
swCommands_See_What_Dcm_Sees: int = 2767
swCommands_Shader_Enable_Scene_Env: int = 2768
swCommands_Shader_Enable_True_Env: int = 2769
swCommands_Shader_Enable_Rotating_Env: int = 2770
swCommands_Debug_Acis_Kernel_Lofting: int = 2771
swCommands_Debug_Noregen_Atload: int = 2772
swCommands_Debug_Acis_Matched_Boolean: int = 2773
swCommands_Debug_Mp_For_Surface: int = 2774
swCommands_Debug_Acis_Sgnewspline_Periodic_Knots: int = 2775
swCommands_Debug_Acis_Procedural_Curves: int = 2776
swCommands_Debug_Acis_Timing_System: int = 2777
swCommands_Insert_2dsketch_On_Plane: int = 2778
swCommands_Shader_Enablerendermanager: int = 2779
swCommands_Swift_Create_Basic_Dim: int = 2780
swCommands_Debug_Vsta: int = 2781
swCommands_Debug_Vsta_Show_Ide: int = 2782
swCommands_Debug_Vsta_Load_Addins: int = 2783
swCommands_Dummy: int = 2784
swCommands_Dim_Stop_Break: int = 2785
swCommands_Update_Msg: int = 2786
swCommands_Heal_Faces_Ok: int = 2787
swCommands_Keep_Constraints: int = 2788
swCommands_FileClose: int = 2789
swCommands_ToolsGrid: int = 2791
swCommands_TrimCornerCorner: int = 2792
swCommands_RectangleAtAngle: int = 2793
swCommands_CentreRectangle: int = 2794
swCommands_CentreRectangleAtAngle: int = 2795
swCommands_WeldBead: int = 2796
swCommands_Shader_Enable_Material_Editor_Realview_Shader_Page: int = 2797
swCommands_Anim_Edit_Dim: int = 2798
swCommands_Scene: int = 2799
swCommands_ICE: int = 2800
swCommands_SwiftAddTaStudy: int = 2801
swCommands_List_Comp_References: int = 2802
swCommands_List_Body_References: int = 2803
swCommands_List_Feat_References: int = 2804
swCommands_List_Face_References: int = 2805
swCommands_List_Edge_References: int = 2806
swCommands_List_Vert_References: int = 2807
swCommands_Select_Display_State: int = 2808
swCommands_Toolbar_Display_States: int = 2809
swCommands_Show_Hidden_comps: int = 2810
swCommands_Sw_Animatorpane: int = 2811
swCommands_Toolbar_ScreenCapture: int = 2812
swCommands_ScreenCaptureToolbar: int = 2813
swCommands_ScreenCaptureAvi_Begin: int = 2814
swCommands_ScreenCaptureAvi_End: int = 2815
swCommands_Toolbar_Layout_Tools: int = 2816
swCommands_Layout: int = 2817
swCommands_Edit_Layout: int = 2818
swCommands_Repeat_Mate: int = 2819
swCommands_Edit_3DCC_Model: int = 2820
swCommands_Edit_RV_Appearance: int = 2821
swCommands_HoleAlignment: int = 2822
swCommands_Add_Part_Block: int = 2823
swCommands_Select_SubAssembly_In_GraphicsView: int = 2824
swCommands_App_Exit: int = 2825
swCommands_Insert_Cosmetic_Pattern: int = 2826
swCommands_Animation_Duplicate: int = 2827
swCommands_SimElementOn: int = 2828
swCommands_SimElementOff: int = 2829
swCommands_SimElementSuppress: int = 2830
swCommands_SimElementUnsuppress: int = 2831
swCommands_DriveWorkXxpress: int = 2832
swCommands_DFMXpress: int = 2833
swCommands_COSMOSFloXpress: int = 2834
swCommands_RapidSketch: int = 2835
swCommands_PlasticsFolder: int = 2836
swCommands_DraftNsplit: int = 2837
swCommands_Pin_Orientation_Dialog: int = 2838
swCommands_Dim_Jog: int = 2839
swCommands_Rmb_Display_Camera_FOV_Box: int = 2840
swCommands_Fmt_Painter: int = 2841
swCommands_PlasticsRegion: int = 2842
swCommands_InsertLiveSection: int = 2843
swCommands_LiveSectionFitToPart: int = 2844
swCommands_LiveSectionReset: int = 2845
swCommands_LiveSectionTriadShow: int = 2846
swCommands_LiveSectionTriadHide: int = 2847
swCommands_ClearanceVerification: int = 2848
swCommands_MarkConvertedDocumentsDirty: int = 2849
swCommands_HandSketch: int = 2850
swCommands_StretchEntities: int = 2851
swCommands_TitleBlockDefine: int = 2852
swCommands_TitleBlockEdit: int = 2853
swCommands_TitleBlockEnterData: int = 2854
swCommands_Dotmenu_FacetContainer_Replace_Test: int = 2855
swCommands_Fmt_Painter_Apply_All: int = 2856
swCommands_FilterSketches: int = 2857
swCommands_End_Adhoc_Rt: int = 2858
swCommands_End_Pipe_Rt_Adhoc: int = 2859
swCommands_End_Flex_Tube_Rt_Adhoc: int = 2860
swCommands_Reimport_From_To_Lst: int = 2861
swCommands_Insert_Connector: int = 2862
swCommands_Dump_Signature: int = 2863
swCommands_SketchSlot_Line: int = 2864
swCommands_SketchSlot_Line_Center: int = 2865
swCommands_SketchSlot_Arc3P: int = 2866
swCommands_SketchSlot_Arc_Center: int = 2867
swCommands_Unload_Hidden_Comps: int = 2868
swCommands_ViewLiveSections: int = 2875
swCommands_Debug_Beam_Analysis: int = 2876
swCommands_PlasticsShelled: int = 2877
swCommands_PlasticsUnShelled: int = 2878
swCommands_PlasticsOpenShelled: int = 2879
swCommands_Rotate_45_Degrees: int = 2880
swCommands_InsertSketchEQCurve: int = 2881
swCommands_SolidToSheetMetal: int = 2882
swCommands_VisualizationTool: int = 2883
swCommands_Create_Sub_LiveSectionFolder: int = 2884
swCommands_AnalysistoolsDraftAnalysis: int = 2885
swCommands_AnalysistoolsUndercutAnalysis: int = 2886
swCommands_AnalysistoolsPartingLineAnalysis: int = 2887
swCommands_LayoutDefault: int = 2888
swCommands_LayoutWidescreen: int = 2889
swCommands_LayoutDualMonitor: int = 2890
swCommands_LayoutCustom: int = 2891
swCommands_ToolsSensor: int = 2892
swCommands_CircuitWorks: int = 2893
swCommands_OfficeButtonTolAnalyst: int = 2894
swCommands_Whats_New_Highlights: int = 2895
swCommands_Body_RV_Appearance: int = 2896
swCommands_Feature_RV_Appearance: int = 2897
swCommands_Component_RV_Appearance: int = 2898
swCommands_Part_RV_Appearance: int = 2899
swCommands_Gantt_Zoomtofit: int = 2916
swCommands_Animkey_EditTime: int = 2917
swCommands_Animation_MoveCurTime: int = 2918
swCommands_AnimEditTime_Dlg_Ok: int = 2919
swCommands_AnimEditTime_Dlg_Cancel: int = 2920
swCommands_AnimEditTime_Dlg_SetTime: int = 2921
swCommands_AnimEditTime_Dlg_SetOffset: int = 2922
swCommands_AnimEditTime_Dlg_Increment: int = 2923
swCommands_Sm_Toggle_Flat_Display: int = 2924
swCommands_ViewDecals: int = 2925
swCommands_ChangeDisplayState: int = 2926
swCommands_RigidGroups: int = 2927
swCommands_InsertFeatureNudge: int = 2928
swCommands_Animation_CancelSolver: int = 2929
swCommands_Animation_SolverStatus: int = 2930
swCommands_Publish_To_Edrawing: int = 2931
swCommands_AnimMateSuppress: int = 2932
swCommands_AnimMateUnsuppress: int = 2933
swCommands_Remove_Feature_Appearance: int = 2934
swCommands_Remove_Body_Appearance: int = 2935
swCommands_Remove_Component_Appearance: int = 2936
swCommands_Remove_Part_Appearance: int = 2937
swCommands_HideShowEdges: int = 2938
swCommands_Swift_Fpo_DimType_Linear: int = 2939
swCommands_Swift_Fpo_DimType_Angular: int = 2940
swCommands_Show_Graphics_Stats: int = 2941
swCommands_Show_Graphics_Framecount: int = 2942
swCommands_Debug_Draw_Sketch_Graphics_Hardware: int = 2943
swCommands_Sm_Show_Problem_Areas: int = 2944
swCommands_Sm_Clear_Problem_Areas: int = 2945
swCommands_LayoutPresentation: int = 2946
swCommands_Dotmenu_Render_In_PhotoView360: int = 2947
swCommands_Iso_draw_pipe_rt: int = 2948
swCommands_TitleBlockTable: int = 2949
swCommands_Whats_New_Pdf: int = 2950
swCommands_Whats_New_Html: int = 2951
swCommands_SageExpress: int = 2952
swCommands_Design_Study: int = 2953
swCommands_ViewDimNames: int = 2954
swCommands_DesignStudy_Add_Parameters: int = 2955
swCommands_Asm_Feat_Fillet: int = 2956
swCommands_Asm_Feat_Chamfer: int = 2957
swCommands_Asm_Feat_Cut_Sweep: int = 2958
swCommands_Insert_Feature_Lock: int = 2959
swCommands_Insert_Walkthrough: int = 2960
swCommands_Exit_Measure: int = 2961
swCommands_RenderToolbar: int = 2962
swCommands_Toolbar_Render: int = 2963
swCommands_Renumber_Hole_Table: int = 2964
swCommands_Renumber_Series_Table: int = 2965
swCommands_Invoke_PhotoviewRender: int = 2966
swCommands_Edit_Scene: int = 2967
swCommands_Render_Options: int = 2968
swCommands_Final_Render: int = 2969
swCommands_Schedule_Render: int = 2970
swCommands_Recall_Last_Render: int = 2971
swCommands_Debug_Dump_Virtual_Comps: int = 2972
swCommands_DimensionSpaceEvenly: int = 2973
swCommands_DimensionAlignCollinear: int = 2974
swCommands_DimensionStagger: int = 2975
swCommands_AutoArrangeDimension: int = 2976
swCommands_DimensionTextAlignTop: int = 2977
swCommands_DimensionTextAlignBottom: int = 2978
swCommands_DimensionTextAlignLeft: int = 2979
swCommands_DimensionTextAlignRight: int = 2980
swCommands_Weld_Gap: int = 2981
swCommands_GridFeature: int = 2982
swCommands_ShowGuidelines: int = 2983
swCommands_Simple_Route: int = 2984
swCommands_Toolbar_Simple_Routing: int = 2985
swCommands_Glassbox_Exit: int = 2986
swCommands_Glassbox_Save: int = 2987
swCommands_Glassbox_ViewOrient: int = 2988
swCommands_Review_Pending_Updates: int = 2989
swCommands_ViewPlaneSections: int = 2990
swCommands_CosmeticWeld: int = 2991
swCommands_ViewSimulationSymbol: int = 2992
swCommands_NoteLPat: int = 2993
swCommands_NoteCPat: int = 2994
swCommands_Display_Simplified_Cosmetic_Weld_Curves: int = 2995
swCommands_Display_Simplified_Cosmetic_Weld_Geometries: int = 2996
swCommands_On_Show_Cosmetic_Welds: int = 2997
swCommands_On_Hide_Cosmetic_Welds: int = 2998
swCommands_Grid_View: int = 2999
swCommands_Blank_Grid_Comp: int = 3000
swCommands_Unblank_Grid_Comp: int = 3001
swCommands_WeldTable: int = 3002
swCommands_Add_Constraint_Planar_Offset: int = 3003
swCommands_ViewCosmeticWeldSymbol: int = 3004
swCommands_Invoke_Integrated_PhotoviewRender: int = 3005
swCommands_SheetmetalCosting: int = 3006
swCommands_MagnetLine: int = 3007
swCommands_Open_Part: int = 3008
swCommands_Open_Assembly: int = 3009
swCommands_BendTable: int = 3010
swCommands_Open_Sub_Assembly: int = 3011
swCommands_Tube_Properties: int = 3012
swCommands_Spool_Command: int = 3013
swCommands_Unfreeze_All: int = 3014
swCommands_Freeze_All: int = 3015
swCommands_SearchHelp: int = 3016
swCommands_SearchKB: int = 3017
swCommands_SearchComunityForum: int = 3018
swCommands_SearchCommands: int = 3019
swCommands_SearchFilesAndModels: int = 3020
swCommands_Show_Hidden_comps_Undo: int = 3021
swCommands_Show_Hidden_comps_Exit: int = 3022
swCommands_Isolate_Changed_Dims: int = 3023
swCommands_ReplaceFormTool: int = 3024
swCommands_Dimension_Driven_Toggle: int = 3025
swCommands_Auto_Dimension_Toggle: int = 3026
swCommands_Edit_Select_All: int = 3027
swCommands_Machined_Parts_Costing: int = 3028
swCommands_Numeric_Input_Toggle: int = 3029
swCommands_Ambient_Occlusion: int = 3030
swCommands_Select_Snapshot: int = 3031
swCommands_Set_QuickView_Transparency: int = 3032
swCommands_Selective_Open: int = 3033
swCommands_Resolve_Top: int = 3034
swCommands_Resolve_Top_LightWeight: int = 3035
swCommands_PunchTable: int = 3036
swCommands_RemoveAllDisplayStates: int = 3037
swCommands_Selective_Open_LightWeight: int = 3038
swCommands_Open_LightWeight: int = 3039
swCommands_Manage_Equations: int = 3040
swCommands_SweptFlange: int = 3041
swCommands_Ok_Command: int = 3042
swCommands_Cancel_Command: int = 3043
swCommands_Spool_Tube_Command: int = 3044
swCommands_SendTo: int = 3045
swCommands_NextCmdMgrTab: int = 3046
swCommands_PrevCmdMgrTab: int = 3047
swCommands_Insert_Baseline_Dimension: int = 3048
swCommands_Conic: int = 3049
swCommands_Defeature: int = 3050
swCommands_Insert_Sculpt: int = 3051
swCommands_RevisionCloud: int = 3052
swCommands_Copy_Appearance: int = 3053
swCommands_Paste_Appearance: int = 3054
swCommands_SaveWithPreBuiltConfigs: int = 3055
swCommands_ChangeLayer: int = 3056
swCommands_InsertCenterOfMass: int = 3057
swCommands_PartReviewer: int = 3058
swCommands_OnViewCenterOfMassSymbol: int = 3059
swCommands_RebuildAndSaveConfig: int = 3060
swCommands_RebuildAndSaveConfigOff: int = 3061
swCommands_RebuildAndSaveConfigActive: int = 3062
swCommands_RebuildAndSaveConfigAll: int = 3063
swCommands_RebuildAndSaveConfigSpecific: int = 3064
swCommands_Measure_PtoP: int = 3065
swCommands_Measure_History: int = 3066
swCommands_Dist_Custom: int = 3067
swCommands_AngularOrdinateDimension: int = 3068
swCommands_InsertCenterOfMassRefPoint: int = 3069
swCommands_UpdateAllSpeedpakConfig: int = 3070
swCommands_View_Rotate_About_Vertical: int = 3071
swCommands_RMB_Blind_Direction_2: int = 3072
swCommands_RMB_UptoVertex_Direction_2: int = 3073
swCommands_RMB_UptoSurface_Direction_2: int = 3074
swCommands_RMB_OffsetFromSurface_Direction_2: int = 3075
swCommands_RMB_Throughall_Direction_2: int = 3076
swCommands_RMB_ThroughNext_Direction_2: int = 3077
swCommands_RMB_UptoBody_Direction_2: int = 3078
swCommands_RMB_Direction_2_OnOff: int = 3079
swCommands_RMB_Reverse_Direction: int = 3080
swCommands_View_Orientation_ViewBox: int = 3081
swCommands_Edit_Ang_Ordinate: int = 3082
swCommands_Re_Jog: int = 3083
swCommands_Set_Current_View_As_Front: int = 3084
swCommands_Set_Current_View_As_Back: int = 3085
swCommands_Set_Current_View_As_Top: int = 3086
swCommands_Set_Current_View_As_Bottom: int = 3087
swCommands_Set_Current_View_As_Right: int = 3088
swCommands_Set_Current_View_As_Left: int = 3089
swCommands_LDR_Update_Model_Graphics: int = 3090
swCommands_RemoveMarkAndPurgeDataForAllConfig: int = 3091
swCommands_Dve_ThroughAll_Both: int = 3092
swCommands_Insert_Light_Sunlight: int = 3093
swCommands_Change_DrView_Reference: int = 3094
swCommands_SolveAsFlexibleOrRigid: int = 3095
swCommands_PathLengthDimension: int = 3096
swCommands_Edit_Path_Length_Dim: int = 3097
swCommands_LoopDve: int = 3098
swCommands_CVSpline: int = 3099
swCommands_InsertCV: int = 3100
swCommands_DimensionPattern: int = 3101
swCommands_SketchCreatePathLength: int = 3102
swCommands_Add_Slope: int = 3103
swCommands_ReplaceEntity: int = 3104
swCommands_Toggle_Notes_UpperCase: int = 3105
swCommands_Set_Dim_Extension_Centerline: int = 3106
swCommands_Reset_Dim_Extension_Centerline: int = 3107
swCommands_Component_Pattern_Sketch: int = 3108
swCommands_Component_Pattern_Curve: int = 3109
swCommands_Rmb_Find_Intersection: int = 3110
swCommands_SMGusset: int = 3111
swCommands_Corner_Relief: int = 3112
swCommands_RefPlane_Flip_Normal: int = 3113
swCommands_Restore_Settings: int = 3114
swCommands_Render_Region: int = 3115
swCommands_SelectConfigurations: int = 3116
swCommands_ConfigurationsToolbar: int = 3117
swCommands_Midpointline: int = 3118
swCommands_ViewCompAnnotations: int = 3119
swCommands_ViewAssemAnnotations: int = 3120
swCommands_ZoomtoSheet: int = 3121
swCommands_AutomaticUpdateCutlists: int = 3122
swCommands_ConvertToStyle: int = 3123
swCommands_ConvertToModif: int = 3124
swCommands_Toggle_Magnified_Selection: int = 3125
swCommands_Component_Pattern_Chain: int = 3126
swCommands_On_Hold_Cosmetic_Welds_Rebuild: int = 3127
swCommands_On_Rebuild_Cosmetic_Welds: int = 3128
swCommands_Segment: int = 3129
swCommands_CurvatureHedgehog: int = 3130
swCommands_Add_to_CMarkSet: int = 3131
swCommands_Rotate_Xaxis_By90: int = 3132
swCommands_Rotate_Yaxis_By90: int = 3133
swCommands_Rotate_Zaxis_By90: int = 3134
swCommands_Select_Annotation_View: int = 3135
swCommands_Rename_Annotation_View: int = 3136
swCommands_Reattach_to_CMarkSet: int = 3137
swCommands_Reference_arrow: int = 3138
swCommands_Surface_Flatten: int = 3139
swCommands_MBD: int = 3140
swCommands_Capture_3dView: int = 3141
swCommands_MBD_Template_Editor: int = 3142
swCommands_Electrical_EditConnector: int = 3143
swCommands_Zone_Editor: int = 3144
swCommands_Dynamic_Annotation_Views: int = 3145
swCommands_OfficeButtonFlowSimulation: int = 3146
swCommands_OfficeButtonPlastics: int = 3147
swCommands_OfficeButtonInspection: int = 3148
swCommands_Fixed_Length_Route: int = 3149
swCommands_Show_Hide_Fixed_Length_Route_Manipulators: int = 3150
swCommand_ReferenceArrow_PopUp: int = 3151
swCommand_ChildReferenceArrow: int = 3152
swCommands_Add_Constraint_SameCurvelen: int = 3153
swCommands_UnUsed: int = 3154
swCommand_Sheet_Format: int = 3155
swCommand_Border_Editor: int = 3156
swCommands_PhotoView_ProofSheet: int = 3157
swCommand_Delete_Selected_BE: int = 3158
swCommand_Restore_Selected_BE: int = 3159
swCommand_Deselect_All_Selected_BE: int = 3160
swCommands_Sort_Stacked_Balloons: int = 3161
swCommand_TemporaryFixGroup: int = 3162
swCommands_Create_Userdefined_Rt_By_Drag_Drop: int = 3163
swCommands_Create_Userdefined_Rt_On_Fly: int = 3164
swCommands_Userdefined_Add_Fitting: int = 3165
swCommands_Userdefined_Rt_On_Fly: int = 3166
swCommands_Edit_Userdefined_Start_At_Point: int = 3167
swCommands_Userdefined_Rt_Properties: int = 3168
swCommand_Hide_Show_Primary_Planes: int = 3169
swCommand_Cartoon_Shading: int = 3170
swCommand_Component_Preview_Window: int = 3171
swCommands_AdvancedHoleWizard: int = 3172
swCommands_InsertBoundingBox: int = 3173
swCommands_SearchMySolidworks: int = 3174
swCommands_SearchBlogs: int = 3175
swCommands_SearchCadModels: int = 3176
swCommands_SearchTraining: int = 3177
swCommands_SearchTwitter: int = 3178
swCommands_SearchYoutube: int = 3179
swCommands_SearchManufacturers: int = 3180
swCommands_InsertThreadWiz: int = 3181
swCommands_SwiftInsertBasicDimension: int = 3182
swCommands_AddFlagNoteToStack: int = 3183
swCommands_ViewDatumReferenceFrame: int = 3184
swCommands_MBD_Load_Unload: int = 3185
swCommands_Pick_Identicalcomponents: int = 3186
swCommands_Exit_Component_Preview: int = 3187
swCommands_ToggleInstant2D: int = 3188
swCommands_ShadedSketchContours: int = 3189
swCommands_OffsetOnSurface: int = 3190
swCommands_3dPrintValidation: int = 3191
swCommands_Rmb_Cpat_Symmetric: int = 3192
swCommands_User_Defined_Route: int = 3193
swCommands_Routing_Reuse_Route: int = 3194
swCommands_Display_States_Target: int = 3195
swCommands_SMNormalCut: int = 3196
swCommands_SwiftInsertBasicSizeDimension: int = 3197
swCommands_PublishSTEP242File: int = 3198
swCommands_Show_Config_Or_DisplayState_Name: int = 3199
swCommands_RebuildAll: int = 3200
swCommands_ViewSimResults: int = 3201
swCommands_Rmb_Edit_SimResults: int = 3202
swCommands_Show_LDR_Configuration: int = 3203
swCommands_Mark_LDR_Config: int = 3204
swCommands_Mark_LDR_ConfigOff: int = 3205
swCommands_Mark_LDR_ConfigActive: int = 3206
swCommands_Mark_LDR_ConfigAll: int = 3207
swCommands_Mark_LDR_ConfigSpecific: int = 3208
swCommands_Remove_Mark_LDR_AndPurgeDataForAllConfig: int = 3209
swCommands_Show_Mesh_Feat: int = 3210
swCommands_Hide_Mesh_Feat: int = 3211
swCommands_3dpmi: int = 3212
swCommands_Rmb_Cpat_Equal_Spacing1: int = 3213
swCommands_Rmb_Cpat_Equal_Spacing2: int = 3214
swCommands_Asset_Publish: int = 3215
swCommands_Toggle_MagMate: int = 3216
swCommands_Ground_Plane: int = 3217
swCommands_SurfFromMesh: int = 3218
swCommands_changeSubDTransparency: int = 3219
swCommands_toggleSubDCage: int = 3220
swCommands_toggleSelectedVisibleSubdElements: int = 3221
swCommands_filterAnySubDEntities: int = 3222
swCommands_filterSubdVerts: int = 3223
swCommands_filterSubdEdges: int = 3224
swCommands_filterSubdFaces: int = 3225
swCommands_filterSubdEdgeRings: int = 3226
swCommands_filterSubdEdgeLoops: int = 3227
swCommands_filterSubdFaceLoops: int = 3228
swCommands_Start_Screen: int = 3229
swCommands_FilterMeshFacet: int = 3230
swCommands_FilterMeshFin: int = 3231
swCommands_FilterMeshVertex: int = 3232
swCommands_GeneralToleranceTable: int = 3233
swCommands_TabAndSlot: int = 3234
swCommands_HandsketchPen: int = 3235
swCommands_HandsketchEraser: int = 3236
swCommands_HandsketchSelect: int = 3237
swCommands_HandsketchColor: int = 3238
swCommands_HandsketchThickness: int = 3239
swCommands_HandsketchConvertShape: int = 3240
swCommands_HandsketchConvertEntity: int = 3241
swCommands_Toolbar_Handsketch: int = 3242
swCommands_InsertHandSketch: int = 3243
swCommands_InsertAutoDim: int = 3244
swCommands_ConvertMeshSolidSurface: int = 3245
swCommands_ToggleGraphicsDisplay: int = 3246
swCommands_AlignRobotToSelection: int = 3247
swCommands_AlignRobotToUCS: int = 3248
swCommands_AlignRobotToScreen: int = 3249
swCommands_Publish_3DByMe: int = 3250
swCommands_InsertSubdQuadBall: int = 3251
swCommands_PreInsertSubdQuadBall: int = 3252
swCommands_InsertSubdBox: int = 3253
swCommands_PreInsertSubdBox: int = 3254
swCommands_InsertSubdCylinder: int = 3255
swCommands_PreInsertSubdCylinder: int = 3256
swCommands_InsertSubdGlobe: int = 3257
swCommands_PreInsertSubdGlobe: int = 3258
swCommands_InsertSubdTorus: int = 3259
swCommands_PreInsertSubdTorus: int = 3260
swCommands_InsertSubdCone: int = 3261
swCommands_PreInsertSubdCone: int = 3262
swCommands_InsertSubdRectangle: int = 3263
swCommands_PreInsertSubdRectangle: int = 3264
swCommands_InsertSubdDisk: int = 3265
swCommands_PreInsertSubdDisk: int = 3266
swCommands_InsertSubdRing: int = 3267
swCommands_PreInsertSubdRing: int = 3268
swCommands_InsertSubdMerge: int = 3269
swCommands_PreInsertSubdMerge: int = 3270
swCommands_InsertSubdSymmetry: int = 3271
swCommands_PreInsertSubdSymmetry: int = 3272
swCommands_InsertSubdExtrudeFace: int = 3273
swCommands_PreInsertSubdExtrudeFace: int = 3274
swCommands_InsertSubdSubDDivideFace: int = 3275
swCommands_PreInsertSubdSubDDivideFace: int = 3276
swCommands_InsertSubdSubDCrease: int = 3277
swCommands_PreInsertSubdSubDCrease: int = 3278
swCommands_InsertSubdInsertLoop: int = 3279
swCommands_PreInsertSubdInsertLoop: int = 3280
swCommands_InsertSubdDeleteLoop: int = 3281
swCommands_PreInsertSubdDeleteLoop: int = 3282
swCommands_InsertSubdSubDAlign: int = 3283
swCommands_PreInsertSubdSubDAlign: int = 3284
swCommands_InsertSubdSubDScale: int = 3285
swCommands_PreInsertSubdSubDScale: int = 3286
swCommands_Toolbar_Freeform: int = 3287
swCommands_3dExperienceDesignEngineer: int = 3288
swCommands_Toolbar_OneClick: int = 3289
swCommands_HandsketchTouch: int = 3290
swCommands_HandsketchRuler: int = 3291
swCommands_Subd_CreateBridgeHole: int = 3292
swCommands_Subd_MergeFacesSubdivide: int = 3293
swCommands_Subd_BtnReverseDir: int = 3294
swCommands_HandsketchPenProps: int = 3295
swCommands_AutoExplodeLine: int = 3296
swCommands_InsertSubdSubDQuickCrease: int = 3298
swCommands_InsertSubdSubDQuickInsertLoop: int = 3299
swCommands_InsertSubdSubDQuickAlign: int = 3300
swCommands_InsertSubdSubDQuickExtrudeFace: int = 3301
swCommands_InsertSubdSubDQuickSubdivide: int = 3302
swCommands_Import_Swift_Schema: int = 3303
swCommands_Reverse_Endpoint_Tangency: int = 3304
swCommands_Mating_Component: int = 3305
swCommands_DissolveEntities: int = 3306
swCommands_DissolveAutoExplodeLine: int = 3307
swCommands_HandsketchUpdateToShape: int = 3308
swCommands_HandsketchUpdateToEntity: int = 3309
swCommands_SelectOverGeometry: int = 3310
swCommands__Force_Rebuild_All: int = 3311
swCommands_InsertSubdFillHole: int = 3312
swCommands_InvertSubDSelection: int = 3313
swCommands_ClearSubDSelection: int = 3314
swCommands_EditSubDMerge: int = 3315
swCommands_InsertSubdSubDQuickDelete: int = 3316
swCommands_XRayToggleAssem: int = 3317
swCommands_XRayTogglePart: int = 3318
swCommands_RMBFreeshapeOK: int = 3319
swCommands_RMBFreeshapeCancel: int = 3320
swCommands_MixModel_Resolve: int = 3321
swCommands_MixModel_LightWeight: int = 3322
swCommands_ViewGlobalBBox: int = 3323
swCommands_SubdConvertMesh: int = 3324
swCommands_SwiftInsertGeneralProfileTolerance: int = 3325
swCommands_ForceMateMisalignment: int = 3326
swCommands_RemoveMateMisalignment: int = 3327
swCommands_InsertSubdExtrude: int = 3328
swCommands_InsertSubdRevolve: int = 3329
swCommands_InsertSubdSweep: int = 3330
swCommands_Make_Trim_As_Construction: int = 3331
swCommands_Ignore_Construction_Geom: int = 3332
swCommands_3dTexturizeSolidSurface: int = 3333
swCommands_Toolbar_Adv_Struct_System: int = 3334
swCommands_AdvancedStructuralMember: int = 3335
swCommands_PrimaryAdvStructMember: int = 3336
swCommands_SecondaryAdvStructMember: int = 3337
swCommands_CornerMgmtAdvStructMember: int = 3338
swCommands_Explode_Roll_Back: int = 3339
swCommands_Explode_Roll_Forward: int = 3340
swCommands_Explode_Roll_To_Previous: int = 3341
swCommands_Explode_Roll_To_End: int = 3342
swCommands_UpdateImportedModel: int = 3343
swCommands_HandsketchReplaceSpline: int = 3344
swCommands_HandsketchReplaceComposite: int = 3345
swCommands_HandsketchReplaceSlot: int = 3346
swCommands_HandsketchReplaceEllipse: int = 3347
swCommands_Explode_Suppress: int = 3348
swCommands_Explode_Unsuppress: int = 3349
swCommands_PostInsertSubdExtrude: int = 3350
swCommands_PostInsertSubdRevolve: int = 3351
swCommands_RemovedSection: int = 3352
swCommands_Iso_Draw_Electrical_Rt: int = 3353
swCommands_InsertFreeShapeConvertMesh: int = 3354
swCommands_PostInsertSubdSweep: int = 3355
swCommands_SolidWorks_backoffice: int = 3356
swCommands_SegmentImportedMeshBody: int = 3357
swCommands_Enable_RenderSystem_Profiling: int = 3358
swCommands_Capture_RenderSystem_ProfilingData: int = 3359
swCommands_DeleteHoleSurface: int = 3360
swCommands_Dotmenu_Test_Graphics_Performance: int = 3361
swCommands_TrimAsGroupWithPreAdvStructMember: int = 3362
swCommands_TrimAsIndAdvStructMember: int = 3363
swCommands_ConvertToGeneric: int = 3364
swCommands_MostRecentlyUsed_File1: int = 3365
swCommands_MostRecentlyUsed_File2: int = 3366
swCommands_MostRecentlyUsed_File3: int = 3367
swCommands_MostRecentlyUsed_File4: int = 3368
swCommands_MostRecentlyUsed_File5: int = 3369
swCommands_MostRecentlyUsed_File6: int = 3370
swCommands_MostRecentlyUsed_File7: int = 3371
swCommands_MostRecentlyUsed_File8: int = 3372
swCommands_MostRecentlyUsed_File9: int = 3373
swCommands_MostRecentlyUsed_File10: int = 3374
swCommands_MostRecentlyUsed_File11: int = 3375
swCommands_MostRecentlyUsed_File12: int = 3376
swCommands_MostRecentlyUsed_File13: int = 3377
swCommands_MostRecentlyUsed_File14: int = 3378
swCommands_MostRecentlyUsed_File15: int = 3379
swCommands_MostRecentlyUsed_File16: int = 3380
swCommands_HandsketchProtractor: int = 3381
swCommands_Fixed_Length_Covering: int = 3382
swCommands_Rmb_BiDir: int = 3383
swCommands_OfficeAddin3dExperienceMarketPlace: int = 3384
swCommands_Explode_Done_With_Step: int = 3385
swCommands_ProfileProperties: int = 3386
swCommands_HandsketchSplineMode: int = 3387
swCommands_AlternativeHandwrittenDim_0: int = 3388
swCommands_AlternativeHandwrittenDim_1: int = 3389
swCommands_AlternativeHandwrittenDim_2: int = 3390
swCommands_AlternativeHandwrittenDim_3: int = 3391
swCommands_AlternativeHandwrittenDim_4: int = 3392
swCommands_AlternativeHandwrittenDim_5: int = 3393
swCommands_AlternativeHandwrittenDim_6: int = 3394
swCommands_AlternativeHandwrittenDim_7: int = 3395
swCommands_AlternativeHandwrittenDim_8: int = 3396
swCommands_AlternativeHandwrittenDim_9: int = 3397
swCommands_InkMarkupView: int = 3398
swCommands_SketchSlicing: int = 3399
swCommands_3DPDF_ADD_ALL_3DVIEWS: int = 3401
swCommands_AssemblyAdd: int = 3402
swCommands_AssemblyAddRoute: int = 3403
swCommands_Exit_Structural_Member: int = 3404
swCommands_Insert_Chain_Dimension: int = 3405
swCommands_AddTo_Chain_Dimension: int = 3406
swCommands_ConvertTo_Chain_Dimension: int = 3407
swCommands_ConvertTo_Base_Dimension: int = 3408
swCommands_HandsketchModify: int = 3409
swCommands_StackFasteners: int = 3410
swCommands_BodyComparison: int = 3411
swCommands_Remove_From_ChainDim: int = 3412
swCommands_HandsketchEditModify: int = 3413
swCommands_SkSilhouetteEnts: int = 3414
swCommands_DefineStructConnection: int = 3415
swCommands_Envelope_Publisher: int = 3416
swCommands_Online_Familytable_Closed: int = 3417
swCommands_ActivateFlexiblePartComp: int = 3418
swCommands_Make_Edit_Sketch: int = 3419
swCommands_Make_Reference_Sketch: int = 3420
swCommands_EditFlexiblePartComp: int = 3421
swCommands_ViewCompEnvelopes: int = 3422
swCommands_ViewAssemEnvelopes: int = 3423
swCommands_Add_OverallDim_To_ChainDim: int = 3424
swCommands_Add_Constraint_G3Touch: int = 3425
swCommands_HandsketchReplaceChamfer: int = 3426
swCommands_HandsketchReplaceFillet: int = 3427
swCommands_HandsketchReplaceExtend: int = 3428
swCommands_DecimateMesh: int = 3429
swCommands_Flexible_Part_Remove_Ref: int = 3430
swCommands_CutListSortingOptions: int = 3431
swCommands_SWPremium: int = 3432
swCommands_SimulationStd: int = 3433
swCommands_SimulationPro: int = 3434
swCommands_SimulationPremium: int = 3435
swCommands_LockViewPlane: int = 3436
swCommands_Toolbar_Inkmarkup: int = 3437
swCommands_InkMarkupPenProps: int = 3438
swCommands_InkMarkupPen: int = 3439
swCommands_InkMarkupMouse: int = 3440
swCommands_InkMarkupEraser: int = 3441
swCommands_InkMarkupSelect: int = 3442
swCommands_InkMarkupTouch: int = 3443
swCommands_InkMarkupText: int = 3444
swCommands_InsertStructConnection: int = 3445
swCommands_GetSupport: int = 3446
swCommands_Resolve_Drawing: int = 3447
swCommands_YUpViewOrientation: int = 3448
swCommands_ZUpViewOrientation: int = 3449
swCommands_SwiftInsertDatumTarget: int = 3450
swCommands_Publish3DPDF: int = 3451
swCommands_InsertNewFamilyMember: int = 3452
swCommands_InsertNewRepresentation: int = 3453
swCommands_InsertNewPrivateFamilyMember: int = 3454
swCommands_HandsketchDraw: int = 3455
swCommands_SaveWithOptions: int = 3456
swCommands_SaveLocally: int = 3457
swCommands_Show_ComponentInstance_Name: int = 3458
swCommands_Show_ComponentReference_Name: int = 3459
swCommands_Show_Representation_Name: int = 3460
swCommands_Show_CADFamily_Name: int = 3461
swCommands_Show_Revision_And_Maturity: int = 3462
swCommands_User_Communities: int = 3463
swCommands_Save_Virtual_Comp: int = 3464
swCommands_Sw_Educator_Resources: int = 3465
swCommands_InsertAbbrView: int = 3466
swCommands_SwiftInsertAngleDimension: int = 3467
swCommands_ViewBendLines: int = 3468
swCommands_SmoothMesh: int = 3469
swCommands_Dim_RadialDiametric_Toggle: int = 3470
swCommands_Skey_SearchBox: int = 3471
swCommands_PLM_Reserve: int = 3472
swCommands_PLM_Unreserve: int = 3473
swCommands_PLM_Reload_fromServer: int = 3474
swCommands_PLM_Replace_By_Revision: int = 3475
swCommands_PLM_Maturity: int = 3476
swCommands_PLM_New_Revision: int = 3477
swCommands_PLM_Move_to: int = 3478
swCommands_PLM_Properties: int = 3479
swCommands_PLM_Relations: int = 3480
swCommands_PLM_Replace_Content: int = 3481
swCommands_PLM_Set_Ent_Item_Number: int = 3482
swCommands_PLM_Gen_Derived_Output_Number: int = 3483
swCommands_Toolbar_Lifecycle_And_Collaboration: int = 3484
swCommands_Disp_Dim_As_Radius: int = 3485
swCommands_Disp_Dim_As_Diameter: int = 3486
swCommands_Disp_Dim_As_Linear: int = 3487
swCommands_On_Screen_Dim_Dialog: int = 3488
swCommands_InsertStudWiz: int = 3489
swCommands_InsertSymmDiaDim: int = 3490
swCommands_PlasticsStd: int = 3491
swCommands_PlasticsPro: int = 3492
swCommands_PlasticsPremium: int = 3493
swCommands_MakeVirtualCompIndependent: int = 3494
swCommands_OpenFromPC: int = 3495
swCommands_Publish_HomeByMe: int = 3496
swCommands_Open_Detailing_Drw: int = 3497
swCommands_Insert_From_PartSupply: int = 3498
swCommands_On_Demand_Maufacturing: int = 3499
swCommands_SwConnected_Release_Notes: int = 3500
swCommands_Work_Offline: int = 3501
swCommands_Publish_3DSwym_Picture: int = 3502
swCommands_Publish_3DSwym_3D: int = 3503
swCommands_Force_Regen_Bucket: int = 3504
swCommands_Bom_Open_Draw_File: int = 3505
swCommands_Open_Partdrawg_For_Drawing: int = 3506
swCommands_FlowSimulation: int = 3507
swCommands_FlowSimulation_HVAC: int = 3508
swCommands_FlowSimulation_ElCooling: int = 3509
swCommands_FlowSimulation_HVAC_ElCooling: int = 3510
swCommands_PatternStructConnection: int = 3511
swCommands_AutoRepair_Mates: int = 3512
swCommands_LaunchFilePrep_Asst: int = 3513
swCommands_Add_To_Bookmark: int = 3514
swCommands_Open_Bookmark_Editor: int = 3515
swCommands_Share_A_File: int = 3516
swCommands_Propagate_Slots: int = 3517
swCommands_SMStamp: int = 3518
swCommands_Preview_Sketch_Dimension_Toggle: int = 3519
swCommands_AutoRepair_Pattern: int = 3520
swCommands_Reattach_Dim: int = 3521
swCommands_Dim_Restore_Original_Value: int = 3522
swCommands_PreviousVersionCheck: int = 3523
swCommands_Share: int = 3524
swCommands_Add_To_Recent_Bookmark: int = 3525
swCommands_Copy_Bookmark_Link: int = 3526
swCommands_SimulationDesigner: int = 3527
swCommands_Hide_3d_Sketch_Triad: int = 3528
swCommands_FlatPatternBendNotch: int = 3529
swCommands_GrooveWeld: int = 3530
swCommands_ConvertMeshBody2Classic: int = 3531
swCommands_SWUltimate: int = 3532
swCommands_CPQ_CreateVariabilityFeatures: int = 3533
swCommands_OpenCollaborativeTask: int = 3534
swCommands_Flip_Endpoint_Tangency: int = 3535
swCommands_AutoGenerateDrawing: int = 3536
swCommands_InsertFamilyTable_Drw: int = 3537
swCommands_View_ShowAnnotationTextExpression: int = 3538
swCommands_Dim_UpdateBreak: int = 3539
swCommands_Dim_AddBreak: int = 3540
swCommands_CmdPrediction_Search_Cmd: int = 3541
swCommands_SWVisualize: int = 3542
swCommands_Invoke_SWVisualize_Render_PM: int = 3543
swCommands_OpenIn_SWVisualize: int = 3544
swCommands_SWVisualize_GroupByAppearance: int = 3545
swCommands_SWVisualize_GroupByPart: int = 3546
swCommands_SWVisualize_ImportWithOptions: int = 3547
swCommands_CreateNewTask: int = 3548
swCommands_SwiftInsertOrdinateDimension: int = 3549
swCommands_Highlight: int = 3550
swCommands_AutoUpdateDrawing: int = 3551

# swCompatibilityDialogOptions_e (SwConst)
swCompatibilityDialogOptions_AlwaysShow: int = 0
swCompatibilityDialogOptions_ShowOnIncompatible: int = 1
swCompatibilityDialogOptions_NeverShow: int = 2

# swComponentCrossSectionType_e (SWRoutingLib)
swRectangularCrossSection: int = 1000
swCircularCrossSection: int = 1010
swNotHVAC: int = 1020

# swComponentIdentifier_e (SwConst)
swComponentIdentifier_None: int = 0
swComponentIdentifier_PhysicalProductTitle: int = 1
swComponentIdentifier_ComponentName: int = 2
swComponentIdentifier_ComponentDescription: int = 4
swComponentIdentifier_EnterpriseItemNumber: int = 8
swComponentIdentifier_PhysicalProductDescription: int = 16
swComponentIdentifier_ConfigurationName: int = 32
swComponentIdentifier_ConfigurationDescription: int = 64
swComponentIdentifier_DisplayStateName: int = 128
swComponentIdentifier_FileTitle: int = 256
swComponentIdentifier_PLMRevision: int = 512

# swComponentLoadStatus_e (SwConst)
swComponentLoadStatus_Unknown: int = 0
swComponentLoadStatus_Hidden: int = 1
swComponentLoadStatus_Suppressed: int = 2

# swComponentReloadError_e (SwConst)
swReloadOkay: int = 0
swWriteAccessError: int = 1
swFutureVersionError: int = 2
swModifiedNotReloadedError: int = 3
swInvalidOption: int = 4
swFileNotSavedError: int = 5
swInvalidComponentError: int = 6
swUnexpectedError: int = 7
swComponentLightWeightError: int = 8
swFileDoesntExistError: int = 9
swFileInvalidOrSameNameError: int = 10
swDocumentHasNoView: int = 11
swDocumentAlreadyOpenedError: int = 12
swDocumentEventError: int = 13
swDocumentNotChanged: int = 14
swReloadCancel: int = 15
swReadOnlyChanged: int = 16

# swComponentReloadOption_e (SwConst)
swAlwaysReload: int = 0
swDontReloadOldComponents: int = 1

# swComponentResolveStatus_e (SwConst)
swResolveOk: int = 0
swResolveAbortedByUser: int = 1
swResolveNotPerformed: int = 2
swResolveError: int = 3

# swComponentRouteType_e (SWRoutingLib)
swFabricatedPipe: int = 1
swTube: int = 2
swElectrical: int = 3
swMixedRouteType: int = 4
swUnknownType: int = 5
swUserDefinedType: int = 6

# swComponentSolvingOption_e (SwConst)
swComponentRigidSolving: int = 0
swComponentFlexibleSolving: int = 1

# swComponentSuppressionState_e (SwConst)
swComponentSuppressed: int = 0
swComponentLightweight: int = 1
swComponentFullyResolved: int = 2
swComponentResolved: int = 3
swComponentFullyLightweight: int = 4
swComponentInternalIdMismatch: int = 5

# swComponentVisibilityState_e (SwConst)
swComponentHidden: int = 0
swComponentVisible: int = 1
swComponentUnknown: int = -1

# swConcentricAlignmentType_e (SwConst)
swConcentricAlignConcentric: int = 0
swConcentricAlignThisMate: int = 1
swConcentricAlignLinkedMate: int = 2
swConcentricAlignSymmetric: int = 3

# swConcentricPositionType (SwConst)
swConcentricPositionType_Default: int = -1
swConcentricPositionType_Aligned: int = 0
swConcentricPositionType_Symmetric: int = 1

# swConfigTreeSortType_e (SwConst)
swSortType_History: int = 0
swSortType_Numeric: int = 1
swSortType_Literal: int = 2
swSortType_DesignTable: int = 3

# swConfigurationChangeTypes_e (SwConst)
swConfigurationChangeTypes_Undefined: int = -1
swConfigurationChangeTypes_DimensionValue: int = 0
swConfigurationChangeTypes_SuppressionState: int = 1
swConfigurationChangeTypes_AddChildConfiguration: int = 2
swConfigurationChangeTypes_RemoveChildConfiguration: int = 3
swConfigurationChangeTypes_ComponentVisibilityState: int = 4
swConfigurationChangeTypes_CustomProperty: int = 5
swConfigurationChangeTypes_AddDisplayState: int = 6
swConfigurationChangeTypes_RemoveDisplayState: int = 7
swConfigurationChangeTypes_RenameDisplayState: int = 8
swConfigurationChangeTypes_Feature: int = 9
swConfigurationChangeTypes_Unused1: int = 10
swConfigurationChangeTypes_Unused2: int = 11
swConfigurationChangeTypes_ConvertToRepresentation: int = 12
swConfigurationChangeTypes_ConvertToPhysicalProduct: int = 13
swConfigurationChangeTypes_ChangeRepresentationParent: int = 14

# swConfigurationOptions2_e (SwConst)
swConfigOption_UseAlternateName: int = 1
swConfigOption_DontShowPartsInBOM: int = 2
swConfigOption_SuppressByDefault: int = 4
swConfigOption_HideByDefault: int = 8
swConfigOption_MinFeatureManager: int = 16
swConfigOption_InheritProperties: int = 32
swConfigOption_LinkToParent: int = 64
swConfigOption_DontActivate: int = 128
swConfigOption_DoDisolveInBOM: int = 256
swConfigOption_UseDescriptionInBOM: int = 512

# swConfigurationOptions_e (SwConst)
swUseAlternateName: int = 1
swDontShowPartsInBOM: int = 2

# swConfigurationType_e (SwConst)
swConfiguration_Standard: int = 0
swConfiguration_AsMachined: int = 1
swConfiguration_AsWelded: int = 2
swConfiguration_SheetMetal: int = 3
swConfiguration_SpeedPak: int = 4
swConfiguration_Defeature: int = 5

# swConnectedSegmentsOption_e (SwConst)
swConnectedSegments_SimpleCut: int = 1
swConnectedSegments_CopedCut: int = 2

# swConnectedSyncSettingsErrors_e (SwConst)
swConnectedSyncSettings_Success: int = 0
swConnectedSyncSettings_ConnectedDisabled: int = 1
swConnectedSyncSettings_ConnectedNotLoggedIn: int = 2
swConnectedSyncSettings_UploadDownloadError: int = 3

# swConnectionPointType_e (SwConst)
swConnectionPoint_Tube: int = 1
swConnectionPoint_FabricatedPipe: int = 2
swConnectionPoint_Electrical: int = 3
swConnectionPoint_UserDefined: int = 4

# swConstrainedCornerAction_e (SwConst)
swConstrainedCornerInteract: int = 0
swConstrainedCornerKeepGeometry: int = 1
swConstrainedCornerDeleteGeometry: int = 2
swConstrainedCornerStopProcessing: int = 3

# swConstrainedStatus_e (SwConst)
swUnknownConstraint: int = 1
swUnderConstrained: int = 2
swFullyConstrained: int = 3
swOverConstrained: int = 4
swNoSolution: int = 5
swInvalidSolution: int = 6
swAutosolveOff: int = 7

# swConstraintType_e (SwConst)
swConstraintType_INVALIDCTYPE: int = 0
swConstraintType_DISTANCE: int = 1
swConstraintType_ANGLE: int = 2
swConstraintType_RADIUS: int = 3
swConstraintType_HORIZONTAL: int = 4
swConstraintType_VERTICAL: int = 5
swConstraintType_TANGENT: int = 6
swConstraintType_PARALLEL: int = 7
swConstraintType_PERPENDICULAR: int = 8
swConstraintType_COINCIDENT: int = 9
swConstraintType_CONCENTRIC: int = 10
swConstraintType_SYMMETRIC: int = 11
swConstraintType_ATMIDDLE: int = 12
swConstraintType_ATINTERSECT: int = 13
swConstraintType_SAMELENGTH: int = 14
swConstraintType_DIAMETER: int = 15
swConstraintType_OFFSETEDGE: int = 16
swConstraintType_FIXED: int = 17
swConstraintType_ARCANG90: int = 18
swConstraintType_ARCANG180: int = 19
swConstraintType_ARCANG270: int = 20
swConstraintType_ARCANGTOP: int = 21
swConstraintType_ARCANGBOTTOM: int = 22
swConstraintType_ARCANGLEFT: int = 23
swConstraintType_ARCANGRIGHT: int = 24
swConstraintType_HORIZPOINTS: int = 25
swConstraintType_VERTPOINTS: int = 26
swConstraintType_COLINEAR: int = 27
swConstraintType_CORADIAL: int = 28
swConstraintType_SNAPGRID: int = 29
swConstraintType_SNAPLENGTH: int = 30
swConstraintType_SNAPANGLE: int = 31
swConstraintType_USEEDGE: int = 32
swConstraintType_ELLIPSEANG90: int = 33
swConstraintType_ELLIPSEANG180: int = 34
swConstraintType_ELLIPSEANG270: int = 35
swConstraintType_ELLIPSEANGTOP: int = 36
swConstraintType_ELLIPSEANGBOTTOM: int = 37
swConstraintType_ELLIPSEANGLEFT: int = 38
swConstraintType_ELLIPSEANGRIGHT: int = 39
swConstraintType_ATPIERCE: int = 40
swConstraintType_DOUBLEDISTANCE: int = 41
swConstraintType_MERGEPOINTS: int = 42
swConstraintType_ANGLE3P: int = 43
swConstraintType_ARCLENGTH: int = 44
swConstraintType_NORMAL: int = 45
swConstraintType_NORMALPOINTS: int = 46
swConstraintType_SKETCHOFFSET: int = 47
swConstraintType_ALONGX: int = 48
swConstraintType_ALONGY: int = 49
swConstraintType_ALONGZ: int = 50
swConstraintType_ALONGXPOINTS: int = 51
swConstraintType_ALONGYPOINTS: int = 52
swConstraintType_ALONGZPOINTS: int = 53
swConstraintType_PARALLELYZ: int = 54
swConstraintType_PARALLELZX: int = 55
swConstraintType_INTERSECTION: int = 56
swConstraintType_PATTERNED: int = 57
swConstraintType_ISOBYPOINT: int = 58
swConstraintType_SAMEISOPARAM: int = 59
swConstraintType_FITSPLINE: int = 60
swConstraintType_EQUALCURVATURE: int = 61
swConstraintType_EQUALTANGENT: int = 62
swConstraintType_TANGENTFACE: int = 63
swConstraintType_ALONGX3D: int = 64
swConstraintType_ALONGY3D: int = 65
swConstraintType_ALONGXPOINTS3D: int = 66
swConstraintType_ALONGYPOINTS3D: int = 67
swConstraintType_TRACTION: int = 68
swConstraintType_BELTTRACTION: int = 69
swConstraintType_BLOCKFIXEDLOCK: int = 70
swConstraintType_BLOCKNORMALLOCK: int = 71
swConstraintType_BLOCKROTATELOCK: int = 72
swConstraintType_FAKESLOTCONSTRAINT: int = 73
swConstraintType_FIXEDSLOT: int = 74
swConstraintType_SAMESLOTS: int = 75
swConstraintType_LINEARPATTCNT: int = 76
swConstraintType_CIRCULARPATTCNT: int = 77
swConstraintType_RADIALOFFSET: int = 78
swConstraintType_PLANAROFFSET: int = 79
swConstraintType_EQUALCURV3DALIGN: int = 80
swConstraintType_FLANGEFACEDIST: int = 81
swConstraintType_CONICRHO: int = 82
swConstraintType_C3TOUCH: int = 83
swConstraintType_DOUBLEANGLE: int = 84
swConstraintType_SAMECURVELENGTH: int = 85

# swContactType_e (SwConst)
swContact: int = 0
swTangent: int = 1
swCurvature: int = 2

# swControlBitmapLabelType_e (SwConst)
swBitmapLabel_LinearDistance: int = 1
swBitmapLabel_AngularDistance: int = 2
swBitmapLabel_SelectEdgeFaceVertex: int = 3
swBitmapLabel_SelectFaceSurface: int = 4
swBitmapLabel_SelectVertex: int = 5
swBitmapLabel_SelectFace: int = 6
swBitmapLabel_SelectEdge: int = 7
swBitmapLabel_SelectFaceEdge: int = 8
swBitmapLabel_SelectComponent: int = 9
swBitmapLabel_Diameter: int = 10
swBitmapLabel_Radius: int = 11
swBitmapLabel_LinearDistance1: int = 12
swBitmapLabel_LinearDistance2: int = 13
swBitmapLabel_Thickness1: int = 14
swBitmapLabel_Thickness2: int = 15
swBitmapLabel_LinearPattern: int = 16
swBitmapLabel_CircularPattern: int = 17
swBitmapLabel_Width: int = 18
swBitmapLabel_Depth: int = 19
swBitmapLabel_KFactor: int = 20
swBitmapLabel_BendAllowance: int = 21
swBitmapLabel_BendDeduction: int = 22
swBitmapLabel_RipGap: int = 23
swBitmapLabel_SelectProfile: int = 24
swBitmapLabel_SelectBoundary: int = 25

# swCoordSysElementType_e (SwConst)
swCoordSysElement_XYPlane: int = 0
swCoordSysElement_XZPlane: int = 1
swCoordSysElement_YZPlane: int = 2
swCoordSysElement_XAxis: int = 3
swCoordSysElement_YAxis: int = 4
swCoordSysElement_ZAxis: int = 5
swCoordSysElement_Point: int = 6

# swCoreFeatureDirection_e (SwConst)
swCoreAlongExtractionDirection: int = 0
swCoreAwayFromExtractionDirection: int = 1

# swCornerReliefBendType_e (SwConst)
swCornerReliefBendType_TwoBend: int = 0
swCornerReliefBendType_ThreeBend: int = 1

# swCornerReliefError_e (SwConst)
swCornerReliefError_None: int = 0
swCornerReliefError_InvalidFaces: int = 1
swCornerReliefError_InvalidBody: int = 2
swCornerReliefError_InvalidCornerType: int = 3
swCornerReliefError_InvalidReliefType: int = 4
swCornerReliefError_IndexNotAvailable: int = 5
swCornerReliefError_GenericFailure: int = 6

# swCornerReliefSuitCaseType_e (SwConst)
swCornerReliefSuitCase_Default: int = 0
swCornerReliefSuitCase_ExtendGapInBendArea: int = 1
swCornerReliefSuitCase_FillInSomeGap: int = 2

# swCornerReliefType_e (SwConst)
swCornerCircularRelief: int = 0
swCornerSquareRelief: int = 1
swCornerBendWaistRelief: int = 2
swCornerTearRelief: int = 3
swCornerConstantWidthRelief: int = 4
swCornerObroundRelief: int = 5
swCornerMixed: int = 6
swCornerFullRoundRelief: int = 7
swCornerSuitCaseRelief: int = 8
swCornerRectangularRelief: int = 9

# swCornerTreatmentPlanarTrimOptions_e (SwConst)
swCornerTreatmentPlanarTrim_FirstContact: int = 0
swCornerTreatmentPlanarTrim_FullContact: int = 1

# swCornerTreatmentPlanarTrimToolType_e (SwConst)
swCornerTreatmentPlanarTrimTool_Automatic: int = 0
swCornerTreatmentPlanarTrimTool_UserDefined: int = 1

# swCornerTreatmentTrimType_e (SwConst)
swCornerTreatmentTrim_PlanarTrim: int = 0
swCornerTreatmentTrim_BodyTrim: int = 1
swCornerTreatmentTrim_MiterTrim: int = 2

# swCornerType_e (SwConst)
swCorner_Simple: int = 0
swCorner_TwoMember: int = 1
swCorner_Complex: int = 2

# swCosmeticConfigOptions_e (SwConst)
swConfigOptions_ThisConfiguration: int = 1
swConfigOptions_AllConfiguration: int = 2
swConfigOptions_SpecifyConfiguration: int = 3

# swCosmeticEndConditions_e (SwConst)
swEndConditionBlind: int = 0
swEndConditionBlindUptoNext: int = 1
swEndConditionThrough: int = 2
swEndConditionBlind2Dia: int = 3

# swCosmeticStandardType_e (SwConst)
swStandardType_StandardAnsiInch: int = 0
swStandardType_StandardAnsiMetric: int = 1
swStandardType_StandardBSI: int = 2
swStandardType_StandardDME: int = 3
swStandardType_StandardDIN: int = 4
swStandardType_StandardHascoMetric: int = 5
swStandardType_StandardHelicoilInch: int = 6
swStandardType_StandardHelicoilMetric: int = 7
swStandardType_StandardISO: int = 8
swStandardType_StandardJIS: int = 9
swStandardType_StandardPCS: int = 10
swStandardType_StandardProgressive: int = 11
swStandardType_StandardSuperior: int = 12
swStandardType_StandardGB: int = 13
swStandardType_StandardKS: int = 14
swStandardType_StandardIS: int = 15
swStandardType_StandardAS: int = 16
swStandardType_StandardNone: int = -2

# swCosmeticThreadDiameterType_e (SwConst)
swCosmeticThread_ConicalOffset: int = 1
swCosmeticThread_MajorDiameter: int = 2
swCosmeticThread_MinorDiameter: int = 3

# swCosmeticThreadType_e (SwConst)
swApplyCosmeticThread_Blind: int = 0
swApplyCosmeticThread_UpToNext: int = 1
swApplyCosmeticThread_ThroughFeature: int = 2

# swCosmeticWeldBeadMode_e (SwConst)
swCosmeticWeldBeadMode_WeldGeometry: int = 0
swCosmeticWeldBeadMode_WeldPath: int = 1

# swCosmeticWeldBeadSide_e (SwConst)
swCosmeticWeldBeadSide_selection: int = 1
swCosmeticWeldBeadSide_bothSides: int = 2
swCosmeticWeldBeadSide_allAround: int = 3

# swCosmosWorksMat (SwConst)
swCosmosWorksMatNone: int = 0
swCosmosWorksMatAcrylic: int = 1
swCosmosWorksMatAluminum: int = 2
swCosmosWorksMatNylon: int = 3
swCosmosWorksMatRubber: int = 4
swCosmosWorksMatSteel: int = 5

# swCreateAngRunDimError_e (SwConst)
swCreateAngRunDimError_Undefined: int = -1
swCreateAngRunDimError_GenFailure: int = 0
swCreateAngRunDimError_Success: int = 1
swCreateAngRunDimError_IdenticalDimension: int = 2
swCreateAngRunDimError_SelectAnotherEntity: int = 3

# swCreateCommandGroupErrors (SwConst)
swCreateCommandGroup_Failed: int = 0
swCreateCommandGroup_Success: int = 1
swCreateCommandGroup_Exceeds_ToolBarIDs: int = 2

# swCreateExplodeStepError_e (SwConst)
swCreateExplodeStepError_Successful: int = 0
swCreateExplodeStepError_Generic: int = 1
swCreateExplodeStepError_NoExplodeView: int = 2
swCreateExplodeStepError_NoComponents: int = 3
swCreateExplodeStepError_InvalidRadialAxis: int = 4
swCreateExplodeStepError_OpenExplodePMP: int = 5
swCreateExplodeStepError_EditingComponentInContext: int = 6

# swCreateFacesBodyAction_e (SwConst)
swCreateFacesBodyActionCap: int = 1
swCreateFacesBodyActionGrow: int = 2
swCreateFacesBodyActionGrowFromParent: int = 3
swCreateFacesBodyActionLeaveRubber: int = 4

# swCreateFeatureBodyOpts_e (SwConst)
swCreateFeatureBodyCheck: int = 1
swCreateFeatureBodySimplify: int = 2

# swCreateFeatureError_e (SwConst)
swCreateFeatureError_GenricError_GeometricError: int = 0
swCreateFeatureError_GenricError_UnknownError: int = 1
swCreateFeatureError_MateController_MateNotSet: int = 2
swCreateFeatureError_MateController_MateTypeNotSupported: int = 3
swCreateFeatureError_MateController_FailedToSolveMates: int = 4
swCreateFeatureError_MateController_DimensionValueOutOfLimit: int = 5
swCreateFeatureError_MateController_MateSelectionsPositionDataMismatch: int = 6
swCreateFeatureError_SolidToSheetMetal_Success: int = 7
swCreateFeatureError_SolidToSheetMetal_FixedFaceOrEdgeIsMissing: int = 8

# swCreateOrdDimError_e (SwConst)
swCreateOrdDimErr_Undefined: int = -1
swCreateOrdDimErr_Success: int = 0
swCreateOrdDimErr_GenFailure: int = 1
swCreateOrdDimErr_GenNoInternalDims: int = 2
swCreateOrdDimErr_GenBadSel: int = 3
swCreateOrdDimErr_GenNeedModelLoaded: int = 4
swCreateOrdDimErr_GenSamePartOnly: int = 5
swCreateOrdDimErr_GenExtraSelection: int = 6
swCreateOrdDimErr_OrdFailure: int = 7
swCreateOrdDimErr_OrdDupInGroup: int = 8
swCreateOrdDimErr_OrdBadDir: int = 9

# swCreatePartExplodeStepError_e (SwConst)
swCreatePartExplodeStepError_Successful: int = 0
swCreatePartExplodeStepError_Generic: int = 1
swCreatePartExplodeStepError_NoBodies: int = 2
swCreatePartExplodeStepError_OpenExplodePMP: int = 3
swCreatePartExplodeStepError_InactiveConfiguration: int = 4

# swCreateSectionViewAtOptions_e (SwConst)
swCreateSectionView_NotAligned: int = 1
swCreateSectionView_OffsetSection: int = 2
swCreateSectionView_ChangeDirection: int = 4
swCreateSectionView_ScaleWithModel: int = 8
swCreateSectionView_Partial: int = 16
swCreateSectionView_DisplaySurfaceCut: int = 32
swCreateSectionView_ExcludeFasteners: int = 64
swCreateSectionView_CutSurfaceBodies: int = 128

# swCreateSeedCutType_e (SwConst)
swCreateSeedCutNone: int = 0
swCreateSeedCutCircle: int = 1
swCreateSeedCutSquare: int = 2
swCreateSeedCutDiamond: int = 3
swCreateSeedCutPolygon: int = 4

# swCreateWireBodyOptions_e (SwConst)
swCreateWireBodyByDefault: int = 0
swCreateWireBodyMergeCurves: int = 1

# swCropViewErrors_e (SwConst)
swCropViewErrors_Unknown: int = 0
swCropViewErrors_NoError: int = 1
swCropViewErrors_CannotCropDetailOrBrokenView: int = 2
swCropViewErrors_CannotUnfoldView: int = 3
swCropViewErrors_IncorrectProfile: int = 4

# swCrossHatchFilter_e (SwConst)
swCrossHatchInclude: int = 0
swCrossHatchExclude: int = 1
swCrossHatchOnly: int = 2
swCrossHatchAndExplodeOnly: int = 3
swSolidHatchOnly: int = 4

# swCurveDrivenPatternAlignment_e (SwConst)
swCurvePatternTangentToCurve: int = 0
swCurvePatternAlignToSeed: int = 1

# swCurveDrivenPatternCurveMethod_e (SwConst)
swCurvePatternTransformCurve: int = 0
swCurvePatternOffsetCurve: int = 1

# swCurveTypes_e (SwConst)
LINE_TYPE: int = 3001
CIRCLE_TYPE: int = 3002
ELLIPSE_TYPE: int = 3003
INTERSECTION_TYPE: int = 3004
BCURVE_TYPE: int = 3005
SPCURVE_TYPE: int = 3006
CONSTPARAM_TYPE: int = 3008
TRIMMED_TYPE: int = 3009

# swCustomInfoAddResult_e (SwConst)
swCustomInfoAddResult_AddedOrChanged: int = 0
swCustomInfoAddResult_GenericFail: int = 1
swCustomInfoAddResult_MismatchAgainstExistingType: int = 2
swCustomInfoAddResult_MismatchAgainstSpecifiedType: int = 3
swCustomInfoAddResult_MismatchAgainstLegacyTypes: int = 4

# swCustomInfoDeleteResult_e (SwConst)
swCustomInfoDeleteResult_OK: int = 0
swCustomInfoDeleteResult_NotPresent: int = 1
swCustomInfoDeleteResult_LinkedProp: int = 2

# swCustomInfoGetResult_e (SwConst)
swCustomInfoGetResult_CachedValue: int = 0
swCustomInfoGetResult_ResolvedValue: int = 2
swCustomInfoGetResult_NotPresent: int = 1

# swCustomInfoSetResult_e (SwConst)
swCustomInfoSetResult_OK: int = 0
swCustomInfoSetResult_NotPresent: int = 1
swCustomInfoSetResult_TypeMismatch: int = 2
swCustomInfoSetResult_LinkedProp: int = 3

# swCustomInfoType_e (SwConst)
swCustomInfoUnknown: int = 0
swCustomInfoText: int = 30
swCustomInfoDate: int = 64
swCustomInfoNumber: int = 3
swCustomInfoDouble: int = 5
swCustomInfoYesOrNo: int = 11
swCustomInfoEquation: int = 105

# swCustomLinkSetResult_e (SwConst)
swCustomLinkSetResult_OK: int = 0
swCustomLinkSetResult_NotPresent: int = 1
swCustomLinkSetResult_Legacy: int = 2
swCustomLinkSetResult_UserProp: int = 3

# swCustomPropertyAddOption_e (SwConst)
swCustomPropertyOnlyIfNew: int = 0
swCustomPropertyDeleteAndAdd: int = 1
swCustomPropertyReplaceValue: int = 2

# swCutListExclusionStatus_e (SwConst)
swCutListExclusionStatus_Success: int = 0
swCutListExclusionStatus_InvalidEntities: int = 1

# swCutListTransferOptions_e (SwConst)
swCutListTransferOptions_None: int = 0
swCutListTransferOptions_FileProperties: int = 1
swCutListTransferOptions_CutListProperties: int = 2

# swCutListType_e (SwConst)
swSolidBodyCutList: int = 1
swSheetmetalCutlist: int = 2
swWeldmentCutlist: int = 3

# swCutSweepOption_e (SwConst)
swProfileSweep: int = 1
swSolidSweep: int = 2

# swDatumDisplayType_e (SwConst)
swDatumDisplayType_Default: int = 0
swDatumDisplayType_Square: int = 1
swDatumDisplayType_Roundgb: int = 2

# swDatumGbLeaderStyle_e (SwConst)
swDatumLeaderStyle_Horizontal: int = 1
swDatumLeaderStyle_Vertical: int = 2
swDatumLeaderStyle_Perpendicular: int = 3

# swDatumTagTextParts_e (SwConst)
swDatumTagTextPrefix: int = 1
swDatumTagTextSuffix: int = 2
swDatumTagTextCalloutAbove: int = 3
swDatumTagTextCalloutBelow: int = 4

# swDatumTargetAreaShape_e (SwConst)
swDatumTargetAreaNone: int = 0
swDatumTargetAreaPoint: int = 1
swDatumTargetAreaCircle: int = 2
swDatumTargetAreaRectangle: int = 3

# swDefaultBOMPartNumberSource_e (SwConst)
swDefaultBOMPartNumberSource_DocumentName: int = 0
swDefaultBOMPartNumberSource_ConfigurationName: int = 1

# swDeleteSelectionOptions_e (SwConst)
swDelete_Children: int = 1
swDelete_Absorbed: int = 2
swDelete_Advanced: int = 4

# swDesignTableErrors_e (SwConst)
swDTblNoError: int = 0
swDTblCfgInvalid: int = 1
swDTblCorrupt: int = 2
swDTblExiting: int = 3
swDTblNoFileName: int = 4
swDTblCurrentlyEditing: int = 5
swDTblTooManyColumns: int = 6
swDTblLinkChanged: int = 7
swDTblFileNotFound: int = 8
swDTblInvalidColumnValue: int = 9
swDTblInvalidColCustomProp: int = 10
swDTblInvalidColumnDimName: int = 11
swDTblInvalidColumnFeatName: int = 12
swDTblInvalidColumnKeyWord: int = 13
swDTblInvalidConfigName: int = 14
swDTblDataInvalidComponetState: int = 15
swDTblDataInvalidFeatureState: int = 16
swDTblInvalidYesNoData: int = 17
swDTblDisplayStateError: int = 18
swDTblModelFeatRequired: int = 19
swDTblParentConfigInvalid: int = 20
swDTblInvalidRowNameKeyword: int = 21
swDTblTolTypeInvalid: int = 22
swDTblNotSuppressible: int = 23
swDTblTableIsEmpty: int = 24
swDTblNegitiveDimension: int = 25
swDTbUnUsedConfiguration: int = 26
swDTbCannotOpen: int = 27
swDTInvalidComponentName: int = 28
swDTNeedsComponent: int = 29
swDTDimValueRangeError: int = 30
swDTDimAngleValueRangeError: int = 31
swDTInvalidEquation: int = 32
swDTConfigCircularDefinition: int = 33
swDTInvalidUserSpecifiedConfigName: int = 34

# swDesignTableSourceTypes_e (SwConst)
swDesignTableSourceNone: int = 1
swDesignTableSourceFromFile: int = 2
swDesignTableSourceLinked: int = 3

# swDesignTableUpdateOptions_e (SwConst)
swUpdateDesignTableSelected: int = 1
swUpdateDesignTableAll: int = 2
swUpdateDesignTableNone: int = 3

# swDestroyNotifyType_e (SwConst)
swDestroyNotifyDestroy: int = 0
swDestroyNotifyHidden: int = 1

# swDetCircleShowType_e (SwConst)
swDetCirclePROFILE: int = 0
swDetCircleCIRCLE: int = 1
swDetCircleDONTSHOW: int = 2

# swDetViewStyle_e (SwConst)
swDetViewSTANDARD: int = 0
swDetViewBROKEN: int = 1
swDetViewLEADER: int = 2
swDetViewNOLEADER: int = 3
swDetViewCONNECTED: int = 4

# swDetailingBalloonAutoBalloons_e (SwConst)
swStraightAutoBalloonLeader: int = 0
swBentAutoBalloonLeader: int = 1

# swDetailingChamferDimLeaderStyle_e (SwConst)
swDetailChamferDimLeaderHorizBeside: int = 1
swDetailChamferDimLeaderHorizAbove: int = 2
swDetailChamferDimLeaderAngBeside: int = 3
swDetailChamferDimLeaderAngAbove: int = 4
swDetailChamferDimLeaderAlongEdge: int = 5

# swDetailingChamferDimLeaderTextStyle_e (SwConst)
swDetailChamferDimDistDist: int = 1
swDetailChamferDimDistAng: int = 2
swDetailChamferDimAngDist: int = 3
swDetailChamferDimCDist: int = 4

# swDetailingChamferDimXStyle_e (SwConst)
swDetailingChamferDimXStyleUpperCaseX: int = 1
swDetailingChamferDimXStyleLowerCaseX: int = 2

# swDetailingDimFractionScaleIndex_e (SwConst)
swDetailingDimFractionScale_100Percent: int = 0
swDetailingDimFractionScale_90Percent: int = 1
swDetailingDimFractionScale_80Percent: int = 2
swDetailingDimFractionScale_70Percent: int = 3
swDetailingDimFractionScale_60Percent: int = 4
swDetailingDimFractionScale_50Percent: int = 5
swDetailingDimFractionScale_40Percent: int = 6
swDetailingDimFractionScale_30Percent: int = 7
swDetailingDimFractionScale_20Percent: int = 8
swDetailingDimFractionScale_10Percent: int = 9

# swDetailingDimFractionStyle_e (SwConst)
swDetailingDimFractionStyle_Slash: int = 0
swDetailingDimFractionStyle_Stack: int = 1
swDetailingDimFractionStyle_DiagonalStack: int = 2
swDetailingDimFractionStyle_Dash: int = 3

# swDetailingDimTrailingZero_e (SwConst)
swDimSmartTrailingZeroes: int = 0
swDimShowTrailingZeroes: int = 1
swDimRemoveTrailingZeroes: int = 2
swDimStandardTrailingZeroes: int = 3
swDimRemoveOnlyOnZero: int = 4
swDimSameAsSource: int = 5
swDimSameAsDocumentDimension: int = 6
swDimSameAsDocumentTolerance: int = 7
swDimSameAsDimension: int = 8

# swDetailingDimXpertChamferInstanceStyle_e (SwConst)
swDetailingDimXpertChamferNone: int = 1
swDetailingDimXpertChamferTyp: int = 2
swDetailingDimXpertChamferInstance: int = 3

# swDetailingDimXpertChamferStyle_e (SwConst)
swDetailingDimXpertChamferDistDist: int = 1
swDetailingDimXpertChamferDistAngle: int = 2

# swDetailingDimXpertFilletInstanceStyle_e (SwConst)
swDetailingDimXpertFilletNone: int = 1
swDetailingDimXpertFilletTyp: int = 2
swDetailingDimXpertFilletInstance: int = 3

# swDetailingDimXpertSlotStyle_e (SwConst)
swDetailingDimXpertSlotCenter: int = 1
swDetailingDimXpertSlotOverall: int = 2

# swDetailingDualDimPosition_e (SwConst)
swDualDimensionsSideBySide: int = 1
swDualDimensionsAboveAndBelow: int = 2
swDualDimensionsOnRight: int = 1
swDualDimensionsOnTop: int = 2
swDualDimensionsOnLeft: int = 3
swDualDimensionsOnBottom: int = 4

# swDetailingForeshortenedDiameterStyle_e (SwConst)
swForeshortenedStyleDoubleArrowhead: int = 1
swForeshortenedStyleZigZagLeader: int = 2

# swDetailingGtolMaterialConditionSymbolPlacement_e (SwConst)
swDetailingGtolMaterialConditionSymbolPlacement_ASME: int = 0
swDetailingGtolMaterialConditionSymbolPlacement_ISO: int = 1

# swDetailingHalfSectionArrow_e (SwConst)
swDetailingHalfSectionArrow_AlternativeDisplay: int = 0
swDetailingHalfSectionArrow_StandardDisplay: int = 1

# swDetailingLeadingZero_e (SwConst)
swLeadingZero_FollowStandard: int = 1
swLeadingZero_Show: int = 2
swLeadingZero_DoNotShow: int = 3

# swDetailingLinearForeshortened_e (SwConst)
swDetailingLinearForeshortened_DoubleArrow: int = 0
swDetailingLinearForeshortened_Zigzag: int = 1
swDetailingLinearForeshortened_Line: int = 2
swDetailingLinearForeshortened_SingleArrow: int = 3

# swDetailingNoteTextContent_e (SwConst)
swDetailingNoteTextCustom: int = 1
swDetailingNoteTextItemNumber: int = 2
swDetailingNoteTextQuantity: int = 3
swDetailingNoteTextCustomProperty: int = 4

# swDetailingSFSymbolStandard_e (SwConst)
swDetailingSFSymbolStandard_1302_1992: int = 0
swDetailingSFSymbolStandard_1302_2002: int = 1
swDetailingSFSymbolStandard_21920_1: int = 2

# swDetailingSectionViewLineStyle_e (SwConst)
swDetailingSectionViewLineStyleDisplay_StandardWithConnector: int = 0
swDetailingSectionViewLineStyleDisplay_AlternateWithoutConnector: int = 1
swDetailingSectionViewLineStyleDisplay_StandardWithoutConnector: int = 2

# swDetailingStandard_e (SwConst)
swDetailingStandardANSI: int = 1
swDetailingStandardISO: int = 2
swDetailingStandardDIN: int = 3
swDetailingStandardJIS: int = 4
swDetailingStandardBS: int = 5
swDetailingStandardGOST: int = 6
swDetailingStandardGB: int = 7
swDetailingStandardUserDefined: int = 8

# swDetailingToleranceTextSizing_e (SwConst)
swToleranceTextSizeUsingScaleValue: int = 1
swToleranceTextSizeUsingHeightValue: int = 2

# swDetailingViewLabelsDelimiter_e (SwConst)
swDetailingViewLabelsDelimiter_none: int = 0
swDetailingViewLabelsDelimiter_XcolonX: int = 1
swDetailingViewLabelsDelimiter_XslashX: int = 2
swDetailingViewLabelsDelimiter_XcolonXparen: int = 3
swDetailingViewLabelsDelimiter_XslashXparen: int = 4
swDetailingViewLabelsDelimiter_numberX: int = 5

# swDetailingViewLabelsLabel_e (SwConst)
swDetailingViewLabelsLabel_none: int = 0
swDetailingViewLabelsLabel_X: int = 1
swDetailingViewLabelsLabel_XdashX: int = 2
swDetailingViewLabelsLabel_XspaceX: int = 3

# swDetailingViewLabelsName_e (SwConst)
swDetailingViewLabelsName_none: int = 0
swDetailingViewLabelsName_VIEW: int = 1
swDetailingViewLabelsName_viewtype: int = 2
swDetailingViewLabelsName_custom: int = 3
swDetailingViewLabelsName_DrawingTree: int = 4

# swDetailingViewLabelsScale_e (SwConst)
swDetailingViewLabelsScale_none: int = 0
swDetailingViewLabelsScale_SCALE: int = 1
swDetailingViewLabelsScale_SCALEcolon: int = 2
swDetailingViewLabelsScale_SCALEcustom: int = 3

# swDetailingViewRotation_e (SwConst)
swDetailingViewRotation_None: int = 0
swDetailingViewRotation_DisplaySymbolAngle: int = 1
swDetailingViewRotation_DisplaySymbol: int = 2
swDetailingViewRotation_DisplayROTATEDAngleCWCCW: int = 3
swDetailingViewRotation_DisplayAngle: int = 4

# swDetailingVirtualSharp_e (SwConst)
swDetailingVirtualSharpNone: int = 0
swDetailingVirtualSharpPlus: int = 1
swDetailingVirtualSharpStar: int = 2
swDetailingVirtualSharpWitness: int = 3
swDetailingVirtualSharpDot: int = 4

# swDimXpertAnnotationType_e (SwDimXpert)
swDimXpertAnnotationType_unknown: int = 0
swDimXpertDimTol_DistanceBetween: int = 101
swDimXpertDimTol_CounterBore: int = 102
swDimXpertDimTol_Depth: int = 103
swDimXpertDimTol_CounterSinkDiameter: int = 104
swDimXpertDimTol_ChamferDimension: int = 105
swDimXpertDimTol_AngleBetween: int = 106
swDimXpertDimTol_CounterSinkAngle: int = 107
swDimXpertDimTol_ConeAngle: int = 108
swDimXpertDimTol_Diameter: int = 109
swDimXpertDimTol_Length: int = 110
swDimXpertDimTol_Radius: int = 111
swDimXpertDimTol_Width: int = 112
swDimXpertDimTol_CompositeDistanceBetween: int = 113
swDimXpertDimTol_PatternAngleBetween: int = 114
swDimXpertDatum: int = 150
swDimXpertGeoTol_Position: int = 201
swDimXpertGeoTol_CompositePosition: int = 202
swDimXpertGeoTol_Symmetry: int = 203
swDimXpertGeoTol_Concentricity: int = 204
swDimXpertGeoTol_LineProfile: int = 205
swDimXpertGeoTol_CompositeLineProfile: int = 206
swDimXpertGeoTol_SurfaceProfile: int = 207
swDimXpertGeoTol_CompositeSurfaceProfile: int = 208
swDimXpertGeoTol_Angularity: int = 210
swDimXpertGeoTol_Parallelism: int = 211
swDimXpertGeoTol_Perpendicularity: int = 212
swDimXpertGeoTol_TotalRunout: int = 213
swDimXpertGeoTol_CircularRunout: int = 214
swDimXpertGeoTol_Flatness: int = 215
swDimXpertGeoTol_Circularity: int = 216
swDimXpertGeoTol_Cylindricity: int = 217
swDimXpertGeoTol_Straightness: int = 218
swDimXpertGeoTol_Tangency: int = 219
swDimXpertDimTol_AngleSize: int = 220
swDimXpertDimTol_AngleBetweenCircular: int = 221

# swDimXpertAutoDimSchemePartType_e (SwDimXpert)
swDimXpertAutoDimSchemePartType_Prismatic: int = 0
swDimXpertAutoDimSchemePartType_Turned: int = 1

# swDimXpertAutoDimSchemePatternType_e (SwDimXpert)
swDimXpertAutoDimSchemePatternType_Linear: int = 0
swDimXpertAutoDimSchemePatternType_Polar: int = 1

# swDimXpertAutoDimSchemeToleranceType_e (SwDimXpert)
swDimXpertAutoDimSchemeToleranceType_PlusMinus: int = 0
swDimXpertAutoDimSchemeToleranceType_Geometric: int = 1

# swDimXpertBlockPrecision_e (SwConst)
swDimXpertBlockPrecsionTwoDecimals: int = 0
swDimXpertBlockPrecisionThreeDecimals: int = 1
swDimXpertBlockPrecisionFourDecimals: int = 2

# swDimXpertBlockToleranceType_e (SwDimXpert)
swDimXpertBlockToleranceType_unknown: int = 0
swDimXpertBlockToleranceType_ASMEInch: int = 1
swDimXpertBlockToleranceType_ISO2768: int = 2

# swDimXpertChamferAngleType_e (SwDimXpert)
swDimXpertChamferAngleType_unknown: int = 0
swDimXpertChamferAngleType_Concave: int = 1
swDimXpertChamferAngleType_Convex: int = 2

# swDimXpertChamferDimensionType_e (SwDimXpert)
swDimXpertChamferDimensionType_unknown: int = 0
swDimXpertChamferDimensionType_Angle: int = 1
swDimXpertChamferDimensionType_LinearDistance1: int = 2
swDimXpertChamferDimensionType_LinearDistance2: int = 3

# swDimXpertChamferType_e (SwDimXpert)
swDimXpertChamferType_unknown: int = 0
swDimXpertChamferType_DistanceAngle: int = 1
swDimXpertChamferType_DistanceDistance: int = 2
swDimXpertChamferType_Vertex: int = 3

# swDimXpertCombineAnnotation_e (SwDimXpert)
swDimXpertCombineAnnotation_swDimXpertCombineFailed: int = 0
swDimXpertCombineAnnotation_swDimXpertCombineSucceeded: int = 1
swDimXpertCombineAnnotation_swDimXpertBreakFailed: int = 2
swDimXpertCombineAnnotation_swDimXpertBreakSucceeded: int = 3

# swDimXpertCompoundHoleType_e (SwDimXpert)
swDimXpertCompoundHoleType_unknown: int = 0
swDimXpertCompoundHoleType_Compound: int = 1
swDimXpertCompoundHoleType_Counterbore: int = 2
swDimXpertCompoundHoleType_Countersink: int = 3
swDimXpertCompoundHoleType_Simple: int = 4

# swDimXpertDimensionPositionOption_e (SwDimXpert)
swDimXpertDimensionPositionOption_N: int = 0
swDimXpertDimensionPositionOption_X: int = 1
swDimXpertDimensionPositionOption_Y: int = 2
swDimXpertDimensionPositionOption_Z: int = 3

# swDimXpertDimensionToleranceType_e (SwDimXpert)
swDimXpertDimensionToleranceType_unknown: int = 0
swDimXpertDimTolType_BlockTolerance: int = 1
swDimXpertDimTolType_BlockToleranceNoNominal: int = 2
swDimXpertDimTolType_ISOLimitsAndFits: int = 3
swDimXpertDimTolType_ISOLimitsAndFitsNoNominal: int = 4
swDimXpertDimTolType_LimitDimension: int = 5
swDimXpertDimTolType_MAXTolerance: int = 6
swDimXpertDimTolType_MINTolerance: int = 7
swDimXpertDimTolType_NoTolerance: int = 8
swDimXpertDimTolType_PlusMinusDimension: int = 9
swDimXpertDimTolType_PlusMinusNoNominal: int = 10

# swDimXpertDisplayDatumGtolLinearDimAttachmentType_e (SwConst)
swDimXpertDisplayDatumGtolLinearDimAttachmentType_ValueSide: int = 0
swDimXpertDisplayDatumGtolLinearDimAttachmentType_ValueTop: int = 1

# swDimXpertDisplayDatumGtolSurfaceAttachmentType_e (SwConst)
swDimXpertDisplayDatumGtolSurfaceAttachmentType_ValueSide: int = 0
swDimXpertDisplayDatumGtolSurfaceAttachmentType_ValueTop: int = 1

# swDimXpertDisplayGtolLinearDimAttachmentType_e (SwConst)
swDimXpertDisplayGtolLinearDimAttachmentType_ValueSide: int = 0
swDimXpertDisplayGtolLinearDimAttachmentType_ValueTop: int = 1

# swDimXpertDisplayHoleDimensionType_e (SwConst)
swDimXpertDisplayHoleDimensionType_Diameters: int = 0
swDimXpertDisplayHoleDimensionType_DiameterDepth: int = 1

# swDimXpertDisplaySlotDimensionType_e (SwConst)
swDimXpertDisplaySlotDimensionType_LengthRadius: int = 0
swDimXpertDisplaySlotDimensionType_LengthWidth: int = 1

# swDimXpertDistanceFosUsage_e (SwDimXpert)
swDimXpertDistanceFosUsage_unknown: int = 0
swDimXpertDistanceFosUsage_Center: int = 1
swDimXpertDistanceFosUsage_MaximumSide: int = 2
swDimXpertDistanceFosUsage_MinimumSide: int = 3

# swDimXpertFeatureFilters_e (SwDimXpert)
swDimXpertFeatureFilters_Plane: int = 1
swDimXpertFeatureFilters_Surface: int = 2
swDimXpertFeatureFilters_Cone: int = 4
swDimXpertFeatureFilters_Cylinder: int = 8
swDimXpertFeatureFilters_Boss: int = 16
swDimXpertFeatureFilters_Fillet: int = 32
swDimXpertFeatureFilters_Chamfer: int = 64
swDimXpertFeatureFilters_SimpleHole: int = 128
swDimXpertFeatureFilters_Counterbore: int = 256
swDimXpertFeatureFilters_Countersink: int = 512
swDimXpertFeatureFilters_Slot: int = 1024
swDimXpertFeatureFilters_Notch: int = 2048
swDimXpertFeatureFilters_Pocket: int = 4096
swDimXpertFeatureFilters_SurfOfRev: int = 8192
swDimXpertFeatureFilters_Torus: int = 16384
swDimXpertFeatureFilters_CompoundHole: int = 32768

# swDimXpertFeatureSelectorOption_e (SwDimXpert)
swDimXpertFeatureSelectorOption_Default: int = -1
swDimXpertFeatureSelectorOption_Plane: int = 0
swDimXpertFeatureSelectorOption_Cylinder: int = 1
swDimXpertFeatureSelectorOption_Sphere: int = 2
swDimXpertFeatureSelectorOption_Freeform: int = 3
swDimXpertFeatureSelectorOption_Cone: int = 4
swDimXpertFeatureSelectorOption_SimpleHole: int = 5
swDimXpertFeatureSelectorOption_Slot: int = 6
swDimXpertFeatureSelectorOption_Width: int = 7
swDimXpertFeatureSelectorOption_Boss: int = 8
swDimXpertFeatureSelectorOption_Tab: int = 9
swDimXpertFeatureSelectorOption_Fillet: int = 10
swDimXpertFeatureSelectorOption_Chamfer: int = 11
swDimXpertFeatureSelectorOption_ConicalHole: int = 12
swDimXpertFeatureSelectorOption_Pocket: int = 13
swDimXpertFeatureSelectorOption_Notch: int = 14
swDimXpertFeatureSelectorOption_Extrude: int = 15
swDimXpertFeatureSelectorOption_SplitPlane: int = 16
swDimXpertFeatureSelectorOption_SplitCylinder: int = 17
swDimXpertFeatureSelectorOption_CntrBore: int = 18
swDimXpertFeatureSelectorOption_CntrSink: int = 19
swDimXpertFeatureSelectorOption_CompoundHole: int = 20
swDimXpertFeatureSelectorOption_HolePattern: int = 21
swDimXpertFeatureSelectorOption_Pattern: int = 22
swDimXpertFeatureSelectorOption_MixedPattern: int = 23

# swDimXpertFeatureType_e (SwDimXpert)
swDimXpertFeatureType_unknown: int = 0
swDimXpertFeature_Plane: int = 1
swDimXpertFeature_Cylinder: int = 2
swDimXpertFeature_Cone: int = 3
swDimXpertFeature_Extrude: int = 4
swDimXpertFeature_Fillet: int = 5
swDimXpertFeature_Chamfer: int = 6
swDimXpertFeature_CompoundHole: int = 7
swDimXpertFeature_CompoundWidth: int = 8
swDimXpertFeature_CompoundNotch: int = 9
swDimXpertFeature_CompoundClosedSlot3D: int = 10
swDimXpertFeature_IntersectPoint: int = 11
swDimXpertFeature_IntersectLine: int = 12
swDimXpertFeature_IntersectCircle: int = 13
swDimXpertFeature_IntersectPlane: int = 14
swDimXpertFeature_Pattern: int = 15
swDimXpertFeature_Sphere: int = 16
swDimXpertFeature_BestfitPlane: int = 17
swDimXpertFeature_Surface: int = 18
swDimXpertFeature_RefPlane: int = 19

# swDimXpertGeneralTolClass_e (SwConst)
swDimXpertGeneralTolClass_Fine: int = 0
swDimXpertGeneralTolClass_Medium: int = 1
swDimXpertGeneralTolClass_Coarse: int = 2
swDimXpertGeneralTolClass_VeryCoarse: int = 3
swDimXpertGeneralTolClass_Custom1: int = 4
swDimXpertGeneralTolClass_Custom2: int = 5

# swDimXpertGtolType_e (SwDimXpert)
swDimXpertGtolType_Straightness: int = 0
swDimXpertGtolType_Flatness: int = 1
swDimXpertGtolType_Circularity: int = 2
swDimXpertGtolType_Cylindricity: int = 3
swDimXpertGtolType_SurfaceProfile: int = 4
swDimXpertGtolType_LineProfile: int = 5
swDimXpertGtolType_Angularity: int = 6
swDimXpertGtolType_Perpendicularity: int = 7
swDimXpertGtolType_Parallelism: int = 8
swDimXpertGtolType_Position: int = 9
swDimXpertGtolType_Symmetry: int = 10
swDimXpertGtolType_Concentricity: int = 11
swDimXpertGtolType_CircularRunout: int = 12
swDimXpertGtolType_TotalRunout: int = 13

# swDimXpertISO2768PartType_e (SwDimXpert)
swDimXpertISO2768PartType_unknown: int = 0
swDimXpertISO2768PartType_Fine: int = 1
swDimXpertISO2768PartType_Medium: int = 2
swDimXpertISO2768PartType_Coarse: int = 3
swDimXpertISO2768PartType_VeryCoarse: int = 4

# swDimXpertMaterialConditionModifier_e (SwDimXpert)
swDimXpertMaterialConditionModifier_unknown: int = 0
swDimXpertMCM_LMC: int = 1
swDimXpertMCM_MMC: int = 2
swDimXpertMCM_NoMCM: int = 3
swDimXpertMCM_RFS: int = 4

# swDimXpertOrientationZoneType_e (SwDimXpert)
swDimXpertOrientationZoneType_unknown: int = 0
swDimXpertOrientationZoneType_Cylindrical: int = 1
swDimXpertOrientationZoneType_Planar: int = 2

# swDimXpertPatternTreatmentType_e (SwDimXpert)
swDimXpertPatternTreatmentType_unknown: int = 0
swDimXpertPatternTreatmentType_CircularPattern: int = 1
swDimXpertPatternTreatmentType_IndividualFeatures: int = 2

# swDimXpertPositionZoneType_e (SwDimXpert)
swDimXpertPositionZoneType_unknown: int = 0
swDimXpertPositionZoneType_Boundary: int = 1
swDimXpertPositionZoneType_CylindricalPosition: int = 2
swDimXpertPositionZoneType_PlanarPosition: int = 3
swDimXpertPositionZoneType_RadialPositionArc: int = 4
swDimXpertPositionZoneType_RadialPositionPlanar: int = 5
swDimXpertPositionZoneType_SphericalPosition: int = 6

# swDimXpertStraightnessZoneType_e (SwDimXpert)
swDimXpertStraightnessZoneType_unknown: int = 0
swDimXpertStraightnessZoneType_Cylindrical: int = 1
swDimXpertStraightnessZoneType_PlanarMedian: int = 2
swDimXpertStraightnessZoneType_Surface: int = 3

# swDimXpertTolType_e (SwConst)
swDimXpertTolType_Bilateral: int = 0
swDimXpertTolType_Symmetric: int = 1
swDimXpertTolType_GeneralOrBlock: int = 2

# swDimXpertTreeDisplay_e (SwConst)
swDimXpertTreeDisplay_Flat: int = 1
swDimXpertTreeDisplay_Annotation: int = 2
swDimXpertTreeDisplay_Feature: int = 3

# swDimensionArrowsSide_e (SwConst)
swDimArrowsInside: int = 0
swDimArrowsOutside: int = 1
swDimArrowsSmart: int = 2
swDimArrowsFollowDoc: int = 3

# swDimensionDrivenState_e (SwConst)
swDimensionDrivenUnknown: int = 0
swDimensionDriven: int = 1
swDimensionDriving: int = 2

# swDimensionParamType_e (SwConst)
swDimensionParamTypeUnknown: int = -1
swDimensionParamTypeDoubleLinear: int = 0
swDimensionParamTypeDoubleAngular: int = 1
swDimensionParamTypeInteger: int = 2

# swDimensionPrecisionSettings_e (SwConst)
swDoNotChangePrecisionSetting: int = -1
swPrecisionFollowsDocumentSetting: int = -2
swTolerancePrecisionFollowsNominal: int = -3

# swDimensionPrefix_e (SwConst)
swDimensionPrefix_None: int = 0
swDimensionPrefix_2X: int = 1
swDimensionPrefix_3X: int = 2
swDimensionPrefix_4X: int = 3
swDimensionPrefix_5X: int = 4
swDimensionPrefix_6X: int = 5
swDimensionPrefix_Unknown: int = 6

# swDimensionSymbol_e (SwConst)
swDimensionSymbol_None: int = 0
swDimensionSymbol_Unknown: int = 1
swDimensionSymbol_Diameter: int = 2
swDimensionSymbol_Depth: int = 3
swDimensionSymbol_Degree: int = 4
swDimensionSymbol_Centerline: int = 5
swDimensionSymbol_CenterOfMass: int = 6
swDimensionSymbol_Counterbore: int = 7
swDimensionSymbol_Countersink: int = 8
swDimensionSymbol_ConicalTaper: int = 9
swDimensionSymbol_Continuous: int = 10
swDimensionSymbol_ControlledRadius: int = 11
swDimensionSymbol_Delta: int = 12
swDimensionSymbol_Encompassing: int = 13
swDimensionSymbol_FlattenedLength: int = 14
swDimensionSymbol_FreeState: int = 15
swDimensionSymbol_Independency: int = 16
swDimensionSymbol_LeastMaterialCondition: int = 17
swDimensionSymbol_MaximumMaterialCondition: int = 18
swDimensionSymbol_PartingLine: int = 19
swDimensionSymbol_PlusMinus: int = 20
swDimensionSymbol_ProjectedToleranceZone: int = 21
swDimensionSymbol_RegardlessOfFeatureSize: int = 22
swDimensionSymbol_Rho: int = 23
swDimensionSymbol_SlopeUp: int = 24
swDimensionSymbol_SlopeDown: int = 25
swDimensionSymbol_SlopeInvertedUp: int = 26
swDimensionSymbol_SlopeInvertedDown: int = 27
swDimensionSymbol_SphericalRadius: int = 28
swDimensionSymbol_SphericalDiameter: int = 29
swDimensionSymbol_Square: int = 30
swDimensionSymbol_SquareBS: int = 31
swDimensionSymbol_Statistical: int = 32
swDimensionSymbol_TangentPlane: int = 33
swDimensionSymbol_Translation: int = 34
swDimensionSymbol_UnequallyDisposedProfile: int = 35
swDimensionSymbol_Radius: int = 36
swDimensionSymbol_Angle: int = 37
swDimensionSymbol_SlotLength: int = 38
swDimensionSymbol_SlotWidth: int = 39
swDimensionSymbol_CalloutText: int = 40

# swDimensionTextParts_e (SwConst)
swDimensionTextAll: int = 0
swDimensionTextPrefix: int = 1
swDimensionTextSuffix: int = 2
swDimensionTextCalloutAbove: int = 3
swDimensionTextCalloutBelow: int = 4
swDimensionTextPrefixDefinition: int = 5
swDimensionTextSuffixDefinition: int = 6
swDimensionTextCalloutAboveDefinition: int = 7
swDimensionTextCalloutBelowDefinition: int = 8

# swDimensionToleranceWarning_e (SwConst)
swDimensionTolerance_ValidForType: int = 0
swDimensionTolerance_NotValidForType: int = 1

# swDimensionType_e (SwConst)
swDimensionTypeUnknown: int = 0
swOrdinateDimension: int = 1
swLinearDimension: int = 2
swAngularDimension: int = 3
swArcLengthDimension: int = 4
swRadialDimension: int = 5
swDiameterDimension: int = 6
swHorOrdinateDimension: int = 7
swVertOrdinateDimension: int = 8
swZAxisDimension: int = 9
swChamferDimension: int = 10
swHorLinearDimension: int = 11
swVertLinearDimension: int = 12
swScalarDimension: int = 13
swRadialLinearDimension: int = 14
swDiametricLinearDimension: int = 15
swAngularOrdinateDimension: int = 16

# swDisplayCircularReferencesInEquations_e (SwConst)
swDisplayCircularReferencesInEquationsEverywhere: int = 0
swDisplayCircularReferencesInEquationsInEquationDialogOnly: int = 1
swDisplayCircularReferencesInEquationsNever: int = 2

# swDisplayDimensionLeaderText_e (SwConst)
swSolidLeaderAlignedText: int = 1
swBrokenLeaderHorizontalText: int = 2
swBrokenLeaderAlignedText: int = 3
swSolidLeaderHorizontalText: int = 4

# swDisplayMode_e (SwConst)
swDisplayModeUNKNOWN: int = -1
swWIREFRAME: int = 0
swHIDDEN_GREYED: int = 1
swHIDDEN: int = 2
swSHADED: int = 3
swFACETED_WIREFRAME: int = 4
swFACETED_HIDDEN_GREYED: int = 5
swFACETED_HIDDEN: int = 6
swSHADED_EDGES: int = 7
swDisplayModeDEFAULT: int = 8

# swDisplayPaneIndex_e (SwConst)
swDisplayPaneNone: int = 0
swDisplayPaneLifeCycleTab: int = 1
swDisplayPaneTab: int = 2
swDisplayPaneAIContentTab: int = 3

# swDisplayPotentialCircularReferencesInEquations_e (SwConst)
swDisplayPotentialCircularReferencesInEquationsEverywhere: int = 0
swDisplayPotentialCircularReferencesInEquationsInEquationDialogOnly: int = 1
swDisplayPotentialCircularReferencesInEquationsNever: int = 2

# swDisplayStateCreationChoices_e (SwConst)
swDisplayStateCreation_AskUser: int = -1
swDisplayStateCreation_PW: int = 1
swDisplayStateCreation_SW: int = 2
swDisplayStateCreation_BothPWSW: int = 3

# swDisplayStateOpts_e (SwConst)
swThisDisplayState: int = 1
swAllDisplayState: int = 2
swSpecifyDisplayState: int = 3

# swDisplayTangentEdges_e (SwConst)
swTangentEdgesHidden: int = 0
swTangentEdgesVisibleAndFonted: int = 1
swTangentEdgesVisible: int = 2

# swDistanceMateArcConditions_e (SwConst)
swArcCondition_NotSet: int = 0
swArcCondition_Center: int = 1
swArcCondition_Minimum: int = 2
swArcCondition_Maximum: int = 3

# swDocTemplateTypes_e (SwConst)
swDocTemplateTypeNONE: int = 1
swDocTemplateTypePART: int = 2
swDocTemplateTypeASSEMBLY: int = 4
swDocTemplateTypeDRAWING: int = 8
swDocTemplateTypeInContext: int = 16

# swDocumentTypes_e (SwConst)
swDocNONE: int = 0
swDocPART: int = 1
swDocASSEMBLY: int = 2
swDocDRAWING: int = 3
swDocSDM: int = 4
swDocLAYOUT: int = 5
swDocIMPORTED_PART: int = 6
swDocIMPORTED_ASSEMBLY: int = 7

# swDofStatus_e (SwConst)
swDofStatus_Unused: int = 0
swDofStatus_Static: int = 1
swDofStatus_StaticNormal: int = 2
swDofStatus_Free: int = 3
swDofStatus_FreeNormal: int = 4
swDofStatus_Instantaneous: int = 5
swDofStatus_InstantaneousNormal: int = 6

# swDraftAnalysisFaceType_e (SwConst)
swDraftAnalysisFaceTypePositive: int = 0
swDraftAnalysisFaceTypeNegative: int = 1
swDraftAnalysisFaceTypeNoDraft: int = 2
swDraftAnalysisFaceTypeStraddle: int = 3

# swDraftAnalysisOptions_e (SwConst)
swDraftAnalysisFlipDir: int = 1
swDraftAnalysisFindSteep: int = 2

# swDraftAnalysisShow_e (SwConst)
swDraftAnalysisShowPositive: int = 1
swDraftAnalysisShowNegative: int = 2
swDraftAnalysisShowDraftRequired: int = 4
swDraftAnalysisShowStraddle: int = 8
swDraftAnalysisShowPositiveSteep: int = 16
swDraftAnalysisShowNegativeSteep: int = 32
swDraftAnalysisShowSurface: int = 64

# swDraftFacePropagationType_e (SwConst)
swFacePropNone: int = 0
swFacePropTangent: int = 1
swFacePropAllLoops: int = 2
swFacePropInnerLoops: int = 3
swFacePropOuterLoops: int = 4

# swDraftStepType_e (SwConst)
swDraftTaperedStep: int = 3
swDraftPerpendicular: int = 6

# swDraftType_e (SwConst)
swNeutralPlaneDraft: int = 0
swPartingLineDraft: int = 1
swStepDraft: int = 3

# swDragArrowManipulatorOptions_e (SwConst)
swDragArrowManipulatorDirection1: int = 0
swDragArrowManipulatorDirection2: int = 1

# swDrawingComponentLineFontOption_e (SwConst)
swDrawingComponentLineFontVisible: int = 1
swDrawingComponentLineFontHidden: int = 2
swDrawingComponentLineFontTangent: int = 3
swDrawingComponentLineFontHatch: int = 4
swDrawingComponentLineFontSpeedpak: int = 5

# swDrawingMode_e (SwConst)
swDrawingMode_None: int = 0
swDrawingMode_Resolved: int = 1
swDrawingMode_Detailing: int = 2

# swDrawingNotify_e (SwConst)
swDrawingRegenNotify: int = 1
swDrawingDestroyNotify: int = 2
swDrawingRegenPostNotify: int = 3
swDrawingViewNewNotify: int = 4
swDrawingNewSelectionNotify: int = 5
swDrawingFileSaveNotify: int = 6
swDrawingFileSaveAsNotify: int = 7
swDrawingLoadFromStorageNotify: int = 8
swDrawingSaveToStorageNotify: int = 9
swDrawingAutoSaveNotify: int = 10
swDrawingAutoSaveToStorageNotify: int = 11
swDrawingConfigChangeNotify: int = 12
swDrawingConfigChangePostNotify: int = 13
swDrawingViewNewNotify2: int = 14
swDrawingAddItemNotify: int = 15
swDrawingRenameItemNotify: int = 16
swDrawingDeleteItemNotify: int = 17
swDrawingModifyNotify: int = 18
swDrawingFileReloadNotify: int = 19
swDrawingAddCustomPropertyNotify: int = 20
swDrawingChangeCustomPropertyNotify: int = 21
swDrawingDeleteCustomPropertyNotify: int = 22
swDrawingFileSaveAsNotify2: int = 23
swDrawingDeleteSelectionPreNotify: int = 24
swDrawingFileReloadPreNotify: int = 25
swDrawingFileSavePostNotify: int = 26
swDrawingLoadFromStorageStoreNotify: int = 27
swDrawingSaveToStorageStoreNotify: int = 28
swDrawingFeatureManagerTreeRebuildNotify: int = 29
swDrawingViewCreatePreNotify: int = 30
swDrawingDynamicHighlightNotify: int = 31
swDrawingDimensionChangeNotify: int = 32
swDrawingFileReloadCancelNotify: int = 33
swDrawingFileSavePostCancelNotify: int = 34
swDrawingSketchSolveNotify: int = 35
swDrawingDeleteItemPreNotify: int = 36
swDrawingClearSelectionsNotify: int = 37
swDrawingEquationEditorPreNotify: int = 38
swDrawingEquationEditorPostNotify: int = 39
swDrawingAddDvePagePreNotify: int = 40
swDrawingUnitsChangeNotify: int = 41
swDrawingDestroyNotify2: int = 42
swDrawingUndoPostNotify: int = 43
swDrawingUserSelectionPreNotify: int = 44
swDrawingRedoPostNotify: int = 45
swDrawingRedoPreNotify: int = 46
swDrawingUndoPreNotify: int = 47
swDrawingAutoSaveToStorageStoreNotify: int = 48
swDrawingInsertTableNotify: int = 49
swDrawingModifyTableNotify: int = 50
swDrawingUserSelectionPostNotify: int = 51
swDrawingActivateSheetPreNotify: int = 52
swDrawingActivateSheetPostNotify: int = 53
swDrawingCommandManagerTabActivatedPreNotify: int = 54
swDrawingFeatureManagerTabActivatedPreNotify: int = 55
swDrawingFeatureManagerTabActivatedNotify: int = 56
swDrawingRenameDisplayTitleNotify: int = 57
swDrawingDisplayPaneExpandNotify: int = 58
swDrawingDisplayPaneCollapseNotify: int = 59
swDrawingStateChangeNotify: int = 60
swViewPositionChangeNotify: int = 61
swDrawingAddDependencyNotify: int = 62
swDrawingDeleteDependencyNotify: int = 63

# swDrawingProjectionType_e (SwConst)
swDrawing1stAngleProjection: int = 1
swDrawing3rdAngleProjection: int = 2

# swDrawingSheetsZonesLetterLayout_e (SwConst)
swDrawingSheetsZonesLetterLayout_Column: int = 0
swDrawingSheetsZonesLetterLayout_Row: int = 1

# swDrawingSheetsZonesOrigin_e (SwConst)
swDrawingSheetsZones_UpperLeft: int = 0
swDrawingSheetsZones_UpperRight: int = 1
swDrawingSheetsZones_LowerLeft: int = 2
swDrawingSheetsZones_LowerRight: int = 3

# swDrawingViewTypes_e (SwConst)
swDrawingSheet: int = 1
swDrawingSectionView: int = 2
swDrawingDetailView: int = 3
swDrawingProjectedView: int = 4
swDrawingAuxiliaryView: int = 5
swDrawingStandardView: int = 6
swDrawingNamedView: int = 7
swDrawingRelativeView: int = 8
swDrawingDetachedView: int = 9
swDrawingAlternatePositionView: int = 10

# swDwgImportEntitiesPositioning_e (SwConst)
swDwgEntitiesCentered: int = 1
swDwgEntitiesSpecifyPosition: int = 2

# swDwgPaperSizes_e (SwConst)
swDwgPaperAsize: int = 0
swDwgPaperAsizeVertical: int = 1
swDwgPaperBsize: int = 2
swDwgPaperCsize: int = 3
swDwgPaperDsize: int = 4
swDwgPaperEsize: int = 5
swDwgPaperA4size: int = 6
swDwgPaperA4sizeVertical: int = 7
swDwgPaperA3size: int = 8
swDwgPaperA2size: int = 9
swDwgPaperA1size: int = 10
swDwgPaperA0size: int = 11
swDwgPapersUserDefined: int = 12

# swDwgTemplates_e (SwConst)
swDwgTemplateAsize: int = 0
swDwgTemplateAsizeVertical: int = 1
swDwgTemplateBsize: int = 2
swDwgTemplateCsize: int = 3
swDwgTemplateDsize: int = 4
swDwgTemplateEsize: int = 5
swDwgTemplateA4size: int = 6
swDwgTemplateA4sizeVertical: int = 7
swDwgTemplateA3size: int = 8
swDwgTemplateA2size: int = 9
swDwgTemplateA1size: int = 10
swDwgTemplateA0size: int = 11
swDwgTemplateCustom: int = 12
swDwgTemplateNone: int = 13

# swDxfFormat_e (SwConst)
swDxfFormat_R12: int = 0
swDxfFormat_R13: int = 1
swDxfFormat_R14: int = 2
swDxfFormat_R2000: int = 3
swDxfFormat_R2004: int = 4
swDxfFormat_R2007: int = 5
swDxfFormat_R2010: int = 6
swDxfFormat_R2013: int = 7
swDxfFormat_R2018: int = 8

# swDxfMultisheet_e (SwConst)
swDxfActiveSheetOnly: int = 0
swDxfSeparateSheets: int = 1
swDxfMultiSheet: int = 2

# swDynamicMode_e (SwConst)
swNoDynamics: int = 0
swSpinDynamics: int = 1
swPanDynamics: int = 2
swZoomDynamics: int = 3
swUnknownDynamics: int = 4
swAnimDynamics: int = 5
swDragDynamics: int = 6

# swEdgeFlangeError_e (SwConst)
swEdgeFlangeError_NoError: int = 0
swEdgeFlangeError_EdgeNotSpecified: int = 1
swEdgeFlangeError_SketchNotSpecified: int = 2
swEdgeFlangeError_NumberOfEdgesAndSketchesNotEqual: int = 3
swEdgeFlangeError_EdgeAlreadyExists: int = 4
swEdgeFlangeError_InvalidEdge: int = 5
swEdgeFlangeError_MustSpecifyAtLeastOneEdge: int = 6
swEdgeFlangeError_GenericError: int = 7

# swEdgeUntrimType_e (SwConst)
swEdgeUntrimTypeExtendEdges: int = 2
swEdgeUntrimTypeConnectEndPoints: int = 1

# swEdgesHiddenEdgeDisplay_e (SwConst)
swEdgesHiddenEdgeDisplaySolid: int = 1
swEdgesHiddenEdgeDisplayDashed: int = 2

# swEdgesInContextEditTransparencyType_e (SwConst)
swEdgesInContextEditTransparency_OpaqueAssembly: int = 1
swEdgesInContextEditTransparency_MaintainAssembly: int = 2
swEdgesInContextEditTransparency_ForceAssembly: int = 3

# swEdgesShadedModeDisplay_e (SwConst)
swEdgesShadedModeDisplayNone: int = 1
swEdgesShadedModeDisplayHLR: int = 2
swEdgesShadedModeDisplayWireframe: int = 3

# swEdgesTangentEdgeDisplay_e (SwConst)
swEdgesTangentEdgeDisplayVisible: int = 1
swEdgesTangentEdgeDisplayPhantom: int = 2
swEdgesTangentEdgeDisplayRemoved: int = 3

# swEditBalloonOption_e (SwConst)
swEditBalloonOption_Replace: int = 0
swEditBalloonOption_Resequence: int = 1

# swEditPartCommandStatus_e (SwConst)
swEditPartFailure: int = -1
swEditPartAsmMustBeSaved: int = -2
swEditPartCompMustBeSelected: int = -3
swEditPartCompMustBeResolved: int = -4
swEditPartCompMustHaveWriteAccess: int = -5
swEditPartSuccessful: int = 0
swEditPartCompNotPositioned: int = 1

# swEdrawingSaveAsOption_e (SwConst)
swEdrawingSaveActive: int = 1
swEdrawingSaveAll: int = 2
swEdrawingSaveSelected: int = 3

# swEdrawingsAttachmentOption_e (SwConst)
swEdrawingsAttachNone: int = 0
swEdrawingsAttachActive: int = 1
swEdrawingsAttachAll: int = 2
swEdrawingsAttachSelected: int = 3

# swEdrawingsAttachmentType_e (SwConst)
swAP_Unknown: int = 0
swAP_203: int = 1
swAP_214: int = 2
swAP_242: int = 3

# swElectricalConnectionPointType_e (SwConst)
swElectricalConnectionPoint_Harness: int = 1
swElectricalConnectionPoint_CableOrWire: int = 2
swElectricalConnectionPoint_Conduit: int = 3
swElectricalConnectionPoint_RibbonCable: int = 4
swElectricalConnectionPoint_CableTray: int = 5
swElectricalConnectionPoint_Trunking: int = 6

# swElectricalRouteSubType_e (SWRoutingLib)
swRouteSubType_Harness: int = 0
swRouteSubType_CableWire: int = 1
swRouteSubType_Conduit: int = 2
swRouteSubType_Ribbon: int = 3

# swElectricalStreamType_e (SWRoutingLib)
swAllStreams: int = 0
swFromToListStream: int = 2
swSegmentDataStream: int = 3
swWireListStream: int = 4

# swElectricalSubType_e (SwConst)
swElectricalSubType_ElectricalHarness: int = 0
swElectricalSubType_ElectricalCableWire: int = 1
swElectricalSubType_ElectricalConduit: int = 2
swElectricalSubType_ElectricalStandardCable: int = 3
swElectricalSubType_NotElectrical: int = 20
swElectricalSubType_ElectricalRibbonCable: int = 30

# swEllipsePts_e (SwConst)
swEllipseStartPt: int = 0
swEllipseEndPt: int = 1
swEllipseCenterPt: int = 2
swEllipseMajorPt: int = 3
swEllipseMinorPt: int = 4

# swEndCapThicknessDirection_e (SwConst)
swExtendOutward: int = 1
swExtendInward: int = 2
swSpecifyInset: int = 3

# swEndConditions_e (SwConst)
swEndCondBlind: int = 0
swEndCondThroughAll: int = 1
swEndCondThroughNext: int = 2
swEndCondUpToVertex: int = 3
swEndCondUpToSurface: int = 4
swEndCondOffsetFromSurface: int = 5
swEndCondMidPlane: int = 6
swEndCondUpToBody: int = 7
swEndCondThroughAllBoth: int = 9
swEndCondUpToSelection: int = 10
swEndCondUpToNext: int = 11

# swEndShape_e (SwConst)
swEndShape_DrillPoint: int = 0
swEndShape_FlatBottom: int = 1

# swExcludeFromBOMError_e (SwConst)
swExcludeFromBOM_Fail: int = 0
swExcludeFromBOM_Success: int = 1
swExcludeFromBOM_EnvelopedComponent: int = 2

# swExplodeDirectionIndex_e (SwConst)
swExplodeDirectionIndex_Unknown: int = -1
swExplodeDirectionIndex_XAxis: int = 0
swExplodeDirectionIndex_YAxis: int = 1
swExplodeDirectionIndex_ZAxis: int = 2

# swExportDataFileType_e (SwConst)
swExportPdfData: int = 1

# swExportDataSheetsToExport_e (SwConst)
swExportData_ExportAllSheets: int = 1
swExportData_ExportCurrentSheet: int = 2
swExportData_ExportSpecifiedSheets: int = 3

# swExportFlatPatternViewOptions_e (SwConst)
swExportFlatPatternOption_None: int = 0
swExportFlatPatternOption_RemoveBends: int = 1

# swExportGeomOptions_e (SwConst)
swExportNone: int = -2
swExportGeomAsPoly: int = -1
swExportViewAsBlock: int = 0
swExportTopLevelCompAsBlock: int = 1

# swExportSVPJFileFormatGroupType_e (SwConst)
swExportSVPJGroupType_ByAppearance: int = 0
swExportSVPJGroupType_ByPart: int = 1

# swExportToDWG_e (SwConst)
swExportToDWG_ExportSheetMetal: int = 1
swExportToDWG_ExportSelectedFacesOrLoops: int = 2
swExportToDWG_ExportAnnotationViews: int = 3

# swExportTubeDataReportType_e (SWRoutingLib)
swExportTubeDataReportType_Tangent: int = 1
swExportTubeDataReportType_XYZ: int = 2

# swExternalFileReferencesConfig_e (SwConst)
swExternalFileReferencesConfigNone: int = 0
swExternalFileReferencesCurrentConfig: int = 1
swExternalFileReferencesNamedConfig: int = 2

# swExternalFileReferencesUpdate_e (SwConst)
swExternalFileReferencesUpdateNone: int = 0
swExternalFileReferencesBreakAll: int = 1
swExternalFileReferencesLockAll: int = 2
swExternalFileReferencesunlockAll: int = 3

# swExternalReferenceStatus_e (SwConst)
swExternalReferenceBroken: int = 0
swExternalReferenceLocked: int = 1
swExternalReferenceInContext: int = 3
swExternalReferenceOutOfContext: int = 4
swExternalReferenceDangling: int = 5

# swExternalReferencesUpdateOutOfDateLinkedDesignTable_e (SwConst)
swUpdateDesignTable_Prompt: int = 0
swUpdateDesignTable_Model: int = 1
swUpdateLinkedDesignTable_ExcelFile: int = 2

# swExtrudeFrom_e (SwConst)
swExtrudeFrom_SketchPlane: int = 0
swExtrudeFrom_SurfaceFacePlane: int = 1
swExtrudeFrom_Vertex: int = 2
swExtrudeFrom_Offset: int = 3

# swFMViewNotify_e (SwConst)
swFMViewActivateNotify: int = 1
swFMViewDeactivateNotify: int = 2
swFMViewDestroyNotify: int = 3

# swFaceCoincidentResult_e (SwConst)
swFaceCoincidentUnknownResult: int = -1
swFaceCoincident_True: int = 0
swFaceCoincident_TrueReversed: int = 1
swFaceCoincident_FalseTopology: int = 2
swFaceCoincident_FalseBoundary1: int = 3
swFaceCoincident_FalseBoundary2: int = 4
swFaceCoincident_FalseFace1: int = 5
swFaceCoincident_FalseFace2: int = 6
swFaceCoincident_FalseSurface: int = 7

# swFaceDeleteOption_e (SwConst)
swFaceDelete_Default: int = 0
swFaceDelete_Patch: int = 1
swFaceDelete_Fill: int = 2
swFaceDelete_FillWithTangent: int = 3

# swFaceUntrimType_e (SwConst)
swFaceUntrimTypeAllEdges: int = 0
swFaceUntrimTypeInternalEdges: int = 1
swFaceUntrimTypeExternalEdges: int = 2

# swFamilyTableDimColumnType_e (SwConst)
swFamilyTable_TableControlled: int = 1
swFamilyTable_MarkedForDrawing: int = 2
swFamilyTable_NotMarkedForDrawing: int = 4

# swFamilyTableGetConfigurationCriteria_e (SwConst)
GetAllConfigurationsAvailableNames: int = 0
GetJustEnabledConfigurationNames: int = 1
GetJustVisibleConfigurationNames: int = 2

# swFastenerTableTypes_e (SwConst)
swSizeTable: int = 0
swThreadDataTable: int = 1
swScrewClearancesTable: int = 2

# swFaultEntityErrorCode_e (SwConst)
swBodyCorrupt: int = 1
swBodyInvalidIdentifiers: int = 2
swBodyInsideOut: int = 3
swBodyRegionsInconsistent: int = 4
swEdgeNonPeriodicCurve: int = 5
swEdgeNonPeriodicNomGeom: int = 6
swEdgeVertexNotLie: int = 7
swEdgeVertexNotLieNomGeom: int = 8
swEdgeWrongDir: int = 9
swEdgeWrongDirNomGeom: int = 10
swEdgeSpcurveOutOfTol: int = 11
swEdgeSpcurveOutOfTolNomGeom: int = 12
swEdgeVerticesTouch: int = 13
swEdgeBadFaceOrder: int = 14
swEdgeBadWire: int = 15
swFaceBadVertex: int = 16
swFaceBadEdge: int = 17
swFaceBadEdgeOrder: int = 18
swFaceNoAccomVertex: int = 19
swFaceBadLoops: int = 20
swFaceSelfIntersecting: int = 21
swFaceBadWireframe: int = 22
swFaceCheckerFailure: int = 23
swFaceFaceInconsistency: int = 24
swGeomStateSelfIntersect: int = 25
swGeomDegenerate: int = 26
swRegionBadShells: int = 27
swShellBadTopologyGeometry: int = 28
swShellIntersect: int = 29
swTopolNotG1Continuous: int = 30
swTopolSizeBoxViolation: int = 31
swTopolStateCheckFail: int = 32
swTopolStateNoGeometry: int = 33
swEntityStateInvalid: int = 34
swTopolMissingGeometry: int = 35
swEdgeTouchEdge: int = 36

# swFeatMgrPane_e (SwConst)
swFeatMgrPaneTop: int = 0
swFeatMgrPaneBottom: int = 1
swFeatMgrPaneTopHidden: int = 2
swFeatMgrPaneBottomHidden: int = 3
swFeatMgrPaneFlyout: int = 4

# swFeatureChamferOption_e (SwConst)
swFeatureChamferFlipDirection: int = 1
swFeatureChamferKeepFeature: int = 2
swFeatureChamferTangentPropagation: int = 4
swFeatureChamferPropagateFeatToParts: int = 8

# swFeatureDimensionParameter_e (SwConst)
swPatternSpacing1: int = 1
swPatternInstanceCount1: int = 2
swPatternSpacing2: int = 3
swPatternInstanceCount2: int = 4

# swFeatureEditStatus_e (SwConst)
swFeature_Editable: int = 0
swFeature_NonEditable: int = 1
swFeature_UnderEditing: int = 2

# swFeatureError_e (SwConst)
swFeatureErrorNone: int = 0
swFeatureErrorUnknown: int = 1
swFeatureErrorFilletNoLoop: int = 10
swFeatureErrorFilletNoFace: int = 11
swFeatureErrorFilletInvalidRadius: int = 12
swFeatureErrorFilletNoEdge: int = 13
swFeatureErrorFilletModelGeometry: int = 14
swFeatureErrorFilletRadiusTooSmall: int = 15
swFeatureErrorFilletCannotExtend: int = 16
swFeatureErrorFilletRadiusEliminateElement: int = 17
swFeatureErrorFilletRadiusTooBig: int = 18
swFeatureErrorFilletRadiusTooBig2: int = 19
swFeatureErrorExtrusionDisjoint: int = 30
swFeatureErrorExtrusionNoEndFound: int = 31
swFeatureErrorExtrusionBadGeometricConditions: int = 32
swFeatureErrorExtrusionCutContourOpenAndClosed: int = 33
swFeatureErrorExtrusionCutContourInvalid: int = 34
swFeatureErrorExtrusionOpenCutContourInvalid: int = 35
swFeatureErrorExtrusionBossContourOpenAndClosed: int = 36
swFeatureErrorExtrusionBossContourInvalid: int = 37
swFeatureErrorMateInvalidEdge: int = 38
swFeatureErrorMateInvalidFace: int = 39
swFeatureErrorMateFailedCreatingSurface: int = 40
swFeatureErrorMateInvalidEntity: int = 41
swFeatureErrorMateUnknownTangent: int = 42
swFeatureErrorMateDanglingGeometry: int = 43
swFeatureErrorMateEntityNotLinear: int = 44
swFeatureErrorMateEntityFailed: int = 45
swFeatureErrorMateOverdefined: int = 46
swFeatureErrorMateIlldefined: int = 47
swFeatureErrorMateBroken: int = 48
swFeatureErrorFeatureDeprecated: int = 49
swFeatureErrorFeatureObsolete: int = 50
swSketchErrorExtRefFail: int = 51
swFeatureErrorPartialEdgeFilletNoIntersection: int = 52
swFeatureErrorPartialEdgeFilletUpdateFailed: int = 53
swFeatureErrorPartialEdgeFilletNoPropagateEdges: int = 54
swFeatureErrorPartialEdgeFilletNoStartEdge: int = 55
swFeatureErrorPartialEdgeFilletNoEndEdge: int = 56
swFeatureErrorPartialEdgeFilletNoMainEdge: int = 57
swFeatureErrorPartialEdgeFilletOffsetTooBig: int = 58
swFeatureErrorPartialEdgeFilletNoReferenceEntity: int = 59
swFeatureErrorPartialEdgeFilletTooManyRefEntities: int = 60
swFeatureErrorPartialEdgeFilletInvalidOffsetValue: int = 61
swFeatureErrorPartialEdgeFilletCrossOverEndCondition: int = 62
swFeatureErrorPartialEdgeFilletMissingReferenceEntity: int = 63
swFeatureErrorPartialEdgeFilletInvalidReferenceEntity: int = 64
swFeatureErrorPartialEdgeFilletNotSupported: int = 65
swFeatureErrorPartialEdgeFilletNotSupportedForClosedLoop: int = 66
swFeatureErrorPartialEdgeFilletMultiProjectionPoint: int = 67
swFeatureErrorPartialEdgeFilletFailedToRepair: int = 68
swFeatureErrorSweptFlangeInvalidProfileOrPath: int = 69
swFeatureErrorSweptFlangeSelfIntersectingGeometry: int = 70
swFeatureErrorCutNotIntersectModel: int = 71
swFeatureErrorSketchContainsSelfIntersectingContour: int = 72
swFeatureErrorMissingItemsInFeature: int = 73

# swFeatureFillSurfaceOptions_e (SwConst)
swOptimizeSurface: int = 1
swTryToFormSolid: int = 2
swMergeResult: int = 4
swReverseDirection: int = 8
swReverseSurface: int = 16

# swFeatureFilletOptions_e (SwConst)
swFeatureFilletPropagate: int = 1
swFeatureFilletUniformRadius: int = 2
swFeatureFilletVarRadiusType: int = 4
swFeatureFilletUseHelpPoint: int = 8
swFeatureFilletUseTangentHoldLine: int = 16
swFeatureFilletCornerType: int = 32
swFeatureFilletAttachEdges: int = 64
swFeatureFilletKeepFeatures: int = 128
swFeatureFilletCurvatureContinuous: int = 256
swFeatureFilletConstantWidth: int = 512
swFeatureFilletNoTrimNoAttached: int = 1024
swFeatureFilletReverseFace1Dir: int = 2048
swFeatureFilletReverseFace2Dir: int = 4096
swFeatureFilletPropagateFeatToParts: int = 8192
swFeatureFilletAsymmetric: int = 16384

# swFeatureFilletProfileType_e (SwConst)
swFeatureFilletCircular: int = 0
swFeatureFilletConicRho: int = 1
swFeatureFilletConicRadius: int = 2
swFeatureFilletConicRhoZeroChamfer: int = 3

# swFeatureFilletType_e (SwConst)
swFeatureFilletType_Simple: int = 0
swFeatureFilletType_VariableRadius: int = 1
swFeatureFilletType_Face: int = 2
swFeatureFilletType_FullRound: int = 3

# swFeatureManagerDisplayWarnings_e (SwConst)
swFeatureManagerDisplayAllWarnings: int = 0
swFeatureManagerDisplayNoWarnings: int = 1
swFeatureManagerDisplayWarningsExceptTopLevel: int = 2

# swFeatureManagerTreeViewCADFamily_e (SwConst)
swFeatureManagerTreeViewCADFamily_CADFamilyOnly: int = 0
swFeatureManagerTreeViewCADFamily_CADFamilyAndConfiguration: int = 1

# swFeatureModifier_e (SwConst)
swGeometricFeatureModifier_None: int = 0
swGeometricFeatureModifier_MaximumMaterialCondition: int = 1
swGeometricFeatureModifier_LeastMaterialCondition: int = 2
swGeometricFeatureModifier_ProjectedTolerance: int = 3
swGeometricFeatureModifier_TangentPlane: int = 4
swGeometricFeatureModifier_FreeState: int = 5
swGeometricFeatureModifier_ToleranceAsDiameter: int = 6
swGeometricFeatureModifier_Unknown: int = 7

# swFeatureNameID_e (SwConst)
swFmChamfer: int = 0
swFmFillet: int = 1
swFmCavity: int = 2
swFmDraft: int = 3
swFmMirrorSolid: int = 4
swFmCirPattern: int = 5
swFmLPattern: int = 6
swFmMirrorPattern: int = 7
swFmShell: int = 8
swFmBlend: int = 9
swFmBlendCut: int = 10
swFmExtrusion: int = 11
swFmBoss: int = 12
swFmCut: int = 13
swFmRefCurve: int = 14
swFmRevolution: int = 15
swFmRevCut: int = 16
swFmSweep: int = 17
swFmSweepCut: int = 18
swFmStock: int = 19
swFmSurfCut: int = 20
swFmThicken: int = 21
swFmThickenCut: int = 22
swFmVarFillet: int = 23
swFmSketchHole: int = 24
swFmHoleWzd: int = 25
swFmImported: int = 26
swFmBaseBody: int = 27
swFmDerivedLPattern: int = 28
swFmCosmeticThread: int = 29
swFmSheetMetal: int = 30
swFmFlattenBends: int = 31
swFmProcessBends: int = 32
swFmOneBend: int = 33
swFmBaseFlange: int = 34
swFmSketchBend: int = 35
swFmSM3dBend: int = 36
swFmEdgeFlange: int = 37
swFmFlatPattern: int = 38
swFmCenterMark: int = 39
swFmDrSheet: int = 40
swFmAbsoluteView: int = 41
swFmDetailView: int = 42
swFmRelativeView: int = 43
swFmSectionPartView: int = 44
swFmSectionAssemView: int = 45
swFmUnfoldedView: int = 46
swFmAuxiliaryView: int = 47
swFmDetailCircle: int = 48
swFmDrSectionLine: int = 49
swFmBomTableFeature: int = 50
swFmHoleTableFeature: int = 51
swFmRevisionTableFeature: int = 52
swFmMateCoincident: int = 53
swFmMateConcentric: int = 54
swFmMateDistanceDim: int = 55
swFmMateParallel: int = 56
swFmMateTangent: int = 57
swFmReference: int = 58
swFmRefPlane: int = 59
swFmRefAxis: int = 60
swFmReferenceCurve: int = 61
swFmRefSurface: int = 62
swFmCoordinateSystem: int = 63
swFmAttribute: int = 64
swFmProfileFeature: int = 65
swFmFeatureFolder: int = 66
swFmSurfaceBodyFolder: int = 67
swFmSolidBodyFolder: int = 68
swFmLibraryFeature: int = 69
swFmBreakCorner: int = 70
swFmCornerTrim: int = 71
swFmWeldMemberFeat: int = 72
swFmFormToolInstance: int = 73
swFmAEMGravity: int = 74
swFmAEMLinearForce: int = 75
swFmAEMTorque: int = 76
swFmAEMLinearMotor: int = 77
swFmAEMRotationalMotor: int = 78
swFmAEMLinearSpring: int = 79
swFmAEMTorsionalSpring: int = 80
swFmAEMLinearMotionSpring: int = 81
swFmAEMTorsionalMotionSpring: int = 82
swFmAEMLinearDamper: int = 83
swFmAEMTorsionalDamper: int = 84
swFmAEM3DContact: int = 85
swFmCrossBreak: int = 86
swFmSweepThread: int = 87
swFmTabAndSlot: int = 88
swFmMatePerpendicular: int = 89
swFmMateLock: int = 90
swFmMateCamTangent: int = 91
swFmMateSlot: int = 92
swFmMatePlanarAngleDim: int = 93
swFmMateHinge: int = 94
swFmMateRackPinionDim: int = 95
swFmMateGearDim: int = 96
swFmMateScrew: int = 97
swFmMateUniversalJoint: int = 98
swFmMateSymmetric: int = 99
swFmMateWidth: int = 100
swFmMateProfileCenter: int = 101
swFmMateLinearCoupler: int = 102
swFmCurvePattern: int = 103
swFmSketchPattern: int = 104
swFmFillPattern: int = 105
swFmTablePattern: int = 106
swFmDimPattern: int = 107
swFmLocalLPattern: int = 108
swFmLocalCirPattern: int = 109
swFmLocalCurvePattern: int = 110
swFmLocalSketchPattern: int = 111
swFmLocalChainPattern: int = 112
swFmGroundPlane: int = 113
swFmBoundingBox: int = 114
swFmNormalCut: int = 115
swFmMirrorComponent: int = 116
swFmSweptFlange: int = 117
swFmSMGusset: int = 118
swFmBeltAndChain: int = 119
swFmCornerRelief: int = 120
swFmStrctSysFeat: int = 121
swFmStrctSysGrpFeat: int = 122
swFmStrctSysMbrFeat: int = 123
swFmStrctSysCnrMgmtFeat: int = 124
swFmStrctSysCnrGrpFeat: int = 125
swFmStrctSysCnrFeat: int = 126
swFmMateController: int = 127
swFmSolidToSheetMetal: int = 128
swFmFamilyTableFeature: int = 129

# swFeatureScope_e (SwConst)
swFeatureScope_AllBodies: int = 0
swFeatureScope_SelectedBodiesWithAutoSelect: int = 1
swFeatureScope_SelectedBodiesWithOutAutoSelect: int = 2

# swFeatureSuppressionAction_e (SwConst)
swSuppressFeature: int = 0
swUnSuppressFeature: int = 1
swUnSuppressDependent: int = 2

# swFeatureTreeFolderType_e (SwConst)
swFeatureTreeFolder_EmptyBefore: int = 1
swFeatureTreeFolder_Containing: int = 2
swFeatureTreeFolder_Mold: int = 3

# swFeatureTreeState_e (SwConst)
swFlyoutFeatureTree_Hidden: int = 0
swFlyoutFeatureTree_ShownUnExpanded: int = 1
swFlyoutFeatureTree_ShownExpanded: int = 2

# swFeaturesToPatternType_e (SwConst)
swFeaturesToPatternSelectedFeatures: int = 0
swFeaturesToPatternCreateSeedCut: int = 1

# swFileCloseNotifyReason_e (SwConst)
swFileCloseNotifyReason_Unknown: int = 0
swFileCloseNotifyReason_CloseForReload: int = 1

# swFileFormatType_e (SwConst)
swFileFormatType_STEP: int = 0
swFileFormatType_STEP_ED1: int = 1
swFileFormatType_STEP_ED2: int = 2
swFileFormatType_STEP_ED3: int = 3

# swFileLoadError_e (SwConst)
swGenericError: int = 1
swFileNotFoundError: int = 2
swIdMatchError: int = 4
swReadOnlyWarn: int = 8
swSharingViolationWarn: int = 16
swDrawingANSIUpdateWarn: int = 32
swSheetScaleUpdateWarn: int = 64
swNeedsRegenWarn: int = 128
swBasePartNotLoadedWarn: int = 256
swFileAlreadyOpenWarn: int = 512
swInvalidFileTypeError: int = 1024
swDrawingsOnlyRapidDraftWarn: int = 2048
swViewOnlyRestrictions: int = 4096
swFutureVersion: int = 8192
swViewMissingReferencedConfig: int = 16384
swDrawingSFSymbolConvertWarn: int = 32768
swFileWithSameTitleAlreadyOpen: int = 65536
swLiquidMachineDoc: int = 131072
swLowResourcesError: int = 262144
swNoDisplayData: int = 524288
swAddinInteruptError: int = 1048576
swFileRequiresRepairError: int = 2097152
swFileCriticalDataRepairError: int = 4194304
swApplicationBusy: int = 8388608
swConnectedIsOffline: int = 16777216

# swFileLoadWarning_e (SwConst)
swFileLoadWarning_IdMismatch: int = 1
swFileLoadWarning_ReadOnly: int = 2
swFileLoadWarning_SharingViolation: int = 4
swFileLoadWarning_DrawingANSIUpdate: int = 8
swFileLoadWarning_SheetScaleUpdate: int = 16
swFileLoadWarning_NeedsRegen: int = 32
swFileLoadWarning_BasePartNotLoaded: int = 64
swFileLoadWarning_AlreadyOpen: int = 128
swFileLoadWarning_DrawingsOnlyRapidDraft: int = 256
swFileLoadWarning_ViewOnlyRestrictions: int = 512
swFileLoadWarning_ViewMissingReferencedConfig: int = 1024
swFileLoadWarning_DrawingSFSymbolConvert: int = 2048
swFileLoadWarning_RevolveDimTolerance: int = 4096
swFileLoadWarning_ModelOutOfDate: int = 8192
swFileLoadWarning_DimensionsReferencedIncorrectlyToModels: int = 16384
swFileLoadWarning_ComponentMissingReferencedConfig: int = 32768
swFileLoadWarning_InvisibleDoc_LinkedDesignTableUpdateFail: int = 65536
swFileLoadWarning_MissingDesignTable: int = 131072
swFileLoadWarning_AutomaticRepair: int = 262144
swFileLoadWarning_CriticalDataRepair: int = 524288
swFileLoadWarning_MissingExternalReferences: int = 1048576

# swFileSaveError_e (SwConst)
swGenericSaveError: int = 1
swReadOnlySaveError: int = 2
swFileNameEmpty: int = 4
swFileNameContainsAtSign: int = 8
swFileLockError: int = 16
swFileSaveFormatNotAvailable: int = 32
swFileSaveWithRebuildError: int = 64
swFileSaveAsDoNotOverwrite: int = 128
swFileSaveAsInvalidFileExtension: int = 256
swFileSaveAsNoSelection: int = 512
swFileSaveAsBadEDrawingsVersion: int = 1024
swFileSaveAsNameExceedsMaxPathLength: int = 2048
swFileSaveAsNotSupported: int = 4096
swFileSaveRequiresSavingReferences: int = 8192
swFileSaveAsDetachedDrawingsNotSupported: int = 16384
swFileSaveDoNotUpgradeError: int = 32768
swFileSaveIncompatibleItemsError: int = 65536

# swFileSaveTo3DExperienceError_e (SwConst)
swFileSaveTo3DExperienceError_swGenericError: int = 1
swFileSaveTo3DExperienceError_swConnectedIsOffline: int = 2
swFileSaveTo3DExperienceError_swFileAlreadyExists: int = 3

# swFileSaveTypes_e (SwConst)
swFileSave: int = 1
swFileSaveAs: int = 2
swFileSaveAsCopy: int = 3
swFileSaveAsCopyAndOpen: int = 4

# swFileSaveWarning_e (SwConst)
swFileSaveWarning_RebuildError: int = 1
swFileSaveWarning_NeedsRebuild: int = 2
swFileSaveWarning_ViewsNeedUpdate: int = 4
swFileSaveWarning_AnimatorNeedToSolve: int = 8
swFileSaveWarning_AnimatorFeatureEdits: int = 16
swFileSaveWarning_EdrwingsBadSelection: int = 32
swFileSaveWarning_AnimatorLightEdits: int = 64
swFileSaveWarning_AnimatorCameraViews: int = 128
swFileSaveWarning_AnimatorSectionViews: int = 256
swFileSaveWarning_MissingOLEObjects: int = 512
swFileSaveWarning_OpenedViewOnly: int = 1024
swFileSaveWarning_XmlInvalid: int = 2048

# swFilletOverFlowType_e (SwConst)
swFilletOverFlowType_Default: int = 0
swFilletOverFlowType_KeepEdge: int = 1
swFilletOverFlowType_KeepSurface: int = 2

# swFitTolDisplay_e (SwConst)
swFitTolDisplay_StackedWithLine: int = 1
swFitTolDisplay_Stacked: int = 2
swFitTolDisplay_Linear: int = 3

# swFitType_e (SwConst)
swFitUSER: int = 0
swFitCLEARANCE: int = 1
swFitTRANSITIONAL: int = 2
swFitPRESS: int = 3

# swFlangeDimTypes_e (SwConst)
swFlangeDimTypeOuterVirtualSharp: int = 1
swFlangeDimTypeInnerVirtualSharp: int = 2
swFlangeDimTypeBendTangentArc: int = 3

# swFlangeOffsetTypes_e (SwConst)
swFlangeOffsetBlind: int = 1
swFlangeOffsetUpToVertex: int = 2
swFlangeOffsetUpToSurface: int = 3
swFlangeOffsetFromSurface: int = 4
swFlangeOffsetMidPlane: int = 5
swFlangeOffsetUptoEdgeAndMerge: int = 6

# swFlangePositionTypes_e (SwConst)
swFlangePositionTypeMaterialInside: int = 1
swFlangePositionTypeMaterialOutside: int = 2
swFlangePositionTypeBendOutside: int = 3
swFlangePositionTypeBendCenterLine: int = 4
swFlangePositionTypeBendSharp: int = 5
swFlangePositionTypeBendTangent: int = 6

# swFlattenRouteErrorType_e (SWRoutingLib)
swNeedsToSaveVirtualComponentError: int = 1
swProblemInRouteAssemblyError: int = 2
swDuplicateComponentError: int = 3
swRouteAssemblyNotSelected: int = 4
swFlattenRouteNoError: int = 5

# swForceUpdateElectricalDataError_e (SWRoutingLib)
swForceUpdateElectricalData_Success: int = 0
swForceUpdateElectricalData_IncorrectStreamInput: int = 1
swForceUpdateElectricalData_IsNotARouteAssembly: int = 2
swForceUpdateElectricalData_BadStreamData: int = 3
swForceUpdateElectricalData_RouteInEditMode: int = 4

# swFractionDisplay_e (SwConst)
swNONE: int = 0
swDECIMAL: int = 1
swFRACTION: int = 2

# swGTolTextParts_e (SwConst)
swGTolTextPrefix: int = 1
swGTolTextSuffix: int = 2
swGTolTextCalloutAbove: int = 3
swGTolTextCalloutBelow: int = 4

# swGeneralImportFreePointCurveEntityOptions_e (SwConst)
swGeneralImportAsSketches: int = 0
swGeneralImportAs3dCurves: int = 1

# swGeneralImportSurfaceSolidEntityOptions_e (SwConst)
swGeneralImportTryFormingSolids: int = 0
swGeneralImportKnitSurfaces: int = 1
swGeneralImportDoNotKnit: int = 2
swGeneralImportByBrep: int = 3

# swGeneralImportUnitsOptions_e (SwConst)
swGeneralImportFileSpecifiedUnit: int = 0
swGeneralImportDocumentTemplateSpeciedUnit: int = 1

# swGeomType_e (SwConst)
swPOINT: int = 0
swLINE: int = 1
swARC: int = 2
swSPLINECURVE: int = 3
swELLIPSE: int = 4
swTEXT: int = 5
swHATCH: int = 6
swPARABOLA: int = 7
sw3DPLANE: int = 8
sw3DCYLINDER: int = 9
sw3DSPHERE: int = 10
sw3DPARAMETRICSURFACE: int = 11
swDIM: int = 12
swSUBSKETCH: int = 13
swINVALIDGTYPE: int = 99

# swGeometricCharacteristic_e (SwConst)
swGeometricCharacteristic_None: int = 0
swGeometricCharacteristic_Unknown: int = 1
swGeometricCharacteristic_Straightness: int = 2
swGeometricCharacteristic_Flatness: int = 3
swGeometricCharacteristic_Circularity: int = 4
swGeometricCharacteristic_Cylindricity: int = 5
swGeometricCharacteristic_LineProfile: int = 6
swGeometricCharacteristic_SurfaceProfile: int = 7
swGeometricCharacteristic_Angularity: int = 8
swGeometricCharacteristic_Parallelism: int = 9
swGeometricCharacteristic_Perpendicularity: int = 10
swGeometricCharacteristic_Position: int = 11
swGeometricCharacteristic_Concentricity: int = 12
swGeometricCharacteristic_Symmetry: int = 13
swGeometricCharacteristic_CircularRunout: int = 14
swGeometricCharacteristic_TotalRunout: int = 15

# swGeometryToSave_e (SwConst)
swGeometryToSave_AllComponents: int = 0
swGeometryToSave_ExteriorFaces: int = 1
swGeometryToSave_IncludeSpecificComponents: int = 2

# swGetOpenFileNameOptions_e (SwConst)
swGetOpenFileNameOptions_Silent: int = 1
swGetOpenFileNameOptions_ReadOnly: int = 2
swGetOpenFileNameOptions_ViewOnly: int = 4
swGetOpenFileNameOptions_RapidDraft: int = 8
swGetOpenFileNameOptions_LoadModel: int = 16
swGetOpenFileNameOptions_AutoMissingConfig: int = 32
swGetOpenFileNameOptions_OverrideDefaultLoadLightweight: int = 64
swGetOpenFileNameOptions_LoadLightweight: int = 128
swGetOpenFileNameOptions_DontLoadHiddenComponents: int = 256
swGetOpenFileNameOptions_LoadExternalReferencesInMemory: int = 512
swGetOpenFileNameOptions_OpenDetailingMode: int = 1024
swGetOpenFileNameOptions_LDR_EditAssembly: int = 2048
swGetOpenFileNameOptions_SpeedPak: int = 4096
swGetOpenFileNameOptions_AdvancedConfig: int = 8192
swGetOpenFileNameOptions_UseLargeAssemblySettings: int = 16384
swGetOpenFileNameOptions_SelectedSheets: int = 32768

# swGlobalBBoxLWTADirectionType_e (SwConst)
swBBox_LWTADir_Unspecified: int = 0
swBBox_LWTDir_XYZ: int = 1
swBBox_LWTDir_YXZ: int = 2
swBBox_LWTDir_YZX: int = 3
swBBox_LWTDir_ZYX: int = 4
swBBox_LWTDir_ZXY: int = 5
swBBox_LWTDir_XZY: int = 6
swBBox_AxisDir_X: int = 7
swBBox_AxisDir_Y: int = 8
swBBox_AxisDir_Z: int = 9

# swGlobalBoundingBoxFitOptions_e (SwConst)
swBoundingBoxType_BestFit: int = 1
swBoundingBoxType_CustomPlane: int = 2
swBoundingBoxType_CustomCoordSys: int = 3

# swGlobalBoundingBoxResult_e (SwConst)
swGlobalBoundingBoxResult_Success: int = 0
swGlobalBoundingBoxResult_NoValidBodiesFound: int = 1
swGlobalBoundingBoxResult_NonPlanarFaceSelected: int = 2

# swGtolDecimalSeparatorType_e (SwConst)
swGeometricTolerance_Decimal_Separator_Period: int = 0
swGeometricTolerance_Decimal_Separator_Comma: int = 1

# swGtolFormatConversionError_e (SwConst)
swGtolFormatConversionFail: int = 1

# swGtolFormatSchemaVersion_e (SwConst)
swGtolFormatSchemaVersion_SW2023: int = 1

# swGtolFormatType_e (SwConst)
GTOL_SW2021: int = 1
GTOL_SW2022: int = 2

# swGtolGeomCharSymbol_e (SwConst)
swGcsNONE: int = 12
swGcsSYMMETRY: int = 13
swGcsSTRAIGHT: int = 14
swGcsFLAT: int = 15
swGcsROUND: int = 16
swGcsCYL: int = 17
swGcsLINEPROF: int = 18
swGcsSURFPROF: int = 19
swGcsANG: int = 20
swGcsPERP: int = 21
swGcsPARALLEL: int = 22
swGcsPOSITION: int = 23
swGcsCONC: int = 24
swGcsCIRCRUNOUT: int = 25
swGcsTOTALRUNOUT: int = 26
swGcsCIRCOPENRUNOUT: int = 27
swGcsTOTALOPENRUNOUT: int = 28
swGcsUBUTTON: int = 29
swGcsSQUARE: int = 30

# swGtolIndicatorBorderType_e (SwConst)
swGtolIndicatorBorderType_OrientationPlane: int = 0
swGtolIndicatorBorderType_IntersectionPlane: int = 1
swGtolIndicatorBorderType_CollectionPlane: int = 2
swGtolIndicatorBorderType_DirectionFeature: int = 3

# swGtolMatCondition_e (SwConst)
swMcNONE: int = 0
swMcMMC: int = 1
swMcRFS: int = 2
swMcLMC: int = 3
swMsNONE: int = 4
swMsPROJTOLZONE: int = 5
swMsDIA: int = 6
swMsSPHDIA: int = 7
swMsRAD: int = 8
swMsSPHRAD: int = 9
swMsREF: int = 10
swMsARCLEN: int = 11

# swGtolTolType_e (SwConst)
swGtolTolType_None: int = 0
swGtolTolType_Unknown: int = 1
swGtolTolType_ProjectedTolerance: int = 2
swGtolTolType_Square: int = 3
swGtolTolType_UnequallyDisposedProfile: int = 4
swGtolTolType_MAX: int = 5

# swGuideCurveInfluence_e (SwConst)
swGuideCurveInfluenceNextGuide: int = 0
swGuideCurveInfluenceNextSharp: int = 1
swGuideCurveInfluenceNextEdge: int = 2
swGuideCurveInfluenceNextGlobal: int = 3

# swGussetProfileLocationType_e (SwConst)
swGussetProfileLocationStart: int = 0
swGussetProfileLocationCenter: int = 1
swGussetProfileLocationEnd: int = 2

# swGussetProfileType_e (SwConst)
swGussetProfilePolygon: int = 0
swGussetProfileTriangle: int = 1

# swGussetThicknessType_e (SwConst)
swGussetThicknessInner: int = 0
swGussetThicknessBothSides: int = 1
swGussetThicknessOuter: int = 2

# swHandleActiveXCreationFailure_e (SwConst)
swHandleActiveXCreationFailure_Cancel: int = 1
swHandleActiveXCreationFailure_Retry: int = 2
swHandleActiveXCreationFailure_Continue: int = 3

# swHandleWindowFromHandleCreationFailure_e (SwConst)
swHandleWindowFromHandleCreationFailure_Cancel: int = 1
swHandleWindowFromHandleCreationFailure_Retry: int = 2
swHandleWindowFromHandleCreationFailure_Continue: int = 3

# swHealActionType_e (SwConst)
swHealAction_Shrink: int = 0
swHealAction_GrowParent: int = 1
swHealAction_Cap: int = 2

# swHelixDefinedBy_e (SwConst)
swHelixDefinedByPitchAndRevolution: int = 0
swHelixDefinedByHeightAndRevolution: int = 1
swHelixDefinedByHeightAndPitch: int = 2
swHelixDefinedBySpiral: int = 3

# swHemPositionTypes_e (SwConst)
swHemPositionTypeInside: int = 0
swHemPositionTypeOutside: int = 1

# swHemTypes_e (SwConst)
swHemTypeOpen: int = 0
swHemTypeClosed: int = 1
swHemTypeTearDrop: int = 2
swHemTypeRolled: int = 3
swHemTypeDouble: int = 4

# swHingeMateEntityType_e (SwConst)
swHingeMateEntityType_Concentric: int = 0
swHingeMateEntityType_Coincident: int = 1
swHingeMateEntityType_Angle: int = 2

# swHlrQuality_e (SwConst)
swPreciseHlr: int = 0
swFastHlr: int = 1

# swHoleElementOrientation_e (SwConst)
swHoleElementOrientation_Nearside: int = 0
swHoleElementOrientation_Farside: int = 1

# swHoleSeriesWhichParts_e (SwConst)
swHoleSeriesFirstPart: int = 0
swHoleSeriesMiddleParts: int = 1
swHoleSeriesLastPart: int = 2

# swHoleTableTagOrder_e (SwConst)
swHoleTableTagOrder_XY: int = 1
swHoleTableTagOrder_ReduceToolPath: int = 2
swHoleTableTagOrder_Radial: int = 3

# swHoleTableTagPrefixApply_e (SwConst)
swHoleTableTagPrefixApply_AllHolesOfSameSize: int = 1
swHoleTableTagPrefixOption_OnlySpecifiedHole: int = 2

# swHoleTableTagStyle_e (SwConst)
swHoleTable_AlphaNumericTags: int = 1
swHoleTable_NumericTags: int = 2
swHoleTable_ManualTags: int = 3

# swHorizontalAutoSplitApply_e (SwConst)
swHorizontalAutoSplitApply_ThisTimeOnly: int = 0
swHorizontalAutoSplitApply_Continuousely: int = 1

# swHorizontalAutoSplitPlacementOfSplitTable_e (SwConst)
swHorizontalAutoSplitPlacementOfSplitTable_NextToLastSplit: int = 0
swHorizontalAutoSplitPlacementOfSplitTable_BelowLastSplit: int = 1

# swIFCExportSaveType_e (SwConst)
swIFCExportSaveType_BREP: int = 0
swIFCExportSaveType_BREPAndTessellation: int = 1
swIFCExportSaveType_Tessellation: int = 2

# swIFCOmniUniClassPreference_e (SwConst)
swIFCSaveAsOmniClass: int = 0
swIFCSaveAsUniClass2: int = 1

# swIGESCurveRepresentation_e (SwConst)
swIGES_CURVES_BSPLINE: int = 0
swIGES_CURVES_PSPLINE: int = 1

# swIGESPreferredSystem_e (SwConst)
swIGES_STANDARD: int = 0
swIGES_NURBS: int = 1
swIGES_ANSYS: int = 2
swIGES_COSMOS: int = 3
swIGES_MASCAM: int = 4
swIGES_SURFCAM: int = 5
swIGES_SMARTCAM: int = 6
swIGES_TEKSOFT: int = 7
swIGES_ALPHACAM: int = 8
swIGES_MULTICAM: int = 9
swIGES_ALIAS: int = 10

# swIGESRepresentation_e (SwConst)
swIGES_TRMSRF: int = 0
swIGES_CURVES: int = 1
swIGES_TRMSRFANDCURVES: int = 2
swIGES_BREP: int = 3
swIGES_BOUNDEDSRF: int = 4

# swImageQualityShaded_e (SwConst)
swShadedImageQualityCoarse: int = 1
swShadedImageQualityFine: int = 2
swShadedImageQualityCustom: int = 3

# swImageQualityWireframe_e (SwConst)
swWireframeImageQualityOptimal: int = 1
swWireframeImageQualityCustom: int = 2

# swImageSizeToUse_e (SwConst)
swImageSizeToUse_20x20: int = 20
swImageSizeToUse_32x32: int = 32
swImageSizeToUse_40x40: int = 40
swImageSizeToUse_64x64: int = 64
swImageSizeToUse_96x96: int = 96
swImageSizeToUse_128x128: int = 128

# swImportDxfDwg_ImportMethod_e (SwConst)
swImportDxfDwg_DoNotImportSheet: int = 0
swImportDxfDwg_ImportToDrawing: int = 1
swImportDxfDwg_ImportToPartSketch: int = 2
swImportDxfDwg_ImportToExistingDrawing: int = 3
swImportDxfDwg_ImportToExistingPart: int = 4

# swImportDxfDwg_LayerVisibility_e (SwConst)
swImportDxfDwg_LayerMaintain: int = 0
swImportDxfDwg_LayerVisible: int = 1
swImportDxfDwg_LayerHidden: int = 2

# swImportModelItemsSource_e (SwConst)
swImportModelItemsFromEntireModel: int = 0
swImportModelItemsFromSelectedFeature: int = 1
swImportModelItemsFromSelectedComponent: int = 2
swImportModelItemsFromAssemblyOnly: int = 3

# swImportNeutralAssemblyStructureMapping_e (SwConst)
swImportNeutralAssemblyStructureMapping_Default: int = 0
swImportNeutralAssemblyStructureMapping_MultipleParts: int = 1
swImportNeutralAssemblyStructureMapping_MultibodyPart: int = 2

# swImportNeutralCurvesAndPointsOptions_e (SwConst)
swImportNeutralCurvesAndPointsOptions_AsSketches: int = 0
swImportNeutralCurvesAndPointsOptions_As3DCurves: int = 1

# swImportNeutralKnitOption_e (SwConst)
swImportNeutralKnitOption_FormSolids: int = 0
swImportNeutralKnitOption_DoNotKnit: int = 1

# swImportNeutralUnits_e (SwConst)
swImportNeutralUnits_ImportFileUnits: int = 0
swImportNeutralUnits_TemplateUnits: int = 1

# swImportPartCustomPropertiesToOptions_e (SwConst)
swImportPropertiesToFileProperties: int = 1
swImportPropertiesToCutlistProperties: int = 2
swImportPartCustomPropertiesNone: int = 3

# swImportSheetMetalInformation_e (SwConst)
swImportWithUnlockedProperties: int = 1
swImportWithoutUnlockedProperties: int = 2
swImportUnlockedPropertiesNone: int = 3

# swImportStlVrmlModelType_e (SwConst)
swImportStlVrmlModelType_Graphics: int = 0
swImportStlVrmlModelType_Surface: int = 1
swImportStlVrmlModelType_Solid: int = 2

# swImprintingFacesOpts_e (SwConst)
swImprintingFacesOnTool: int = 1
swImprintingFacesOnOverlapping: int = 2
swImprintingFacesOnExtendFace: int = 4

# swInConfigurationOpts_e (SwConst)
swConfigPropertySuppressFeatures: int = 0
swThisConfiguration: int = 1
swAllConfiguration: int = 2
swSpecifyConfiguration: int = 3
swLinkedToParent: int = 4
swSpeedpakConfiguration: int = 5

# swInContextEditTransparencyType_e (SwConst)
swInContextEditTransparencyOpaque: int = 0
swInContextEditTransparencyForce: int = 1
swInContextEditTransparencyMaintain: int = 2

# swIndentSelectionState_e (SwConst)
swIndentSelectionStateKeepSelection: int = 0
swIndentSelectionStateRemoveSelection: int = 1

# swInsertAnnotation_e (SwConst)
swInsertCThreads: int = 1
swInsertDatums: int = 2
swInsertDatumTargets: int = 4
swInsertDimensions: int = 8
swInsertInstanceCounts: int = 16
swInsertGTols: int = 32
swInsertNotes: int = 64
swInsertSFSymbols: int = 128
swInsertWelds: int = 256
swInsertAxes: int = 512
swInsertCurves: int = 1024
swInsertPlanes: int = 2048
swInsertSurfaces: int = 4096
swInsertPoints: int = 8192
swInsertOrigins: int = 16384
swInsertDimensionsMarkedForDrawing: int = 32768
swInsertHoleWizardProfileDimensions: int = 65536
swInsertHoleWizardLocationDimensions: int = 131072
swInsertRefPoints: int = 262144
swInsertDimensionsNotMarkedForDrawing: int = 524288
swInsertholeCallout: int = 1048576
swInsertWeldBeads: int = 2097152
swInsertSketches: int = 4194304
swInsertWeldBeads_ET: int = 8388608
swInsertTolerancedDims: int = 16777216
swInsertCenterOfMass: int = 33554432

# swInsertAssyOptions_e (SwConst)
swInsertAssySurfaceBodies: int = 1
swInsertAssyMaterials: int = 2
swInsertAssyRefPlanes: int = 4
swInsertAssyRefAxes: int = 8
swInsertAssyCoordinateSystems: int = 16
swInsertAssyCosmeticThreads: int = 32
swInsertAssyVisualProperties: int = 64
swInsertAssySketches: int = 128
swInsertAssyCustomProperties: int = 256
swInsertAssyHoleWizardData: int = 512
swInsertAssyGraphicsBodies: int = 1024
swInsertAssyPartCutListProps: int = 2048

# swInsertEdgeFlangeOptions_e (SwConst)
swInsertEdgeFlangeUseDefaultRadius: int = 1
swInsertEdgeFlangeFlipDir: int = 2
swInsertEdgeFlangeDoOffset: int = 4
swInsertEdgeFlangeReverseOffsetDir: int = 8
swInsertEdgeFlangeTearClip: int = 16
swInsertEdgeFlangeTrimSideBend: int = 32
swInsertEdgeFlangeUseReliefRatio: int = 64
swInsertEdgeFlangeUseDefaultRelief: int = 128

# swInsertNewAssemblyErrorCode_e (SwConst)
swInsertNewAssemblyError_ErrorUknown: int = 0
swInsertNewAssemblyError_NoError: int = 1
swInsertNewAssemblyError_FilePathEmpty: int = 2
swInsertNewAssemblyError_FileAlreadyExists: int = 3
swInsertNewAssemblyError_FolderDoesNotExist: int = 4
swInsertNewAssemblyError_ExtensionNotSldAsm: int = 5

# swInsertNewPartErrorCode_e (SwConst)
swInsertNewPartError_ErrorUknown: int = 0
swInsertNewPartError_NoError: int = 1
swInsertNewPartError_FilePathEmpty: int = 2
swInsertNewPartError_FileAlreadyExists: int = 3
swInsertNewPartError_FolderDoesNotExist: int = 4
swInsertNewPartError_ExtensionNotSldPrt: int = 5
swInsertNewPartError_NotAFaceOrPlane: int = 6
swInsertNewPartError_CannotSelectFaceOrPlane: int = 7

# swInsertOptions_e (SwConst)
swInsertOption_BeforeSelectedSheet: int = 0
swInsertOption_AfterSelectedSheet: int = 1
swInsertOption_MoveToEnd: int = 2

# swInsertPartOptions_e (SwConst)
swInsertPartImportSolids: int = 1
swInsertPartImportSurfaces: int = 2
swInsertPartImportAxes: int = 4
swInsertPartImportPlanes: int = 8
swInsertPartImportCosmeticThreads: int = 16
swInsertPartImportAbsorbedSketchs: int = 32
swInsertPartImportUnabsorbedSketchs: int = 64
swInsertPartImportCustomProperties: int = 128
swInsertPartImportCoordinateSystem: int = 256
swInsertPartBreakLink: int = 512
swInsertPartImportModelDimensions: int = 1024
swInsertPartImportCutListProperties: int = 2048
swInsertPartImportHoleWzdData: int = 4096
swInsertPartImportSMInfo: int = 8192
swInsertPartImportIndProps: int = 16384
swInsertPartImportCustomToFileProperties: int = 32768
swInsertPartImportCustomToCutlistProperties: int = 65536
swInsertPartImportDimXpertAnnotations: int = 131072
swInsertPartDontZoomAll: int = 262144
swInsertPartImportMaterial: int = 524288
swInsertPartImportPropagateVisualPropertiesFromOriginalPart: int = 1048576
swInsertPartImportPoints: int = 2097152
swInsertPartImportPartMaterial: int = 4194304
swInsertPartImportGraphicBodies: int = 8388608

# swInsertSlicingError_e (SwConst)
swInsertSlicingError_NoError: int = 0
swInsertSlicingError_GenericError: int = 1
swInsertSlicingError_InvalidTotalAngle: int = 2
swInsertSlicingError_InvalidSlicesToGenerateOption: int = 4
swInsertSlicingError_InvalidSlicingPlaneEntities: int = 8
swInsertSlicingError_EntitiesCannotFormPlane: int = 16
swInsertSlicingError_NoBodiesInsideBox: int = 32
swInsertSlicingError_InvalidSlicingData: int = 64
swInsertSlicingError_InvalidNumberOfPlanes: int = 128

# swInsertTableColumnWidthStyle_e (SwConst)
swInsertColumn_DefaultWidth: int = 0
swInsertColumn_SingleLineTight: int = 1
swInsertColumn_MultilineTight: int = 2

# swInstanceToVaryModificationType_e (SwConst)
swInstanceToVaryModificationType_D1Spacing: int = 1
swInstanceToVaryModificationType_D2Spacing: int = 2
swInstanceToVaryModificationType_Dimensions: int = 3

# swInterfaceBrightnessColor_e (SwConst)
swIBColor_FeatureMgrBkgnd: int = 0
swIBColor_EnabledTextColor: int = 1
swIBColor_DisabledTextColor: int = 2
swIBColor_ActiveTabColor: int = 3
swIBColor_InactiveTabColor: int = 4
swIBColor_ButtonFillHotColor: int = 5
swIBColor_ButtonFillCheckedColor: int = 6
swIBColor_ButtonFillPressedColor: int = 7
swIBColor_ButtonFillCheckedAndHotColor: int = 8

# swInterfaceBrightnessTheme_e (SwConst)
swInterfaceBrightnessTheme_Light: int = 0
swInterfaceBrightnessTheme_Medium: int = 1
swInterfaceBrightnessTheme_Dark: int = 2
swInterfaceBrightnessTheme_MediumLight: int = 3
swInterfaceBrightnessTheme_3DExperience: int = 4

# swInterpolationType_e (SwConst)
swInvalidInterpolation: int = 0
swCubicInterpolation: int = 1
swAkimaInterpolation: int = 2

# swIntersectionType_e (SwConst)
swIntersectionSIMPLE: int = 1
swIntersectionTANGENT: int = 2
swIntersectionCOINCIDENCE_START: int = 3
swIntersectionCOINCIDENCE_END: int = 4

# swIsolateVisibility_e (SwConst)
swIsolateVisibility_WIREFRAME: int = 0
swIsolateVisibility_TRANSPARENT: int = 1
swIsolateVisibility_HIDDEN: int = 2

# swJogDimensionPositionType_e (SwConst)
swJogDimensionPositionInsideOffset: int = 1
swJogDimensionPositionOutsideOffset: int = 2
swJogDimensionPositionOverallPosition: int = 3

# swJogOffsetTypes_e (SwConst)
swJogOffsetBlind: int = 1
swJogOffsetUpToVertex: int = 2
swJogOffsetUpToSurface: int = 3
swJogOffsetFromSurface: int = 4
swJogOffsetMidPlane: int = 5

# swJogPositionType_e (SwConst)
swJogPositionBendCenterline: int = 1
swJogPositionMaterialInside: int = 2
swJogPositionMaterialOutside: int = 3
swJogPositionBendOutside: int = 4

# swKeepReplacedCompOption_e (SwConst)
swKeepBothNewItemNumber: int = 0
swKeepBothSameItemNumber: int = 1
swKeepItemNumber: int = 2
swKeepNewItemNumberRemoveReplacedComp: int = 3

# swKernelErrorCode_e (SwConst)
swErrorSuccess: int = 1
swErrorError: int = 0
swErrorNotEntity: int = -100022
swErrorInvalidParameter: int = -100120
swErrorSurfaceDiscontinuous: int = -100129
swErrorCurveDiscontinuous: int = -100131
swErrorInvalidEntity: int = -100914
swErrorInvalidSharing: int = -100921
swErrorInvalidKnots: int = -100978
swErrorInvalidGeometry: int = -100999
swErrorHasInvalidentity: int = -101004
swErrorBodyDontKnit: int = -101041
swErrorInvalidPattern: int = -101042
swErrorCurveShort: int = -101057
swErrorFailed: int = -101063
swErrorCheckFailed: int = -105061
swErrorGeometryMissing: int = -113803
swErrorTopologySelfx: int = -113804
swErrorGeometrySelfx: int = -113805
swErrorGeometryDegenerate: int = -113806
swErrorInvalidGeometry2: int = -113808
swErrorCheckFailed2: int = -113812
swErrorFaceFaceInconsistent: int = -113816
swErrorVertexNotOnCurve: int = -113818
swErrorVerticesTouch: int = -113821
swErrorLoopsInconsistent: int = -113826
swErrorGeometryDiscontinuous: int = -113827
swErrorFacecheckFailed: int = -113829
swErrorFaceRedundant: int = -116402
swErrorInconsistentDirs: int = -116403
swErrorEdgeisectInvalid: int = -116404
swErrorInvalidLoop: int = -116405
swErrorEdgeIncorrectOrder: int = -116406
swErrorUnknown: int = -1

# swLargeDesignReviewState_e (SwConst)
swLargeDesignReviewState_None: int = 0
swLargeDesignReviewState_LDR: int = 1
swLargeDesignReviewState_LDR_EditAssembly: int = 2

# swLayerItemsOption_e (SwConst)
swLayerItemsOption_Annotations: int = 1
swLayerItemsOption_SketchSegments: int = 2
swLayerItemsOption_SketchBlockInstance: int = 4
swLayerItemsOption_SketchPoint: int = 8
swLayerItemsOption_SketchHatch: int = 16

# swLayerOverride_e (SwConst)
swLayerOverrideNone: int = 0
swLayerOverrideColor: int = 1
swLayerOverrideStyle: int = 2
swLayerOverrideWidth: int = 4

# swLeaderLineVisibility_e (SwConst)
swLeaderLineBoth: int = 0
swLeaderLineFirst: int = 1
swLeaderLineSecond: int = 2
swLeaderLineNone: int = 3

# swLeaderSide_e (SwConst)
swLS_SMART: int = 0
swLS_LEFT: int = 1
swLS_RIGHT: int = 2

# swLeaderStyle_e (SwConst)
swNO_LEADER: int = 0
swSTRAIGHT: int = 1
swBENT: int = 2
swUNDERLINED: int = 3
swAlwaysAttachToBalloon: int = 4100
swSPLINE: int = 4
swAttachLeaderTop: int = 256
swAttachLeaderCenter: int = 512
swAttachLeaderBottom: int = 1024
swAttachLeaderNearest: int = 2048
swVDA: int = 8

# swLengthUnit_e (SwConst)
swMM: int = 0
swCM: int = 1
swMETER: int = 2
swINCHES: int = 3
swFEET: int = 4
swFEETINCHES: int = 5
swANGSTROM: int = 6
swNANOMETER: int = 7
swMICRON: int = 8
swMIL: int = 9
swUIN: int = 10

# swLibFeatDimensionType_e (SwConst)
swLibFeatLocatingDimension: int = 0
swLibFeatSizeDimension: int = 1

# swLibFeatureData_e (SwConst)
swLibFeatureData_FeatureRespect: int = 0
swLibFeatureData_PartRespect: int = 1

# swLicenseType_e (SwConst)
swLicenseType_Full: int = 0
swLicenseType_Educational: int = 1
swLicenseType_Student: int = 2
swLicenseType_StudentDesignKit: int = 3
swLicenseType_PersonalEdition: int = 4
swLicenseType_Full_Office: int = 5
swLicenseType_Full_Professional: int = 6
swLicenseType_Full_Premium: int = 7
swLicenseType_Maker: int = 8
swLicenseType_Full_Ultimate: int = 9

# swLineEndCaps_e (SwConst)
swLineEndCapFlat: int = 1
swLineEndCapRound: int = 2
swLineEndCapSquare: int = 3

# swLineStyles_e (SwConst)
swLineCONTINUOUS: int = 0
swLineHIDDEN: int = 1
swLinePHANTOM: int = 2
swLineCHAIN: int = 3
swLineCENTER: int = 4
swLineSTITCH: int = 5
swLineCHAINTHICK: int = 6
swLineDEFAULT: int = 7

# swLineTypes_e (SwConst)
swLF_VISIBLE: int = 0
swLF_HIDDEN: int = 1
swLF_SKETCH: int = 2
swLF_DETAIL: int = 3
swLF_SECTION: int = 4
swLF_DIMENSION: int = 5
swLF_CENTER: int = 6
swLF_HATCH: int = 7
swLF_TANGENT: int = 8

# swLineWeights_e (SwConst)
swLW_NONE: int = -1
swLW_THIN: int = 0
swLW_NORMAL: int = 1
swLW_THICK: int = 2
swLW_THICK2: int = 3
swLW_THICK3: int = 4
swLW_THICK4: int = 5
swLW_THICK5: int = 6
swLW_THICK6: int = 7
swLW_NUMBER: int = 8
swLW_LAYER: int = 9
swLW_CUSTOM: int = 10

# swLinkBomToDisplayStateError_e (SwConst)
swLinkBomToDisplayState_Success: int = 0
swLinkBomToDisplayState_InvalidDisplayState: int = 1
swLinkBomToDisplayState_MultipleConfigurations: int = 2

# swLinkDimensionError_e (SwConst)
swLinkDimensionError_ErrorUknown: int = 0
swLinkDimensionError_NoError: int = 1
swLinkDimensionError_LinkAcrossDocs: int = 2
swLinkDimensionError_IncompatibleDimTypes: int = 3
swLinkDimensionError_AlreadyLinked: int = 4
swLinkDimensionError_ReadOnlyOrDriven: int = 5
swLinkDimensionError_IncompatibleValues: int = 6
swLinkDimensionError_DrivenByEquation: int = 7
swLinkDimensionError_CannotLink: int = 8
swLinkDimensionError_UnableToCreateSharedParam: int = 9
swLinkDimensionError_UnlinkFailure: int = 10
swLinkDimensionError_EmptyString: int = 11
swLinkDimensionError_InvalidString: int = 12

# swLinkString (SwConst)
swLinkStringNone: int = 0
swLinkStringUserDefined: int = 1
swLinkStringTroubleShootTip: int = 2

# swLoadAddinError_e (SwConst)
swUnknownError: int = -1
swSuccess: int = 0
swAddinNotLoaded: int = 1
swAddinAlreadyLoaded: int = 2
swFileNotFound: int = 3
swAddinsDisabled: int = 4
swLoadConflict: int = 5
swRegistrationError: int = 6
swLicenseError: int = 7

# swLoadDetachedModelRules_e (SwConst)
swLoadDetachedModelPrompt: int = 0
swLoadDetachedModelAuto: int = 1
swDoNotLoadDetachedModel: int = 2
swLoadDetailedModel: int = 3

# swLoadExternalReferences_e (SwConst)
swLoadExternalReferences_Prompt: int = 0
swLoadExternalReferences_All: int = 1
swLoadExternalReferences_None: int = 2
swLoadExternalReferences_ChangedOnly: int = 3

# swLocalCurvePatternAlignment_e (SwConst)
swLocalCurvePatternTangentToCurve: int = 0
swLocalCurvePatternAlignToSeed: int = 1

# swLocalCurvePatternCurveMethod_e (SwConst)
swLocalCurvePatternTransformCurve: int = 0
swLocalCurvePatternOffsetCurve: int = 1

# swLocalCurvePatternReferencePoint_e (SwConst)
swLocalCurvePatternSelectedPoint: int = 0
swLocalCurvePatternBoundingBoxCenter: int = 1
swLocalCurvePatternComponentOrigin: int = 2

# swLocalSketchPatternReferencePoint_e (SwConst)
swLocalSketchPatternSelectedPoint: int = 0
swLocalSketchPatternBoundingBoxCenter: int = 1
swLocalSketchPatternComponentOrigin: int = 2

# swLocationLabelText_e (SwConst)
swLocationLabelTextSheet: int = 0
swLocationLabelTextSheetWithLabel: int = 1
swLocationLabelTextZone: int = 2
swLocationLabelTextViewLetter: int = 3
swLocationLabelTextText: int = 4

# swLoftedBendFacetOptions_e (SwConst)
swChordTolerance: int = 0
swBendsPerTransitionSegment: int = 1
swMaxSegmentLength: int = 2
swAngleBetweenSegments: int = 3

# swLoopProcessOption_e (SwConst)
swLoopProcess_Together: int = 0
swLoopProcess_Independent: int = 1
swLoopProcess_Auto: int = 2

# swMBDSTEP242PublishEdition_e (SwConst)
swPublishSTEP242Edition_1_0: int = 1
swPublishSTEP242Edition_2_0: int = 2
swPublishSTEP242Edition_3_0: int = 3

# swMacroFeatureEntityIdType_e (SwConst)
swMacroFeatureEntityIdNotApplied: int = -1
swMacroFeatureEntityIdUndefined: int = 0
swMacroFeatureEntityIdUnique: int = 1
swMacroFeatureEntityIdDerived: int = 2
swMacroFeatureEntityIdUserDefined: int = 3

# swMacroFeatureOptions_e (SwConst)
swMacroFeatureByDefault: int = 0
swMacroFeatureAlwaysAtEnd: int = 1
swMacroFeatureIsPatternable: int = 2
swMacroFeatureIsDragable: int = 4
swMacroFeatureNoCachedBody: int = 8
swMacroFeatureEmbedMacroFile: int = 16

# swMacroFeatureParamType_e (SwConst)
swMacroFeatureParamTypeString: int = 0
swMacroFeatureParamTypeDouble: int = 1
swMacroFeatureParamTypeInteger: int = 2

# swMacroFeatureSecurityOptions_e (SwConst)
swMacroFeatureSecurityByDefault: int = 0
swMacroFeatureSecurityCannotBeDeleted: int = 1
swMacroFeatureSecurityNotEditable: int = 2
swMacroFeatureSecurityCannotBeSuppressed: int = 4
swMacroFeatureSecurityCannotBeReplaced: int = 8
swMacroFeatureSecurityEnableNote: int = 16
swMacroFeatureSecurityCannotBeRolledBack: int = 32

# swMacroMethods_e (SwConst)
swMethodsWithoutArguments: int = 1
swMethodsWithArguments: int = 2
swAllMethods: int = 3

# swManipulatorCursor_e (SwConst)
swManipulatorMoveCursor: int = 1
swManipulatorRotateCursor: int = 2
swManipulatorMoveRotateCursor: int = 3

# swManipulatorOptions_e (SwConst)
swManipulatorOpts_Default: int = 0
swManipulatorOpts_KeepAfterComponentModify: int = 1

# swManipulatorRepresentation_e (SwConst)
swManipulatorRepresentationNone: int = 0
swManipulatorRepresentationSquare: int = 1
swManipulatorRepresentationCircle: int = 2
swManipulatorRepresentationDiamond: int = 3
swManipulatorRepresentationTriangle: int = 4
swManipulatorRepresentationArrow: int = 5
swManipulatorRepresentationTextBox: int = 6
swManipulatorRepresentationRotationHandle: int = 7
swManipulatorRepresentationPanHandle: int = 8
swManipulatorRepresentationScaleHandle: int = 9
swManipulatorRepresentationSurfTopol: int = 10
swManipulatorRepresentationWireTopol: int = 11
swManipulatorRepresentationMiscTopol: int = 12
swManipulatorRepresentationBitmap: int = 13
swManipulatorRepresentationShadow: int = 14
swManipulatorRepresentationEmpty: int = 15

# swManipulatorType_e (SwConst)
swTriadManipulator: int = 0
swDragArrowManipulator: int = 1
swPlaneManipulator: int = 2

# swMassPropertiesStatus_e (SwConst)
swMassPropertiesStatus_OK: int = 0
swMassPropertiesStatus_UnknownError: int = 1
swMassPropertiesStatus_NoBody: int = 2

# swMassPropertyAccuracyLevel_e (SwConst)
swMassPropertyAccuracyLevel_Lower: int = 0
swMassPropertyAccuracyLevel_Medium: int = 1
swMassPropertyAccuracyLevel_Higher: int = 2

# swMassPropertyMoment_e (SwConst)
swMassPropertyMomentAboutCenterOfMass: int = 0
swMassPropertyMomentAboutCoordSys: int = 1

# swMateAlign_e (SwConst)
swMateAlignALIGNED: int = 0
swMateAlignANTI_ALIGNED: int = 1
swMateAlignCLOSEST: int = 2
swAlignNONE: int = 0
swAlignSAME: int = 1
swAlignAGAINST: int = 2

# swMateEntity2ReferenceType_e (SwConst)
swMateEntity2ReferenceType_Point: int = 0
swMateEntity2ReferenceType_Line: int = 1
swMateEntity2ReferenceType_Circle: int = 2
swMateEntity2ReferenceType_Plane: int = 3
swMateEntity2ReferenceType_Cylinder: int = 4
swMateEntity2ReferenceType_Sphere: int = 5
swMateEntity2ReferenceType_Set: int = 6
swMateEntity2ReferenceType_Cone: int = 7
swMateEntity2ReferenceType_SweptSurface: int = 8
swMateEntity2ReferenceType_MultipleSurface: int = 9
swMateEntity2ReferenceType_GenSurface: int = 10
swMateEntity2ReferenceType_Ellipse: int = 11
swMateEntity2ReferenceType_GeneralCurve: int = 12
swMateEntity2ReferenceType_UNKNOWN: int = 13

# swMateEntityTypes_e (SwConst)
swMateUnsupported: int = 0
swMatePoint: int = 1
swMateLine: int = 2
swMatePlane: int = 3
swMateCylinder: int = 4
swMateCone: int = 5
swMateSphere: int = 6
swMateCircle: int = 7

# swMateReferenceAlignment_e (SwConst)
swMateReferenceAlignment_Any: int = 0
swMateReferenceAlignment_Aligned: int = 1
swMateReferenceAlignment_AntiAligned: int = 2
swMateReferenceAlignment_Closest: int = 3

# swMateReferenceIndex_e (SwConst)
swMateReference_Primary: int = 0
swMateReference_Secondary: int = 1
swMateReference_Tertiary: int = 2

# swMateReferenceType_e (SwConst)
swMateReferenceType_default: int = 0
swMateReferenceType_Tangent: int = 1
swMateReferenceType_Coincident: int = 2
swMateReferenceType_Concentric: int = 3
swMateReferenceType_Parallel: int = 4

# swMateType_e (SwConst)
swMateCOINCIDENT: int = 0
swMateCONCENTRIC: int = 1
swMatePERPENDICULAR: int = 2
swMatePARALLEL: int = 3
swMateTANGENT: int = 4
swMateDISTANCE: int = 5
swMateANGLE: int = 6
swMateUNKNOWN: int = 7
swMateSYMMETRIC: int = 8
swMateCAMFOLLOWER: int = 9
swMateGEAR: int = 10
swMateWIDTH: int = 11
swMateLOCKTOSKETCH: int = 12
swMateRACKPINION: int = 13
swMateMAXMATES: int = 14
swMatePATH: int = 15
swMateLOCK: int = 16
swMateSCREW: int = 17
swMateLINEARCOUPLER: int = 18
swMateUNIVERSALJOINT: int = 19
swMateCOORDINATE: int = 20
swMateSLOT: int = 21
swMateHINGE: int = 22
swMateSLIDER: int = 23
swMatePROFILECENTER: int = 24
swMateMAGNETIC: int = 25

# swMateWidthOptions_e (SwConst)
swMateWidth_Centered: int = 0
swMateWidth_Free: int = 1
swMateWidth_Dimension: int = 2
swMateWidth_Percent: int = 3

# swMaterialModifier_e (SwConst)
swMaterialModifier_None: int = 0
swMaterialModifier_Unknown: int = 1
swMaterialModifier_MaximumMaterialCondition: int = 2
swMaterialModifier_LeastMaterialCondition: int = 3
swMaterialModifier_RegardlessOfFeatureSize: int = 4
swMaterialModifier_Translation: int = 5

# swMatesDefaultMisalignment_e (SwConst)
swMatesAlignFirstConcentricMate: int = 0
swMatesAlignSecondConcentricMate: int = 1
swMatesSymmetric: int = 2

# swMeasureArcCircleOption_e (SwConst)
swMeasureArcCircle_CenterToCenter: int = 0
swMeasureArcCircle_MinimumDistance: int = 1
swMeasureArcCircle_MaximumDistance: int = 2
swMeasureArcCircle_CustomCenterToCenter: int = 3
swMeasureArcCircle_CustomMinimumToMinimum: int = 4
swMeasureArcCircle_CustomMaximumToMaximum: int = 5
swMeasureArcCircle_CustomCenterToMinimum: int = 6
swMeasureArcCircle_CustomCenterToMaximum: int = 7
swMeasureArcCircle_CustomMinimumToCenter: int = 8
swMeasureArcCircle_CustomMaximumToCenter: int = 9
swMeasureArcCircle_CustomMinimumToMaximum: int = 10
swMeasureArcCircle_CustomMaximumToMinimum: int = 11

# swMeasureProjectOnOption_e (SwConst)
swMeasureProjectOn_None: int = 0
swMeasureProjectOn_Screen: int = 1
swMeasureProjectOn_FaceOrPlane: int = 2

# swMenuIdentifiers_e (SwConst)
swFileMenu: int = 0
swEditMenu: int = 1
swViewMenu: int = 2
swInsertMenu: int = 3
swToolsMenu: int = 4
swWindowMenu: int = 5
swHelpMenu: int = 6
swDeveloperToolsMenu: int = 7
swViewToolbarsMenu: int = 8

# swMenuItemType_e (SwConst)
swMenuItemType_Default: int = 0
swMenuItemType_Break: int = 1
swMenuItemType_Separator: int = 2

# swMessageBoxBtn_e (SwConst)
swMbAbortRetryIgnore: int = 1
swMbOk: int = 2
swMbOkCancel: int = 3
swMbRetryCancel: int = 4
swMbYesNo: int = 5
swMbYesNoCancel: int = 6

# swMessageBoxIcon_e (SwConst)
swMbWarning: int = 1
swMbInformation: int = 2
swMbQuestion: int = 3
swMbStop: int = 4

# swMessageBoxResult_e (SwConst)
swMbHitAbort: int = 1
swMbHitIgnore: int = 2
swMbHitNo: int = 3
swMbHitOk: int = 4
swMbHitRetry: int = 5
swMbHitYes: int = 6
swMbHitCancel: int = 7

# swMinimumBendRadiusChecks_e (SWRoutingLib)
swMinimumBendRadiusChecks_None: int = 0
swMinimumBendRadiusChecks_WiresOnly: int = 1
swMinimumBendRadiusChecks_CablesAndWires: int = 2

# swMirrorComponentMirrorType_e (SwConst)
swMirrorType_CenterOfBoundingBox: int = 0
swMirrorType_CenterOfMass: int = 1
swMirrorType_ComponentOrigin: int = 2

# swMirrorComponentNameModifier_e (SwConst)
swMirrorComponentName_Prefix: int = 0
swMirrorComponentName_Suffix: int = 1
swMirrorComponentName_Custom: int = 2

# swMirrorComponentOrientation2_e (SwConst)
swOrientation_MirroredX_MirroredY: int = 0
swOrientation_MirroredAndFlippedX_MirroredY: int = 1
swOrientation_MirroredX_MirroredAndFlippedY: int = 2
swOrientation_MirroredAndFlippedX_MirroredAndFlippedY: int = 3

# swMirrorComponentOrientation_e (SwConst)
swMirrorComponentOrientation_RotatePlaneY: int = 0
swMirrorComponentOrientation_None: int = 1
swMirrorComponentOrientation_RotatePlaneXY: int = 2
swMirrorComponentOrientation_RotatePlaneX: int = 3

# swMirrorPartOptions_e (SwConst)
swMirrorPartOptions_ImportSolids: int = 1
swMirrorPartOptions_ImportSurfaces: int = 2
swMirrorPartOptions_ImportAxes: int = 4
swMirrorPartOptions_ImportPlanes: int = 8
swMirrorPartOptions_ImportCosmeticThreads: int = 16
swMirrorPartOptions_ImportAbsorbedSketchs: int = 32
swMirrorPartOptions_ImportUnabsorbedSketchs: int = 64
swMirrorPartOptions_ImportCustomProperties: int = 128
swMirrorPartOptions_ImportCoordinateSystem: int = 256
swMirrorPartOptions_ImportModelDimensions: int = 512
swMirrorPartOptions_ImportHoleWizardData: int = 1024
swMirrorPartOptions_ImportCutListProperties: int = 2048
swMirrorPartOptions_ImportSMInfo: int = 4096
swMirrorPartOptions_ImportIndProps: int = 8192
swMirrorPartOptions_ImportDimXpertAnnotations: int = 16384
swMirrorPartOptions_ImportBodyMaterial: int = 32768
swMirrorPartOptions_ImportPartMaterial: int = 65536

# swMirrorPlaneType_e (SwConst)
swMirrorPlaneType_Face: int = 0
swMirrorPlaneType_Plane: int = 1

# swMirrorProfileOrAlignmentAxis_e (SwConst)
swMirrorProfileOrAlignmentAxis_Horizontal: int = 1
swMirrorProfileOrAlignmentAxis_Vertical: int = 2

# swMirrorViewPositions_e (SwConst)
swMirrorViewPosition_NotDefined: int = -1
swMirrorViewPosition_Horizontal: int = 0
swMirrorViewPosition_Vertical: int = 1

# swModelRebuildStatus_e (SwConst)
swModelRebuildStatus_FullyRebuilt: int = 0
swModelRebuildStatus_NonFrozenFeatureNeedsRebuild: int = 1
swModelRebuildStatus_FrozenFeatureNeedsRebuild: int = 2

# swModelRouteType_e (SwConst)
swModelRouteType_Harness: int = 0
swModelRouteType_Tube: int = 1
swModelRouteType_FabricatedPipe: int = 2
swModelRouteType_FormedPipe: int = 3
swModelRouteType_Trunking: int = 4
swModelRouteType_UnknownRouteType: int = 5
swModelRouteType_Electrical: int = 6
swModelRouteType_AnyRouteType: int = 7
swModelRouteType_MixedRouteType: int = 8

# swModifyTableNotifyReason_e (SwConst)
swModifyTableNotifyReason_ColumnInsertionLeft: int = 0
swModifyTableNotifyReason_ColumnInsertionRight: int = 1
swModifyTableNotifyReason_RowInsertionAbove: int = 2
swModifyTableNotifyReason_RowInsertionBelow: int = 3
swModifyTableNotifyReason_ColumnRellocation: int = 4
swModifyTableNotifyReason_RowRellocation: int = 5
swModifyTableNotifyReason_ColumnDeletion: int = 6
swModifyTableNotifyReason_CellDataModify: int = 7
swModifyTableNotifyReason_ColumnPropertyModify: int = 8
swModifyTableNotifyReason_CellMerge: int = 9
swModifyTableNotifyReason_CellUnMerge: int = 10
swModifyTableNotifyReason_EditMultiProp: int = 11
swModifyTableNotifyReason_CustomPropertyModify: int = 12
swModifyTableNotifyReason_TableSplitVerticallyLeft: int = 13
swModifyTableNotifyReason_TableSplitVerticallyRight: int = 14
swModifyTableNotifyReason_TableSplitHorizontallyAbove: int = 15
swModifyTableNotifyReason_TableSplitHorizontallyBelow: int = 16
swModifyTableNotifyReason_TableMerge: int = 17

# swMomentsOfInertiaReferenceFrame_e (SwConst)
swMomentsOfInertiaReferenceFrame_CenterOfMass: int = 0
swMomentsOfInertiaReferenceFrame_DefaultCoordinateSystem: int = 1
swMomentsOfInertiaReferenceFrame_UserCoordinateSystem: int = 2

# swMotionContactFrictionType_e (SwConst)
swMotionContactFrictionOff: int = 0
swMotionContactFrictionFull: int = 1
swMotionContactFrictionDynamic: int = 2

# swMotionIntegratorType_e (SwMotionStudy)
swMotionIntegrator_GSTIFF: int = 1
swMotionIntegrator_WSTIFF: int = 2
swMotionIntegrator_SI2_GSTIFF: int = 3

# swMotionMat_e (SwConst)
swMotionMatNone: int = 1000
swMotionMatAcrylic: int = 1001
swMotionMatAluminumDry: int = 1002
swMotionMatAluminumGreasy: int = 1003
swMotionMatNylon: int = 1004
swMotionMatRubberDry: int = 1005
swMotionMatRubberGreasy: int = 1006
swMotionMatSteelDry: int = 1007
swMotionMatSteelGreasy: int = 1008

# swMotionPlotAxisComponent_e (SwConst)
swMotionPlotAxisComponent_X: int = 0
swMotionPlotAxisComponent_Y: int = 1
swMotionPlotAxisComponent_Z: int = 2
swMotionPlotAxisComponent_MAGNITUDE: int = 3
swMotionPlotAxisComponent_RADIAL_MAGNITUDE: int = 4
swMotionPlotAxisComponent_EULER_PSI: int = 5
swMotionPlotAxisComponent_EULER_THETA: int = 6
swMotionPlotAxisComponent_EULER_PHI: int = 7
swMotionPlotAxisComponent_YAW: int = 8
swMotionPlotAxisComponent_PITCH: int = 9
swMotionPlotAxisComponent_ROLL: int = 10
swMotionPlotAxisComponent_RODRIGUEZ_PARAM1: int = 11
swMotionPlotAxisComponent_RODRIGUEZ_PARAM2: int = 12
swMotionPlotAxisComponent_RODRIGUEZ_PARAM3: int = 13
swMotionPlotAxisComponent_BRYANT_ANGLE1: int = 14
swMotionPlotAxisComponent_BRYANT_ANGLE2: int = 15
swMotionPlotAxisComponent_BRYANT_ANGLE3: int = 16

# swMotionPlotAxisType_e (SwConst)
swMotionPlotAxisType_XAXISTIME: int = 0
swMotionPlotAxisType_XAXISFRAME: int = 1
swMotionPlotAxisType_CM_POSITION: int = 2
swMotionPlotAxisType_PRESSURE_ANGLE: int = 3
swMotionPlotAxisType_CM_VELOCITY: int = 4
swMotionPlotAxisType_CM_ACCELERATION: int = 5
swMotionPlotAxisType_TRANS_DISP: int = 6
swMotionPlotAxisType_TRANS_VELOCITY: int = 7
swMotionPlotAxisType_TRANS_ACCELERATION: int = 8
swMotionPlotAxisType_ANGULAR_DISP: int = 9
swMotionPlotAxisType_ANGULAR_VELOCITY: int = 10
swMotionPlotAxisType_ANGULAR_ACCEL: int = 11
swMotionPlotAxisType_TRANS_MOMENTUM: int = 12
swMotionPlotAxisType_ANGULAR_MOMENTUM: int = 13
swMotionPlotAxisType_REACTION_FORCE: int = 14
swMotionPlotAxisType_REACTION_TORQUE: int = 15
swMotionPlotAxisType_PROJ_ANGLES: int = 16
swMotionPlotAxisType_EULER_ANGLES: int = 17
swMotionPlotAxisType_PITCH: int = 18
swMotionPlotAxisType_BRYANT_ANGLE: int = 19
swMotionPlotAxisType_RODRIQUEZ_PARAM: int = 20
swMotionPlotAxisType_MOTION_APPLIED_FORCE: int = 21
swMotionPlotAxisType_MOTION_APPLIED_TORQUE: int = 22
swMotionPlotAxisType_FRICTION_FORCE: int = 23
swMotionPlotAxisType_FRICTION_MOMENT: int = 24
swMotionPlotAxisType_KINETIC_ENERGY: int = 25
swMotionPlotAxisType_TRANS_KINETIC_ENERGY: int = 26
swMotionPlotAxisType_ANGULAR_KINETIC_ENERGY: int = 27
swMotionPlotAxisType_POTENTIAL_ENERGY_DELTA: int = 28
swMotionPlotAxisType_POWER_CONSUMPTION: int = 29
swMotionPlotAxisType_TRACE_PATH: int = 30
swMotionPlotAxisType_CONTACT_FORCE: int = 31
swMotionPlotAxisType_REFLECTED_MASS: int = 32
swMotionPlotAxisType_REFLECTED_INERTIA: int = 33

# swMotionStudyNotify_e (SwMotionStudy)
swMotionStudyMotorTimeStepChangeNotify: int = 1
swMotionStudyForceTimeStepChangeNotify: int = 2
swMotionStudyPartCollideNotify: int = 3
swMotionStudyMotorOutputTimeStepChangeNotify: int = 4
swMotionStudyStartCalculateNotify: int = 5
swMotionStudyStopCalculateNotify: int = 6
swMotionStudyForceOutputTimeStepChangeNotify: int = 7
swMotionStudySpecialEventNotify: int = 8
swMotionStudyOutputTimeStepChangeNotify: int = 9

# swMotionStudyType_e (SwMotionStudy)
swMotionStudyTypeAssembly: int = 1
swMotionStudyTypePhysicalSimulation: int = 2
swMotionStudyTypeCosmosMotion: int = 4
swMotionStudyTypeLegacyCosmosMotion: int = 8
swMotionStudyTypeNewCosmosMotion: int = 16

# swMouseDragMode_e (SwConst)
swTranslateAssemblyComponent: int = 1
swRotateAssemblyComponentAboutCenter: int = 2
swRotateAssemblyComponentAboutAxis: int = 3
swAssemblySmartMates: int = 4
swRotateView: int = 5
swTranslateView: int = 6
swZoomView: int = 7
swZoomToAreaOfView: int = 8
swInsertDimension: int = 9
swRollView: int = 10
swTurnView: int = 11

# swMouseNotify_e (SwConst)
swMouseNotify: int = 1
swMouseMoveNotify: int = 2
swMouseLBtnDownNotify: int = 3
swMouseLBtnUpNotify: int = 4
swMouseRBtnDownNotify: int = 5
swMouseRBtnUpNotify: int = 6
swMouseMBtnDownNotify: int = 7
swMouseMBtnUpNotify: int = 8
swMouseLBtnDblClkNotify: int = 9
swMouseRBtnDblClkNotify: int = 10
swMouseMBtnDblClkNotify: int = 11
swMouseSelectNotify: int = 12

# swMouse_e (SwCommands)
swMouse_MouseMove: int = 1
swMouse_LeftDown: int = 2
swMouse_LeftUp: int = 4
swMouse_RightDown: int = 8
swMouse_RightUp: int = 16
swMouse_MiddleDown: int = 32
swMouse_MiddleUp: int = 64
swMouse_Wheel: int = 128
swMouse_Absolute: int = 256
swMouse_Click: int = 512
swMouse_DoubleClick: int = 1024
swMouse_RightClick: int = 2048
swMouse_RightDoubleClick: int = 4096
swMouse_MiddleDoubleClick: int = 8192
swMouse_SelectEDGES: int = 65536
swMouse_SelectFACES: int = 131072
swMouse_SelectVERTICES: int = 196608
swMouse_SelectDATUMPLANES: int = 262144
swMouse_SelectDATUMAXES: int = 327680
swMouse_SelectDATUMPOINTS: int = 393216
swMouse_SelectOLEITEMS: int = 458752
swMouse_SelectATTRIBUTES: int = 524288
swMouse_SelectSKETCHES: int = 589824
swMouse_SelectSKETCHSEGS: int = 655360
swMouse_SelectSKETCHPOINTS: int = 720896
swMouse_SelectDRAWINGVIEWS: int = 786432
swMouse_SelectGTOLS: int = 851968
swMouse_SelectDIMENSIONS: int = 917504
swMouse_SelectNOTES: int = 983040
swMouse_SelectSECTIONLINES: int = 1048576
swMouse_SelectDETAILCIRCLES: int = 1114112
swMouse_SelectSECTIONTEXT: int = 1179648
swMouse_SelectSHEETS: int = 1245184
swMouse_SelectCOMPONENTS: int = 1310720
swMouse_SelectMATES: int = 1376256
swMouse_SelectBODYFEATURES: int = 1441792
swMouse_SelectREFCURVES: int = 1507328
swMouse_SelectEXTSKETCHSEGS: int = 1572864
swMouse_SelectEXTSKETCHPOINTS: int = 1638400
swMouse_SelectHELIX: int = 1703936
swMouse_SelectREFERENCECURVES: int = 1703936
swMouse_SelectREFSURFACES: int = 1769472
swMouse_SelectCENTERMARKS: int = 1835008
swMouse_SelectINCONTEXTFEAT: int = 1900544
swMouse_SelectMATEGROUP: int = 1966080
swMouse_SelectBREAKLINES: int = 2031616
swMouse_SelectINCONTEXTFEATS: int = 2097152
swMouse_SelectMATEGROUPS: int = 2162688
swMouse_SelectSKETCHTEXT: int = 2228224
swMouse_SelectSFSYMBOLS: int = 2293760
swMouse_SelectDATUMTAGS: int = 2359296
swMouse_SelectCOMPPATTERN: int = 2424832
swMouse_SelectWELDS: int = 2490368
swMouse_SelectCTHREADS: int = 2555904
swMouse_SelectDTMTARGS: int = 2621440
swMouse_SelectPOINTREFS: int = 2686976
swMouse_SelectDCABINETS: int = 2752512
swMouse_SelectEXPLVIEWS: int = 2818048
swMouse_SelectEXPLSTEPS: int = 2883584
swMouse_SelectEXPLLINES: int = 2949120
swMouse_SelectSILHOUETTES: int = 3014656
swMouse_SelectCONFIGURATIONS: int = 3080192
swMouse_SelectOBJHANDLES: int = 3145728
swMouse_SelectARROWS: int = 3211264
swMouse_SelectZONES: int = 3276800
swMouse_SelectREFEDGES: int = 3342336
swMouse_SelectREFFACES: int = 3407872
swMouse_SelectREFSILHOUETTE: int = 3473408
swMouse_SelectBOMS: int = 3538944
swMouse_SelectEQNFOLDER: int = 3604480
swMouse_SelectSKETCHHATCH: int = 3670016
swMouse_SelectIMPORTFOLDER: int = 3735552
swMouse_SelectVIEWERHYPERLINK: int = 3801088
swMouse_SelectMIDPOINTS: int = 3866624
swMouse_SelectCUSTOMSYMBOLS: int = 3932160
swMouse_SelectCOORDSYS: int = 3997696
swMouse_SelectDATUMLINES: int = 4063232
swMouse_SelectROUTECURVES: int = 4128768
swMouse_SelectBOMTEMPS: int = 4194304
swMouse_SelectROUTEPOINTS: int = 4259840
swMouse_SelectCONNECTIONPOINTS: int = 4325376
swMouse_SelectROUTESWEEPS: int = 4390912
swMouse_SelectPOSGROUP: int = 4456448
swMouse_SelectBROWSERITEM: int = 4521984
swMouse_SelectFABRICATEDROUTE: int = 4587520
swMouse_SelectSKETCHPOINTFEAT: int = 4653056
swMouse_SelectEMPTYSPACE: int = 4718592
swMouse_SelectCOMPSDONTOVERRIDE: int = 4718592
swMouse_SelectLIGHTS: int = 4784128
swMouse_SelectWIREBODIES: int = 4849664
swMouse_SelectSURFACEBODIES: int = 4915200
swMouse_SelectSOLIDBODIES: int = 4980736
swMouse_SelectFRAMEPOINT: int = 5046272
swMouse_SelectSURFBODIESFIRST: int = 5111808
swMouse_SelectMANIPULATORS: int = 5177344
swMouse_SelectPICTUREBODIES: int = 5242880
swMouse_SelectSOLIDBODIESFIRST: int = 5308416
swMouse_SelectHOLESERIES: int = 5439488
swMouse_SelectLEADERS: int = 5505024
swMouse_SelectSKETCHBITMAP: int = 5570560
swMouse_SelectDOWELSYMS: int = 5636096
swMouse_SelectEXTSKETCHTEXT: int = 5767168
swMouse_SelectBLOCKINST: int = 6094848
swMouse_SelectFTRFOLDER: int = 6160384
swMouse_SelectSKETCHREGION: int = 6225920
swMouse_SelectSKETCHCONTOUR: int = 6291456
swMouse_SelectBOMFEATURES: int = 6356992
swMouse_SelectANNOTATIONTABLES: int = 6422528
swMouse_SelectBLOCKDEF: int = 6488064
swMouse_SelectCENTERMARKSYMS: int = 6553600
swMouse_SelectSIMULATION: int = 6619136
swMouse_SelectSIMELEMENT: int = 6684672
swMouse_SelectCENTERLINES: int = 6750208
swMouse_SelectHOLETABLEFEATS: int = 6815744
swMouse_SelectHOLETABLEAXES: int = 6881280
swMouse_SelectWELDMENT: int = 6946816
swMouse_SelectSUBWELDFOLDER: int = 7012352
swMouse_SelectEXCLUDEMANIPULATORS: int = 7274496
swMouse_SelectREVISIONTABLE: int = 7405568
swMouse_SelectSUBSKETCHINST: int = 7471104
swMouse_SelectWELDMENTTABLEFEATS: int = 7602176
swMouse_SelectBODYFOLDER: int = 7733248
swMouse_SelectREVISIONTABLEFEAT: int = 7798784
swMouse_SelectSUBATOMFOLDER: int = 7929856
swMouse_SelectWELDBEADS: int = 7995392
swMouse_SelectEMBEDLINKDOC: int = 8060928
swMouse_SelectJOURNAL: int = 8126464
swMouse_SelectDOCSFOLDER: int = 8192000
swMouse_SelectCOMMENTSFOLDER: int = 8257536
swMouse_SelectCOMMENT: int = 8323072
swMouse_SelectSWIFTANNOTATIONS: int = 8519680
swMouse_SelectSWIFTFEATURES: int = 8650752
swMouse_SelectCAMERAS: int = 8912896
swMouse_SelectMATESUPPLEMENT: int = 9043968
swMouse_SelectANNOTATIONVIEW: int = 9109504
swMouse_SelectGENERALTABLEFEAT: int = 9306112
swMouse_SelectDISPLAYSTATE: int = 9699328
swMouse_SelectSUBSKETCHDEF: int = 10092544
swMouse_SelectSWIFTSCHEMA: int = 10420224
swMouse_SelectTITLEBLOCK: int = 12582912
swMouse_SelectTITLEBLOCKTABLEFEAT: int = 13500416
swMouse_SelectOBJGROUP: int = 13565952
swMouse_SelectPLANESECTIONS: int = 14352384
swMouse_SelectCOSMETICWELDS: int = 14417920
swMouse_SelectMAGNETICLINES: int = 14745600
swMouse_SelectPUNCHTABLEFEATS: int = 15335424
swMouse_SelectREVISIONCLOUDS: int = 15728640
swMouse_SelectBorder: int = 16646144
swMouse_SelectSELECTIONSETFOLDER: int = 16908288
swMouse_SelectSELECTIONSETNODE: int = 16973824

# swMoveCopyBodyFeatureTransformType_e (SwConst)
swTransformType_None: int = 0
swTransformType_Translation: int = 1
swTransformType_Rotation: int = 2

# swMoveCopyError_e (SwConst)
swMoveCopyErrorNone: int = 0
swMoveCopyErrorSourceDoesNotExist: int = 1
swMoveCopyErrorFail: int = 2

# swMoveCopyOptions_e (SwConst)
swMoveCopyOptionsOverwriteExistingDocs: int = 1
swMoveCopyOptionsCreateNewFolder: int = 2

# swMoveFaceType_e (SwConst)
swMoveFaceTypeOffset: int = 0
swMoveFaceTypeTranslate: int = 1
swMoveFaceTypeRotate: int = 2

# swMoveFreezeBarTo_e (SwConst)
swMoveFreezeBarToEnd: int = 1
swMoveFreezeBarToBeforeFeature: int = 2
swMoveFreezeBarToAfterFeature: int = 3
swMoveFreezeBarToTop: int = 4

# swMoveLocation_e (SwConst)
swMoveAfter: int = 3
swMoveBefore: int = 2
swMoveToEnd: int = 1
swMoveToTop: int = 4
swMoveToFolder: int = 5

# swMoveRollbackBarTo_e (SwConst)
swMoveRollbackBarToEnd: int = 1
swMoveRollbackBarToPreviousPosition: int = 2
swMoveRollbackBarToBeforeFeature: int = 3
swMoveRollbackBarToAfterFeature: int = 4

# swMoveableDatumDirection_e (SwConst)
swMoveableDatumDirectionLeft: int = 0
swMoveableDatumDirectionRight: int = 1
swMoveableDatumDirectionUp: int = 2
swMoveableDatumDirectionDown: int = 3
swMoveableDatumDirectionFreeDrag: int = 4
swMoveableDatumDirectionBySelection: int = 5

# swMoveableDatumStyle_e (SwConst)
swMoveableDatumStyle_NotMoveable: int = 0
swMoveableDatumStyle_Horizontal: int = 1
swMoveableDatumStyle_Rotational: int = 2

# swNameType_e (SwConst)
swBodyName: int = 0
swFeatureName: int = 1

# swNonInterferingComponentDisplay_e (SwConst)
swNonInterferingComponentDisplay_Wireframe: int = 0
swNonInterferingComponentDisplay_Hidden: int = 1
swNonInterferingComponentDisplay_Transparent: int = 2
swNonInterferingComponentDisplay_Current: int = 3

# swNormalCutErrors_e (SwConst)
swAddNormalCutGroup_Success: int = 0
swAddNormalCutGroup_Failed: int = 1

# swNormalCutParameters_e (SwConst)
swNormalCutExtent: int = 0
swNormalCutOffsetPlane: int = 1

# swNotifyEntityType_e (SwConst)
swNotifyConfiguration: int = 1
swNotifyComponent: int = 2
swNotifyFeature: int = 3
swNotifyDerivedConfiguration: int = 4
swNotifyDrawingSheet: int = 5
swNotifyDrawingView: int = 6
swNotifyBlockDef: int = 7
swNotifyComponentInternal: int = 8

# swNumberboxUnitType_e (SwConst)
swNumberBox_UnitlessInteger: int = 1
swNumberBox_UnitlessDouble: int = 2
swNumberBox_Length: int = 3
swNumberBox_Angle: int = 4
swNumberBox_Density: int = 5
swNumberBox_Stress: int = 6
swNumberBox_Force: int = 7
swNumberBox_Gravity: int = 8
swNumberBox_Time: int = 9
swNumberBox_Frequency: int = 10
swNumberBox_Percent: int = 11

# swNumberedListStartType_e (SwConst)
swStartNumberingInvalid: int = -1
swStartNumberingFromTop: int = 0
swStartNumberingFromBottom: int = 1

# swNumberedListType_e (SwConst)
swNumberedListTypeInvalid: int = 0
swNumberedListType1: int = 1
swNumberedListType2: int = 2
swNumberedListType3: int = 3
swNumberedListType4: int = 4
swNumberedListType5: int = 5

# swNumberingFormat_e (SwConst)
swNumberingFormatInvalid: int = -1
swNumberingFormat1: int = 0
swNumberingFormat2: int = 1
swNumberingFormat3: int = 2

# swNumberingType_e (SwConst)
swNumberingType_None: int = 0
swNumberingType_Detailed: int = 1
swNumberingType_Flat: int = 2
swIndentedBOMNotSet: int = 3

# swObjectEquality (SwConst)
swObjectNotSame: int = 0
swObjectSame: int = 1
swObjectUnsupported: int = 2

# swOffsetPlanarWireBodyOptions_e (SwConst)
swOffsetPlanarWireBodyOptions_GapFillRound: int = 0
swOffsetPlanarWireBodyOptions_GapFillExtend: int = 1
swOffsetPlanarWireBodyOptions_GapFillTangent: int = 2

# swOleObjectOptions_e (SwConst)
swOleObjectOptions_GetAll: int = 0
swOleObjectOptions_GetOnCurrentSheet: int = 1

# swOnSurfacePlaneProjectType_e (SwConst)
swOnSurfacePlaneProjecttoNearestLocation: int = 0
swOnSurfacePlaneProjectAlongSketchNormal: int = 1

# swOpenDocOptions_e (SwConst)
swOpenDocOptions_Silent: int = 1
swOpenDocOptions_ReadOnly: int = 2
swOpenDocOptions_ViewOnly: int = 4
swOpenDocOptions_RapidDraft: int = 8
swOpenDocOptions_LoadModel: int = 16
swOpenDocOptions_AutoMissingConfig: int = 32
swOpenDocOptions_OverrideDefaultLoadLightweight: int = 64
swOpenDocOptions_LoadLightweight: int = 128
swOpenDocOptions_DontLoadHiddenComponents: int = 256
swOpenDocOptions_LoadExternalReferencesInMemory: int = 512
swOpenDocOptions_OpenDetailingMode: int = 1024
swOpenDocOptions_LDR_EditAssembly: int = 2048
swOpenDocOptions_SpeedPak: int = 4096
swOpenDocOptions_AdvancedConfig: int = 8192

# swOrdDimEndSymbol_e (SwConst)
swOrdDimEndSymbol_None: int = 0
swOrdDimEndSymbol_Dowel: int = 1
swOrdDimEndSymbol_UpwardRight: int = 2
swOrdDimEndSymbol_DownwardLeft: int = 3

# swOutOfDateStatus_e (SwConst)
swUnknownState: int = 0
swModelUpToDate: int = 1
swModelOutOfDate: int = 2

# swPLYQuality_e (SwConst)
swPLYQuality_Coarse: int = 1
swPLYQuality_Fine: int = 2
swPLYQuality_Custom: int = 3

# swPMContainer_e (SwConst)
swPMInTabsWithFM: int = 0
swPMPinnedAboveFM: int = 1
swPMPinnedNextToFM: int = 2
swPMFloating: int = 3
swPMPinnedLowerRight: int = 4

# swPMIDatumAnchorStyle_e (SwConst)
swPMIDatumAnchorStyle_FilledTriangle: int = 0
swPMIDatumAnchorStyle_FilledTriangleWithShoulder: int = 1
swPMIDatumAnchorStyle_EmptyTriangle: int = 2
swPMIDatumAnchorStyle_EmptyTriangleWithShoulder: int = 3

# swPMIDatumShape_e (SwConst)
swPMIDatumShape_Square: int = 0
swPMIDatumShape_Round: int = 1

# swPMIDatumTargetAreaStyle_e (SwConst)
swPMIDatumTargetAreaStyle_None: int = 0
swPMIDatumTargetAreaStyle_Unknown: int = 1
swPMIDatumTargetAreaStyle_X: int = 2
swPMIDatumTargetAreaStyle_Circular: int = 3
swPMIDatumTargetAreaStyle_Rectangular: int = 4

# swPMIDatumTargetMovableStyle_e (SwConst)
swPMIDatumTargetMovableStyle_None: int = 0
swPMIDatumTargetMovableStyle_Unknown: int = 1
swPMIDatumTargetMovableStyle_Horizontal: int = 2
swPMIDatumTargetMovableStyle_Rotational: int = 3

# swPMIDatumTargetSymbolStyle_e (SwConst)
swPMIDatumTargetSymbolStyle_None: int = 0
swPMIDatumTargetSymbolStyle_Unknown: int = 1
swPMIDatumTargetSymbolStyle_Symbol: int = 2
swPMIDatumTargetSymbolStyle_AreaOutside: int = 3

# swPMIDatumType_e (SwConst)
swPMIDatumType_DatumFeature: int = 0
swPMIDatumType_DatumTarget: int = 1

# swPMILeaderLocation_e (SwConst)
swPMILeaderLocation_None: int = 0
swPMILeaderLocation_Left: int = 1
swPMILeaderLocation_Right: int = 2
swPMILeaderLocation_Nearest: int = 3

# swPMILeaderModifier_e (SwConst)
swPMILeaderModifier_None: int = 0
swPMILeaderModifier_AllAround: int = 1
swPMILeaderModifier_AllAroundThisSide: int = 2
swPMILeaderModifier_AllOver: int = 3
swPMILeaderModifier_AllOverThisSide: int = 4

# swPMILeaderStyle_e (SwConst)
swPMILeaderStyle_None: int = 0
swPMILeaderStyle_Straight: int = 1
swPMILeaderStyle_Bent: int = 2
swPMILeaderStyle_Perpendicular: int = 3
swPMILeaderStyle_Outside: int = 4
swPMILeaderStyle_Inside: int = 5
swPMILeaderStyle_Smart: int = 6

# swPMILeaderType_e (SwConst)
swPMILeaderType_NoLeader: int = 0
swPMILeaderType_Leader: int = 1
swPMILeaderType_MultiJog: int = 2

# swPMITolPerUnitAreaType_e (SwConst)
swPMITolPerUnitType_None: int = 0
swPMITolPerUnitType_Unknown: int = 1
swPMITolPerUnitType_Circular: int = 2
swPMITolPerUnitType_Rectangular: int = 3
swPMITolPerUnitType_Square: int = 4

# swPMIType_e (SwConst)
swPMIType_None: int = 0
swPMIType_Dimension: int = 1
swPMIType_Datum: int = 2
swPMIType_GTol: int = 3
swPMIType_Unknown: int = 4

# swPMIUnit_e (SwConst)
swPMIUnit_None: int = 0
swPMIUnit_ANGSTROM: int = 1
swPMIUnit_CM: int = 2
swPMIUnit_FEET: int = 3
swPMIUnit_FEETINCHES: int = 4
swPMIUnit_INCHES: int = 5
swPMIUnit_METER: int = 6
swPMIUnit_MICRON: int = 7
swPMIUnit_MIL: int = 8
swPMIUnit_MM: int = 9
swPMIUnit_NANOMETER: int = 10
swPMIUnit_UIN: int = 11
swPMIUnit_DEGREE: int = 12
swPMIUnit_RADIAN: int = 13

# swPackAndGoDocumentStatus_e (SwConst)
swPackAndGoDocumentStatus_Normal: int = 0
swPackAndGoDocumentStatus_Virtual: int = 1
swPackAndGoDocumentStatus_UnKnown: int = 2

# swPackAndGoFolderOptions_e (SwConst)
swPackAndGoFolderOptions_SingleFolder: int = 0
swPackAndGoFolderOptions_MinimalFolders: int = 1
swPackAndGoFolderOptions_FullStructure: int = 2

# swPackAndGoSaveStatus_e (SwConst)
swPackAndGoSaveStatus_Succeed: int = 0
swPackAndGoSaveStatus_UserInputNotCorrect: int = 1
swPackAndGoSaveStatus_FileAlreadyExist: int = 2
swPackAndGoSaveStatus_SaveToEmpty: int = 3
swPackAndGoSaveStatus_SaveError: int = 4

# swPageSetupDrawingColor_e (SwConst)
swPageSetup_AutomaticDrawingColor: int = 1
swPageSetup_ColorGrey: int = 2
swPageSetup_BlackAndWhite: int = 3

# swPageSetupInUse_e (SwConst)
swPageSetupInUse_Application: int = 1
swPageSetupInUse_Document: int = 2
swPageSetupInUse_DrawingSheet: int = 3

# swPageSetupOrientation_e (SwConst)
swPageSetupOrient_Portrait: int = 1
swPageSetupOrient_Landscape: int = 2

# swParabolaPts_e (SwConst)
swParabolaStartPt: int = 0
swParabolaEndPt: int = 1
swParabolaFocusPt: int = 2
swParabolaApexPt: int = 3

# swParagraphType_e (SwConst)
swParagraphNone: int = -1
swParagraphBullet: int = 0
swParagraphNumbered: int = 1

# swParamType_e (SwConst)
swParamTypeDouble: int = 0
swParamTypeString: int = 1
swParamTypeInteger: int = 2
swParamTypeDVector: int = 3

# swParameterizationPropertyType_e (SwConst)
swParameterizationPropertyType_Periodic: int = 13701
swParameterizationPropertyType_AllDerivativesContinuous: int = 13737
swParameterizationPropertyType_AllDerivativesNotContinuous: int = 13738
swParameterizationPropertyType_Linear: int = 13739
swParameterizationPropertyType_Circular: int = 13740
swParameterizationPropertyType_BoundsCoincident: int = 13746

# swParasolidOutputVersion_e (SwConst)
swParasolidOutputVersion_latest: int = 0
swParasolidOutputVersion_80: int = 1
swParasolidOutputVersion_90: int = 2
swParasolidOutputVersion_91: int = 3
swParasolidOutputVersion_100: int = 4
swParasolidOutputVersion_110: int = 5
swParasolidOutputVersion_111: int = 6
swParasolidOutputVersion_120: int = 7
swParasolidOutputVersion_121: int = 8
swParasolidOutputVersion_130: int = 9
swParasolidOutputVersion_140: int = 10
swParasolidOutputVersion_150: int = 11
swParasolidOutputVersion_151: int = 12
swParasolidOutputVersion_160: int = 13
swParasolidOutputVersion_161: int = 14
swParasolidOutputVersion_171: int = 15
swParasolidOutputVersion_181: int = 16
swParasolidOutputVersion_191: int = 17
swParasolidOutputVersion_200: int = 18
swParasolidOutputVersion_210: int = 19
swParasolidOutputVersion_220: int = 20
swParasolidOutputVersion_230: int = 21
swParasolidOutputVersion_240: int = 22
swParasolidOutputVersion_250: int = 23
swParasolidOutputVersion_260: int = 24
swParasolidOutputVersion_270: int = 25
swParasolidOutputVersion_280: int = 26
swParasolidOutputVersion_290: int = 27
swParasolidOutputVersion_300: int = 28
swParasolidOutputVersion_310: int = 29
swParasolidOutputVersion_320: int = 30
swParasolidOutputVersion_330: int = 31
swParasolidOutputVersion_341: int = 32
swParasolidOutputVersion_351: int = 33

# swPartConfigurationGroupingOption_e (SwConst)
swDisplay_ConfigurationOfSamePart_AsSeparateItem: int = 1
swDisplay_AllConfigurationOfSamePart_AsOneItem: int = 2
swDisplay_ConfigurationWithSameName_AsOneItem: int = 3

# swPartDimXpertToleranceMethod_e (SwConst)
swPartDimXpertToleranceMethod_BlockTolerance: int = 0
swPartDimXpertToleranceMethod_GeneralTolerance: int = 1
swPartDimXpertToleranceMethod_GeneralBlockTolerance: int = 2

# swPartNotify_e (SwConst)
swPartRegenNotify: int = 1
swPartDestroyNotify: int = 2
swPartRegenPostNotify: int = 3
swPartViewNewNotify: int = 4
swPartNewSelectionNotify: int = 5
swPartFileSaveNotify: int = 6
swPartFileSaveAsNotify: int = 7
swPartLoadFromStorageNotify: int = 8
swPartSaveToStorageNotify: int = 9
swPartConfigChangeNotify: int = 10
swPartConfigChangePostNotify: int = 11
swPartAutoSaveNotify: int = 12
swPartAutoSaveToStorageNotify: int = 13
swPartViewNewNotify2: int = 14
swPartLightingDialogCreateNotify: int = 15
swPartAddItemNotify: int = 16
swPartRenameItemNotify: int = 17
swPartDeleteItemNotify: int = 18
swPartModifyNotify: int = 19
swPartFileReloadNotify: int = 20
swPartAddCustomPropertyNotify: int = 21
swPartChangeCustomPropertyNotify: int = 22
swPartDeleteCustomPropertyNotify: int = 23
swPartFeatureEditPreNotify: int = 24
swPartFeatureSketchEditPreNotify: int = 25
swPartFileSaveAsNotify2: int = 26
swPartDeleteSelectionPreNotify: int = 27
swPartFileReloadPreNotify: int = 28
swPartBodyVisibleChangeNotify: int = 29
swPartRegenPostNotify2: int = 30
swPartFileSavePostNotify: int = 31
swPartLoadFromStorageStoreNotify: int = 32
swPartSaveToStorageStoreNotify: int = 33
swPartFeatureManagerTreeRebuildNotify: int = 34
swPartFileDropPostNotify: int = 35
swPartDynamicHighlightNotify: int = 36
swPartDimensionChangeNotify: int = 37
swPartFileReloadCancelNotify: int = 38
swPartFileSavePostCancelNotify: int = 39
swPartSketchSolveNotify: int = 40
swPartDeleteItemPreNotify: int = 41
swPartClearSelectionsNotify: int = 42
swPartEquationEditorPreNotify: int = 43
swPartEquationEditorPostNotify: int = 44
swPartOpenDesignTableNotify: int = 45
swPartCloseDesignTableNotify: int = 46
swPartPromptBodiesToKeepNotify: int = 47
swPartAddDvePagePreNotify: int = 48
swPartUnitsChangeNotify: int = 49
swPartDestroyNotify2: int = 50
swPartConfigurationChangeNotify: int = 51
swPartSuppressionStateChangeNotify: int = 52
swPartActiveViewChangeNotify: int = 53
swPartFeatureManagerFilterStringChangeNotify: int = 54
swPartFlipLoopNotify: int = 55
swPartFileDropPreNotify: int = 56
swPartSensorAlertPreNotify: int = 57
swPartUndoPostNotify: int = 58
swPartUserSelectionPreNotify: int = 59
swPartActiveDisplayStateChangePreNotify: int = 60
swPartActiveDisplayStateChangePostNotify: int = 61
swPartRedoPostNotify: int = 62
swPartRedoPreNotify: int = 63
swPartUndoPreNotify: int = 64
swPartWeldmentCutListUpdatePostNotify: int = 65
swPartAutoSaveToStorageStoreNotify: int = 66
swPartDragStateChangeNotify: int = 67
swPartInsertTableNotify: int = 68
swPartModifyTableNotify: int = 69
swPartUserSelectionPostNotify: int = 70
swPartCommandManagerTabActivatedPreNotify: int = 71
swPartPreRenameItemNotify: int = 72
swPartRenamedDocumentNotify: int = 73
swPartFeatureManagerTabActivatedPreNotify: int = 74
swPartFeatureManagerTabActivatedNotify: int = 75
swPartPublishTo3DPDFNotify: int = 76
swPartConvertToBodiesPreNotify: int = 77
swPartConvertToBodiesPostNotify: int = 78
swPartRenameDisplayTitleNotify: int = 79
swPartActiveAnnotationViewChangeNotify: int = 80
swPartDisplayPaneExpandNotify: int = 81
swPartDisplayPaneCollapseNotify: int = 82
swPartSolidBodyFolderReorderNotify: int = 83
swPartAddDependencyNotify: int = 84
swPartDeleteDependencyNotify: int = 85

# swPartingLineFeatureStatus_e (SwConst)
STATUS_MOLD_REDUNDANT_EDGES: int = 1
STATUS_MOLD_PARTINGLINE_EDGES_OPEN: int = 2
STATUS_MOLD_PARTINGLINE_SEPARABLE: int = 3
STATUS_MOLD_PARTINGLINE_NON_SEPARABLE: int = 4

# swPartingSurfaceMoldParmType_e (SwConst)
swPartingSurfaceMoldParmTangent: int = 0
swPartingSurfaceMoldParmNormal: int = 1
swPartingSurfaceMoldParmPerpendicular: int = 4

# swPartingSurfaceSmoothingType_e (SwConst)
swPartingSurfaceSharp: int = 1
swPartingSurfaceSmooth: int = 2

# swPartnerEntitlementStatus_e (SwConst)
swPESuccess: int = 0
swPEFail: int = 1
swPEAddinNameMismatch: int = 2
swPEAddinGUIDMismatch: int = 4
swPEVersionMismatch: int = 8
swPELicenseExpired: int = 16
swPETierMismatch: int = 32
swPELicenseError: int = 64

# swPatternElementSelection_e (SwConst)
swErrorInPatternElementSelection: int = 0
swFeatureFaces: int = 1
swBodiesToPattern: int = 2

# swPatternEndCondition_e (SwConst)
swPatternEndCondition_SpacingAndInstances: int = 0
swPatternEndCondition_UpToReference: int = 1

# swPatternFeatureImportExportError_e (SwConst)
swPatternFeatureImportExportError_Succeed: int = 0
swPatternFeatureImportExportError_Failed: int = 1
swPatternFeatureImportExportError_UnequalNumOfCellsInColumn: int = 2
swPatternFeatureImportExportError_UnequalNumOfCellsInRow: int = 3
swPatternFeatureImportExportError_EmptyRowsOrColumns: int = 4
swPatternFeatureImportExportError_ColumnARows1And2Error: int = 5
swPatternFeatureImportExportError_InstNumStartsFromNonZero: int = 6
swPatternFeatureImportExportError_ColumnBRows1And2Error: int = 7
swPatternFeatureImportExportError_ImproperValuesForColumnB: int = 8
swPatternFeatureImportExportError_FeatureDoesNotExist: int = 9
swPatternFeatureImportExportError_DuplicateDimensions: int = 10
swPatternFeatureImportExportError_OutOfRangeDimensionValue: int = 11
swPatternFeatureImportExportError_DimensionNameDoesNotExist: int = 12
swPatternFeatureImportExportError_FeatureOrDimDoesNotExist: int = 13
swPatternFeatureImportExportError_NoValidDimensionToImport: int = 14
swPatternFeatureImportExportError_DimValueFormatIncorrect: int = 15
swPatternFeatureImportExportError_FailedToRetrieveModelDocument: int = 16
swPatternFeatureImportExportError_FileExistsAndOverwriteIsFalse: int = 17
swPatternFeatureImportExportError_ReadOnlyFile: int = 18
swPatternFeatureImportExportError_AccessDeniedOrInvalidPath: int = 19
swPatternFeatureImportExportError_FailedToRetrieveExcelApp: int = 20

# swPatternLayoutSpacingType_e (SwConst)
swPatternLayoutTargetSpacing: int = 0
swPatternLayoutInstances: int = 1

# swPatternLayoutType_e (SwConst)
swPatternLayoutCircular: int = 0
swPatternLayoutSquare: int = 1
swPatternLayoutPolygon: int = 2
swPatternLayoutPerforation: int = 3

# swPatternReferenceTypes_e (SwConst)
swPatternReferenceTypeAxis: int = 0
swPatternReferenceTypeEdge: int = 1
swPatternReferenceTypeRefDim: int = 2
swPatternReferenceTypeFace: int = 3

# swPerformanceFeedback_e (SwConst)
swPerformanceFeedback_No: int = 0
swPerformanceFeedback_Yes: int = 1
swPerformanceFeedback_RemindLater: int = 2
swPerformanceFeedback_RemindNow: int = 3

# swPersistReferencedObjectStates_e (SwConst)
swPersistReferencedObject_Ok: int = 0
swPersistReferencedObject_Invalid: int = 1
swPersistReferencedObject_Suppressed: int = 2
swPersistReferencedObject_Deleted: int = 4

# swPipingPenetrationStatus_e (SwConst)
swPenetrationSucceeded: int = 0
swPenetrationFailed: int = 1
swPenetrationFailedPipeTooWide: int = 2
swPenetrationFailedDllNotLoaded: int = 3
swPenetrationFailedNoSelection: int = 4
swPenetrationFailedNotRouting: int = 5
swPenetrationFailedBadSelection: int = 6
swPenetrationFailedBadFitting: int = 7
swPenetrationFailedAlreadyPenetrating: int = 8
swPenetrationFailedMultiBody: int = 9

# swPointInferenceBrokerOption_e (SwConst)
swPointInferenceBrokerOption_IncludeHidden: int = 1

# swPointStyle_e (SwConst)
swPointStyle_X: int = 1
swPointStyle_Plus: int = 2
swPointStyle_XPlus: int = 3
swPointStyle_Circle: int = 4

# swPointToPointAutoRouteConversionMode_e (SWRoutingLib)
swFlexibleMode: int = 1
swOrthogonalMode: int = 2

# swPointToPointAutoRouteErrorType_e (SWRoutingLib)
swRouteTypeAndConversionModeMismatch: int = 1
swCouldNotCreateRoute: int = 2
swNoRouteFound: int = 3
swPointToPointAutoRouteNoError: int = 4

# swPresentationOpts_e (SwConst)
swPresentationOpts_None: int = 0
swPresentationOpts_Pres: int = 1
swPresentationOpts_U3D: int = 2
swPresentationOpts_Animations: int = 4
swPresentationOpts_Explodes: int = 8
swPresentationOpts_CameraMovement: int = 16
swPresentationOpts_ActiveView: int = 32
swPresentationOpts_TopView: int = 64
swPresentationOpts_BottomView: int = 128
swPresentationOpts_LeftView: int = 256
swPresentationOpts_RightView: int = 512
swPresentationOpts_FrontView: int = 1024
swPresentationOpts_BackView: int = 2048
swPresentationOpts_NormalView: int = 4096
swPresentationOpts_IsometricView: int = 8192
swPresentationOpts_TrimetricView: int = 16384
swPresentationOpts_DimetricView: int = 32768
swPresentationOpts_OpenPDF: int = 65536
swPresentationOpts_ExcludeFromAnnoView: int = 131072
swPresentationOpts_CreateAttachSTEP242: int = 262144
swPresentationOpts_LowAccuracy: int = 524288
swPresentationOpts_HighAccuracy: int = 1048576
swPresentationOpts_MedAccuracy: int = 2097152
swPresentationOpts_MaxAccuracy: int = 4194304
swPresentationOpts_CompressTesselation: int = 8388608
swPresentationOpts_DisablePrinting3DPDF: int = 16777216
swPresentationOpts_DisableEditing3DPDF: int = 33554432
swPresentationOpts_DisableCopying3DPDF: int = 67108864
swPresentationOpts_ShowOnlyGraphicalData: int = 134217728
swPresentationOpts_PDFPreview: int = 268435456
swPresentationOpts_SingleHTML: int = 536870912
swPresentationOpts_ChkOpenPassword3DPDF: int = 1073741824

# swPrimaryMemberPointLengthEndCondition_e (SwConst)
swPrimaryMemberPointLengthEndCondition_Length: int = 0
swPrimaryMemberPointLengthEndCondition_Point: int = 1
swPrimaryMemberPointLengthEndCondition_UpToPoint: int = 2
swPrimaryMemberPointLengthEndCondition_UpToPlane: int = 3

# swPrintProperties_e (SwConst)
swPrintPaperSize: int = 0
swPrintOrientation: int = 1
swPrintPaperLength: int = 2
swPrintPaperWidth: int = 3

# swPrintSelectionScaleFactor_e (SwConst)
swPrintAll: int = 0
swPrintCurrentSheet: int = 1
swPrintScreenImage: int = 2
swPrintSelection: int = 3

# swPrompForFilenameCause_e (SwConst)
swUnused: int = 0
swGeneric: int = 1
swMirrorComponent: int = 2
swWeldBead: int = 3
swDerivedPart: int = 4
swSplitAssembly: int = 5
swSplitPart: int = 6
swInsertEnvelopeFromFile: int = 7
swMirrorComponentBrowse: int = 8
swCreateNamedViewFromFile: int = 9
swComponentPropsReplace: int = 10
swOpenAssociatedDrawing: int = 11
swFileReloadReplace: int = 12
swDrawingAddViewFromFile: int = 13
swDrawingInsert3ViewFromFile: int = 14
swAddComponent: int = 15
swStartRouteAssembly: int = 16
swSaveRoutePart: int = 17
swSaveVirtualComponentExternally: int = 18
swEditReadOnlyComponent: int = 19
swInsertBlock: int = 20
swSketchBlock: int = 21
swSaveDefeaturedModel: int = 22
swFormNewSubAssembly: int = 23
swAddVirtualComponent: int = 24
swMakeComponentIndependent: int = 25
swPromptForFilename_Cancelled: int = 26

# swPromptAlwaysNever_e (SwConst)
swResponsePrompt: int = 0
swResponseAlways: int = 1
swResponseNever: int = 2

# swPropMgrPageComboBoxStyle_e (SwConst)
swPropMgrPageComboBoxStyle_Sorted: int = 1
swPropMgrPageComboBoxStyle_EditableText: int = 2
swPropMgrPageComboBoxStyle_EditBoxReadOnly: int = 4
swPropMgrPageComboBoxStyle_AvoidSelectionText: int = 8

# swPropMgrPageControlOnResizeOptions_e (SwConst)
swControlOptionsOnResize_LockLeft: int = 1
swControlOptionsOnResize_LockRight: int = 2

# swPropMgrPageLabelStyle_e (SwConst)
swPropMgrPageLabelStyle_LeftText: int = 1
swPropMgrPageLabelStyle_CenterText: int = 2
swPropMgrPageLabelStyle_RightText: int = 4
swPropMgrPageLabelStyle_Sunken: int = 8

# swPropMgrPageLabelUnderlineStyle_e (SwConst)
swPropMgrPageLabel_NoUnderline: int = 0
swPropMgrPageLabel_SolidUnderline: int = 1
swPropMgrPageLabel_DashedUnderline: int = 2

# swPropMgrPageListBoxStyle_e (SwConst)
swPropMgrPageListBoxStyle_Sorted: int = 1
swPropMgrPageListBoxStyle_NoIntegralHeight: int = 2
swPropMgrPageListBoxStyle_MultipleItemSelect: int = 4

# swPropMgrPageNumberBoxStyle_e (SwConst)
swPropMgrPageNumberBoxStyle_ComboEditBox: int = 1
swPropMgrPageNumberBoxStyle_EditBoxReadOnly: int = 2
swPropMgrPageNumberBoxStyle_AvoidSelectionText: int = 4
swPropMgrPageNumberBoxStyle_NoScrollArrows: int = 8
swPropMgrPageNumberBoxStyle_Slider: int = 16
swPropMgrPageNumberBoxStyle_Thumbwheel: int = 32
swPropMgrPageNumberBoxStyle_SuppressNotifyWhileTracking: int = 64

# swPropMgrPageOptionStyle_e (SwConst)
swPropMgrPageOptionStyle_FirstInGroup: int = 1

# swPropMgrPageSelectionBoxStyle_e (SwConst)
swPropMgrPageSelectionBoxStyle_HScroll: int = 1
swPropMgrPageSelectionBoxStyle_UpAndDownButtons: int = 2
swPropMgrPageSelectionBoxStyle_MultipleItemSelect: int = 4
swPropMgrPageSelectionBoxStyle_WantListboxSelectionChanged: int = 8

# swPropMgrPageSliderStyle_e (SwConst)
swPropMgrPageSliderStyle_Vertical: int = 1
swPropMgrPageSliderStyle_AutoTicks: int = 2
swPropMgrPageSliderStyle_BottomLeftTicks: int = 4
swPropMgrPageSliderStyle_TopRightTicks: int = 8
swPropMgrPageSliderStyle_NotifyWhileTracking: int = 16

# swPropMgrPageTextBoxStyle_e (SwConst)
swPropMgrPageTextBoxStyle_NotifyOnlyWhenFocusLost: int = 1
swPropMgrPageTextBoxStyle_ReadOnly: int = 2
swPropMgrPageTextBoxStyle_NoBorder: int = 4
swPropMgrPageTextBoxStyle_Multiline: int = 8

# swPropSheetType_e (SwConst)
swPropSheetNotValid: int = 0
swPropSheetLighting: int = 1
swPropSheetToolsOptions: int = 2
swPropSheetAmbientLight: int = 3
swPropSheetDirectionalLight: int = 4
swPropSheetPositionLight: int = 5
swPropSheetSpotLight: int = 6

# swPropertyManagerButtonTypes_e (SwConst)
swPropertyManager_OkayButton: int = 1
swPropertyManager_CancelButton: int = 2
swPropertyManager_HelpButton: int = 4
swPropertyManager_PreviewButton: int = 8
swPropertyManager_PushpinButton: int = 16

# swPropertyManagerCheckboxState_e (SwConst)
Unchecked: int = 0
Checked: int = 1
Indeterminate: int = 2

# swPropertyManagerColorScheme_e (SwConst)
swPropertyManagerColorScheme_Blue: int = 1
swPropertyManagerColorScheme_Gray: int = 2
swPropertyManagerColorScheme_Mustard: int = 3
swPropertyManagerColorScheme_Olive: int = 4
swPropertyManagerColorScheme_Sand: int = 5
swPropertyManagerColorScheme_SeaGreen: int = 6
swPropertyManagerColorScheme_Default: int = 7
swPropertyManagerColorScheme_Windows: int = 8

# swPropertyManagerPageBitmapButtons_e (SwConst)
swBitmapButtonImage_alongz: int = 1
swBitmapButtonImage_angle: int = 2
swBitmapButtonImage_auto_bal_circular: int = 3
swBitmapButtonImage_auto_bal_left: int = 4
swBitmapButtonImage_auto_bal_right: int = 5
swBitmapButtonImage_auto_bal_square: int = 6
swBitmapButtonImage_auto_bal_top: int = 7
swBitmapButtonImage_diameter: int = 8
swBitmapButtonImage_distance1: int = 9
swBitmapButtonImage_distance2: int = 10
swBitmapButtonImage_draft: int = 11
swBitmapButtonImage_dve_but_cmark_bolt: int = 12
swBitmapButtonImage_dve_but_cmark_linear: int = 13
swBitmapButtonImage_dve_but_cmark_single: int = 14
swBitmapButtonImage_leader_ang_above: int = 15
swBitmapButtonImage_leader_ang_beside: int = 16
swBitmapButtonImage_leader_hor_above: int = 17
swBitmapButtonImage_leader_hor_beside: int = 18
swBitmapButtonImage_leader_left: int = 19
swBitmapButtonImage_leader_no: int = 20
swBitmapButtonImage_leader_right: int = 21
swBitmapButtonImage_leader_yes: int = 22
swBitmapButtonImage_parallel: int = 23
swBitmapButtonImage_perpendicular: int = 24
swBitmapButtonImage_reverse_direction: int = 25
swBitmapButtonImage_revision_circle: int = 26
swBitmapButtonImage_revision_hexagon: int = 27
swBitmapButtonImage_revision_square: int = 28
swBitmapButtonImage_revision_triangle: int = 29
swBitmapButtonImage_stackleft: int = 30
swBitmapButtonImage_stackright: int = 31
swBitmapButtonImage_stackup: int = 32
swBitmapButtonImage_stack: int = 33
swBitmapButtonImage_favorite_add: int = 34
swBitmapButtonImage_favorite_delete: int = 35
swBitmapButtonImage_favorite_save: int = 36
swBitmapButtonImage_favorite_load: int = 37
swBitmapButtonImage_dimension_set_default_attributes: int = 38

# swPropertyManagerPageButtons_e (SwConst)
swPropertyManagerPageButton_Ok: int = 1
swPropertyManagerPageButton_Cancel: int = 2
swPropertyManagerPageButton_Help: int = 3
swPropertyManagerPageButton_Next: int = 4
swPropertyManagerPageButton_Back: int = 5
swPropertyManagerPageButton_Undo: int = 6
swPropertyManagerPageButton_Preview: int = 7
swPropertyManagerPageButton_Pushpin: int = 8
swPropertyManagerPageButton_Redo: int = 9
swPropertyManagerPageButton_WhatsNew: int = 10

# swPropertyManagerPageCloseReasons_e (SwConst)
swPropertyManagerPageClose_UnknownReason: int = 0
swPropertyManagerPageClose_Okay: int = 1
swPropertyManagerPageClose_Cancel: int = 2
swPropertyManagerPageClose_ParentClosed: int = 3
swPropertyManagerPageClose_Closed: int = 4
swPropertyManagerPageClose_UserEscape: int = 5
swPropertyManagerPageClose_Apply: int = 6
swPropertyManagerPageClose_Preview: int = 7

# swPropertyManagerPageControlLeftAlign_e (SwConst)
swControlAlign_LeftEdge: int = 1
swControlAlign_Indent: int = 2
swControlAlign_DoubleIndent: int = 3

# swPropertyManagerPageControlType_e (SwConst)
swControlType_Label: int = 1
swControlType_Checkbox: int = 2
swControlType_Button: int = 3
swControlType_Option: int = 4
swControlType_Textbox: int = 5
swControlType_Listbox: int = 6
swControlType_Combobox: int = 7
swControlType_Numberbox: int = 8
swControlType_Selectionbox: int = 9
swControlType_ActiveX: int = 10
swControlType_BitmapButton: int = 11
swControlType_CheckableBitmapButton: int = 12
swControlType_Slider: int = 13
swControlType_Bitmap: int = 14
swControlType_WindowFromHandle: int = 15

# swPropertyManagerPageCursors_e (SwConst)
swPropertyManagerPageCursors_None: int = 0
swPropertyManagerPageCursors_Okay: int = 1
swPropertyManagerPageCursors_Advance: int = 2

# swPropertyManagerPageMessageExpanded (SwConst)
swMessageBoxMaintainExpandState: int = 0
swMessageBoxExpand: int = 1
swMessageBoxCompress: int = 2

# swPropertyManagerPageMessageVisibility (SwConst)
swNoMessageBox: int = 1
swMessageBoxHidden: int = 2
swMessageBoxVisible: int = 3
swImportantMessageBox: int = 4

# swPropertyManagerPageOptions_e (SwConst)
swPropertyManagerOptions_OkayButton: int = 1
swPropertyManagerOptions_CancelButton: int = 2
swPropertyManagerOptions_LockedPage: int = 4
swPropertyManagerOptions_CloseDialogButton: int = 8
swPropertyManagerOptions_MultiplePages: int = 16
swPropertyManagerOptions_PushpinButton: int = 32
swPropertyManagerOptions_AllowHorizontalResize: int = 64
swPropertyManagerOptions_PreviewButton: int = 128
swPropertyManagerOptions_DisableSelection: int = 256
swPropertyManagerOptions_WhatsNew: int = 512
swPropertyManagerOptions_AbortCommands: int = 1024
swPropertyManagerOptions_UndoButton: int = 2048
swPropertyManagerOptions_CanEscapeCancel: int = 4096
swPropertyManagerOptions_HandleKeystrokes: int = 8192
swPropertyManagerOptions_RedoButton: int = 16384
swPropertyManagerOptions_DisablePageBuildDuringHandlers: int = 32768
swPropertyManagerOptions_GrayOutDisabledSelectionListboxes: int = 65536
swPropertyManagerOptions_SupportsChainSelection: int = 131072
swPropertyManagerOptions_SupportsIsolate: int = 262144

# swPropertyManagerPageShowOptions_e (SwConst)
swPropertyManagerShowOptions_StackPage: int = 1

# swPropertyManagerPageStatus_e (SwConst)
swPropertyManagerPage_Okay: int = 0
swPropertyManagerPage_UnsupportedHandler: int = 1
swPropertyManagerPage_CreationFailure: int = -1
swPropertyManagerPage_NoDocument: int = -2

# swPropertyManagerStatus_e (SwConst)
swPropertyManagerStatus_Okay: int = 0
swPropertyManagerStatus_Failed: int = -1
swPropertyManagerStatus_Disconnected: int = -2

# swPropertySheetNotify_e (SwConst)
swPropertySheetDestroyNotify: int = 1
swPropertySheetHelpNotify: int = 2
swPropertySheetOnOKNotify: int = 3
swPropertySheetOnCancelNotify: int = 4
swPropertySheetCreateControlNotify: int = 5

# swPublishStepOpts_e (SwConst)
swPublishStepOpts_None: int = 0
swPublishStepOpts_SplitFacesSTEP242: int = 1
swPublishStepOpts_FaceEdgeSTEP242: int = 2

# swPublishTo3DPDFError_e (SwConst)
swPublishTo3DPDF_Success: int = 0
swPublishTo3DPDF_InvalidPath: int = 1
swPublishTo3DPDF_InvalidTheme: int = 2
swPublishTo3DPDF_UnknownError: int = 3
swPublishTo3DPDF_MBDLicenseNotAvailable: int = 4
swPublishTo3DPDF_NothingToPublish: int = 5
swPublishTo3DPDF_Step242EditionError: int = 6

# swPunchTableTagStyle_e (SwConst)
swPunchTable_AlphaNumericTags: int = 1
swPunchTable_NumericTags: int = 2

# swQuadant_e (SwConst)
swQuadUnknown: int = 0
swQuadPosQ1: int = 1
swQuadNegQ1: int = 2
swQuadPosQ2: int = 3
swQuadNegQ2: int = 4

# swQuickTipMode_e (SwConst)
swQuickTipNoMode: int = 0
swQuickTipEmptySWFrameMode: int = 1
swQuickTipEmptyPartMode: int = 2
swQuickTipSketchingMode: int = 4
swQuickTipClosedProfileCompletedMode: int = 8
swQuickTipSketchDoneMode: int = 16
swQuickTipFirstFeatureDoneMode: int = 32
swQuickTipEmptyAssemblyMode: int = 64
swQuickTipAssemblyOneCompMode: int = 128
swQuickTipAssemblyMultiCompMode: int = 256
swQuickTipAssemblyMatedMode: int = 512
swQuickTipAssemblySimulatingMode: int = 1024
swQuickTipEmptyDrawingMode: int = 2048
swQuickTipDrawingOneViewMode: int = 4096
swQuickTipPMBaseFeatureDialogMode: int = 8192
swQuickTipPMYellowErrorMessageMode: int = 16384
swQuickTipPMMateDialogMode: int = 32768
swQuickTipSheetMetalMode: int = 65536
swQuickTipSketching3DMode: int = 131072
swQuickTipDrawingEditSheetMode: int = 262144
swQuickTipPMInsertModelViewMode: int = 524288
swQuickTipPMInsertProjectedViewMode: int = 1048576
swQuickTipPMInsertComponentMode: int = 2097152
swQuickTipPMYellowGuidelinesMode: int = 4194304

# swQuickTipPointAt_e (SwConst)
swQTPA_NONE: int = 0
swQTPA_FilletFeature: int = 1
swQTPA_RefPlanes: int = 3
swQTPA_SheetMetalFeature: int = 18
swQTPA_MateGroupFeature: int = 33
swQTPA_MateFeature: int = 105
swQTPA_ExtrudedCut: int = 52
swQTPA_ExtrudedBoss: int = 53
swQTPA_BaseExtrudeFeature: int = 54
swQTPA_RevolvedCut: int = 57
swQTPA_RevolvedBoss: int = 57
swQTPA_BaseRevolvedFeature: int = 57
swQTPA_FirstBodyFeature: int = 998
swQTPA_LastBodyFeature: int = 999
swQTPA_SketchFeature: int = 78
swQTPA_Origin: int = 79
swTPA_SheetFeature: int = 88
swTPA_SheetFormat: int = 97
swTPA_DwgViewFeature: int = 43
swTPA_FeatureMgrTree: int = 100
swTPA_SketchingDorito: int = 1000
swTPA_OnScreenCancel: int = 1001
swQTPA_Triad: int = 1002
swQTPA_RollbackBar: int = 1003
swQTPA_SheetMetalFlattenedFeature: int = 1004
swQTPA_SheetMetalProcessedFeature: int = 1005
swQTPA_AssemblyComponentFeature: int = 1006
swQTPA_ArrowManipulator: int = 1007
swQTPA_PropertyManager: int = 1008
swQTPA_AssemblyComponentNonFixed: int = 1009
swQTPA_MateOperationBar: int = 1010
swQTPA_QTStatusBarButton: int = 1011
swQTPA_Nothing_FloatTRGraphics: int = 1012
swQTPA_ConstraintStatusBarButton: int = 1013
swQTPA_ChangedFilesStatusBarButton: int = 1014
swQTPA_PM_MSG_DIVIDER: int = 5085
swQTPA_UpperAppFrame: int = 387099

# swRackPinionMateDistanceOptions_e (SwConst)
swPinionPitchDiameter: int = 0
swRackTravelPerRevolution: int = 1

# swRackPinionMateEntityType_e (SwConst)
swRackPinionMateEntityType_Rack: int = 0
swRackPinionMateEntityType_Pinion: int = 1

# swRayPtsOpts_e (SwConst)
swRayPtsOptsNORMALS: int = 1
swRayPtsOptsTOPOLS: int = 2
swRayPtsOptsENTRY_EXIT: int = 4
swRayPtsOptsUNBLOCK: int = 8

# swRayPtsResults_e (SwConst)
swRayPtsResultsUnknown: int = 0
swRayPtsResultsFACE: int = 1
swRayPtsResultsSILHOUETTE: int = 2
swRayPtsResultsEDGE: int = 4
swRayPtsResultsVERTEX: int = 8
swRayPtsResultsENTER: int = 16
swRayPtsResultsEXIT: int = 32

# swRayTraceRenderImageFormat_e (SwConst)
swImageFormat_FlexiblePrecision: int = 0
swImageFormat_Targa: int = 1
swImageFormat_WindowsBmp: int = 2
swImageFormat_HDR: int = 3
swImageFormat_JPEG2000: int = 4
swImageFormat_JPEG2000_16bit: int = 5
swImageFormat_JPEG2000_16bit_Lossless: int = 6
swImageFormat_JPEG: int = 7
swImageFormat_PNG: int = 8
swImageFormat_PNG_16bit: int = 9
swImageFormat_SGI_RGB: int = 10
swImageFormat_TIF: int = 11
swImageFormat_TIF_16bit: int = 12
swImageFormat_TIF_16bit_uncompr: int = 13
swImageFormat_OpenEXR: int = 14
swImageFormat_OpenEXR_32bit: int = 15
swImageFormat_OpenEXR_TILED16bit: int = 16
swImageFormat_OpenEXR_TILED32bit: int = 17

# swRayTraceRenderQuality_e (SwConst)
swRenderQuality_Good: int = 0
swRenderQuality_Better: int = 1
swRenderQuality_Best: int = 2
swRenderQuality_Maximum: int = 3

# swRayTraceRenderType_e (SwConst)
swPhotoView: int = 1

# swRayTraceRenderingType_e (SwConst)
swRayTraceCartoon: int = 0
swRayTraceContour: int = 1

# swRebuildOnActivation_e (SwConst)
swUserDecision: int = 0
swDontRebuildActiveDoc: int = 1
swRebuildActiveDoc: int = 2

# swRebuildOptions_e (SwConst)
swRebuildAll: int = 1
swForceRebuildAll: int = 2
swUpdateMates: int = 4
swCurrentSheetDisp: int = 8
swUpdateDirtyOnly: int = 16

# swRefAxisType_e (SwConst)
swAxisTypeOneLine: int = 0
swAxisTypeTwoPlanes: int = 1
swAxisTypeTwoPoints: int = 2
swAxisTypeCylOrConeFace: int = 3
swAxisTypePtAndPlane: int = 4

# swRefGeometryError_e (SwConst)
swEdgeNotFound: int = -1
swValidEdge: int = 0
swNonlinearEdgeSelection: int = 1
swInvalidEdgeSelection: int = 2

# swRefPlaneReferenceConstraints_e (SwConst)
swRefPlaneReferenceConstraint_Parallel: int = 1
swRefPlaneReferenceConstraint_Perpendicular: int = 2
swRefPlaneReferenceConstraint_Coincident: int = 4
swRefPlaneReferenceConstraint_Distance: int = 8
swRefPlaneReferenceConstraint_Angle: int = 16
swRefPlaneReferenceConstraint_Tangent: int = 32
swRefPlaneReferenceConstraint_Project: int = 64
swRefPlaneReferenceConstraint_MidPlane: int = 128
swRefPlaneReferenceConstraint_OptionFlip: int = 256
swRefPlaneReferenceConstraint_OptionOriginOnCurve: int = 512
swRefPlaneReferenceConstraint_OptionProjectToNearestLocation: int = 1024
swRefPlaneReferenceConstraint_OptionProjectAlongSketchNormal: int = 2048
swRefPlaneReferenceConstraint_ParallelToScreen: int = 4096
swRefPlaneReferenceConstraint_OptionReferenceFlip: int = 8192

# swRefPlaneReferenceIndex_e (SwConst)
swRefPlaneReference_First: int = 0
swRefPlaneReference_Second: int = 1
swRefPlaneReference_Third: int = 2

# swRefPlaneType_e (SwConst)
swRefPlaneInvalid: int = 0
swRefPlaneUndefined: int = 1
swRefPlaneLinePoint: int = 2
swRefPlaneThreePoint: int = 3
swRefPlaneLineLine: int = 4
swRefPlaneDistance: int = 5
swRefPlaneParallel: int = 6
swRefPlaneAngle: int = 7
swRefPlaneNormal: int = 8
swRefPlaneOnSurface: int = 9
swRefPlaneSWStandard: int = 10
swRefPlaneConstraintBase: int = 11

# swRefPointAlongCurveType_e (SwConst)
swRefPointAlongCurveDistance: int = 0
swRefPointAlongCurvePercentage: int = 1
swRefPointAlongCurveEvenlyDistributed: int = 2

# swRefPointType_e (SwConst)
swRefPointInvalid: int = 0
swRefPointUndefined: int = 1
swRefPointAlongCurve: int = 2
swRefPointCenterEdge: int = 3
swRefPointFaceCenter: int = 4
swRefPointFaceVertexProjection: int = 5
swRefPointIntersection: int = 6
swRefPointSketchPoint: int = 7

# swReferencedFileStatus_e (SwConst)
swReferencedFileStatus_FileOk: int = 0
swReferencedFileStatus_InternalIdMismatch: int = 1

# swRegionType_e (SwConst)
swRegionTypeMargins: int = 0
swRegionTypeSheet: int = 1

# swRelativeViewCreationDirection_e (SwConst)
swRelativeViewCreationDirection_FRONT: int = 0
swRelativeViewCreationDirection_RIGHT: int = 1
swRelativeViewCreationDirection_TOP: int = 2
swRelativeViewCreationDirection_BACK: int = 3
swRelativeViewCreationDirection_LEFT: int = 4
swRelativeViewCreationDirection_BOTTOM: int = 5
swRelativeViewCreationDirection_AUXILIARY: int = 6

# swReliefTearTypes_e (SwConst)
swReliefTearTypeRip: int = 1
swReliefTearTypeExtend: int = 2

# swReloadTemplateResult_e (SwConst)
swReloadTemplate_Success: int = 0
swReloadTemplate_UnknownError: int = 1
swReloadTemplate_FileNotFound: int = 2
swReloadTemplate_CustomSheet: int = 3
swReloadTemplate_ViewOnly: int = 4

# swRemainingDofs_e (SwConst)
swRemainingDofs_Restricted: int = 0
swRemainingDofs_Unrestricted: int = 1
swRemainingDofs_Unavailable: int = 2
swRemainingDofs_Failed: int = 3
swRemainingDofs_RootComponent: int = 4

# swRemoveCommandGroupErrors (SwConst)
swRemoveCommandGroup_Failed: int = 0
swRemoveCommandGroup_Success: int = 1

# swRenameDocumentError_e (SwConst)
swRenameDocumentError_None: int = 0
swRenameDocumentError_UnspecifiedInternalError: int = 1
swRenameDocumentError_InvalidSelection: int = 2
swRenameDocumentError_InvalidForDrawings: int = 3
swRenameDocumentError_NoModelLoaded: int = 4
swRenameDocumentError_ComponentNotResolved: int = 5
swRenameDocumentError_LightWeightComponent: int = 6
swRenameDocumentError_RoutingComponent: int = 7
swRenameDocumentError_FileAlreadyExists: int = 8
swRenameDocumentError_InvalidCharactersInName: int = 9
swRenameDocumentError_InvalidVirtualComponent: int = 10
swRenameDocumentError_NameTooLong: int = 11
swRenameDocumentError_DocumentNameInUse: int = 12
swRenameDocumentError_PendingNameAlreadyInUse: int = 13
swRenameDocumentError_ReadOnlyDocument: int = 14
swRenameDocumentError_DocumentNotSaved: int = 15
swRenameDocumentError_VirtualComponent: int = 16
swRenameDocumentError_NotAllowedWithPDM: int = 17
swRenameDocumentError_ToolboxComponent: int = 18
swRenameDocumentError_PatternedComponent: int = 19

# swRenameOptions_e (SwConst)
swRenameOption_Yes: int = 1
swRenameOption_No: int = 2

# swRenamedDocumentFinalAction_e (SwConst)
swRenamedDocumentFinalAction_Default: int = 0
swRenamedDocumentFinalAction_Ok: int = 1
swRenamedDocumentFinalAction_Cancel: int = 2

# swRenderMaterialBumpMap_e (SwConst)
swRenderMaterialBumpMapNone: int = 0
swRenderMaterialBumpMapFrom_File: int = 1
swRenderMaterialBumpMapCasting: int = 2
swRenderMaterialBumpMapRough: int = 3
swRenderMaterialBumpMapTread_Plate: int = 4
swRenderMaterialBumpMapDimpled: int = 5
swRenderMaterialBumpMapKnurled: int = 6
swRenderMaterialBumpMapChips: int = 7
swRenderMaterialBumpMapCircular: int = 8
swRenderMaterialBumpMapRough_Smooth: int = 9

# swRenderMaterialColorForms_e (SwConst)
swRenderMaterialColorFormsColor_Undefined: int = -1
swRenderMaterialColorFormsImage: int = 0
swRenderMaterialColorFormsOne_Color: int = 1
swRenderMaterialColorFormsTwo_Colors: int = 2
swRenderMaterialColorFormsThree_Colors: int = 3

# swRenderMaterialIlluminationTypes_e (SwConst)
swRenderMaterialIlluminationTypes_illumination_undefined: int = -1
swRenderMaterialIlluminationType_use_underlying_material: int = 0
swRenderMaterialIlluminationTypes_constant: int = 1
swRenderMaterialIlluminationType_matte: int = 2
swRenderMaterialIlluminationTypes_plastic: int = 3
swRenderMaterialIlluminationTypes_metal: int = 4
swRenderMaterialIlluminationTypes_satin_finish: int = 5
swRenderMaterialIlluminationTypes_mirror: int = 6
swRenderMaterialIlluminationTypes_conductor: int = 7
swRenderMaterialIlluminationTypes_translucent: int = 8
swRenderMaterialIlluminationTypes_translucent_plastic: int = 9
swRenderMaterialIlluminationTypes_anisotropic: int = 10
swRenderMaterialIlluminationTypes_circular_anisotropic: int = 11
swRenderMaterialIlluminationTypes_woven_anisotropic: int = 12
swRenderMaterialIlluminationTypes_multilayer_paint: int = 13
swRenderMaterialIlluminationTypes_glass: int = 14
swRenderMaterialIlluminationTypes_dielectric: int = 15
swRenderMaterialIlluminationTypes_dielectric_advanced: int = 16
swRenderMaterialIlluminationTypes_cut_hole_with_decal: int = 17
swRenderMaterialIlluminationTypes_studio_plastic: int = 18
swRenderMaterialIlluminationTypes_car_paint: int = 19

# swRendererType_e (SwConst)
swRendererType_Solidworks_Screen: int = 0
swRendererType_Photoworks_Buffer: int = 1

# swReorderComponentsWhere_e (SwConst)
swReorderComponents_After: int = 1
swReorderComponents_Before: int = 2
swReorderComponents_LastInFolder: int = 3
swReorderComponents_FirstInFolder: int = 4

# swRepaintTypes_e (SwConst)
swStandardUpdate: int = 0
swLightUpdate: int = 1
swMaterialUpdate: int = 2
swSectionedUpdate: int = 3
swExplodedUpdate: int = 4
swInsertSketchUpdate: int = 5
swViewDisplayUpdate: int = 6
swDamageRepairUpdate: int = 7
swSelectionUpdate: int = 8
swSectionedExitUpdate: int = 9
swScrollViewUpdate: int = 10

# swRepairSketchOption_e (SwConst)
swRepairSketchCleanup: int = 0
swRepairSketchZeroSegment: int = 1
swRepairSketchMergeSegment: int = 2
swRepairSketchCloseGaps: int = 4
swRepairSketchBreakIntersection: int = 8

# swReplaceComponentError_e (SwConst)
swReplaceComponent_Undefined: int = 0
swReplaceComponent_Success: int = 1
swReplaceComponent_EmptyName: int = 2
swReplaceComponent_InvalidFileName: int = 3
swReplaceComponent_SameModelDifferentPath: int = 4
swReplaceComponent_SameFile: int = 5
swReplaceComponent_NotTopLevelComponent: int = 6
swReplaceComponent_UnknownError: int = 7

# swReplaceComponentsConfiguration_e (SwConst)
swReplaceComponentsConfiguration_MatchName: int = 0
swReplaceComponentsConfiguration_ManuallySelect: int = 1

# swReverseEndPointTangentResult_e (SwConst)
swReverseEndPointTangent_Success: int = 0
swReverseEndPointTangent_InvalidSelection: int = 1
swReverseEndPointTangent_ConstraintConflict: int = 2

# swRevisionCloudShape_e (SwConst)
swRevisionCloudShape_Freehand: int = 0
swRevisionCloudShape_Ellipse: int = 1
swRevisionCloudShape_Rectangle: int = 2
swRevisionCloudShape_Polygon: int = 3

# swRevisionTableMultipleSheetStyle_e (SwConst)
swRevisionTable_SeeSheet1: int = 1
swRevisionTable_LinkedToSheet1: int = 2
swRevisionTable_Independent: int = 3

# swRevisionTableSymbolShape_e (SwConst)
swRevisionTable_CircleSymbol: int = 1
swRevisionTable_SquareSymbol: int = 2
swRevisionTable_TriangleSymbol: int = 3
swRevisionTable_HexagonSymbol: int = 4

# swRevisionTableTagStyle_e (SwConst)
swRevisionTable_AlphabeticTags: int = 1
swRevisionTable_NumericTags: int = 2

# swRevolveOptions_e (SwConst)
swRevolveOptionsNone: int = 0
swAutoCloseSketch: int = 1

# swRevolveType_e (SwConst)
swRevolveTypeOneDirection: int = 0
swRevolveTypeMidPlane: int = 1
swRevolveTypeTwoDirection: int = 2
swRevolveTypeOneDirection360Degrees: int = 3
swRevolveTypeMidPlane360Degrees: int = 4
swRevolveTypeTwoDirection360Degrees: int = 5

# swRibExtrusionDirection_e (SwConst)
swRibParallelToSketch: int = 0
swRibNormalToSketch: int = 1

# swRibType_e (SwConst)
swRibLinear: int = 0
swRibNatural: int = 1

# swRotationAxisIndex_e (SwConst)
swRotationAxisIndex_Unknown: int = -1
swRotationAxisIndex_XYRing: int = 0
swRotationAxisIndex_YZRing: int = 1
swRotationAxisIndex_ZXRing: int = 2

# swRouteComponentTypeID_e (SWRoutingLib)
swRouteCompType_Unknown: int = 0
swRouteCompType_Pipe: int = 1
swRouteCompType_EndConnector: int = 2
swRouteCompType_Flange: int = 3
swRouteCompType_OLet: int = 4
swRouteCompType_Tee: int = 5
swRouteCompType_ReducingTee: int = 6
swRouteCompType_Elbow: int = 7
swRouteCompType_Reducer: int = 8
swRouteCompType_EccentricReducer: int = 9
swRouteCompType_Union: int = 10
swRouteCompType_Adapter: int = 11
swRouteCompType_Cross: int = 12
swRouteCompType_ReducingCross: int = 13
swRouteCompType_Clip: int = 14
swRouteCompType_Support: int = 15
swRouteCompType_Equipment: int = 16
swRouteCompType_TeeAdapter: int = 17
swRouteCompType_HybridComponents: int = 18
swRouteCompType_FittingOther: int = 19
swRouteCompType_Hanger: int = 20
swRouteCompType_ConduitAdapter: int = 21
swRouteCompType_Gasket: int = 22
swRouteCompType_Valve: int = 23
swRouteCompType_RibbonCable: int = 24
swRouteCompType_Tube: int = 25
swRouteCompType_Conduit: int = 26
swRouteCompType_Splice: int = 27
swRouteCompType_ConduitElbow: int = 28
swRouteCompType_AssemblyFittings: int = 29
swRouteCompType_CableTray: int = 30
swRouteCompType_DuctingTrunking: int = 31
swRouteCompType_FlexCableConnector: int = 32
swRouteCompType_Nipple: int = 33

# swRouteType_e (SWRoutingLib)
swRouteType_Electrical: int = 2

# swRoutingComponentGroupingOption_e (SwConst)
swShowOnlyRoutingComponentsInBOM: int = 1
swGroupPipesOrTubesWithTheSameDiameterAndSchedule: int = 2
swDisplayUnitsInBOM: int = 4
swRoutingGroupSpoolComponents: int = 8

# swRoutingExportDataError_e (SWRoutingLib)
swRoutingExportDataError_Success: int = 0
swRoutingExportDataError_UnknownError: int = 1
swRoutingExportDataError_IncorrectFilePath: int = 2
swRoutingExportDataError_AssemblyTypeMismatch: int = 3
swRoutingExportDataError_WrongUnit: int = 4
swRoutingExportDataError_WrongType: int = 5

# swRoutingExportPipeDataError_e (SWRoutingLib)
swRoutingExportPipeDataError_Success: int = 0
swRoutingExportPipeDataError_UnknownError: int = 1
swRoutingExportPipeDataError_IncorrectFilePath: int = 2
swRoutingExportPipeDataError_AssemblyTypeMismatch: int = 3
swRoutingExportPipeDataError_WrongUnit: int = 4

# swRoutingFlattenConnectorOptions_e (SwConst)
swDisplay3DConnectors_e: int = 1
SwUseDrawingConnectorBlocks_e: int = 2

# swRoutingFlattenSegmentOrientation_e (SwConst)
swVertical_e: int = 1
SwHorizontal_e: int = 2

# swRoutingFlattenTypes_e (SwConst)
swAnnotation_e: int = 1
SwManufacture_e: int = 2

# swRoutingSearchType_e (SwConst)
swRoutingConnectorSearch: int = 0
swRoutingComponentSearch: int = 1
swRoutingWireSearch: int = 2
swRoutingCableSearch: int = 3
swRoutingSignalSearch: int = 4
swRoutingPipeSearch: int = 5
swRoutingPipeSegmentSearch: int = 6
swRoutingFittingSearch: int = 7

# swRuledSurfaceType_e (SwConst)
swRuledSurfaceType_TangentToSurface: int = 1
swRuledSurfaceType_NormalToSurface: int = 2
swRuledSurfaceType_TaperedToVector: int = 3
swRuledSurfaceType_PerpendicularToVector: int = 4
swRuledSurfaceType_Sweep: int = 5

# swRunMacroError_e (SwConst)
swRunMacroError_InvalidArg: int = 1
swRunMacroError_MacrosAreDisabled: int = 2
swRunMacroError_NotInDesignMode: int = 3
swRunMacroError_OnlyCodeModules: int = 4
swRunMacroError_OutOfMemory: int = 5
swRunMacroError_InvalidProcname: int = 6
swRunMacroError_InvalidPropertyType: int = 7
swRunMacroError_SuborfuncExpected: int = 8
swRunMacroError_BadParmCount: int = 9
swRunMacroError_BadVarType: int = 10
swRunMacroError_UserInterrupt: int = 11
swRunMacroError_Exception: int = 12
swRunMacroError_Overflow: int = 13
swRunMacroError_TypeMismatch: int = 14
swRunMacroError_ParmNotOptional: int = 15
swRunMacroError_UnknownLcid: int = 16
swRunMacroError_Busy: int = 17
swRunMacroError_ConnectionTerminated: int = 18
swRunMacroError_CallRejected: int = 19
swRunMacroError_CallFailed: int = 20
swRunMacroError_Zombied: int = 21
swRunMacroError_Invalidindex: int = 22
swRunMacroError_NoPermission: int = 23
swRunMacroError_Reverted: int = 24
swRunMacroError_TooManyOpenFiles: int = 25
swRunMacroError_DiskError: int = 26
swRunMacroError_CantSave: int = 27
swRunMacroError_OpenFileFailed: int = 28

# swRunMacroOption_e (SwConst)
swRunMacroDefault: int = 0
swRunMacroUnloadAfterRun: int = 1

# swSFLaySym_e (SwConst)
swSFNone: int = 0
swSFCircular: int = 1
swSFCross: int = 2
swSFMultiDir: int = 3
swSFParallel: int = 4
swSFPerp: int = 5
swSFRadial: int = 6
swSFParticulate: int = 7

# swSFProfileDirection_e (SwConst)
swSFProfileDirectionNone: int = 0
swSFProfileDirectionPerp: int = 1
swSFProfileDirectionParallel: int = 2
swSFProfileDirectionCircular: int = 3
swSFProfileDirectionDefinedAngle: int = 4

# swSFSymType_e (SwConst)
swSFBasic: int = 0
swSFMachining_Req: int = 1
swSFDont_Machine: int = 2
swSFJIS_Surface_Texture_1: int = 3
swSFJIS_Surface_Texture_2: int = 4
swSFJIS_Surface_Texture_3: int = 5
swSFJIS_Surface_Texture_4: int = 6
swSFJIS_No_Machining: int = 7
swSFJIS_Basic: int = 8
swSFJIS_Machining_Req: int = 9

# swSMBendState_e (SwConst)
swSMBendStateNone: int = 0
swSMBendStateSharps: int = 1
swSMBendStateFlattened: int = 2
swSMBendStateFolded: int = 3

# swSMCommandStatus_e (SwConst)
swSMErrorNone: int = 0
swSMErrorUnknown: int = 1
swSMErrorNotAPart: int = 2
swSMErrorNotASheetMetalPart: int = 3
swSMErrorInvalidBendState: int = 4

# swSMGExportProfiles_e (SwConst)
swSMGExportProfiles_Custom: int = 0
swSMGExportProfiles_swDefault: int = 1
swSMGExportProfiles_swWithSurfaceParts: int = 2

# swSMGRefineRelativeType_e (SwConst)
swSMGRefineRelativeType_ChordalError: int = 0
swSMGRefineRelativeType_NormalDeviation: int = 1

# swSMGRefinementType_e (SwConst)
swSMGRefinementType_Relative: int = 0
swSMGRefinementType_Absolute: int = 1

# swSMNormalCutError_e (SwConst)
swSMNormalCutError_NoError: int = 0
swSMNormalCutError_FaceAlreadyExists: int = 1
swSMNormalCutError_InvalidFace: int = 2
swSMNormalCutError_FaceNotPresent: int = 3
swSMNormalCutError_InvalidFaceArray: int = 4

# swSTLQuality_e (SwConst)
swSTLQuality_Coarse: int = 1
swSTLQuality_Fine: int = 2
swSTLQuality_Custom: int = 3

# swSafeArrayType_e (SwConst)
swWordArray: int = 2
swLongArray: int = 3
swDoubleArray: int = 5
swBstrArray: int = 8
swDispatchArray: int = 9
swBooleanArray: int = 11
swUnknownArray: int = 13
swByteArray: int = 16
swUnsignedByteArray: int = 17
swLongLongArray: int = 20
swUnsignedLongLongArray: int = 21

# swSameAs_Status_e (SwConst)
swSameAs_NotImplemented: int = -1
swSameAs_Same: int = 1
swSameAs_Different: int = 0

# swSaveAVIImageSize_e (SwMotionStudy)
swImage_Custom: int = 0
swImage_Screen: int = 1
swImage_160x120: int = 2
swImage_320x200: int = 3
swImage_320x240: int = 4
swImage_512x384: int = 5
swImage_640x480: int = 6
swImage_800x600: int = 7

# swSaveAsOptions_e (SwConst)
swSaveAsOptions_Silent: int = 1
swSaveAsOptions_Copy: int = 2
swSaveAsOptions_SaveReferenced: int = 4
swSaveAsOptions_AvoidRebuildOnSave: int = 8
swSaveAsOptions_UpdateInactiveViews: int = 16
swSaveAsOptions_OverrideSaveEmodel: int = 32
swSaveAsOptions_SaveEmodelData: int = 64
swSaveAsOptions_DetachedDrawing: int = 128
swSaveAsOptions_IgnoreBiography: int = 256
swSaveAsOptions_CopyAndOpen: int = 512
swSaveAsOptions_IncludeVirtualSubAsmComps: int = 1024
swSaveAsOptions_ExportTo2DPdfFromInspection: int = 2048
swSaveAsOptions_PropagateVisualProperties: int = 4096

# swSaveAsVersion_e (SwConst)
swSaveAsCurrentVersion: int = 0
swSaveAsSW98plus: int = 1
swSaveAsFormatProE: int = 2
swSaveAsStandardDrawing: int = 3
swSaveAsDetachedDrawing: int = 4

# swSaveAsmAsPartOptions_e (SwConst)
swSaveAsmAsPart_AllComponents: int = 1
swSaveAsmAsPart_ExteriorComponents: int = 2
swSaveAsmAsPart_ExteriorFaces: int = 3
swSaveAsmAsPart_UserDefinedComponents: int = 4

# swSaveItemsPathError_e (SwConst)
swSaveItemsPathError_Succeeded: int = 0
swSaveItemsPathError_ArraySizeNotMatching: int = 1
swSaveItemsPathError_InvalidPath: int = 2
swSaveItemsPathError_WrongComponentName: int = 3

# swSaveReminderIntervalMode_e (SwConst)
swSaveReminderIntervalMode_Changes: int = 1
swSaveReminderIntervalMode_Minutes: int = 2

# swSaveRestoreSettingsResults_e (SwConst)
swSaveRestoreSettingsSuccess: int = 0
swSaveRestoreSettingsFailure_Generic: int = 1
swSaveRestoreSettingsFailure_InvalidFilename: int = 2

# swSaveToVersion_e (SwConst)
swSaveToVersion_DoNotUpgrade: int = 0
swSaveToVersion_Penultimate: int = 1
swSaveToVersion_Antepenultimate: int = 2

# swSaveWithReferencesOptions_e (SwConst)
swSaveWithReferencesOptions_None: int = 0
swSaveWithReferencesOptions_IncludeVirtualComponents: int = 1
swSaveWithReferencesOptions_IncludeToolBoxParts: int = 2
swSaveWithReferencesOptions_IncludeBrokenReferences: int = 4

# swScaleType_e (SwConst)
swScaleAboutCentroid: int = 0
swScaleAboutOrigin: int = 1
swScaleAboutCoordinateSystem: int = 2

# swSceneBackgroundType_e (SwConst)
swBackgroundType_None: int = 0
swBackgroundType_Plain: int = 1
swBackgroundType_Graduated: int = 2
swBackgroundType_Image: int = 3
swBackgroundType_UseEnvironment: int = 4
swBackgroundType_Color: int = 5

# swSceneFloorAlign_e (SwConst)
swSceneFloorAlign_VIEW: int = 0
swSceneFloorAlign_XY: int = 1
swSceneFloorAlign_YZ: int = 2
swSceneFloorAlign_ZX: int = 3

# swScrewMateDistanceOptions_e (SwConst)
swRevolutionsPerUnitLength: int = 0
swDistancePerRevolution: int = 1

# swSearchFolderTypes_e (SwConst)
swDocumentType: int = 0

# swSearchIndexingPerformance_e (SwConst)
swSearchIndexingPerformanceIndexOnlyWhenComputerIsIdle: int = 0
swSearchIndexingPerformanceAlwaysIndex: int = 1

# swSecondaryMemberBetweenPointsDistanceFromEndType_e (SwConst)
swSecondaryMemberBetweenPointsDistanceFromEndType_Distance: int = 0
swSecondaryMemberBetweenPointsDistanceFromEndType_LengthRatio: int = 1

# swSecondaryMemberUpToMembersDistanceFromEndType_e (SwConst)
swSecondaryMemberUpToMembersDistanceFromEndType_Distance: int = 0
swSecondaryMemberUpToMembersDistanceFromEndType_LengthRatio: int = 1

# swSecondaryMemberUpToMembersMemberPointParameters_e (SwConst)
swSecondaryMemberUpToMembersMemberPointParameters_PointMemberPair: int = 0
swSecondaryMemberUpToMembersMemberPointParameters_FromPoint: int = 1

# swSeedAlignmentReferencePoint_e (SwConst)
swSeedAlignmentReferencePoint_BoundingBoxCenter: int = 0
swSeedAlignmentReferencePoint_ComponentOrigin: int = 1

# swSelectOption_e (SwConst)
swSelectOptionDefault: int = 0
swSelectOptionExtensive: int = 1

# swSelectType_e (SwConst)
swSelNOTHING: int = 0
swSelEDGES: int = 1
swSelFACES: int = 2
swSelVERTICES: int = 3
swSelDATUMPLANES: int = 4
swSelDATUMAXES: int = 5
swSelDATUMPOINTS: int = 6
swSelOLEITEMS: int = 7
swSelATTRIBUTES: int = 8
swSelSKETCHES: int = 9
swSelSKETCHSEGS: int = 10
swSelSKETCHPOINTS: int = 11
swSelDRAWINGVIEWS: int = 12
swSelGTOLS: int = 13
swSelDIMENSIONS: int = 14
swSelNOTES: int = 15
swSelSECTIONLINES: int = 16
swSelDETAILCIRCLES: int = 17
swSelSECTIONTEXT: int = 18
swSelSHEETS: int = 19
swSelCOMPONENTS: int = 20
swSelMATES: int = 21
swSelBODYFEATURES: int = 22
swSelREFCURVES: int = 23
swSelEXTSKETCHSEGS: int = 24
swSelEXTSKETCHPOINTS: int = 25
swSelHELIX: int = 26
swSelREFERENCECURVES: int = 26
swSelREFSURFACES: int = 27
swSelCENTERMARKS: int = 28
swSelINCONTEXTFEAT: int = 29
swSelMATEGROUP: int = 30
swSelBREAKLINES: int = 31
swSelINCONTEXTFEATS: int = 32
swSelMATEGROUPS: int = 33
swSelSKETCHTEXT: int = 34
swSelSFSYMBOLS: int = 35
swSelDATUMTAGS: int = 36
swSelCOMPPATTERN: int = 37
swSelWELDS: int = 38
swSelCTHREADS: int = 39
swSelDTMTARGS: int = 40
swSelPOINTREFS: int = 41
swSelDCABINETS: int = 42
swSelEXPLVIEWS: int = 43
swSelEXPLSTEPS: int = 44
swSelEXPLLINES: int = 45
swSelSILHOUETTES: int = 46
swSelCONFIGURATIONS: int = 47
swSelOBJHANDLES: int = 48
swSelARROWS: int = 49
swSelZONES: int = 50
swSelREFEDGES: int = 51
swSelREFFACES: int = 52
swSelREFSILHOUETTE: int = 53
swSelBOMS: int = 54
swSelEQNFOLDER: int = 55
swSelSKETCHHATCH: int = 56
swSelIMPORTFOLDER: int = 57
swSelVIEWERHYPERLINK: int = 58
swSelMIDPOINTS: int = 59
swSelCUSTOMSYMBOLS: int = 60
swSelCOORDSYS: int = 61
swSelDATUMLINES: int = 62
swSelROUTECURVES: int = 63
swSelBOMTEMPS: int = 64
swSelROUTEPOINTS: int = 65
swSelCONNECTIONPOINTS: int = 66
swSelROUTESWEEPS: int = 67
swSelPOSGROUP: int = 68
swSelBROWSERITEM: int = 69
swSelFABRICATEDROUTE: int = 70
swSelSKETCHPOINTFEAT: int = 71
swSelEMPTYSPACE: int = 72
swSelCOMPSDONTOVERRIDE: int = 72
swSelLIGHTS: int = 73
swSelWIREBODIES: int = 74
swSelSURFACEBODIES: int = 75
swSelSOLIDBODIES: int = 76
swSelFRAMEPOINT: int = 77
swSelSURFBODIESFIRST: int = 78
swSelMANIPULATORS: int = 79
swSelPICTUREBODIES: int = 80
swSelSOLIDBODIESFIRST: int = 81
swSelHOLESERIES: int = 83
swSelLEADERS: int = 84
swSelSKETCHBITMAP: int = 85
swSelDOWELSYMS: int = 86
swSelEXTSKETCHTEXT: int = 88
swSelBLOCKINST: int = 93
swSelFTRFOLDER: int = 94
swSelSKETCHREGION: int = 95
swSelSKETCHCONTOUR: int = 96
swSelBOMFEATURES: int = 97
swSelANNOTATIONTABLES: int = 98
swSelBLOCKDEF: int = 99
swSelCENTERMARKSYMS: int = 100
swSelSIMULATION: int = 101
swSelSIMELEMENT: int = 102
swSelCENTERLINES: int = 103
swSelHOLETABLEFEATS: int = 104
swSelHOLETABLEAXES: int = 105
swSelWELDMENT: int = 106
swSelSUBWELDFOLDER: int = 107
swSelEXCLUDEMANIPULATORS: int = 111
swSelREVISIONTABLE: int = 113
swSelSUBSKETCHINST: int = 114
swSelWELDMENTTABLEFEATS: int = 116
swSelBODYFOLDER: int = 118
swSelREVISIONTABLEFEAT: int = 119
swSelSUBATOMFOLDER: int = 121
swSelWELDBEADS: int = 122
swSelEMBEDLINKDOC: int = 123
swSelJOURNAL: int = 124
swSelDOCSFOLDER: int = 125
swSelCOMMENTSFOLDER: int = 126
swSelCOMMENT: int = 127
swSelSWIFTANNOTATIONS: int = 130
swSelSWIFTFEATURES: int = 132
swSelCAMERAS: int = 136
swSelMATESUPPLEMENT: int = 138
swSelANNOTATIONVIEW: int = 139
swSelGENERALTABLEFEAT: int = 142
swSelDISPLAYSTATE: int = 148
swSelBELTCHAINFEATS: int = 149
swSelSUBSKETCHDEF: int = 154
swSelSWIFTSCHEMA: int = 159
swSelTITLEBLOCK: int = 192
swSelTITLEBLOCKTABLEFEAT: int = 206
swSelOBJGROUP: int = 207
swSelPLANESECTIONS: int = 219
swSelCOSMETICWELDS: int = 220
SwSelMAGNETICLINES: int = 225
swSelPUNCHTABLEFEATS: int = 234
swSelREVISIONCLOUDS: int = 240
swSelBorder: int = 254
swSelSELECTIONSETFOLDER: int = 258
swSelSELECTIONSETNODE: int = 259
swSelGRAPHICSBODY: int = 262
swSelFACETS: int = 268
swSelMESHFACETEDGES: int = 269
swSelMESHFACETVERTICES: int = 270
swSelMESHSOLIDBODIES: int = 274
swSelADVSTRUCTMEMBER: int = 295
swSelFAMILYTABLEFEAT: int = 316
swSelFAMILYTABLE: int = 317
swSelEVERYTHING: int = -3
swSelLOCATIONS: int = -2
swSelUNSUPPORTED: int = -1

# swSelectionMarkAction_e (SwConst)
swSelectionMarkSet: int = 0
swSelectionMarkAppend: int = 1
swSelectionMarkRemove: int = 2
swSelectionMarkClear: int = 3

# swSelectionReferenceTypes_e (SwConst)
swReferenceTypeVertex: int = 1
swReferenceTypeEdge: int = 2
swReferenceTypeFace: int = 3
swReferenceTypeRefSurface: int = 4
swReferenceTypeRefPlan: int = 5
swReferenceTypeSketchPoint: int = 6
swReferenceTypeBody: int = 7

# swSensorAlertType_e (SwConst)
swSensorAlert_GreaterThan: int = 0
swSensorAlert_LessThan: int = 1
swSensorAlert_Exactly: int = 2
swSensorAlert_NotGreaterThan: int = 3
swSensorAlert_NotLessThan: int = 4
swSensorAlert_NotExactly: int = 5
swSensorAlert_Between: int = 6
swSensorAlert_NotBetween: int = 7
swSensorAlert_True: int = 8
swSensorAlert_False: int = 9

# swSensorType_e (SwConst)
swSensorSimulation: int = 0
swSensorMassProperty: int = 1
swSensorDimension: int = 2
swSensorInterfaceDetection: int = 3
swSensorProximity: int = 5

# swSetComponentIdentifierResult_e (SwConst)
swSetComponentIdentifierResult_Success: int = 0
swSetComponentIdentifierResult_InvalidPrimary: int = 1
swSetComponentIdentifierResult_InvalidSecondary: int = 2
swSetComponentIdentifierResult_InvalidTertiary: int = 4
swSetComponentIdentifierResult_BlockedBySystemOption: int = 8

# swSetComponentsAndTransformsStatus_e (SwConst)
swSetComponentsAndTransforms_Failed: int = 0
swSetComponentsAndTransforms_Succeeded: int = 1
swSetComponentsAndTransforms_InvalidInput: int = 2

# swSetHelixRegionParameterStatus_e (SwConst)
swSetHelixRegionParam_Succeeded: int = 0
swSetHelixRegionParam_Failed: int = 1
swSetHelixRegionParam_InvalidInput: int = 2

# swSetRouteFixedLengthError_e (SwConst)
swSetRouteFixedLengthError_NoError: int = 0
swSetRouteFixedLengthError_NotFixedLengthSegment: int = 1
swSetRouteFixedLengthError_NotFlexible: int = 2
swSetRouteFixedLengthError_NoProperty: int = 3
swSetRouteFixedLengthError_SetLengthFailed: int = 4
swSetRouteFixedLengthError_SelectionFailed: int = 5
swSetRouteFixedLengthError_FailedMinBendRadius: int = 6

# swSetRoutePathForWireErrorType_e (SWRoutingLib)
swSetRoutePathSuccess: int = 0
swSetRoutePathTooManyConnectorsSelected: int = 1
swSetRoutePathFailed: int = 2

# swSetSectionLabelStatus_e (SwConst)
swSetSectionLabel_DuplicateLabelFailure: int = -2
swSetSectionLabel_Failure: int = -1
swSetSectionLabel_Okay: int = 0
swSetSectionLabel_DuplicateLabelWarning: int = 1

# swSetValueInConfiguration_e (SwConst)
swSetValue_NoConfiguration: int = -1
swSetValue_UseCurrentSetting: int = 0
swSetValue_InThisConfiguration: int = 1
swSetValue_InAllConfigurations: int = 2
swSetValue_InSpecificConfigurations: int = 3

# swSetValueReturnStatus_e (SwConst)
swSetValue_Successful: int = 0
swSetValue_Failure: int = 1
swSetValue_InvalidValue: int = 2
swSetValue_DrivenDimension: int = 3
swSetValue_ModelNotLoaded: int = 4
swSetValue_FrozenFeatureOwner: int = 5

# swSheetMetalAutoReliefTypes_e (SwConst)
swSheetMetalAutoReliefTypes_e_Rectangular: int = 1
swSheetMetalAutoReliefTypes_e_Obround: int = 2
swSheetMetalAutoReliefTypes_e_Tear: int = 3

# swSheetMetalBendNotesBorderSize_e (SwConst)
swSheetMetalBendNotesBorderSizeTightFit: int = 0
swSheetMetalBendNotesBorderSizeOneCharacter: int = 1
swSheetMetalBendNotesBorderSizeTwoCharacters: int = 2
swSheetMetalBendNotesBorderSizeThreeCharacters: int = 3
swSheetMetalBendNotesBorderSizeFourCharacters: int = 4
swSheetMetalBendNotesBorderSizeFiveCharacters: int = 5
swSheetMetalBendNotesBorderSizeUserDefined: int = 6

# swSheetMetalGussetProfileDimType_e (SwConst)
swSheetMetalGussetProfileDimType_IndentDepth: int = 0
swSheetMetalGussetProfileDimType_ProfileDimensions: int = 1

# swSheetMetalGussetProfileType_e (SwConst)
swSheetMetalGussetProfileType_Rib: int = 0
swSheetMetalGussetProfileType_Custom: int = 1

# swSheetMetalMBDBendNotesStyle_e (SwConst)
swSheetMetalMBDBendNotesStyle_AboveBendLine: int = 0
swSheetMetalMBDBendNotesStyle_BelowBendLine: int = 1
swSheetMetalMBDBendNotesStyle_WithLeader: int = 2

# swSheetMetalModifierError_e (SwConst)
swSheetMetalModifierError_NoError: int = 0
swSheetMetalModifierError_OldArchitecture: int = 1
swSheetMetalModifierError_NotEnabledOnTemplate: int = 2
swSheetMetalModifierError_InvalidProperty: int = 3
swSheetMetalModifierError_UnspecifiedError: int = 4
swSheetMetalModifierError_GaugeTablePathNotEmpty: int = 5

# swSheetMetalOverlapTypes_e (SwConst)
swSheetMetalOverlapTypes_OpenButt: int = 0
swSheetMetalOverlapTypes_Overlap: int = 1
swSheetMetalOverlapTypes_Underlap: int = 2

# swSheetMetalOverrideDefaultParameters_e (SwConst)
swSheetMetalOverrideDefaultParameters_BendParameters: int = 0
swSheetMetalOverrideDefaultParameters_BendAllowance: int = 1
swSheetMetalOverrideDefaultParameters_AutoRelief: int = 2

# swSheetMetalReliefTypes_e (SwConst)
swSheetMetalReliefRectangular: int = 1
swSheetMetalReliefTear: int = 2
swSheetMetalReliefObround: int = 3
swSheetMetalReliefNone: int = 4
swSheetMetalReliefTearBend: int = 5

# swSheetMetalRibGussetType_e (SwConst)
swSheetMetalRibGussetType_Rounded: int = 0
swSheetMetalRibGussetType_Flat: int = 1

# swSheetPrintQuadrant_e (SwConst)
swSheetPrintQuadNotSet: int = 0
swSheetPrintQuadQ1: int = 1
swSheetPrintQuadQ2: int = 2
swSheetPrintQuadQ3: int = 3
swSheetPrintQuadQ4: int = 4

# swSheetSewingError_e (SwConst)
swSewingOk: int = 0
swBadArgument: int = 1
swUnspecifiedError: int = 2
swSewingFailed: int = 3
swSewingIncomplete: int = 4

# swSheetSewingOption_e (SwConst)
swSewToSolid: int = 0
swSewToSheets: int = 1
swSewToSolidOrSheets: int = 2

# swShowMessageBarResult_e (SwConst)
swShowMessageBarResult_Shown: int = 0
swShowMessageBarResult_DontShowAgain: int = 1
swShowMessageBarResult_FailedInvalidDefinition: int = 2
swShowMessageBarResult_FailedInvalidHandler: int = 3

# swShowNotificationResult_e (SwConst)
swShowNotificationResult_Shown: int = 0
swShowNotificationResult_DontShowAgain: int = 1
swShowNotificationResult_FailedInvalidDefinition: int = 2
swShowNotificationResult_FailedInvalidHandler: int = 3

# swShutOffSurfaceFeatureStatus_e (SwConst)
STATUS_SHUTOFF_REDUNDANT: int = 1
STATUS_SHUTOFF_COMPLETE: int = 2
STATUS_SHUTOFF_INCOMPLETE: int = 3

# swShutOffSurfacePatchType_e (SwConst)
swPatchTypeNoFill: int = 0
swPatchTypeContact: int = 1
swPatchTypeTangent: int = 2

# swSimpleFilletPartialEdgeCondition_e (SwConst)
swPartialEdgeNone: int = 0
swPartialEdgeDistanceOffset: int = 1
swPartialEdgePercentOffset: int = 2
swPartialEdgeReferenceOffset: int = 3

# swSimpleFilletType_e (SwConst)
swConstRadiusFillet: int = 0
swFaceFillet: int = 2
swFullRoundFillet: int = 3

# swSimpleFilletWhichFaces_e (SwConst)
swSimpleFilletSingleRadius: int = 0
swFaceFilletSet1: int = 1
swFaceFilletSet2: int = 2
swFullRoundFilletSet1: int = 3
swFullRoundFilletCenterSet: int = 4
swFullRoundFilletSet2: int = 5

# swSimulationDamperType_e (SwConst)
swSimulationDamper_Linear: int = 0
swSimulationDamper_Torsional: int = 1

# swSimulationForceActionType_e (SwConst)
swSimulationForceAction_ActionOnly: int = 0
swSimulationForceAction_ActionAndRecation: int = 1

# swSimulationForceFunctionType_e (SwConst)
swSimulationForceFunction_Constant: int = 0
swSimulationForceFunction_Step: int = 1
swSimulationForceFunction_Harmonic: int = 2
swSimulationForceFunction_Function: int = 3
swSimulationForceFunction_Spline: int = 4

# swSimulationForceType_e (SwConst)
swSimulationForce_LinearForce: int = 0
swSimulationForce_Torque: int = 1

# swSimulationGravityAxisName_e (SwConst)
swSimulationGravityAxis_Invalid: int = -1
swSimulationGravityAxis_X: int = 0
swSimulationGravityAxis_Y: int = 1
swSimulationGravityAxis_Z: int = 2

# swSimulationMotorDriveType_e (SwConst)
swSimulationMotorDrive_Displacement: int = 0
swSimulationMotorDrive_Velocity: int = 1
swSimulationMotorDrive_Acceleration: int = 2

# swSimulationMotorMotionType_e (SwConst)
swSimulationMotorMotion_Constant: int = 0
swSimulationMotorMotion_Step: int = 1
swSimulationMotorMotion_Harmonic: int = 2
swSimulationMotorMotion_Function: int = 3
swSimulationMotorMotion_Spline: int = 4

# swSimulationMotorType_e (SwConst)
swSimulationLinearMotor: int = 0
swSimulationRotaryMotor: int = 1

# swSimulationSpringType_e (SwConst)
swSimulationSpring_Linear: int = 0
swSimulationSpring_Torsional: int = 1

# swSkInternalPntOpts_e (SwConst)
swSkPntsOff: int = 0
swSkPntsOn: int = 1
swSkPntsDefault: int = 2

# swSkOffsetCapEndType_e (SwConst)
swSkOffsetNoCaps: int = 0
swSkOffsetArcCaps: int = 1
swSkOffsetLineCaps: int = 2

# swSkOffsetMakeConstructionType_e (SwConst)
swSkOffsetDontMakeConstruction: int = 0
swSkOffsetMakeOrigConstruction: int = 1
swSkOffsetMakeOffsConstruction: int = 2
swSkOffsetMakeBothConstruction: int = 3

# swSketchChamferType_e (SwConst)
swSketchChamfer_DistanceAngle: int = 0
swSketchChamfer_DistanceDistance: int = 1
swSketchChamfer_DistanceEqual: int = 2

# swSketchCheckFeatureProfileUsage_e (SwConst)
swSketchCheckFeature_UNSET: int = 0
swSketchCheckFeature_BASEEXTRUDE: int = 1
swSketchCheckFeature_BASEEXTRUDETHIN: int = 2
swSketchCheckFeature_BOSSEXTRUDE: int = 3
swSketchCheckFeature_BOSSEXTRUDETHIN: int = 4
swSketchCheckFeature_SURFACEEXTRUDE: int = 5
swSketchCheckFeature_BASEREVOLVE: int = 6
swSketchCheckFeature_BASEREVOLVETHIN: int = 7
swSketchCheckFeature_BOSSREVOLVE: int = 8
swSketchCheckFeature_BOSSREVOLVETHIN: int = 9
swSketchCheckFeature_SURFACEREVOLVE: int = 10
swSketchCheckFeature_CUTEXTRUDE: int = 11
swSketchCheckFeature_CUTEXTRUDETHIN: int = 12
swSketchCheckFeature_CUTREVOLVE: int = 13
swSketchCheckFeature_CUTREVOLVETHIN: int = 14
swSketchCheckFeature_SWEEPSECTION: int = 15
swSketchCheckFeature_SURFACESWEEPSECTION: int = 16
swSketchCheckFeature_SWEEPPATHORGUIDE: int = 17
swSketchCheckFeature_LOFTSECTION: int = 18
swSketchCheckFeature_SURFACELOFTSECTION: int = 19
swSketchCheckFeature_LOFTGUIDE: int = 20
swSketchCheckFeature_RIBSECTION: int = 21
swSketchCheckFeature_SHEETMETAL_BASEFLANGE: int = 22
swSketchCheckFeature_MOLD_PARTINGSURFACES: int = 23

# swSketchCheckFeatureStatus_e (SwConst)
swSketchCheckFeatureStatus_UnknownError: int = -1
swSketchCheckFeatureStatus_OK: int = 0
swSketchCheckFeatureStatus_EntXEnt: int = 1
swSketchCheckFeatureStatus_EntXSelf: int = 2
swSketchCheckFeatureStatus_EntUnspecBad: int = 3
swSketchCheckFeatureStatus_ThreeEnts: int = 4
swSketchCheckFeatureStatus_EmptySketch: int = 5
swSketchCheckFeatureStatus_WrongOpen: int = 6
swSketchCheckFeatureStatus_WrongManyContours: int = 7
swSketchCheckFeatureStatus_ZeroLengthEnt: int = 8
swSketchCheckFeatureStatus_ManyOpen: int = 9
swSketchCheckFeatureStatus_NoOpen: int = 10
swSketchCheckFeatureStatus_MixedContours: int = 11
swSketchCheckFeatureStatus_CturXCtur: int = 12
swSketchCheckFeatureStatus_DisjCturs: int = 13
swSketchCheckFeatureStatus_OpenWantClosed: int = 14
swSketchCheckFeatureStatus_ClosedWantOpen: int = 15
swSketchCheckFeatureStatus_DoubleContainment: int = 16
swSketchCheckFeatureStatus_MoreThanOneContour: int = 17
swSketchCheckFeatureStatus_OneOpenContourExpected: int = 18
swSketchCheckFeatureStatus_OneClosedContourExpected: int = 19
swSketchCheckFeatureStatus_WantSingleOpenOrMultiClosedDisjoint: int = 20
swSketchCheckFeatureStatus_NeedsAxis: int = 21
swSketchCheckFeatureStatus_OpenOrUnclear: int = 22
swSketchCheckFeatureStatus_ContourIntersectsCenterLine: int = 23

# swSketchEntityType_e (SwConst)
swSketchEntityPoint: int = 1
swSketchEntityLine: int = 2
swSketchEntityArc: int = 3
swSketchEntityEllipse: int = 4
swSketchEntityParabola: int = 5
swSketchEntitySpline: int = 6

# swSketchFullyDefineRelationType_e (SwConst)
swSketchFullyDefineRelationType_Equal: int = 1
swSketchFullyDefineRelationType_Horizontal: int = 2
swSketchFullyDefineRelationType_Vertical: int = 4
swSketchFullyDefineRelationType_Tangent: int = 8
swSketchFullyDefineRelationType_Perpendicular: int = 16
swSketchFullyDefineRelationType_Colinear: int = 32
swSketchFullyDefineRelationType_Concentric: int = 64
swSketchFullyDefineRelationType_Parallel: int = 128
swSketchFullyDefineRelationType_Midpoint: int = 256
swSketchFullyDefineRelationType_Coincident: int = 512

# swSketchPictureTransparencyStyle_e (SwConst)
swSketchPictureTransparencyNone: int = 0
swSketchPictureTransparencyFromFile: int = 1
swSketchPictureTransparencyFullImage: int = 2
swSketchPictureTransparencyUserDefined: int = 3

# swSketchPointType_e (SwConst)
swSketchPointType_Unknown: int = -1
swSketchPointType_Internal: int = 0
swSketchPointType_User: int = 1
swSketchPointType_Spline: int = 2
swSketchPointType_Datum: int = 3
swSketchPointType_VirtualSharp: int = 4
swSketchPointType_Parabola: int = 5
swSketchPointType_MidPoint: int = 6
swSketchPointType_FramePoint: int = 7
swSketchPointType_Origin: int = 8
swSketchPointType_Ellipse: int = 9
swSketchPointType_External: int = 10

# swSketchRelationEntityTypes_e (SwConst)
swSketchRelationEntityType_Unknown: int = 0
swSketchRelationEntityType_SubSketch: int = 1
swSketchRelationEntityType_Point: int = 2
swSketchRelationEntityType_Line: int = 3
swSketchRelationEntityType_Arc: int = 4
swSketchRelationEntityType_Ellipse: int = 5
swSketchRelationEntityType_Parabola: int = 6
swSketchRelationEntityType_Spline: int = 7
swSketchRelationEntityType_Hatch: int = 8
swSketchRelationEntityType_Text: int = 9
swSketchRelationEntityType_Plane: int = 10
swSketchRelationEntityType_Cylinder: int = 11
swSketchRelationEntityType_Sphere: int = 12
swSketchRelationEntityType_Surface: int = 13
swSketchRelationEntityType_Dimension: int = 14

# swSketchRelationFilterType_e (SwConst)
swAll: int = 0
swDangling: int = 1
swOverDefining: int = 2
swExternal: int = 3
swDefinedInContext: int = 4
swLocked: int = 5
swBroken: int = 6
swSelectedEntities: int = 7

# swSketchSegmentType_e (SwConst)
swSketchSegmentType_sketchpoints: int = 1
swSketchSegmentType_sketchsegments: int = 2

# swSketchSegments_e (SwConst)
swSketchLINE: int = 0
swSketchARC: int = 1
swSketchELLIPSE: int = 2
swSketchSPLINE: int = 3
swSketchTEXT: int = 4
swSketchPARABOLA: int = 5

# swSketchSlotCreationType_e (SwConst)
swSketchSlotCreationType_line: int = 0
swSketchSlotCreationType_center_line: int = 1
swSketchSlotCreationType_arc: int = 2
swSketchSlotCreationType_3pointarc: int = 3

# swSketchSlotLengthType_e (SwConst)
swSketchSlotLengthType_CenterCenter: int = 0
swSketchSlotLengthType_FullLength: int = 1

# swSketchTrimChoice_e (SwConst)
swSketchTrimClosest: int = 0
swSketchTrimCorner: int = 1
swSketchTrimTwoEntities: int = 2
swSketchTrimEntityPoint: int = 3
swSketchTrimEntities: int = 4
swSketchTrimOutside: int = 5
swSketchTrimInside: int = 6

# swSlicingTypes_e (SwConst)
swSlicingTypes_None: int = 0
swSlicingTypes_Intersection: int = 1
swSlicingTypes_Exact: int = 2
swSlicingTypes_Circle: int = 4
swSlicingTypes_Rectangle: int = 8

# swSlotMateConstraintOptions_e (SwConst)
swSlotMateConstraintOption_Free: int = 0
swSlotMateConstraintOption_Centered: int = 1
swSlotMateConstraintOption_Distance: int = 2
swSlotMateConstraintOption_Percent: int = 3

# swSmartComponentSelectionTypes_e (SwConst)
swSmartComponentFeatures: int = 1
swSmartComponentComponents: int = 2

# swSmartDimensionDirection_e (SwConst)
swSmartDimensionDirection_Right: int = 0
swSmartDimensionDirection_Up: int = 1
swSmartDimensionDirection_Left: int = 2
swSmartDimensionDirection_Down: int = 3

# swSolidBodiesDescriptionPropertyIndex (SwConst)
swSolidBodiesDescriptionProp_None: int = 0
swSolidBodiesDescriptionProp_Length: int = 1
swSolidBodiesDescriptionProp_Thickness: int = 2
swSolidBodiesDescriptionProp_Width: int = 3

# swSolidworksEditionOptions_e (SwConst)
SolidworksUnknownEdition: int = 0
SolidworksCommercialEdition: int = 1
SolidworksEducationalEdition: int = 2
SolidworksStudentEdition: int = 3
SolidworksStudentDesignKitEdition: int = 4
SolidworksPersonalEdition: int = 5
SolidworksMakerEdition: int = 6

# swSolidworksWeldmentEndCondOptions_e (SwConst)
swEndConditionNone: int = 0
swEndConditionMiter: int = 1
swEndConditionButt1: int = 2
swEndConditionButt2: int = 3
swEndConditionTrim: int = 4
swEndConditionUseDefault: int = 5

# swSpecialMotionEventType_e (SwMotionStudy)
swSpecialMotionEventType_Contact: int = 1

# swSpeedpakUpdate_e (SwConst)
swSpeedpakUpdate_All: int = 0
swSpeedpakUpdate_None: int = 1
swSpeedpakUpdate_WithRebuildOnSaveMark: int = 2

# swSplitBodyType_e (SwConst)
swSplitBodyType_e_Show: int = 0
swSplitBodyType_e_Hide: int = 1
swSplitBodyType_e_Consume: int = 2

# swSplitFaceOnParam_e (SwConst)
swSplitFaceOnParamU: int = 1
swSplitFaceOnParamV: int = 2

# swSplitFacesOption_e (SwConst)
swSplitFacesAtPlusMinusDraftTransition: int = 0
swSplitFacesAtSpecifiedAngle: int = 1

# swSplitLineFeatureType_e (SwConst)
swSplitLineFeatureType_Draft: int = 0
swSplitLineFeatureType_Projection: int = 1
swSplitLineFeatureType_Intersection: int = 2

# swSplitLineSplitSurfaceType_e (SwConst)
swSplitLineSplitSurfaceType_Natural: int = 0
swSplitLineSplitSurfaceType_Linear: int = 1

# swSplitMemberDimensionType_e (SwConst)
swSplitMemberDimensionType_SplitLength: int = 0
swSplitMemberDimensionType_Instance: int = 1

# swSpringDefineType_e (SwConst)
swSpringDefineType_PitchAndRevolution: int = 0
swSpringDefineType_HeightAndRevolution: int = 1
swSpringDefineType_HeightAndPitch: int = 2

# swSpringExtensionEndType_e (SwConst)
swSpringExtensionEndType_FullLoop: int = 0
swSpringExtensionEndType_HalfLoop: int = 1
swSpringExtensionEndType_UserDefined: int = 2

# swSpringProfileType_e (SwConst)
swSpringProfileType_Circle: int = 0
swSpringProfileType_Rectangle: int = 1
swSpringProfileType_Trapezoid: int = 2

# swSpringTorsionEndType_e (SwConst)
swSpringTorsionEndType_Hook: int = 0
swSpringTorsionEndType_Straight: int = 1
swSpringTorsionEndType_Hinge: int = 2
swSpringTorsionEndType_StraightOffset: int = 3

# swSpringType_e (SwConst)
swSpringType_Compression: int = 0
swSpringType_Extension: int = 1
swSpringType_Torsion: int = 2
swSpringType_Spiral: int = 3

# swStackedBalloonDirection_e (SwConst)
swStackedBalloonDir_None: int = 0
swStackedBalloonDir_Up: int = 1
swStackedBalloonDir_Down: int = 2
swStackedBalloonDir_Left: int = 3
swStackedBalloonDir_Right: int = 4

# swStandardHeaderFooterPageSetupTexts_e (SwConst)
swHeaderFooterText_PageNumber: int = 1
swHeaderFooterText_PageCount: int = 2
swHeaderFooterText_Date: int = 3
swHeaderFooterText_Time: int = 4
swHeaderFooterText_Filename: int = 5

# swStandardViews_e (SwConst)
swFrontView: int = 1
swBackView: int = 2
swLeftView: int = 3
swRightView: int = 4
swTopView: int = 5
swBottomView: int = 6
swIsometricView: int = 7
swTrimetricView: int = 8
swDimetricView: int = 9

# swStartConditions_e (SwConst)
swStartSketchPlane: int = 0
swStartSurface: int = 1
swStartVertex: int = 2
swStartOffset: int = 3

# swStep242Error_e (SwConst)
swPublishStep242_Success: int = 0
swPublishStep242_InvalidPath: int = 1
swPublishStep242_UnknownError: int = 3
swPublishStep242_MBDLicenseNotAvailable: int = 4
swPublishStep242_EditionError: int = 5
swPublishStep242_CustomPropertyError: int = 6

# swStopContinuePrompt_e (SwConst)
swContinueResponse_Stop: int = 1
swContinueResponse_Continue: int = 2
swContinueResponse_Prompt: int = 3

# swStraightHoleClassificationType_e (SwConst)
swStraightHoleClassificationType_Nominal: int = 0
swStraightHoleClassificationType_Clearance: int = 1
swStraightHoleClassificationType_Transitional: int = 2
swStraightHoleClassificationType_Press: int = 3

# swStraightHoleFilter_e (SwConst)
swStraightHoleFilter_All: int = 0
swStraightHoleFilter_Nuts: int = 1
swStraightHoleFilter_Fasteners: int = 2
swStraightHoleFilter_Standoffs: int = 3
swStraightHoleFilter_Studs: int = 4
swStraightHoleFilter_Pins: int = 5

# swStraightHoleFitType_e (SwConst)
swStraightHoleFitType_Close: int = 0
swStraightHoleFitType_Normal: int = 1
swStraightHoleFitType_Loose: int = 2

# swStraightTapHoleCustomSizing_e (SwConst)
swStraightTapHoleCustomSizing_TapDrillDiameter: int = 0
swStraightTapHoleCustomSizing_TapDrillDiameterWithCosmeticThread: int = 1
swStraightTapHoleCustomSizing_MajorDiameter: int = 2

# swStraightTapHoleEquation_e (SwConst)
swStraightTapHoleEquation_Diameter: int = 0
swStraightTapHoleEquation_DiameterAndHalf: int = 1
swStraightTapHoleEquation_TwiceTheDiameter: int = 2
swStraightTapHoleEquation_UserDefinedValue: int = 3

# swStraightTapHoleThreadClass_e (SwConst)
swStraightTapHoleThreadClass_1B: int = 1
swStraightTapHoleThreadClass_2B: int = 2
swStraightTapHoleThreadClass_3B: int = 3

# swStructureProfileAlignmentType_e (SwConst)
swStructureProfileAlignmentType_HorizontalAxis: int = 0
swStructureProfileAlignmentType_VerticalAxis: int = 1

# swStructureProfileMirrorType_e (SwConst)
swStructureProfileMirrorType_HorizontalAxis: int = 0
swStructureProfileMirrorType_VerticalAxis: int = 1

# swStructureProfilePiercePointType_e (SwConst)
swStructureProfilePiercePoint_Center: int = 0
swStructureProfilePiercePoint_TopCenter: int = 1
swStructureProfilePiercePoint_BottomCenter: int = 2
swStructureProfilePiercePoint_TopLeft: int = 3
swStructureProfilePiercePoint_TopRight: int = 4
swStructureProfilePiercePoint_CenterLeft: int = 5
swStructureProfilePiercePoint_CenterRight: int = 6
swStructureProfilePiercePoint_BottomLeft: int = 7
swStructureProfilePiercePoint_BottomRight: int = 8
swStructureProfilePiercePoint_Selection: int = 9

# swStructureSplitMemberType_e (SwConst)
swStructureSplitMember_Reference: int = 0
swStructureSplitMember_Dimension: int = 1

# swStructureSystemMemberCreationType_e (SwConst)
swStructureSystemMemberCreationType_Primary_PathSegment: int = 0
swStructureSystemMemberCreationType_Primary_RefPlane: int = 1
swStructureSystemMemberCreationType_Primary_PointLength: int = 2
swStructureSystemMemberCreationType_Primary_FacePlaneIntersection: int = 3
swStructureSystemMemberCreationType_Secondary_SupportPlane: int = 4
swStructureSystemMemberCreationType_Secondary_BetweenPoints: int = 5
swStructureSystemMemberCreationType_Secondary_UpToMembers: int = 6

# swStructureSystemMemberType_e (SwConst)
swStructureSystemMemberType_Primary: int = 0
swStructureSystemMemberType_Secondary: int = 1

# swStyleSplineCurveType_e (SwConst)
BezierCurve: int = 0
BSpline_Degree3: int = 1
BSpline_Degree5: int = 2
BSpline_Degree7: int = 3

# swSummInfoField_e (SwConst)
swSumInfoTitle: int = 0
swSumInfoSubject: int = 1
swSumInfoAuthor: int = 2
swSumInfoKeywords: int = 3
swSumInfoComment: int = 4
swSumInfoSavedBy: int = 5
swSumInfoCreateDate: int = 6
swSumInfoSaveDate: int = 7
swSumInfoCreateDate2: int = 8
swSumInfoSaveDate2: int = 9

# swSunlightInfoType_e (SwConst)
swSunlight_Sunrise: int = 1
swSunlight_Sunset: int = 2
swSunlight_LengthOfDay: int = 3

# swSuppressDialog_e (SwConst)
swSuppressDialog_None: int = 1
swSuppressDialog_All: int = 2
swSuppressDialog_LocateReference: int = 4

# swSuppressionError_e (SwConst)
swSuppressionBadComponent: int = 0
swSuppressionBadState: int = 1
swSuppressionChangeOk: int = 2
swSuppressionChangeFailed: int = 3

# swSurfaceCutFeatureError_e (SwConst)
swSurfaceCutFeatureError_NoError: int = 0
swSurfaceCutFeatureError_BodiesNotSpecified: int = 1
swSurfaceCutFeatureError_InvalidVariant: int = 2

# swSurfaceExtendEndCond_e (SwConst)
swSurfaceExtendEndCondDistance: int = 0
swSurfaceExtendEndCondUpToPoint: int = 1
swSurfaceExtendEndCondUpToSurface: int = 2

# swSurfaceFinishSymbolOrientation_e (SwConst)
swSFOrientation_Upright: int = 1
swSFOrientation_Rotated90: int = 2
swSFOrientation_Perpendicular: int = 3
swSFOrientation_PerpendicularFlipped: int = 4
swSFOrientation_UserDefined: int = 5

# swSurfaceFinishSymbolText_e (SwConst)
swSFSymbolMaterialRemovalAllowance: int = 1
swSFSymbolProductionMethod: int = 2
swSFSymbolSamplingLength: int = 3
swSFSymbolOtherRoughnessValue: int = 4
swSFSymbolMaximumRoughness: int = 5
swSFSymbolMinimumRoughness: int = 6
swSFSymbolRoughnessSpacing: int = 7
swSFSymbolRoughnessValue1: int = 8
swSFSymbolRoughnessValue2: int = 9
swSFSymbolRoughnessValue3: int = 10

# swSurfaceTrimType_e (SwConst)
swTypeTrimTool: int = 0
swTypeMutualTrim: int = 1

# swSurfaceTypes_e (SwConst)
PLANE_TYPE: int = 4001
CYLINDER_TYPE: int = 4002
CONE_TYPE: int = 4003
SPHERE_TYPE: int = 4004
TORUS_TYPE: int = 4005
BSURF_TYPE: int = 4006
BLEND_TYPE: int = 4007
OFFSET_TYPE: int = 4008
EXTRU_TYPE: int = 4009
SREV_TYPE: int = 4010

# swSustainabilityDurationType_e (sustainabilityLib)
swSustainabilityYear: int = 1
swSustainabilityMonth: int = 2
swSustainabilityDay: int = 3
swSustainabilityHour: int = 4

# swSustainabilityEnergyType_e (sustainabilityLib)
swSustainabilityNone: int = -1
swSustainabilityElectricity: int = 0
swSustainabilityNaturalGas: int = 1
swSustainabilityDiesel: int = 2
swSustainabilityGasoline: int = 3
swSustainabilityKerosene: int = 4
swSustainabilityLightFuelOil: int = 5

# swSustainabilityErrors_e (sustainabilityLib)
swSustainabilityUnkownError: int = 0
swSustainabilityNoData: int = 1
swSustainabilityNoError: int = 2

# swSustainabilityFuelType_e (sustainabilityLib)
swSustainabilityFuelNone: int = -1
swSustainabilityFuelElectricity: int = 0
swSustainabilityFuelNaturalGas: int = 1

# swSustainabilityManufacturingPaintType_e (sustainabilityLib)
swSustainabilityNoPaint: int = -1
swSustainabilityWaterbasedPaint: int = 0
swSustainabilitySolventbasedPaint: int = 1

# swSustainabilityManufacturingProcessType_e (sustainabilityLib)
swSustainabilityCustom: int = 0
swSustainabilityDieCasted: int = 1
swSustainabilityExtrusion: int = 2
swSustainabilityForged: int = 3
swSustainabilityMachinedSandCasting: int = 4
swSustainabilityMilled: int = 5
swSustainabilityManufacturingNone: int = 6
swSustainabilitySandCasted: int = 7
swSustainabilitySheetmetal: int = 8
swSustainabilityStamped_FormedSheetmetal: int = 9
swSustainabilityTurned: int = 10

# swSustainabilityRegionName_e (sustainabilityLib)
swSustainabilityUnknownRegion: int = 0
swSustainabilityNorthAmerica: int = 1
swSustainabilityEurope: int = 2
swSustainabilityAsia: int = 3
swSustainabilityJapan: int = 4
swSustainabilitySouthAmerica: int = 5
swSustainabilityAustralia: int = 6
swSustainabilityIndia: int = 7
swSustainabilityNumElems: int = 8

# swSustainabilitySaveAsFileType_e (sustainabilityLib)
swSustainabilityDocxReport: int = 1
swSustainabilitySpreadsheet: int = 2
swSustainabilityGabiInputFile: int = 3

# swSweepDirection_e (SwConst)
swSweepDirection1: int = 0
swSweepBidirectional: int = 1
swSweepDirection2: int = 2

# swSweptFlangeError_e (SwConst)
swSweptFlangeError_None: int = 0
swSweptFlangeError_InvalidProfile: int = 1
swSweptFlangeError_InvalidPath: int = 2
swSweptFlangeError_SelfIntersectingGeometry: int = 4
swSweptFlangeError_InvalidSheetMetalParameters: int = 8

# swSweptFlangePositionTypes_e (SwConst)
swSweptFlangePositionType_MaterialInside: int = 1
swSweptFlangePositionType_MaterialOutside: int = 2
swSweptFlangePositionType_BendOutside: int = 3

# swSymbol_e (SwConst)
swSymNONE: int = 0
swSymDEGREE: int = 32
swSymPLUSMINUS: int = 33
swSymCENTERLINE: int = 34
swSymFREESTATE: int = 35
swSymSTATISTICAL: int = 36
swSymTANGENTPLANE: int = 37
swSymCONTINUOUS: int = 38

# swSystemColorsCurrentColorScheme_e (SwConst)
swSystemColorsCurrentColorSchemeBlueHighlight: int = 0
swSystemColorsCurrentColorSchemeGreenHighlight: int = 1
swSystemColorsCurrentColorSchemeOrangeHighlight: int = 2

# swSystemColorsEnvelopes_e (SwConst)
swSystemColorsEnvelopes_SemiTransparent: int = 0
swSystemColorsEnvelopes_Opaque: int = 1
swSystemColorsEnvelopes_DoNotChange: int = 2

# swSystemColorsIconColor_e (SwConst)
swSystemColorsIconColorDefault: int = 0
swSystemColorsIconColorClassic: int = 1

# swSystemOptionDisplayAntiAliasing_e (SwConst)
swSystemOptionDisplayAntiAliasing_None: int = 1
swSystemOptionDisplayAntiAliasing_Edges: int = 2
swSystemOptionDisplayAntiAliasing_FullScene: int = 3

# swTabEdgesType_e (SwConst)
SharpEdge: int = 0
FilletEdge: int = 1
ChamferEdge: int = 2

# swTabSlotFeatureHeightType_e (SwConst)
Blind: int = 0
UpToSurface: int = 1
OffsetFromSurface: int = 2

# swTabSlotFeatureSpacingType_e (SwConst)
EqualSpacing: int = 0
SpacingLength: int = 1

# swTableAnnotationType_e (SwConst)
swTableAnnotation_General: int = 0
swTableAnnotation_HoleChart: int = 1
swTableAnnotation_BillOfMaterials: int = 2
swTableAnnotation_RevisionBlock: int = 3
swTableAnnotation_WeldmentCutList: int = 4
swTableAnnotation_TitleBlock: int = 5
swTableAnnotation_WeldTable: int = 6
swTableAnnotation_BendTable: int = 7
swTableAnnotation_PunchTable: int = 8
swTableAnnotation_GeneralTolerance: int = 9
swTableAnnotation_FamilyTable: int = 10

# swTableCellOrientation_e (SwConst)
swTableCellOrientation_Right: int = 0
swTableCellOrientation_Left: int = 1
swTableCellOrientation_Up: int = 2
swTableCellOrientation_Down: int = 3
swTableCellOrientation_Varies: int = 4
swTableCellOrientation_Rotate90CW: int = 5
swTableCellOrientation_Rotate90CCW: int = 6

# swTableCellRangeIdentifier_e (SwConst)
swTableCellRange_Current: int = -1
swTableCellRange_All: int = -2

# swTableColumnTypes_e (SwConst)
swTableColumnType_UserDefined: int = 0
swHoleTableColumnType_XLocation: int = 101
swHoleTableColumnType_YLocation: int = 102
swHoleTableColumnType_Tag: int = 103
swHoleTableColumnType_Quantity: int = 104
swHoleTableColumnType_Size: int = 105
swBomTableColumnType_PartNumber: int = 201
swBomTableColumnType_ItemNumber: int = 202
swBomTableColumnType_Quantity: int = 203
swBomTableColumnType_CustomProperty: int = 204
swBomTableColumnType_UnitOfMeasure: int = 205
swBomTableColumnType_Equation: int = 206
swBomTableColumnType_ComponentReference: int = 207
swBomTableColumnType_ToolboxProperty: int = 208
swBomTableColumnType_CutListProperties: int = 209
swBomTableColumnType_CutListItemName: int = 210
swBomTableColumnType_PLMProperty: int = 211
swRevisionTableColumnType_Zone: int = 301
swRevisionTableColumnType_Revision: int = 302
swRevisionTableColumnType_Description: int = 303
swRevisionTableColumnType_Date: int = 304
swRevisionTableColumnType_Approved: int = 305
swRevisionTableColumnType_CustomProperties: int = 306
swWeldTableColumnType_ItemNumber: int = 401
swWeldTableColumnType_Quantity: int = 402
swWeldTableColumnType_CutListName: int = 403
swWeldTableColumnType_CustomProperty: int = 404
swBendTableColumnType_Tag: int = 501
swBendTableColumnType_Direction: int = 502
swBendTableColumnType_Angle: int = 503
swBendTableColumnType_InnerRadius: int = 504
swBendTableColumnType_ComplementaryAngle: int = 505
swBendTableColumnType_BendOrder: int = 506
swBendTableColumnType_BendAllowance: int = 507
swPunchTableColumnType_XLocation: int = 601
swPunchTableColumnType_YLocation: int = 602
swPunchTableColumnType_PunchID: int = 603
swPunchTableColumnType_Quantity: int = 604
swPunchTableColumnType_Angle: int = 605
swPunchTableColumnType_Tag: int = 606

# swTableHeaderPosition_e (SwConst)
swTableHeader_None: int = 0
swTableHeader_Top: int = 1
swTableHeader_Bottom: int = 2

# swTableItemInsertPosition_e (SwConst)
swTableItemInsertPosition_First: int = 1
swTableItemInsertPosition_Before: int = 2
swTableItemInsertPosition_After: int = 3
swTableItemInsertPosition_Last: int = 4
swTableItemMovePosition_Relative: int = 5

# swTableMergeLocations_e (SwConst)
swTableMerge_WithPrevious: int = 1
swTableMerge_WithNext: int = 2
swTableMerge_All: int = 3

# swTableRowColSizeChangeBehavior_e (SwConst)
swTableRowColChange_TableSizeCanChange: int = 0
swTableRowColChange_AbsorbedByNext: int = 1
swTableRowColChange_AbsorbedByPrevious: int = 2

# swTableSplitDirection_e (SwConst)
swTableSplit_None: int = 0
swTableSplit_Horizontal: int = 1
swTableSplit_Vertical: int = 2

# swTableSplitLocations_e (SwConst)
swTableSplit_BeforeRow: int = 1
swTableSplit_AfterRow: int = 2
swTableSplit_BeforeColumn: int = 3
swTableSplit_AfterColumn: int = 4

# swTableTagStyle_e (SwConst)
swTable_AlphaNumericTags: int = 1
swTable_NumericTags: int = 2
swTable_ManualTags: int = 3

# swTangencyType_e (SwConst)
swTangencyNone: int = 0
swTangencyNormalToProfile: int = 1
swTangencyDirectionVector: int = 2
swTangencyAllFaces: int = 3
swMinimumTwist: int = 10

# swTangentArcTypes_e (SwConst)
swForward: int = 1
swLeft: int = 2
swBack: int = 3
swRight: int = 4

# swTangentMagnitudeDirection_e (SwConst)
swTangentMagnitudeDirection1: int = 1
swTangentMagnitudeDirection2: int = 2

# swTaperedTapCustomSizing_e (SwConst)
swTaperedTapCustomSizing_MinorDiameterWithCosmeticThread: int = 1
swTaperedTapCustomSizing_MajorDiameter: int = 2

# swTaperedTapThreadClass_e (SwConst)
swTaperedTapThreadClass_1: int = 1
swTaperedTapThreadClass_2: int = 2

# swTaskPaneBitmapsOptions_e (SwConst)
swTaskPaneBitmapsOptions_Close: int = 1
swTaskPaneBitmapsOptions_Help: int = 2
swTaskPaneBitmapsOptions_Ok: int = 3
swTaskPaneBitmapsOptions_Next: int = 4
swTaskPaneBitmapsOptions_Back: int = 5
swTaskPaneBitmapsOptions_Options: int = 6

# swTaskPaneNotify_e (SwConst)
swAppTaskPaneActivateNotify: int = 1
swAppTaskPaneDeactivateNotify: int = 2
swAppTaskPaneDestroyNotify: int = 3
swAppTaskPaneToolbarButtonClicked: int = 4

# swTaskPaneTab_e (SwConst)
swDesignLibrary: int = 1
swFileExplorer: int = 2
swResources: int = 3
swClipBoard: int = 4
swCustomProps: int = 5
swPnID: int = 6

# swTaskpaneViewStatus_e (SwConst)
swTaskpaneView_Okay: int = 0
swTaskpaneView_UnsupportedHandler: int = 1
swTaskpaneView_CreationFailure: int = -1

# swTbCommand_e (SwConst)
swTbCONTROL: int = -2
swTbACTIVE: int = -1
swTbNONE: int = 0
swTbPART: int = 1
swTbASSEMBLY: int = 2
swTbDRAWING: int = 3

# swTbControlModes_e (SwConst)
swTbSTOP: int = 0
swTbCONTINUE: int = 1
swTbOleInplaceMode: int = 2

# swTbSaveModes_e (SwConst)
swTbSAVE: int = 0
swTbLOAD: int = 1

# swTempBodySelectOptions_e (SwConst)
swTempBodySelectOptionNone: int = 0
swTempBodySelectable: int = 1

# swTesselationMatchType_e (SwConst)
swTesselationMatchFacetTopology: int = 0
swTesselationMatchFacetGeometry: int = 1
swTesselationMatchEdgeCurve: int = 2

# swTextAlignmentVertical_e (SwConst)
swTextAlignmentTop: int = 0
swTextAlignmentMiddle: int = 1
swTextAlignmentBottom: int = 2

# swTextInBoxStyle_e (SwConst)
swTextInBoxStyleNone: int = 0
swTextInBoxStyleWrap: int = 1
swTextInBoxStyleFit: int = 2

# swTextJustification_e (SwConst)
swTextJustificationNone: int = 0
swTextJustificationLeft: int = 1
swTextJustificationCenter: int = 2
swTextJustificationRight: int = 3

# swTextPosition_e (SwConst)
swUPPER_LEFT: int = 0
swLOWER_LEFT: int = 1
swCENTER: int = 2
swUPPER_RIGHT: int = 3
swLOWER_RIGHT: int = 4
swUPPER_CENTER: int = 5

# swTextSize_e (SwConst)
swTextSize_Small: int = 0
swTextSize_Medium: int = 1
swTextSize_Large: int = 2

# swTextureRenderModes_e (SwConst)
swTextureRenderModeImage: int = 0
swTextureRenderModeBlend: int = 1
swTextureRenderModeLuminance: int = 2

# swThickenDirection_e (SwConst)
swThickenDirection_Side1: int = 0
swThickenDirection_Side2: int = 1
swThickenDirection_Both: int = 2

# swThickenThicknessType_e (SwConst)
swThickenSideOne: int = 0
swThickenSideTwo: int = 1
swThickenSideBoth: int = 2

# swThinWallType_e (SwConst)
swThinWallOneDirection: int = 0
swThinWallOppDirection: int = 1
swThinWallMidPlane: int = 2
swThinWallTwoDirection: int = 3

# swThreadEndCondition_e (SwConst)
swThreadEndCondition_Blind: int = 0
swThreadEndCondition_Revolutions: int = 1
swThreadEndCondition_UpToSelection: int = 2

# swThreadMethod_e (SwConst)
swThreadMethod_Cut: int = 0
swThreadMethod_Extrude: int = 1

# swThreadMirrorType_e (SwConst)
swThreadMirrorType_Horizontally: int = 0
swThreadMirrorType_Vertically: int = 1

# swTiffCompressionScheme_e (SwConst)
swTiffUncompressed: int = 0
swTiffPackbitsCompression: int = 1
swTiffGroup4FaxCompression: int = 2

# swTiffImageType_e (SwConst)
swTiffImageBlackAndWhite: int = 0
swTiffImageRGB: int = 1
swTiffImageGrayScale: int = 2
swTiffImageRGBA: int = 3

# swTolType_e (SwConst)
swTolNONE: int = 0
swTolBASIC: int = 1
swTolBILAT: int = 2
swTolLIMIT: int = 3
swTolSYMMETRIC: int = 4
swTolMIN: int = 5
swTolMAX: int = 6
swTolMETRIC: int = 7
swTolFIT: int = 7
swTolFITWITHTOL: int = 8
swTolFITTOLONLY: int = 9
swTolBLOCK: int = 10
swTolGeneral: int = 11

# swToleranceZoneModifier_e (SwConst)
swToleranceZoneModifier_None: int = 0
swToleranceZoneModifier_Unknown: int = 1
swToleranceZoneModifier_Diameter: int = 2
swToleranceZoneModifier_SphericalDiameter: int = 3

# swTolerances_e (SwConst)
swBSCurveOutputTol: int = 0
swBSCurveNonRationalOutputTol: int = 1
swUVCurveOutputTol: int = 2
swSurfChordTessellationTol: int = 3
swSurfAngularTessellationTol: int = 4
swCurveChordTessellationTol: int = 5

# swToolBoxPartType_e (SwConst)
swNotAToolboxPart: int = 0
swToolboxStandardPart: int = 1
swToolboxCopiedPart: int = 2

# swToolBoxPropertyName_e (SwConst)
swToolBoxPropertyName_PartName: int = 0
swToolBoxPropertyName_Specification: int = 1
swToolBoxPropertyName_Standard: int = 2

# swToolbarDockStatePosition_e (SwConst)
swDockNoToolbar: int = -1
swNoDock: int = 0
swDockTop: int = 1
swDockBottom: int = 2
swDockRight: int = 3
swDockLeft: int = 4

# swToolbarLayoutOption_e (SwConst)
swToolbarLayoutOption_None: int = 0
swToolbarLayoutOption_AllToolbars: int = 1
swToolbarLayoutOption_MacroToolbarOnly: int = 2

# swToolbarStates_e (SwConst)
swToolbarHidden: int = 0

# swToolbar_e (SwConst)
swSketchToolsToolbar: int = 0
swMainToolbar: int = 1
swStandardToolbar: int = 2
swViewToolbar: int = 3
swSketchRelationsToolbar: int = 4
swMacroToolbar: int = 5
swSketchToolbar: int = 6
swAssemblyToolbar: int = 7
swDrawingToolbar: int = 8
swAnnotationToolbar: int = 9
swWebToolbar: int = 10
swFeatureToolbar: int = 11
swFontToolbar: int = 12
swLineToolbar: int = 13
swSelectionFilterToolbar: int = 14
swReferenceGeometryToolbar: int = 15
swStandardViewsToolbar: int = 16
swToolsToolbar: int = 17
swCurvesToolbar: int = 18
swMoldToolsToolbar: int = 19
swSheetMetalToolbar: int = 20
swSurfacesToolbar: int = 21
swAlignToolbar: int = 22
swLayerToolbar: int = 23
sw2Dto3DToolbar: int = 24
swRoutingToolbar: int = 25
swSimulationToolbar: int = 26
swSplineToolbar: int = 27
swContextToolbar: int = 28
swBlocksToolbar: int = 29
swTaskPaneToolbar: int = 30
swQuickSnapToolbar: int = 31
swOfficeToolbar: int = 32
swTolXpertToolbar: int = 33
swDimXpertToolbar: int = 33
swTableToolbar: int = 34
swWeldmentToolbar: int = 35
swAnimationPaneToolbar: int = 36
swScreenCaptureToolbar: int = 37
swLayoutToolbar: int = 38
swRenderToolbar: int = 39
swSheetFormatToolbar: int = 40
swConfigurationToolbar: int = 41
swDisplayStatesToolbar: int = 42
swSOLIDWORKSMBDToolbars: int = 43

# swTopoEntity_e (SwConst)
swTopoVertex: int = 1
swTopoEdge: int = 2
swTopoLoop: int = 3
swTopoFace: int = 4
swTopoShell: int = 5
swTopoBody: int = 6
swTopoRegion: int = 7

# swTopologyTypes_e (SwConst)
swTopologyNull: int = 0
swTopologyCoEdge: int = 1
swTopologyVertex: int = 2

# swTopology_e (SwConst)
swTopoSolidBody: int = 1
swTopoSheetBody: int = 2
swTopoWireBody: int = 3
swTopoMinimumBody: int = 4

# swTrackingIDError_e (SwConst)
swTrackingIDError_NoError: int = 0
swTrackingIDError_UnknownError: int = 1
swTrackingIDError_InvalidTrackingCookie: int = 2
swTrackingIDError_InvalidTrackingID: int = 3
swTrackingIDError_UntrackableObject: int = 4
swTrackingIDError_UntrackedObject: int = 5

# swTranslationNotifyOptions_e (SwConst)
swTranslationNotifySilentMode: int = 1

# swTransparencyState_e (SwConst)
swTransparencyStateUnknown: int = -1
swTransparencyStateTransparent: int = 0
swTransparencyStateNonTransparent: int = 1

# swTreeControlItemType_e (SwConst)
swFeatureManagerItem_Unsupported: int = 0
swFeatureManagerItem_Feature: int = 1
swFeatureManagerItem_Component: int = 2

# swTriadManipulatorControlPoints_e (SwConst)
swTriadManipulatorOrigin: int = 0
swTriadManipulatorXAxis: int = 1
swTriadManipulatorYAxis: int = 2
swTriadManipulatorZAxis: int = 3
swTriadManipulatorXYPlane: int = 4
swTriadManipulatorYZPlane: int = 5
swTriadManipulatorZXPlane: int = 6

# swTriadManipulatorDoNotShow_e (SwConst)
swTriadManipulatorShowAll: int = 0
swTriadManipulatorDoNotShowOrigin: int = 1
swTriadManipulatorDoNotShowXAxis: int = 2
swTriadManipulatorDoNotShowYAxis: int = 4
swTriadManipulatorDoNotShowZAxis: int = 8
swTriadManipulatorDoNotShowXYPlane: int = 16
swTriadManipulatorDoNotShowYZPlane: int = 32
swTriadManipulatorDoNotShowZXPlane: int = 64
swTriadManipulatorDoNotShowXYRING: int = 128
swTriadManipulatorDoNotShowYZRING: int = 256
swTriadManipulatorDoNotShowZXRING: int = 512

# swTrimToolMemberObjectType_e (SwConst)
swTrimToolMemberObjectType_swCornerMember: int = 0
swTrimToolMemberObjectType_swCornerTreatmentFeature: int = 1

# swTwistControlType_e (SwConst)
swTwistControlFollowPath: int = 0
swTwistControlKeepNormalConstant: int = 1
swTwistControlFollowPathFirstGuideCurve: int = 2
swTwistControlFollowFirstSecondGuideCurves: int = 3
swTwistControlConstantTwistAlongPath: int = 8
swTwistControlNormalConstantTwistAlongPath: int = 9

# swUIStates_e (SwConst)
swIsHiddenInFeatureMgr: int = 1

# swUnitSystem_e (SwConst)
swUnitSystem_CGS: int = 1
swUnitSystem_MKS: int = 2
swUnitSystem_IPS: int = 3
swUnitSystem_Custom: int = 4
swUnitSystem_MMGS: int = 5

# swUnitsDecimalRounding_e (SwConst)
swUnitsDecimalRounding_HalfAway: int = 0
swUnitsDecimalRounding_HalfTowards: int = 1
swUnitsDecimalRounding_HalfToEven: int = 2
swUnitsDecimalRounding_Truncate: int = 3

# swUnitsEnergyUnit_e (SwConst)
swUnitsEnergyUnit_Joule: int = 1
swUnitsEnergyUnit_Ergs: int = 2
swUnitsEnergyUnit_BTU: int = 3
swUnitsEnergyUnit_KilowattHour: int = 4

# swUnitsForce_e (SwConst)
swUnitsForce_Dynes: int = 1
swUnitsForce_Millinewtons: int = 2
swUnitsForce_Newtons: int = 3
swUnitsForce_Kilonewtons: int = 4
swUnitsForce_Meganewtons: int = 5
swUnitsForce_Poundfeet: int = 6
swUnitsForce_KgForce: int = 7
swUnitsForce_OunceForce: int = 8

# swUnitsMassPropMass_e (SwConst)
swUnitsMassPropMass_Milligrams: int = 1
swUnitsMassPropMass_Grams: int = 2
swUnitsMassPropMass_Kilograms: int = 3
swUnitsMassPropMass_Pounds: int = 4

# swUnitsMassPropVolume_e (SwConst)
swUnitsMassPropVolume_Angstroms3: int = 1
swUnitsMassPropVolume_Nanometers3: int = 2
swUnitsMassPropVolume_Microns3: int = 3
swUnitsMassPropVolume_Millimeters3: int = 4
swUnitsMassPropVolume_Centimeters3: int = 5
swUnitsMassPropVolume_Meters3: int = 6
swUnitsMassPropVolume_Microinches3: int = 7
swUnitsMassPropVolume_Mils3: int = 8
swUnitsMassPropVolume_Inches3: int = 9
swUnitsMassPropVolume_Feet3: int = 10
swUnitsMassPropVolume_MicroLiters: int = 11
swUnitsMassPropVolume_MilliLiters: int = 12
swUnitsMassPropVolume_CentiLiters: int = 13
swUnitsMassPropVolume_DeciLiters: int = 14
swUnitsMassPropVolume_Liters: int = 15
swUnitsMassPropVolume_HectoLiters: int = 16
swUnitsMassPropVolume_USFluidOunce: int = 17
swUnitsMassPropVolume_USPints: int = 18
swUnitsMassPropVolume_USGallons: int = 19
swUnitsMassPropVolume_IMPGallons: int = 20
swUnitsMassPropVolume_IMPCubicYards: int = 21

# swUnitsPowerUnit_e (SwConst)
swUnitsPowerUnit_Watt: int = 1
swUnitsPowerUnit_Horsepower: int = 2
swUnitsPowerUnit_Kilowatt: int = 3

# swUnitsTimeUnit_e (SwConst)
swUnitsTimeUnit_Second: int = 1
swUnitsTimeUnit_Millisecond: int = 2
swUnitsTimeUnit_Minute: int = 3
swUnitsTimeUnit_Hour: int = 4
swUnitsTimeUnit_Microsecond: int = 5
swUnitsTimeUnit_Nanosecond: int = 6

# swUpdateProgressError_e (SwConst)
swUpdateProgressError_UnknownError: int = 0
swUpdateProgressError_Success: int = 1
swUpdateProgressError_UserCancel: int = 2
swUpdateProgressError_OutOfBounds: int = 3
swUpdateProgressError_NotInitialized: int = 4

# swUserMessageBarResponseType_e (SwConst)
swUserMessageBarResponseType_None: int = 0
swUserMessageBarResponseType_Button: int = 1
swUserMessageBarResponseType_Link: int = 2

# swUserMessageBarSeverity_e (SwConst)
swUserMessageBarSeverity_Information: int = 0
swUserMessageBarSeverity_Acknowledgement: int = 1
swUserMessageBarSeverity_Warning: int = 2
swUserMessageBarSeverity_Error: int = 3

# swUserNotificationPosition_e (SwConst)
swUserNotificationPosition_Default: int = 0
swUserNotificationPosition_TopCenter: int = 1
swUserNotificationPosition_TopRight: int = 2
swUserNotificationPosition_BottomCenter: int = 3
swUserNotificationPosition_BottomRight: int = 4

# swUserNotificationResponseType_e (SwConst)
swUserNotificationResponseType_None: int = 0
swUserNotificationResponseType_Button: int = 1
swUserNotificationResponseType_Link: int = 2

# swUserNotificationSeverity_e (SwConst)
swUserNotificationSeverity_Information: int = 0
swUserNotificationSeverity_Acknowledgement: int = 1
swUserNotificationSeverity_Warning: int = 2
swUserNotificationSeverity_Error: int = 3

# swUserPreferenceDoubleValue_e (SwConst)
swDetailingNoteFontHeight: int = 0
swDetailingDimFontHeight: int = 1
swSTLDeviation: int = 2
swSTLAngleTolerance: int = 3
swSpinBoxMetricLengthIncrement: int = 4
swSpinBoxEnglishLengthIncrement: int = 5
swSpinBoxAngleIncrement: int = 6
swMaterialPropertyDensity: int = 7
swTiffPrintPaperWidth: int = 8
swTiffPrintPaperHeight: int = 9
swTiffPrintDrawingPaperHeight: int = 8
swTiffPrintDrawingPaperWidth: int = 9
swDetailingCenterlineExtension: int = 10
swDetailingBreakLineGap: int = 11
swDetailingCenterMarkSize: int = 12
swDetailingWitnessLineGap: int = 13
swDetailingWitnessLineExtension: int = 14
swDetailingObjectToDimOffset: int = 15
swDetailingDimToDimOffset: int = 16
swDetailingMaxLinearToleranceValue: int = 17
swDetailingMinLinearToleranceValue: int = 18
swDetailingMaxAngularToleranceValue: int = 19
swDetailingMinAngularToleranceValue: int = 20
swDetailingToleranceTextScale: int = 21
swDetailingToleranceTextHeight: int = 22
swDetailingNoteBentLeaderLength: int = 23
swDetailingArrowHeight: int = 24
swDetailingArrowWidth: int = 25
swDetailingArrowLength: int = 26
swDetailingSectionArrowHeight: int = 27
swDetailingSectionArrowWidth: int = 28
swDetailingSectionArrowLength: int = 29
swGridMajorSpacing: int = 30
swSnapToAngleValue: int = 31
swImageQualityShadedDeviation: int = 32
swDrawingDefaultSheetScaleNumerator: int = 33
swDrawingDefaultSheetScaleDenominator: int = 34
swDrawingDetailViewScale: int = 35
swViewRotationArrowKeys: int = 36
swMateAnimationSpeed: int = 37
swViewAnimationSpeed: int = 38
swDetailingDimBentLeaderLength: int = 39
swMaterialPropertyCrosshatchScale: int = 40
swMaterialPropertyCrosshatchAngle: int = 41
swDrawingAreaHatchScale: int = 42
swDrawingAreaHatchAngle: int = 43
swPageSetupPrinterTopMargin: int = 44
swPageSetupPrinterBottomMargin: int = 45
swPageSetupPrinterLeftMargin: int = 46
swPageSetupPrinterRightMargin: int = 47
swPageSetupPrinterThinLineWeight: int = 48
swPageSetupPrinterNormalLineWeight: int = 49
swPageSetupPrinterThickLineWeight: int = 50
swPageSetupPrinterThick2LineWeight: int = 51
swPageSetupPrinterThick3LineWeight: int = 52
swPageSetupPrinterThick4LineWeight: int = 53
swPageSetupPrinterThick5LineWeight: int = 54
swPageSetupPrinterThick6LineWeight: int = 55
swPageSetupPrinterDrawingScale: int = 56
swPageSetupPrinterPartAsmScale: int = 57
swCustomizedImportTolerance: int = 58
swDetailingBalloonBentLeaderLength: int = 60
swBOMControlSplitHeight: int = 61
swAnnotationTextScaleNumerator: int = 62
swAnnotationTextScaleDenominator: int = 63
swDetailingDimBreakGap: int = 64
swCurvatureValue1: int = 65
swCurvatureValue2: int = 66
swCurvatureValue3: int = 67
swCurvatureValue4: int = 68
swCurvatureValue5: int = 69
swDetailingBreakLineExtension: int = 70
swDetailingToleranceFitTolTextScale: int = 71
swDetailingToleranceFitTolTextHeight: int = 72
swDocumentColorAdvancedAmbient: int = 73
swDocumentColorAdvancedDiffuse: int = 74
swDocumentColorAdvancedSpecularity: int = 75
swDocumentColorAdvancedShininess: int = 76
swDocumentColorAdvancedTransparency: int = 77
swDocumentColorAdvancedEmission: int = 78
swDxfOutputScaleFactor: int = 79
swHoleTableTagAngle: int = 80
swHoleTableTagOffset: int = 81
swDetailingMaxWitnessLineLength: int = 82
swDrawingKeyboardMovementIncrement: int = 83
swSketchSnapsAngleValue: int = 84
swDxfMergingDistance: int = 85
swDetailingDimRadialSnapAngle: int = 86
swViewTransitionHideShowComponent: int = 87
swViewTransitionIsolate: int = 88
swLineFontVisibleEdgesThicknessCustom: int = 89
swLineFontHiddenEdgesThicknessCustom: int = 90
swLineFontSketchCurvesThicknessCustom: int = 91
swLineFontDetailCircleThicknessCustom: int = 92
swLineFontSectionLineThicknessCustom: int = 93
swLineFontDimensionsThicknessCustom: int = 94
swLineFontConstructionCurvesThicknessCustom: int = 95
swLineFontCrosshatchThicknessCustom: int = 96
swLineFontTangentEdgesThicknessCustom: int = 97
swLineFontDetailBorderThicknessCustom: int = 98
swLineFontCosmeticThreadThicknessCustom: int = 99
swLineFontHideTangentEdgeThicknessCustom: int = 100
swLineFontViewArrowThicknessCustom: int = 101
swLineFontExplodedLinesThicknessCustom: int = 102
swLineFontBreakLineThicknessCustom: int = 103
swDetailingBalloonLeaderLineThicknessCustom: int = 104
swDetailingBalloonFrameLineThicknessCustom: int = 105
swDetailingDatumLeaderLineThicknessCustom: int = 106
swDetailingDatumFrameLineThicknessCustom: int = 107
swDetailingGtolLeaderLineThicknessCustom: int = 108
swDetailingGtolFrameLineThicknessCustom: int = 109
swDetailingNoteLeaderLineThicknessCustom: int = 110
swDetailingSFSymbolLeaderLineThicknessCustom: int = 111
swDetailingWeldSymbolLeaderLineThicknessCustom: int = 112
swDetailingAnnotationBentLeaderLength: int = 113
swDetailingGtolBentLeaderLength: int = 114
swDetailingSFSymbolBentLeaderLength: int = 115
swDetailingMaxToleranceValue: int = 116
swDetailingMinToleranceValue: int = 117
swSpinBoxTimeIncrement: int = 118
swDetailingBorderUserDefined: int = 119
swDetailingBOMBalloonCustomSize: int = 120
swDetailingBOMStackedBalloonCustomSize: int = 121
swLineFontSpeedPakDrawingsModelEdgesThicknessCustom: int = 122
swPartDimXpertLengthUnitTol1Value: int = 123
swPartDimXpertLengthUnitTol2Value: int = 124
swPartDimXpertLengthUnitTol3Value: int = 125
swPartDimXpertAngularUnitTolValue: int = 126
swPartDimXpertLocationDistanceTolUpperValue: int = 127
swPartDimXpertLocationDistanceTolLowerValue: int = 128
swPartDimXpertLocationAngleTolUpperValue: int = 129
swPartDimXpertLocationAngleTolLowerValue: int = 130
swPartDimXpertChainPatternLocTolUpperValue: int = 131
swPartDimXpertChainPatternLocTolLowerValue: int = 132
swPartDimXpertChainInnerTolUpperValue: int = 133
swPartDimXpertChainInnerTolLowerValue: int = 134
swPartDimXpertGeometricPrimaryTolValue: int = 135
swPartDimXpertGeometricSecondFeatureSizeTolValue: int = 136
swPartDimXpertGeometricSecondPlaneFeatureTolValue: int = 137
swPartDimXpertGeometricThirdFeatureSizeTolValue: int = 138
swPartDimXpertGeometricThirdPlaneFeatureTolValue: int = 139
swPartDimXpertGeometricPositionTolValue: int = 140
swPartDimXpertGeometricPositionCompositeTolValue: int = 141
swPartDimXpertGeometricSurfaceProfileTolValue: int = 142
swPartDimXpertGeometricSurfaceProfileCompositeTolValue: int = 143
swPartDimXpertGeometricRunoutTolValue: int = 144
swPartDimXpertChamferWidthRatio: int = 145
swPartDimXpertChamferMaxWidth: int = 146
swPartDimXpertChamferDistanceTolUpperValue: int = 147
swPartDimXpertChamferDistanceTolLowerValue: int = 148
swPartDimXpertChamferAngleTolUpperValue: int = 149
swPartDimXpertChamferAngleTolLowerValue: int = 150
swPartDimXpertSizeDiameterTolUpperValue: int = 151
swPartDimXpertSizeDiameterTolLowerValue: int = 152
swPartDimXpertSizeCounterboreDiameterTolUpperValue: int = 153
swPartDimXpertSizeCounterboreDiameterTolLowerValue: int = 154
swPartDimXpertSizeCountersinkDiameterTolUpperValue: int = 155
swPartDimXpertSizeCountersinkDiameterTolLowerValue: int = 156
swPartDimXpertSizeCountersinkAngleTolUpperValue: int = 157
swPartDimXpertSizeCountersinkAngleTolLowerValue: int = 158
swPartDimXpertSizeLengthSlotTolUpperValue: int = 159
swPartDimXpertSizeLengthSlotTolLowerValue: int = 160
swPartDimXpertSizeWidthSlotTolUpperValue: int = 161
swPartDimXpertSizeWidthSlotTolLowerValue: int = 162
swPartDimXpertSizeDepthTolUpperValue: int = 163
swPartDimXpertSizeDepthTolLowerValue: int = 164
swPartDimXpertSizeFilletRadiusTolUpperValue: int = 165
swPartDimXpertSizeFilletRadiusTolLowerValue: int = 166
swPunchTableTagAngle: int = 167
swPunchTableTagOffset: int = 168
swLineFontAdjoiningComponentCustom: int = 169
swQuickViewTransparencyLevel: int = 170
swDetailingRevisionCloudLineThicknessCustom: int = 171
swDetailingRevisionCloudMaxArcRadius: int = 172
swSheetMetalBendNotesLeaderLineThicknessCustom: int = 173
swSheetMetalBendNotesBorderSizeCustom: int = 174
swSheetMetalBendNotesLeaderLength: int = 175
swDetailingBorderAddPadding: int = 176
swDetailingBOMBalloonPadding: int = 177
swDetailingBOMStackedBalloonPadding: int = 178
swDetailingTablesHorizontalPadding: int = 179
swDetailingTablesVerticalPadding: int = 180
swLineFontBendLineUpThicknessCustom: int = 181
swLineFontBendLineDownThicknessCustom: int = 182
swLineFontEnvelopeComponentThicknessCustom: int = 183
swDetailingCenterOfMassSize: int = 184
swViewSelectorSpeed: int = 185
swDetailingBalloonQtyGapDistance: int = 186
swDimensionsExtensionLineStyleThicknessCustom: int = 188
swSmartMateSensitivity: int = 189
swSystemTouchRotateWidth: int = 190
swSystemTouchRotateVersusPanThreshhold: int = 191
swDetailingParaSpacing: int = 192
swTwistCountValuePerMeter: int = 194
swDetailingLocationLabelFrameLineThicknessCustom: int = 195
swDetailingLocationLabelStyleCustomSize: int = 196
swDetailingLocationLabelPadding: int = 197
swDetailingCenterMarkGap: int = 198
swDetailingBorderLeaderCustomLineThickness: int = 199
swDetailingBorderZoneDividerLength: int = 200
swDetailingBorderOuterCenterZoneDividerLength: int = 201
swDetailingBorderInnerCenterZoneDividerLength: int = 202
swDetailingBorderZoneDividerCustomLineThickness: int = 203
swDetailingOrdinateSize: int = 204
swLineFontEmphasizedSectionThicknessCustom: int = 205
swPrint3DBoxX: int = 206
swPrint3DBoxY: int = 207
swPrint3DBoxZ: int = 208
swMatesMaximumDeviationForMisalignedMates: int = 209
swASMSLDPRT_ExcludeComponentsByVisibilityThreshold: int = 210
swASMSLDPRT_ExcludeComponentsByBBoxVolumeThreshold: int = 211
swPLYDeviation: int = 212
swPLYAngleTolerance: int = 213
swSheetMetalMBDLeaderLineThicknessCustom: int = 214
swSheetMetalMBDBorderSizeCustom: int = 215
swSheetMetalMBDLeaderLength: int = 216
swDetailingHatchDensityLimit: int = 217
swAbsChordalErrorVal: int = 218
swAbsNormalDeviationVal: int = 219
swAbsEdgeLengthVal: int = 220

# swUserPreferenceIntegerValue_e (SwConst)
swDxfVersion: int = 0
swDxfOutputFonts: int = 1
swDxfMappingFileIndex: int = 2
swAutoSaveInterval: int = 3
swResolveLightweight: int = 4
swAcisOutputVersion: int = 5
swTiffScreenOrPrintCapture: int = 6
swTiffImageType: int = 7
swTiffCompressionScheme: int = 8
swTiffPrintDPI: int = 9
swTiffPrintPaperSize: int = 10
swTiffPrintScaleFactor: int = 11
swCreateBodyFromSurfacesOption: int = 12
swDetailingDimensionStandard: int = 13
swDetailingDualDimPosition: int = 14
swDetailingDimTrailingZero: int = 15
swDetailingArrowStyleForDimensions: int = 16
swDetailingDimensionArrowPosition: int = 17
swDetailingLinearDimLeaderStyle: int = 18
swDetailingRadialDimLeaderStyle: int = 19
swDetailingAngularDimLeaderStyle: int = 20
swDetailingLinearToleranceStyle: int = 21
swDetailingAngularToleranceStyle: int = 22
swDetailingToleranceTextSizing: int = 23
swDetailingLinearDimPrecision: int = 24
swDetailingLinearTolPrecision: int = 25
swDetailingAltLinearDimPrecision: int = 26
swDetailingAltLinearTolPrecision: int = 27
swDetailingAngularDimPrecision: int = 28
swDetailingAngularTolPrecision: int = 29
swDetailingNoteTextAlignment: int = 30
swDetailingNoteLeaderSide: int = 31
swDetailingBalloonStyle: int = 32
swDetailingBalloonFit: int = 33
swDetailingBOMBalloonStyle: int = 34
swDetailingBOMBalloonFit: int = 35
swDetailingBOMUpperText: int = 36
swDetailingBOMLowerText: int = 37
swDetailingArrowStyleForEdgeVertexAttachment: int = 38
swDetailingArrowStyleForFaceAttachment: int = 39
swDetailingArrowStyleForUnattached: int = 40
swDetailingVirtualSharpStyle: int = 41
swGridMinorLinesPerMajor: int = 42
swSnapPointsPerMinor: int = 43
swImageQualityShaded: int = 44
swImageQualityWireframe: int = 45
swImageQualityWireframeValue: int = 46
swUnitsLinear: int = 47
swUnitsLinearDecimalDisplay: int = 48
swUnitsLinearDecimalPlaces: int = 49
swUnitsLinearFractionDenominator: int = 50
swUnitsAngular: int = 51
swUnitsAngularDecimalPlaces: int = 52
swLineFontVisibleEdgesThickness: int = 53
swLineFontVisibleEdgesStyle: int = 54
swLineFontHiddenEdgesThickness: int = 55
swLineFontHiddenEdgesStyle: int = 56
swLineFontSketchCurvesThickness: int = 57
swLineFontSketchCurvesStyle: int = 58
swLineFontDetailCircleThickness: int = 59
swLineFontDetailCircleStyle: int = 60
swLineFontSectionLineThickness: int = 61
swLineFontSectionLineStyle: int = 62
swLineFontDimensionsThickness: int = 63
swLineFontDimensionsStyle: int = 64
swLineFontConstructionCurvesThickness: int = 65
swLineFontConstructionCurvesStyle: int = 66
swLineFontCrosshatchThickness: int = 67
swLineFontCrosshatchStyle: int = 68
swLineFontTangentEdgesThickness: int = 69
swLineFontTangentEdgesStyle: int = 70
swLineFontDetailBorderThickness: int = 71
swLineFontDetailBorderStyle: int = 72
swLineFontCosmeticThreadThickness: int = 73
swLineFontCosmeticThreadStyle: int = 74
swStepAP: int = 75
swHiddenEdgeDisplayDefault: int = 76
swTangentEdgeDisplayDefault: int = 77
swSTLQuality: int = 78
swDrawingProjectionType: int = 79
swDrawingPrintCrosshatchOutOfDateViews: int = 80
swPerformanceAssemRebuildOnLoad: int = 81
swLoadExternalReferences: int = 82
swIGESRepresentation: int = 83
swIGESSystem: int = 84
swIGESCurveRepresentation: int = 85
swViewRotationMouseSpeed: int = 86
swBackupCopiesPerDocument: int = 87
swCheckForOutOfDateLightweightComponents: int = 88
swParasolidOutputVersion: int = 89
swLineFontHideTangentEdgeThickness: int = 90
swLineFontHideTangentEdgeStyle: int = 91
swLineFontViewArrowThickness: int = 92
swLineFontViewArrowStyle: int = 93
swEdgesHiddenEdgeDisplay: int = 94
swEdgesTangentEdgeDisplay: int = 95
swEdgesShadedModeDisplay: int = 96
swDetailingBOMStackedBalloonStyle: int = 97
swDetailingBOMStackedBalloonFit: int = 98
swSystemColorsViewportBackground: int = 99
swSystemColorsTopGradientColor: int = 100
swSystemColorsBottomGradientColor: int = 101
swSystemColorsDynamicHighlight: int = 102
swSystemColorsHighlight: int = 103
swSystemColorsSelectedItem1: int = 104
swSystemColorsSelectedItem2: int = 105
swSystemColorsSelectedItem3: int = 106
swSystemColorsSelectedFaceShaded: int = 107
swSystemColorsDrawingsVisibleModelEdge: int = 108
swSystemColorsDrawingsHiddenModelEdge: int = 109
swSystemColorsDrawingsPaperBorder: int = 110
swSystemColorsDrawingsPaperShadow: int = 111
swSystemColorsDrawingsSheetBorder: int = 111
swSystemColorsImportedDrivingAnnotation: int = 112
swSystemColorsImportedDrivenAnnotation: int = 113
swSystemColorsSketchOverDefined: int = 114
swSystemColorsSketchFullyDefined: int = 115
swSystemColorsSketchUnderDefined: int = 116
swSystemColorsSketchInvalidGeometry: int = 117
swSystemColorsSketchNotSolved: int = 118
swSystemColorsGridLinesMinor: int = 119
swSystemColorsGridLinesMajor: int = 120
swSystemColorsConstructionGeometry: int = 121
swSystemColorsDanglingDimension: int = 122
swSystemColorsText: int = 123
swSystemColorsAssemblyEditPart: int = 124
swSystemColorsAssemblyEditPartHiddenLines: int = 125
swSystemColorsAssemblyNonEditPart: int = 126
swSystemColorsInactiveEntity: int = 127
swSystemColorsTemporaryGraphics: int = 128
swSystemColorsTemporaryGraphicsShaded: int = 129
swSystemColorsActiveSelectionListBox: int = 130
swSystemColorsSurfacesOpenEdge: int = 131
swSystemColorsTreeViewBackground: int = 132
swAcisOutputUnits: int = 133
swSystemColorsShadedEdge: int = 134
swDxfOutputLineStyles: int = 135
swDxfOutputNoScale: int = 136
swPageSetupPrinterOrientation: int = 138
swPageSetupPrinterDrawingColor: int = 139
swImportCheckAndRepair: int = 140
swUseCustomizedImportTolerance: int = 141
swStepExportPreference: int = 142
swEdgesInContextEditTransparencyType: int = 143
swEdgesInContextEditTransparency: int = 144
swPlaneDisplayFrontFaceColor: int = 145
swPlaneDisplayBackFaceColor: int = 146
swPlaneDisplayTransparency: int = 147
swPlaneDisplayIntersectionLineColor: int = 148
swDetailingDatumDisplayType: int = 149
swBOMConfigurationAnchorType: int = 150
swBOMConfigurationWhatToShow: int = 151
swBOMControlMissingRowDisplay: int = 152
swBOMControlSplitDirection: int = 153
swDetailingChamferDimLeaderStyle: int = 154
swDetailingChamferDimTextStyle: int = 155
swDetailingChamferDimXStyle: int = 156
swDocumentColorFeatBend: int = 157
swDocumentColorFeatBoss: int = 158
swDocumentColorFeatCavity: int = 159
swDocumentColorFeatChamfer: int = 160
swDocumentColorFeatCut: int = 161
swDocumentColorFeatLoftCut: int = 162
swDocumentColorFeatSurfCut: int = 163
swDocumentColorFeatSweepCut: int = 164
swDocumentColorFeatWeldBead: int = 165
swDocumentColorFeatExtrude: int = 166
swDocumentColorFeatFillet: int = 167
swDocumentColorFeatHole: int = 168
swDocumentColorFeatLibrary: int = 169
swDocumentColorFeatLoft: int = 170
swDocumentColorFeatMidSurface: int = 171
swDocumentColorFeatPattern: int = 172
swDocumentColorFeatRefSurface: int = 173
swDocumentColorFeatRevolution: int = 174
swDocumentColorFeatShell: int = 175
swDocumentColorFeatDerivedPart: int = 176
swDocumentColorFeatSweep: int = 177
swDocumentColorFeatThicken: int = 178
swDocumentColorFeatRib: int = 179
swDocumentColorFeatDome: int = 180
swDocumentColorFeatForm: int = 181
swDocumentColorFeatShape: int = 182
swDocumentColorFeatReplaceFace: int = 183
swDocumentColorWireFrame: int = 184
swDocumentColorShading: int = 185
swDocumentColorHidden: int = 186
swLineFontExplodedLinesThickness: int = 187
swLineFontExplodedLinesStyle: int = 188
swSystemColorsRefTriadX: int = 189
swSystemColorsRefTriadY: int = 190
swSystemColorsRefTriadZ: int = 191
swAcisOutputGeometryPreference: int = 192
swSystemColorsDTDim: int = 193
swLargeAsmModeThreshold: int = 194
swLargeAsmModeAutoActivate: int = 195
swLargeAsmModeCheckOutOfDateLightweight: int = 196
swLargeAsmModeAutoRecoverCount: int = 197
swLargeAsmModeDisplayModeForNewDrawViews: int = 198
swLineFontBreakLineThickness: int = 199
swLineFontBreakLineStyle: int = 200
swSaveAssemblyAsPartOptions: int = 201
swDetailingDimensionTextAlignmentVertical: int = 202
swDetailingDimensionTextAlignmentHorizontal: int = 203
swDetailingToleranceFitTolTextSizing: int = 204
swImportUnitPreference: int = 205
swImportCurvePreference: int = 206
swImportUseBrep: int = 207
swImportStlVrmlModelType: int = 208
swSystemColorsSelectedItem4: int = 209
swImportStlVrmlUnits: int = 210
swExportStlUnits: int = 211
swExportVrmlUnits: int = 212
swSystemColorsSketchInactive: int = 213
swExternalReferencesUpdateOutOfDateLinkedDesignTable: int = 214
swSystemColorsTreeItemNormal: int = 215
swSystemColorsTreeItemSelected: int = 216
swSystemColorsDrawingsPaper: int = 217
swSystemColorsDrawingsBackground: int = 218
swSystemColorsDrawingsViewBorder: int = 219
swDetailingNotesLeaderStyle: int = 220
swSystemColorsDrawingsLockedFocus: int = 221
swRevisionTableTagStyle: int = 222
swRevisionTableSymbolShape: int = 223
swBomTableZeroQuantityDisplay: int = 224
swDocumentColorFeatStructuralMember: int = 225
swDocumentColorFeatGusset: int = 226
swDocumentColorFeatEndCap: int = 227
swDetailingAutoBalloonLayout: int = 228
swDocumentColorFeatWrap: int = 229
swRebuildOnActivation: int = 230
swSystemColorsImportedAnnotation: int = 231
swSystemColorsNonImportedAnnotation: int = 232
swLevelOfDetail: int = 233
swLargeAsmLevelOfDetail: int = 234
swPropertyManagerColorDivider: int = 235
swCollabCheckReadOnlyModifiedInterval: int = 236
swEdrawingsSaveAsSelectionOption: int = 237
swHoleTableOriginStandard: int = 238
swHoleTableTagStyle: int = 239
swHoleTableHoleLocationPrecision: int = 240
swDetailingDetailViewLabels_Name: int = 241
swDetailingDetailViewLabels_Label: int = 242
swDetailingDetailViewLabels_Scale: int = 243
swDetailingDetailViewLabels_Delimiter: int = 244
swDetailingSectionViewLabels_Name: int = 245
swDetailingSectionViewLabels_Label: int = 246
swDetailingSectionViewLabels_Scale: int = 247
swDetailingSectionViewLabels_Delimiter: int = 248
swDetailingAuxViewLabels_Name: int = 249
swDetailingAuxViewLabels_Label: int = 250
swDetailingAuxViewLabels_Scale: int = 251
swDetailingAuxViewLabels_Delimiter: int = 252
swDxfMultiSheetOption: int = 253
swUnitsDualLinear: int = 254
swUnitsDualLinearDecimalDisplay: int = 255
swUnitsDualLinearDecimalPlaces: int = 256
swUnitsDualLinearFractionDenominator: int = 257
swUnitsMassPropLength: int = 258
swUnitsMassPropMass: int = 259
swUnitsMassPropVolume: int = 260
swUnitsMassPropDecimalPlaces: int = 261
swUnitsForce: int = 262
swUnitSystem: int = 263
swBendNoteStyle: int = 264
swDetailingLeadingZero: int = 265
swDetailingToleranceFitTolDisplayLinear: int = 266
swDetailingToleranceFitTolDisplayAngular: int = 267
swMaterialPropertyAreaHatchFillStyle: int = 268
swDrawingAreaHatchFillStyle: int = 269
swPerformanceViewsToDraftQuality: int = 270
swFeatureManagerDisplayWarnings: int = 271
swSheetMetalColorBendLinesUp: int = 272
swSheetMetalColorBendLinesDown: int = 273
swSheetMetalColorFormFeature: int = 274
swSheetMetalColorBendLinesHems: int = 275
swSheetMetalColorModelEdges: int = 276
swSystemColorsDimsNotMarkedForDrawing: int = 277
swSystemColorsAsmInterferenceVolume: int = 278
swSystemColorsSwiftAnnotations: int = 279
swSystemColorsSwiftUnderConstrained: int = 280
swSystemColorsSwiftFullyConstrained: int = 281
swSystemColorsSwiftOverConstrained: int = 282
swSystemColorsToleranceAnalysisDim: int = 283
swSystemColorsPropertyManagerColor: int = 284
swPropertyManagerColorBackground: int = 285
swPropertyManagerColorActiveClosedDivider: int = 286
swPropertyManagerColorEditBox: int = 287
swPropertyManagerColorEditText: int = 288
swPropertyManagerColorLabelAndIcon: int = 289
swPropertyManagerColorTitle: int = 290
swPropertyManagerColorOuterBorder: int = 291
swPropertyManagerColorInnerBorder: int = 292
swPropertyManagerColorTopBorder: int = 293
swPropertyManagerColorImportantMessage: int = 294
swSystemColorsHiddenEdgeSelectionShow: int = 295
swDetailingForeshortenedDiameterStyle: int = 296
swRevisionTableMultipleSheetStyle: int = 297
swUndoStepsMaximum: int = 298
swDetailingDimFractionStyle: int = 299
swDetailingDimFractionScaleIndex: int = 300
swAutoSaveIntervalMode: int = 301
swBackupRemoveInterval: int = 302
swSaveReminderInterval: int = 303
swSaveReminderIntervalMode: int = 304
swColorsBackgroundAppearance: int = 305
swRebuildErrorAction: int = 306
swSheetMetalColorFlatPatternSketch: int = 307
swLineFontVisibleEdgesEndCap: int = 308
swLineFontHiddenEdgesEndCap: int = 309
swLineFontSketchCurvesEndCap: int = 310
swDetailingDimXpertChamferScheme: int = 311
swDetailingDimXpertSlotScheme: int = 312
swDetailingDimXpertFilletOptions: int = 313
swDetailingDimXpertChamferOptions: int = 314
swSystemColorsGhostSelColor: int = 315
swFeatureManagerBlocksVisibility: int = 318
swFeatureManagerDesignBinderVisibility: int = 319
swFeatureManagerAnnotationsVisibility: int = 320
swFeatureManagerLightsVisibility: int = 321
swFeatureManagerSolidBodiesVisibility: int = 322
swFeatureManagerSurfaceBodiesVisibility: int = 323
swFeatureManagerEquationsVisibility: int = 324
swFeatureManagerMaterialVisibility: int = 325
swFeatureManagerDefaultPlanesVisibility: int = 326
swFeatureManagerOriginVisibility: int = 327
swFeatureManagerMateReferencesVisibility: int = 328
swFeatureManagerDesignTableVisibility: int = 329
swSearchResultsPerPage: int = 330
swSearchMaxResultsPerDataSource: int = 331
swUnitsForceDecimalPlaces: int = 332
swUnitsEnergyUnits: int = 333
swUnitsEnergyDecimalPlaces: int = 334
swUnitsPowerUnits: int = 335
swUnitsPowerDecimalPlaces: int = 336
swUnitsTimeUnits: int = 337
swUnitsTimeDecimalPlaces: int = 338
swSystemColorsInactiveHandles: int = 339
swPropertyMgrDockingState: int = 340
swDetailingBalloonLeaderStyle: int = 341
swDetailingBalloonLeaderLineStyle: int = 342
swDetailingBalloonLeaderLineThickness: int = 343
swDetailingBalloonFrameLineStyle: int = 344
swDetailingBalloonFrameLineThickness: int = 345
swDetailingDatumLeaderLineStyle: int = 346
swDetailingDatumLeaderLineThickness: int = 347
swDetailingDatumFrameLineStyle: int = 348
swDetailingDatumFrameLineThickness: int = 349
swDetailingGtolLeaderStyle: int = 350
swDetailingGtolLeaderSide: int = 351
swDetailingGtolLeaderLineStyle: int = 352
swDetailingGtolLeaderLineThickness: int = 353
swDetailingGtolFrameLineStyle: int = 354
swDetailingGtolFrameLineThickness: int = 355
swDetailingNoteLeaderLineStyle: int = 356
swDetailingNoteLeaderLineThickness: int = 357
swDetailingSFSymbolLeaderStyle: int = 358
swDetailingSFSymbolLeaderLineStyle: int = 359
swDetailingSFSymbolLeaderLineThickness: int = 360
swDetailingWeldSymbolLeaderSide: int = 361
swDetailingWeldSymbolLeaderLineStyle: int = 362
swDetailingWeldSymbolLeaderLineThickness: int = 363
swDetailingGeneralTableBorderLineWeight: int = 364
swDetailingGeneralTableGridLineWeight: int = 365
swDetailingBillOfMaterialBorderLineWeight: int = 366
swDetailingBillOfMaterialGridLineWeight: int = 367
swDetailingHoleTableBorderLineWeight: int = 368
swDetailingHoleTableGridLineWeight: int = 369
swDetailingRevisionTableBorderLineWeight: int = 370
swDetailingRevisionTableGridLineWeight: int = 371
swDetailingDimensionTextAndLeaderStyle: int = 372
swDetailingToleranceStyle: int = 375
swDetailingToleranceFitTolDisplay: int = 376
swFeatureManagerSensorVisibility: int = 377
swFeatureManagerTableFolderVisibility: int = 378
swSystemColorsDrawingsSpeedPakModelEdge: int = 379
swFeatureManagerConfigTableFolderVisibility: int = 380
swDetailingDatumGbLeaderStyle: int = 381
swDetailingTitleBlockTableBorderLineWeight: int = 382
swDetailingTitleBlockTableGridLineWeight: int = 383
swExportVrmlVersion: int = 384
swExportJpegCompression: int = 385
swSystemColorsDrawingsModelTangentEdges: int = 386
swSystemColorsMateCalloutHealthy: int = 387
swSystemColorsMateCalloutWarning: int = 388
swSystemColorsMateCalloutError: int = 389
swCenterLineMarkOrient: int = 390
swLineFontSpeedPakDrawingsModelEdgesThickness: int = 400
swLineFontSpeedPakDrawingsModelEdgesStyle: int = 401
swDisplayStateCreationChoice: int = 402
swSystemColorsSheetMetalTemporaryGraphics: int = 403
swSystemColorsMeasureSelection: int = 404
swPartDimXpertLengthUnitTol1Decimals: int = 405
swPartDimXpertLengthUnitTol2Decimals: int = 406
swPartDimXpertLengthUnitTol3Decimals: int = 407
swPartDimXpertGeneralToleranceClass: int = 408
swPartDimXpertLocationDistanceTolType: int = 409
swPartDimXpertLocationAngleTolType: int = 410
swPartDimXpertLocationDistanceBlockPrecision: int = 411
swPartDimXpertLocationAngleBlockPrecision: int = 412
swPartDimXpertChainPatternLocTolType: int = 413
swPartDimXpertChainInnerTolType: int = 414
swPartDimXpertChainPatternLocBlockPrecision: int = 415
swPartDimXpertChainDistanceBwtnFeatBlockPrecision: int = 416
swPartDimXpertChamferDistanceTolType: int = 417
swPartDimXpertChamferAngleTolType: int = 418
swPartDimXpertChamferDistanceBlockPrecision: int = 419
swPartDimXpertChamferAngleBlockPrecision: int = 420
swPartDimXpertSizeDiameterTolType: int = 421
swPartDimXpertSizeCounterboreDiameterTolType: int = 422
swPartDimXpertSizeCountersinkDiameterTolType: int = 423
swPartDimXpertSizeCountersinkAngleTolType: int = 424
swPartDimXpertSizeLengthSlotTolType: int = 425
swPartDimXpertSizeWidthSlotTolType: int = 426
swPartDimXpertSizeDepthTolType: int = 427
swPartDimXpertSizeFilletRadiusTolType: int = 428
swPartDimXpertSizeDiameterBlockPrecsion: int = 429
swPartDimXpertSizeCounterboreDiameterBlockPrecsion: int = 430
swPartDimXpertSizeCountersinkDiameterBlockPrecsion: int = 431
swPartDimXpertSizeCountersinkAngleBlockPrecision: int = 432
swPartDimXpertSizeLengthSlotBlockPrecision: int = 433
swPartDimXpertSizeWidthSlotBlockPrecision: int = 434
swPartDimXpertSizeDepthBlockPrecision: int = 435
swPartDimXpertSizeFilletRadiusBlockPrecision: int = 436
swPartDimXpertDisplaySlotDimensionType: int = 437
swPartDimXpertDisplayHoleDimensionType: int = 438
swPartDimXpertDisplayGtolLinearDimAttachment: int = 439
swPartDimXpertDisplayDatumGtolSurfaceAttachment: int = 440
swPartDimXpertDisplayDatumGtolLinearDimAttachment: int = 441
swExportIFCUnits: int = 442
swDetailingOrthoViewLabels_Scale: int = 443
swDetailingOrthoViewLabels_Delimiter: int = 444
swSystemOptionDisplayAntiAliasing: int = 445
swTableHoleDualDimensionPos: int = 446
swSystemColorsDrawingsChangedDimensions: int = 447
swDetailingBendTableBorderLineWeight: int = 448
swDetailingBendTableGridLineWeight: int = 449
swBendLeadingZero: int = 450
swBendTableZeroQuantityDisplay: int = 451
swBendInnerRadiusPrecision: int = 452
swBendAngularPrecision: int = 453
swBendTableTagStyle: int = 454
swPunchTableOriginStandard: int = 455
swPunchTableLocationPrecision: int = 456
swTablePunchDualDimensionPos: int = 457
swPunchTableTagStyle: int = 458
swDetailingSectionArrowStyle: int = 459
swPerformanceFeedback: int = 460
swLineFontAdjoiningComponent: int = 461
swLineFontAdjoiningComponentStyle: int = 462
swSystemColorsNoteHandle: int = 463
swSystemColorsCrossHair: int = 464
swSystemColorsNoteEditHandle: int = 465
swSystemColorsTemporarySketchDragging: int = 466
swSystemColorsWeldPathSelection: int = 467
swDetailingPunchTableBorderLineWeight: int = 468
swShowEquationCircularReferencesMessage: int = 469
swDetailingPunchTableGridLineWeight: int = 470
swDetailingWeldTableGridLineWeight: int = 471
swDetailingWeldTableBorderLineWeight: int = 472
swSearchIndexingPerformance: int = 473
swLargeAsmModeLargeDesignReviewThreshhold: int = 474
swShowEquationPotentialCircularReferencesMessage: int = 475
swSaveReminderAutoDismissInterval: int = 476
swDetailingRevisionCloudLineStyle: int = 477
swDetailingRevisionCloudLineThickness: int = 478
swDetailingHalfSectionArrow: int = 479
swBendAllowancePrecision: int = 480
swFeatureManagerFavorites: int = 481
swFeatureManagerEDrawingMarkups: int = 482
swSheetMetalColorBoundingBox: int = 483
swSheetMetalBendNotesLeaderLineStyle: int = 484
swSheetMetalBendNotesLeaderLineThickness: int = 485
swSheetMetalBendNotesBorderStyle: int = 486
swSheetMetalBendNotesBorderSize: int = 487
swSheetMetalBendNotesTextAlignment: int = 488
swSheetMetalBendNotesLeaderAnchor: int = 489
swSheetMetalBendNotesLeaderDisplay: int = 490
swSystemColorsCurrentColorScheme: int = 491
swSystemColorsEnvelopes: int = 492
swDetailingRadialDimsArrowPlacement: int = 493
swSearchDissectionDailyStartTime: int = 494
swSearchDissectionDailyStopTime: int = 495
swLineFontBendLineUpStyle: int = 496
swLineFontBendLineDownStyle: int = 497
swLineFontEnvelopeComponentStyle: int = 498
swLineFontBendLineUpThickness: int = 499
swLineFontBendLineDownThickness: int = 500
swLineFontEnvelopeComponentThickness: int = 501
swEnvelopeComponentColor: int = 502
swAssemblyVisualizationComponentColor1: int = 503
swAssemblyVisualizationComponentColor2: int = 504
swAssemblyVisualizationComponentColor3: int = 505
swAssemblyVisualizationComponentColor4: int = 506
swAssemblyVisualizationComponentColor5: int = 507
swAssemblyVisualizationComponentColor6: int = 508
swDetailingMiscView_Scale: int = 509
swDetailingMiscView_Delimiter: int = 510
swDetailingMiscView_Name: int = 511
swDetailingAuxView_ViewIndication: int = 512
swDetailingAuxView_Rotation: int = 513
swDetailingSectionView_Rotation: int = 515
swDimensionsExtensionLineStyle: int = 516
swDimensionsExtensionLineStyleThickness: int = 517
swDetailingOrthoView_Name: int = 518
swAssemblyOpenMessagesDismissTime: int = 519
swButtonSize: int = 520
swTextSize: int = 521
swUnitsDecimalRounding: int = 522
swDetailingLocationLabelFrameLineStyle: int = 523
swDetailingLocationLabelFrameLineThickness: int = 524
swDetailingLocationLabelStyle: int = 525
swDetailingLocationLabelFit: int = 526
swDetailingLocationLabelUpperText: int = 527
swDetailingLocationLabelLowerText: int = 528
swDrawingSheetsZonesOrigin: int = 529
swDrawingSheetsZonesLetterLayout: int = 530
swDetailingBalloonAutoBalloons: int = 531
swFeatureManagerSelectionSetsVisibility: int = 532
swFeatureManagerHistory: int = 533
swPDFExportShadedDraftDPI: int = 534
swPDFExportOleDPI: int = 535
swTwistCountValue: int = 536
swManipConnectionPointColor: int = 537
swRefVisualizationParentColor: int = 538
swRefVisualizationChildrenColor: int = 539
swDrawingSheetCustomPropSheetNo: int = 540
swIFCExportSaveType: int = 541
swDetailingSectionViewLineStyleDisplay: int = 542
swSaveIFCFormat: int = 543
swDetailingLinearForeshortened: int = 544
swCartoonEdgeThickness: int = 545
swTempGraphicsAddMaterialColor: int = 546
swTempGraphicsRemoveMaterialColor: int = 547
swDetailingBorderLeaderLineStyle: int = 548
swDetailingBorderLeaderLineThickness: int = 549
swDetailingBorderZoneDividerLineStyle: int = 550
swDetailingBorderZoneDividerLineThickness: int = 551
swIFCOmniUniClassPreference: int = 552
swSystemColorsIconColor: int = 553
swSystemColorsBackground: int = 554
swShadedSketchContourColor: int = 555
sw3DPDFAccuracy: int = 556
swLineFontEmphasizedSectionOutlineStyle: int = 557
swLineFontEmphasizedSectionThickness: int = 558
swLineFontEmphasizedSectionEndCapStyle: int = 559
swBasicDimType: int = 560
swPolarMinHoles: int = 561
swGraphicsTreeItemNormalColor: int = 562
swZoneLineColor: int = 563
swSketch_Auto_Solve_Threshold: int = 564
swDrawing_Auto_Solve_Threshold: int = 565
swPenSketchStrokeThickness: int = 566
swPenSketchStrokeColor: int = 567
swMatesDefaultMisalignedType: int = 569
swUpdateOutOfDateSpeedPakConfigOnSave: int = 570
swFeatureManagerMeshBodiesVisibility: int = 571
swSolidBodiesDescriptionFirstPropertyIndex: int = 572
swSolidBodiesDescriptionSecondPropertyIndex: int = 573
swSolidBodiesDescriptionThirdPropertyIndex: int = 574
swDefaultConfigSortOrder: int = 575
swGraphicalAnnotationsColor: int = 576
swImportNeutral_KnitOption: int = 577
swImportNeutral_CurvesAndPointsOption: int = 578
swImportNeutralAssemblyStructureMapping: int = 579
swImportNeutralUnits: int = 580
swBBoxDescriptionApplyMethod: int = 581
swDetailingTrailingZeroTolerance: int = 582
swDetailingTrailingZeroProperties: int = 583
swDetailingAngleTrailingZero: int = 584
swDetailingAngleTrailingZeroTolerance: int = 585
swDetailingAngularRunningTrailingZero: int = 586
swDetailingAngularRunningTrailingZeroTolerance: int = 587
swEdrawingsAttachmentOption: int = 588
swEdrawingsAttachmentType: int = 589
swExportPlyUnits: int = 591
swPLYQuality: int = 592
swMaximumRecentDocuments: int = 593
swFlatPatternColorsBendLinesUpDirection: int = 594
swFlatPatternColorsBendLinesDownDirection: int = 595
swFlatPatternColorsFromFeature: int = 596
swFlatPatternColorsBendLinesHems: int = 597
swFlatPatternColorsModelEdges: int = 598
swFlatPatternColorsFlatPatternSketchColor: int = 599
swFlatPatternColorsBoundingBox: int = 600
swSheetMetalMBDBendNotesStyle: int = 601
swSheetMetalMBDLeaderStyle: int = 602
swSheetMetalMBDLeaderLineThickness: int = 603
swSheetMetalMBDTextAlignment: int = 604
swSheetMetalMBDLeaderAnchor: int = 605
swSheetMetalMBDLeaderDisplay: int = 606
swSheetMetalMBDBalloonStyle: int = 607
swSheetMetalMBDFit: int = 608
swSheetMetalMBDLineStyle_BendLinesUp: int = 609
swSheetMetalMBDLineStyle_BendLinesDown: int = 610
swFeatureManagerMarkupsVisibility: int = 611
swEnableAutoMateFlip: int = 612
swSystemColorsSelectedItem5: int = 613
swSystemColorsSelectedItem6: int = 614
swFeatureManagerTranslatedLanguage: int = 615
swAssemblyLoadComponents: int = 616
swConfigurationViewForFeatureManagerTree: int = 617
swDetailingGtolMaterialConditionSymbolPlacement: int = 618
swBomOverriddenCellValueColor: int = 619
swSheetPrintQuadrant: int = 620
swSketchExplodedColor: int = 621
swDefaultBOMPartNumberForNewConfig: int = 622
swDimOverriddenCellValueColor: int = 623
swOppHandMirrorComp: int = 624
swGtolDecimalSeparatorType: int = 625
swCollinearChainDimensionArrowHeadTerminationStyle: int = 626
swRecognizedMeshFaceColor: int = 627
swUnrecognizedMeshFaceColor: int = 628
swDetailingSFSymbolStandard: int = 629
swZoomLevelOnOpen: int = 630
swSMGExportProfile: int = 631
swSMGRefineRelativeType: int = 632
swSMGRefinementType: int = 633
swSMGRefinementRelativeQuality: int = 634
swPMIEditColor: int = 635
swPrimaryComponentIdentifier: int = 636
swPartDimXpertToleranceMethod: int = 637
swDetailingFamilyTableGridLineWeight: int = 638
swDetailingFamilyTableBorderLineWeight: int = 639
swExportSVPJFileFormatGroupType: int = 640
swMarkAssyAsModifiedWhenCosmeticChangesToRefDocs: int = 641
swDxfGeomExportOption: int = 642
swSaveToVersion: int = 643

# swUserPreferenceOption_e (SwConst)
swDetailingNoOptionSpecified: int = 0
swDetailingAnnotation: int = 100
swDetailingBalloon: int = 101
swDetailingDatum: int = 102
swDetailingGeometricTolerance: int = 103
swDetailingNote: int = 104
swDetailingSurfaceFinishSymbol: int = 105
swDetailingWeldSymbol: int = 106
swDetailingRevisionCloud: int = 107
swDetailingTableAnnotation: int = 150
swDetailingGeneralTable: int = 151
swDetailingBillOfMaterial: int = 152
swDetailingHoleTable: int = 153
swDetailingRevisionTable: int = 154
swDetailingDimension: int = 200
swDetailingAngleDimension: int = 201
swDetailingArcLengthDimension: int = 202
swDetailingChamferDimension: int = 203
swDetailingDiameterDimension: int = 204
swDetailingHoleDimension: int = 205
swDetailingLinearDimension: int = 206
swDetailingOrdinateDimension: int = 207
swDetailingRadiusDimension: int = 208
swDetailingAngularRunningDimension: int = 209
swDetailingDrawingView: int = 300
swDetailingDetailView: int = 301
swDetailingSectionView: int = 302
swDetailingAuxiliaryView: int = 303
swDetailingOrthoView: int = 304
swDetailingBendTable: int = 305
swDetailingPunchTable: int = 306
swDetailingWeldTable: int = 307
swDetailingMiscView: int = 308
swDetailingLocationLabel: int = 309
swDetailingFamilyTable: int = 310

# swUserPreferenceRoutingDouble_e (SWRoutingLib)
swSlackPercentage: int = 1
swTextSizeForConnectionAndRoutePoints: int = 2

# swUserPreferenceRoutingFileLocations_e (SWRoutingLib)
swRoutingLibraryPath: int = 1
swFileLocationsRoutingAssemblyTemplate: int = 2
swFileLocationsRoutingStandardTubes: int = 3
swFileLocationsRoutingPipeTubeCoveringLibrary: int = 4
swFileLocationsRoutingCableLibrary: int = 5
swFileLocationsRoutingComponentLibrary: int = 6
swFileLocationsRoutingStandardCable: int = 7
swFileLocationsRoutingCoveringLibrary: int = 8
swFileLocationsRoutingTagSchemes: int = 9
swFileLocationsRoutingInterconnectsLibrary: int = 10

# swUserPreferenceRoutingInteger_e (SWRoutingLib)
swComponentRotationIncrementDegrees: int = 1
swEnableMinimumBendRadiusChecks: int = 2

# swUserPreferenceRoutingToggle_e (SWRoutingLib)
swAutomaticallyCreateSketchFillets: int = 1
swSaveRouteAssemblyExternally: int = 2
swSaveRoutePartsExternally: int = 3
swUseAutomaticNamingForRouteParts: int = 4
swCreateCustomFittings: int = 5
swCreatePipesOnOpenLineSegments: int = 6
swAutomaticallyRouteOnDropOfFlangeConnectors: int = 7
swAutomaticallyRouteOnDropOfClips: int = 8
swAutomaticallyAddDimensionToRouteStubs: int = 9
swEnableRouteErrorChecking: int = 10
swDisplayErrorBalloons: int = 11
swIncludeCoveringsInBOM: int = 12
swAlwaysUseDefaultDocumentTemplate: int = 13
swUseTriadToPosAndOrientComp: int = 14
swUseAutoNamingForRouteParts: int = 15
swUseCenterlineDim: int = 16
swAutomaticallyZoomToFitRouteComponents: int = 17
swUseConfigureComponentsToSelectConfigurations: int = 18
swCreateRoutePartForSegmentsHavingBendRadiusLessThanMinimum: int = 19
swHideConfigurationDialogForSWElectricalComponents: int = 20

# swUserPreferenceStringListValue_e (SwConst)
swDxfMappingFiles: int = 0
swEmodelSelectionList: int = 1
swEmodelAttachmentList: int = 2

# swUserPreferenceStringValue_e (SwConst)
swFileLocationsDocuments: int = 1
swFileLocationsPaletteFeatures: int = 2
swFileLocationsPaletteParts: int = 3
swFileLocationsPaletteFormTools: int = 4
swFileLocationsBlocks: int = 5
swFileLocationsDocumentTemplates: int = 6
swFileLocationsSheetFormat: int = 7
swDefaultTemplatePart: int = 8
swDefaultTemplateAssembly: int = 9
swDefaultTemplateDrawing: int = 10
swBackupDirectory: int = 11
swFileLocationsBendTable: int = 12
swMaterialPropertyCrosshatchPattern: int = 13
swDrawingAreaHatchPattern: int = 14
swDetailingNextDatumFeatureLabel: int = 15
swFileSaveAsCoordinateSystem: int = 16
swFileLocationsPaletteAssemblies: int = 17
swCustomPropertyUsedAsComponentDescription: int = 18
swFileLocationsLibraryFeatures: int = 19
swFileLocationsMacroFeatures: int = 20
swFileLocationsWebFolders: int = 21
swFileLocationsBOMTemplates: int = 22
swFileLocationsMacros: int = 23
swFileLocationsJournalFile: int = 24
swFileLocationsCustomPropertyFile: int = 25
swFileLocationsHoleCalloutFormatFile: int = 26
swFileLocationsDimensionFavorites: int = 27
swFileLocationsMaterialDatabases: int = 28
swFileLocationsWeldmentProfiles: int = 29
swFileLocationsColorSwatches: int = 30
swFileLocationsTextures: int = 31
swFileLocationsWeldmentPropertyFile: int = 32
swFileLocationsHoleTableTemplates: int = 33
swFileLocationsWeldmentCutListTemplates: int = 34
swFileLocationsRevisionTableTemplates: int = 35
swDrawingCustomPropertyUsedAsRevision: int = 36
swFileLocationsRouteComponentLibrary: int = 37
swFileLocationsDesignLibrary: int = 38
swFileLocationsLineStyleDefinitions: int = 39
swFileLocationsDesignJournalTemplate: int = 40
swFileLocationsRouteCableLibrary: int = 41
swFileLocationsAppearances: int = 42
swFileLocationsScenes: int = 43
swFileLocationsLights: int = 44
swFileLocationsBendNoteFormatFile: int = 45
swSeparatorCharacterForDims: int = 46
swFileLocationsRouteCoveringLibrary: int = 47
swFileLocationsDesignCheckerFile: int = 48
swReferenceTriadXLabel: int = 49
swReferenceTriadYLabel: int = 50
swReferenceTriadZLabel: int = 51
swHoleWizardToolBoxFolder: int = 52
swAutoSaveDirectory: int = 53
swColorsBackgroundImageFile: int = 54
swDetailingBOMUpperCustomProperty: int = 55
swDetailingBOMLowerCustomProperty: int = 56
swFileLocationsTxCalloutFormatFile: int = 57
swFileLocations3DCCModelFolder: int = 58
swFileLocationsHoleWizardFavoritesDB: int = 59
swFileLocationsSearchPaths: int = 60
swFileLocationsSheetMetalGaugeTable: int = 61
swFileLocationsSpellingFolders: int = 62
swDetailingLayer: int = 63
swFileLocationsDraftingStandard: int = 64
swDetailingDimensionStandardName: int = 65
swOverriddenQuantityColumnName: int = 66
swFileLocationsCustomAppearances: int = 67
swFileLocationsCustomDecals: int = 68
swFileLocationsCustomScenes: int = 69
swFileLocationsTitleBlockTableTemplate: int = 70
swFileLocationsBendCalculationTable: int = 71
swFileLocationsThemeFolder: int = 72
swExportIFCType: int = 73
swFileLocationsFuncBldrSegTypeDefinitions: int = 74
swFileLocationsSustainabilityReportTemplateFolder: int = 75
swFileLocationsCostingReportTemplateFolder: int = 76
swFileLocationsCostingTemplates: int = 77
swFileLocationsWeldTableTemplate: int = 78
swFileLocationsBendTableTemplate: int = 79
swFileLocationsPunchTableTemplate: int = 80
swDetailingDetailViewLabels_CustomName: int = 81
swDetailingDetailViewLabels_CustomScale: int = 82
swDetailingSectionViewLabels_CustomName: int = 83
swDetailingSectionViewLabels_CustomScale: int = 84
swDetailingAuxViewLabels_CustomName: int = 85
swDetailingAuxViewLabels_CustomScale: int = 86
swCenterLineLayer: int = 87
swCenterMarkLayer: int = 88
swSheetMetalBendNotesLayer: int = 89
swSearchDissectionLocation: int = 91
swFileLocationsSymbolLibraryFolder: int = 92
swFileLocationsNewSheetFormat: int = 93
swDetailingMiscView_CustomName: int = 94
swDetailingMiscView_CustomScale: int = 95
swDraftStandardExclusionList: int = 96
swDetailingOrthoView_CustomName: int = 97
swDetailingOrthoView_CustomScale: int = 98
swElecDuctingDuctName: int = 99
swElecCableTrayDuctName: int = 100
swHvacRectDuctName: int = 101
swHvacCirDuctName: int = 102
swElecDuctingElbowName: int = 102
swElecCableTrayElbowName: int = 103
swHvacRectElbowName: int = 104
swHvacCirElbowName: int = 105
swBorderLayer: int = 106
swFileLocationsThreadProfiles: int = 107
swFileLocationsGeneralTablesTemplate: int = 108
swFileLocationsTxGeneralFileLocation: int = 109
swMySldSettings: int = 110
swSolidBodiesBBoxDescriptionPrefix: int = 111
swSolidBodiesBBoxDescriptionFirstSeparator: int = 112
swSolidBodiesBBoxDescriptionSecondSeparator: int = 113
swSolidBodiesBBoxDescriptionSuffix: int = 114
swSheetMetalDescription: int = 115
swDimXpertGeneralToleranceCustomTable: int = 116
swFileLocationsDefaultSave: int = 117
swHoleTagsList: int = 118
swBomTableBOMHeaderCustomText_ForTopLevelOnlyBOM: int = 119
swBomTableBOMHeaderCustomText_ForPartOnlyBOM: int = 120
swBomTableBOMHeaderCustomText_ForIndentedBOM: int = 121
swFileLocationsDrawingScaleStandard: int = 122
swStructureSystemsFolder: int = 123
swWeldmentStructureCutlistID: int = 124
swWeldmentSheetmetalCutlistID: int = 125
swWeldmentGenericCutlistID: int = 126
swFileLocationsHatchPatternFile: int = 127
swFileLocationsInspectionProjects: int = 128
swFileLocationsInspectionReports: int = 129
swLastSynchronizationTimeStamp: int = 130
swFileLocationsInspectionExports: int = 131
swFileLocationsStructureSystemsConnectionElements: int = 132
swFileLocationsConnectedLibrary: int = 133
swExportOutputCoordinateSystem: int = 134
swFileLocationsDefeatureRuleSets: int = 135
swOppPrefixSuffixText: int = 136
swVirtualComponentPrefixedit: int = 137
swIFCExportPropertySetMappingFile: int = 138
swSMGMetaPropertyName: int = 139
swFileLocationsFamilyTableTemplates: int = 140
swMultiCAD_ImportQueuePath: int = 141

# swUserPreferenceTextFormat_e (SwConst)
swDetailingNoteTextFormat: int = 0
swDetailingDimensionTextFormat: int = 1
swDetailingSectionTextFormat: int = 2
swDetailingDetailTextFormat: int = 3
swDetailingViewArrowTextFormat: int = 4
swDetailingSurfaceFinishTextFormat: int = 5
swDetailingWeldSymbolTextFormat: int = 6
swDetailingGeneralTableTextFormat: int = 7
swDetailingBalloonTextFormat: int = 8
swDetailingDetailLabelTextFormat: int = 9
swDetailingSectionLabelTextFormat: int = 10
swDetailingBillOfMaterialTextFormat: int = 11
swDetailingHoleTableTextFormat: int = 12
swDetailingRevisionTableTextFormat: int = 13
swDetailingDatumTextFormat: int = 14
swDetailingGeometricToleranceTextFormat: int = 15
swDetailingAuxiliaryLabelTextFormat: int = 16
swDetailingTableTextFormat: int = 17
swDetailingViewTextFormat: int = 18
swDetailingAnnotationTextFormat: int = 19
swDetailingTitleBlockTableTextFormat: int = 20
swDetailingOrthoLabelTextFormat: int = 21
swDetailingBendTextFormat: int = 22
swDetailingSectionLabelNameTextFormat: int = 23
swDetailingSectionLabelLabelTextFormat: int = 24
swDetailingSectionLabelScaleTextFormat: int = 25
swDetailingSectionLabelDelimiterTextFormat: int = 26
swDetailingPunchTextFormat: int = 27
swSheetMetalBendNotesTextFormat: int = 28
swDetailingWeldSymbolTextRootInsideFont: int = 29
swDetailingMiscView_NameTextFormat: int = 30
swDetailingMiscView_ScaleTextFormat: int = 31
swDetailingMiscView_DelimiterTextFormat: int = 32
swDetailingAuxView_NameTextFormat: int = 33
swDetailingAuxView_LabelTextFormat: int = 34
swDetailingAuxView_RotationTextFormat: int = 35
swDetailingAuxView_ScaleTextFormat: int = 36
swDetailingAuxView_DelimiterTextFormat: int = 37
swDetailingSectionView_RotationTextFormat: int = 38
swDetailingOrthoView_NameTextFormat: int = 39
swDetailingOrthoView_ScaleTextFormat: int = 40
swDetailingOrthoView_DelimiterTextFormat: int = 41
swDetailingDetailView_NameTextFormat: int = 42
swDetailingDetailView_LabelTextFormat: int = 43
swDetailingDetailView_ScaleTextFormat: int = 44
swDetailingDetailView_DelimiterTextFormat: int = 45
swDetailingLocationLabelTextFormat: int = 46
swPointAxisCoordSystemNameFontTextFormat: int = 47
swPointAxisCoordSystemLabelFontTextFormat: int = 48
swSheetMetalMBDTextFormat: int = 49
swDetailingFamilyTableTextFormat: int = 50

# swUserPreferenceToggle_e (SwConst)
swUseFolderSearchRules: int = 0
swDisplayArcCenterPoints: int = 1
swDisplayEntityPoints: int = 2
swIgnoreFeatureColors: int = 3
swDisplayAxes: int = 4
swDisplayPlanes: int = 5
swDisplayOrigins: int = 6
swDisplayTemporaryAxes: int = 7
swDxfMapping: int = 8
swSketchAutomaticRelations: int = 9
swInputDimValOnCreate: int = 10
swFullyConstrainedSketchMode: int = 11
swXTAssemSaveFormat: int = 12
swDisplayCoordSystems: int = 13
swExtRefOpenReadOnly: int = 14
swExtRefNoPromptOrSave: int = 15
swExtRefMultipleContexts: int = 16
swExtRefAutoGenNames: int = 17
swExtRefUpdateCompNames: int = 18
swDisplayReferencePoints: int = 19
swDisplayRoutePoints: int = 19
swUseShadedFaceHighlight: int = 20
swDXFDontShowMap: int = 21
swThumbnailGraphics: int = 22
swUseAlphaTransparency: int = 23
swDynamicDrawingViewActivation: int = 24
swAutoLoadPartsLightweight: int = 25
swIGESStandardSetting: int = 26
swIGESNurbsSetting: int = 27
swTiffPrintScaleToFit: int = 28
swDisplayVirtualSharps: int = 29
swUpdateMassPropsDuringSave: int = 30
swDisplayAnnotations: int = 31
swDisplayFeatureDimensions: int = 32
swDisplayReferenceDimensions: int = 33
swDisplayAnnotationsUseAssemblySettings: int = 34
swDisplayNotes: int = 35
swDisplayGeometricTolerances: int = 36
swDisplaySurfaceFinishSymbols: int = 37
swDisplayWeldSymbols: int = 38
swDisplayDatums: int = 39
swDisplayDatumTargets: int = 40
swDisplayCosmeticThreads: int = 41
swDetailingDisplayWithBrokenLeaders: int = 42
swDetailingDualDimensions: int = 43
swDetailingDisplayDatumsPer1982: int = 44
swDetailingDisplayAlternateSection: int = 45
swDetailingCenterMarkShowLines: int = 46
swDetailingFixedSizeWeldSymbol: int = 47
swDetailingDimsShowParenthesisByDefault: int = 48
swDetailingDimsSnapTextToGrid: int = 49
swDetailingDimsCenterText: int = 50
swDetailingRadialDimsDisplay2ndOutsideArrow: int = 51
swDetailingRadialDimsArrowsFollowText: int = 52
swDetailingDimLeaderOverrideStandard: int = 53
swDetailingNotesDisplayWithBentLeader: int = 54
swDisplayTextAtSameSizeAlways: int = 55
swDisplayOnlyInViewOfCreation: int = 56
swGridDisplay: int = 57
swGridDisplayDashed: int = 58
swGridAutomaticScaling: int = 59
swSnapToPoints: int = 60
swSnapToAngle: int = 61
swUnitsLinearRoundToNearestFraction: int = 62
swUnitsLinearFeetAndInchesFormat: int = 63
swFeatureManagerEnsureVisible: int = 64
swFeatureManagerNameFeatureWhenCreated: int = 65
swFeatureManagerKeyboardNavigation: int = 66
swFeatureManagerDynamicHighlight: int = 67
swColorsGradientPartBackground: int = 68
swSTLBinaryFormat: int = 69
swSTLShowInfoOnSave: int = 70
swSTLDontTranslateToPositive: int = 71
swSTLComponentsIntoOneFile: int = 72
swSTLCheckForInterference: int = 73
swOpenLastUsedDocumentAtStart: int = 74
swSingleCommandPerPick: int = 75
swShowDimensionNames: int = 76
swShowErrorsEveryRebuild: int = 77
swMaximizeDocumentOnOpen: int = 78
swEditDesignTableInSeparateWindow: int = 80
swEnablePropertyManager: int = 81
swUseSystemSeparatorForDims: int = 82
swUseEnglishLanguage: int = 83
swDrawingAutomaticModelDimPlacement: int = 84
swDrawingDisplayViewBorders: int = 85
swAutomaticScaling3ViewDrawings: int = 86
swDrawingAutomaticBomUpdate: int = 87
swDrawingSelectHiddenEntities: int = 88
swDrawingCreateDetailAsCircle: int = 89
swAutomaticDrawingViewUpdate: int = 90
swDrawingDetailInferCorner: int = 91
swDrawingDetailInferCenter: int = 92
swDrawingViewShowContentsWhileDragging: int = 93
swSketchAlternateSplineCreation: int = 94
swSketchInferFromModel: int = 95
swSketchPromptToCloseSketch: int = 96
swSketchCreateSketchOnNewPart: int = 97
swSketchOverrideDimensionsOnDrag: int = 98
swSketchDisplayPlaneWhenShaded: int = 99
swSketchOverdefiningDimsPromptToSetState: int = 100
swSketchOverdefiningDimsSetDrivenByDefault: int = 101
swPerformanceVerifyOnRebuild: int = 102
swPerformanceDynamicUpdateOnMove: int = 103
swPerformanceAlwaysGenerateCurvature: int = 104
swPerformanceWin95ZoomClipping: int = 105
swIGESDuplicateEntities: int = 106
swIGESHighTrimCurveAccuracy: int = 107
swIGESExportSketchEntities: int = 108
swIGESComponentsIntoOneFile: int = 109
swIGESFlattenAssemHierarchy: int = 110
swAlwaysUseDefaultTemplates: int = 111
swUseSimpleOpenGL: int = 112
swShowRefGeomName: int = 113
swUseShadedPreview: int = 114
swEdgesHiddenEdgeSelectionInWireframe: int = 115
swEdgesHiddenEdgeSelectionInHLR: int = 116
swEdgesRepaintAfterSelectionInHLR: int = 117
swEdgesHighlightFeatureEdges: int = 118
swEdgesDynamicHighlight: int = 119
swEdgesHighQualityDisplay: int = 120
swEdgesOpenEdgesDifferentColor: int = 121
swEnableConfirmationCorner: int = 122
swAutoShowPropertyManager: int = 123
swIncontextFeatureHolderVisibility: int = 124
swTransparencyHighQualityDynamic: int = 125
swEdgesShadedEdgesDifferentColor: int = 126
swEdgesAntiAlias: int = 127
swPageSetupPrinterUsePrinterMargin: int = 128
swPageSetupPrinterDrawingScaleToFit: int = 129
swPageSetupPrinterPartAsmPrintWindow: int = 130
swDisplayShadowsInShadedMode: int = 131
swDrawingViewSmoothDynamicMotion: int = 132
swDrawingEliminateDuplicateDimsOnInsert: int = 133
swRapidDraftPrintOutOfSynchWaterMark: int = 134
swDrawingViewAutoHideComponents: int = 135
swEdgesDisplayShadedPlanes: int = 136
swPlaneDisplayShowEdges: int = 137
swPlaneDisplayShowIntersections: int = 138
swColorsUseSpecifiedEditColors: int = 139
swEnablePerformanceEmail: int = 141
swSnapOnlyIfGridDisplayed: int = 142
swDetailingBalloonsDisplayWithBentLeader: int = 143
swBOMConfigurationLocked: int = 144
swBOMConfigurationUseDocumentFont: int = 145
swBOMConfigurationUseSummaryInfo: int = 146
swBOMConfigurationAlignBottom: int = 147
swBOMContentsDisplayAtTop: int = 148
swBOMControlIdFromAssembly: int = 149
swBOMControlMissingRows: int = 150
swBOMControlSplitTable: int = 151
swAutomaticDrawingViewUpdateDefault: int = 152
swAutomaticDrawingViewUpdateForceOff: int = 153
swAnnotationDisplayHideDanglingDim: int = 154
swDetailingDimBreakAroundArrow: int = 155
swDetailingDimensionsToleranceUseParentheses: int = 156
swDetailingDimensionsToleranceUseDimensionFont: int = 157
swImageQualityApplyToAllReferencedPartDoc: int = 158
swPrintBackground: int = 159
swEDrawingsCompression: int = 160
swImportSolidSurface: int = 161
swImportFreeCurves: int = 162
swImport2dCurvesAs2dSketch: int = 163
swLargeAsmModeAutoLoadLightweight: int = 166
swLargeAsmModeUpdateMassPropsOnSave: int = 167
swLargeAsmModeAutoRecover: int = 168
swLargeAsmModeRemoveDetail: int = 169
swLargeAsmModeHideAllItems: int = 170
swLargeAsmModeDynHighlightFeatureMgr: int = 171
swLargeAsmModeDynHighlightGraphicsView: int = 172
swLargeAsmModeAntiAliasEdgesFastMode: int = 173
swLargeAsmModeShadowsShadedMode: int = 174
swLargeAsmModeTransparencyNormalViewMode: int = 175
swLargeAsmModeTransparencyDynamicViewMode: int = 176
swLargeAsmModeShowContentsDragDrawView: int = 177
swLargeAsmModeSmoothDynamicMotionDrawView: int = 178
swLargeAsmModeDrawingHLREdgesWhenShaded: int = 179
swLargeAsmModeAutoHideCompsDrawViewCreation: int = 180
swLargeAsmModeDrawingAutoLoadModels: int = 181
swLargeAsmModeAlwaysGenerateCurvature: int = 182
swImportStepConfigData: int = 183
swIGESExportSolidAndSurface: int = 184
swIGESExportFreeCurves: int = 185
swIGESExportAsWireframe: int = 186
swDetailingDimensionsAngularToleranceUseParentheses: int = 187
swDetailingDimensionsToleranceFitTolUseDimensionFont: int = 188
swDetailingAutoInsertCenterMarks: int = 189
swDetailingAutoInsertCenterLines: int = 190
swSTLPreview: int = 191
swDetailingCenterMarkUseCenterLine: int = 192
swMaterialPropertySolidFill: int = 193
swSaveEModelData: int = 194
swDisplayCurves: int = 195
swDisplaySketches: int = 196
swDisplayAllAnnotations: int = 197
swViewDisplayHideAllTypes: int = 198
swColorsUseShadedEdgeColor: int = 199
swViewpointPreserveNormals: int = 200
swSaveBackupFilesInSameLocationAsOriginal: int = 201
swNotifySNLNotObtainedForEDrawingsSave: int = 202
swPerformanceRemoveDetailDuringZoomPanRotate: int = 203
swDisplayEnableSelectionThroughTransparency: int = 204
swDisplayReferenceTriad: int = 205
swDrawingsDefaultDisplayTypeFastHLRHLV: int = 206
swDrawingsDefaultDisplayTypeHLREdgesWhenShaded: int = 207
swPerformanceSave: int = 208
swDetailingAutoUpdateBOM: int = 209
swImageQualityUseHighQualityEdgeSize: int = 210
swDrawingSaveShadedData: int = 211
swEDrawingsOkayToMeasure: int = 212
swBomTableKeepMissingItems: int = 213
swBomTableStrikeThroughMissingItems: int = 214
swRevisionTableUpdateAllLabels: int = 215
swIGESImportShowLevel: int = 216
swColorsMatchViewAndFeatureManagerBackground: int = 217
swEDrawingsSaveShadedDataInDrawings: int = 218
swDisplayReferencePoints2: int = 219
swImportMultBodyAsPartData: int = 220
swEDrawingsExportSTLOkay: int = 221
swDetailingDisplaySFSymbolsPer2002: int = 222
swDontCopyQTYColumnNameFromTemplate: int = 223
swEDrawingsSaveAnimationOkay: int = 224
swInsertViewForNewDrawing: int = 225
swInsertComponentForNewAssembly: int = 226
swCollabTopDocsNoPromptOrSave: int = 227
swCollabEnableMultiUser: int = 228
swViewSketchRelations: int = 229
swDisplayShadedCosmeticThreads: int = 230
swCollabAddShortcutMenuItems: int = 231
swCollabCheckReadOnlyModifiedByOthers: int = 232
swDisplayAllSplineHandles: int = 233
swAssemblyAllowComponentMoveByDragging: int = 234
swHoleTableCombineTags: int = 235
swHoleTableCombineSameSize: int = 236
swHoleTableHoleCentersVisible: int = 237
swHoleTableAutomaticUpdate: int = 238
swDetailingDimOffsetText: int = 239
swDetailingDetailViewLabels_PerStandard: int = 240
swDetailingDetailViewLabels_Stacked: int = 241
swDetailingSectionViewLabels_PerStandard: int = 242
swDetailingSectionViewLabels_Stacked: int = 243
swDetailingAuxViewLabels_PerStandard: int = 244
swDetailingAuxViewLabels_Stacked: int = 245
swExportVrmlAllComponentsInSingleFile: int = 246
swDetailingAutoInsertBalloons: int = 247
swDetailingAutoInsertDimsMarkedForDrawing: int = 248
swSketchInference: int = 249
swSketchNoSolveMove: int = 250
swDetailingDimANSIBentLeader: int = 251
swUnitsDualLinearRoundToNearestFraction: int = 252
swUnitsDualLinearFeetAndInchesFormat: int = 253
swOneConfigOnlyTopLevelBom: int = 254
swImageQualitySaveTesselationWithPartDoc: int = 255
swShowSheetMetalBendNotes: int = 256
swDetailingCThreadDisplayHighQuality: int = 257
swDetailingDimsPrefixInsideBasicTolBox: int = 258
swDetailingDimsAutoJogOrdinates: int = 259
swColorsWireframeHLRShadedSame: int = 260
swEditMacroAfterRecord: int = 261
swUseEnglishLanguageFeatureNames: int = 262
swDrawingDisplayArcCenterPoints: int = 263
swDrawingDisplayEntityPoints: int = 264
swDrawingPrintBreaklinesInBrokenView: int = 265
swSketchSnapsPoints: int = 266
swSketchSnapsCenterPoints: int = 267
swSketchSnapsMidPoints: int = 268
swSketchSnapsQuadrantPoints: int = 269
swSketchSnapsIntersections: int = 270
swSketchSnapsNearest: int = 271
swSketchSnapsTangent: int = 272
swSketchSnapsPerpendicular: int = 273
swSketchSnapsParallel: int = 274
swSketchSnapsHVLines: int = 275
swSketchSnapsHVPoints: int = 276
swSketchSnapsLength: int = 277
swSketchSnapsGrid: int = 278
swSketchSnapToGridIfDisplayed: int = 279
swSketchSnapsAngle: int = 280
swPerformanceSheetMetalIgnoreSelfIntersect: int = 281
swExternalReferencesDisable: int = 282
swFileExplorerShowMyDocuments: int = 283
swFileExplorerShowMyComputer: int = 284
swFileExplorerShowMyNetworkPlaces: int = 285
swFileExplorerShowRecentDocuments: int = 286
swFileExplorerShowHiddenReferencedDocuments: int = 287
swFileExplorerShowSamples: int = 288
swBomTableDontAddQTYNextToConfigName: int = 289
swImportAutoRunImportDiagnosticsPersist: int = 290
swImportAutoRunImportDiagnostics: int = 291
swQuickTipsPart: int = 292
swQuickTipsAssembly: int = 293
swQuickTipsDrawing: int = 294
swSketchLineLengthVirtualSharp3d: int = 295
swSketchShowSplineControlPolygon: int = 296
swLargeAsmModeEnabled: int = 297
swLargeAsmModeSuspendAutoRebuild: int = 298
swLargeAsmModeUseHLREdgesInShaded: int = 299
swFourViewportProjectionType: int = 300
swImportIDFAddDrilledHoles: int = 301
swImportIDFReverseUndersideComponents: int = 302
swImportStlVrmlTextureInformation: int = 303
swImportUGToolBodies: int = 304
swDxfUseSolidworksLayers: int = 305
swDisplayRelationsShowPropertyManager: int = 306
swReferenceTriadUseAlternateLabels: int = 307
swDetailingAutoInsertCenterMarksForHoles: int = 308
swDetailingAutoInsertCenterMarksForFillets: int = 309
swDetailingScaleWithDimHeight: int = 310
swDetailingScaleWithSectionTextHeight: int = 311
swUserEnableAutoFix: int = 312
swDisplayLights: int = 313
swDisplayCameras: int = 314
swDxfEndPointMerge: int = 316
swPerformancePreviewDuringOpen: int = 317
swImportDxfDimsToPartSketch: int = 318
swAutoSaveEnable: int = 319
swBackupEnable: int = 320
swBackupRemoveEnable: int = 321
swSaveReminderEnable: int = 322
swPDFExportInColor: int = 323
swPDFExportEmbedFonts: int = 324
swPDFExportHighQuality: int = 325
swPDFExportPrintHeaderFooter: int = 326
swPDFExportUseCurrentPrintLineWeights: int = 327
swSketchShadowDrag: int = 328
swWarnSaveUpdateErrors: int = 329
swEnablePerformanceFeedback: int = 330
swShowDrawingViewPalette: int = 331
swDisplayDimensionsFlatToScreen: int = 332
swPerformanceAlwaysResolveSubassemblies: int = 333
swWarnSavingReferencedDoc: int = 334
swFeatureManagerTransparentFlyout: int = 335
swDetailingDimsShowBroken: int = 336
swDetailingDetailViewLabels_AboveView: int = 337
swDetailingSectionViewLabels_AboveView: int = 338
swDetailingAuxViewLabels_AboveView: int = 339
swPreserveRedundantGeometry: int = 340
swTranslateNameAttribFromKernelBody: int = 341
swPageSetupHighQuality: int = 345
swSketchShowSplineOuterComb: int = 346
swViewShowAnnotationLinkErrors: int = 347
swViewShowAnnotationLinkVariables: int = 348
swHideUnitsOfLengthValues: int = 349
swShowNewsFeedsInTaskPane: int = 350
swViewReverseWheelZoomDirection: int = 351
swDrawingMarkAllDimensionsForDrawing: int = 352
swDrawingShowSheetFormatDialog: int = 353
swDrawingSheetBackgroundAsPicture: int = 354
swDisplayNotesFlatToScreen: int = 355
swDisplayMissingRefsWhenEditFeature: int = 356
swSearchWhileTyping: int = 357
swDxfExportSplinesAsSplines: int = 358
swDetailingDimsFollowDimXpertLayout: int = 359
swDisplayDimXpertDimensions: int = 360
swDetailingShowHaloAroundAnnotation: int = 361
swDetailingImportEntireAssemblyAnnotations: int = 362
swSearchIncludeContentCentral: int = 363
swUserEnablePlasticsMode: int = 364
swDrawingDisableNoteDimensionInference: int = 365
swEDrawingsSaveAnimationToAllConfigs: int = 366
swEDrawingsSaveAnimationRecalculate: int = 367
swPromptForAutoMateFlip: int = 368
swViewZoomFitAndCenter: int = 369
swDisplayCameraFOVBox: int = 370
swSketchAcceptNumericInput: int = 372
swDisableWeldmentConfigStrings: int = 373
swDisplayLiveSections: int = 374
swDetailingAnnotationUseBentLeaders: int = 375
swDetailingBalloonUseDocBentLeaderLength: int = 376
swDetailingGtolUseDocBentLeaderLength: int = 377
swDetailingNoteUseDocBentLeaderLength: int = 378
swDetailingSFSymbolUseDocBentLeaderLength: int = 379
swDetailingShowDualDimensionUnits: int = 380
swDetailingOrdinateDisplayAsChain: int = 382
swDetailingDatumsAnchorFilled: int = 383
swDetailingDatumsAnchorShoulder: int = 384
swEDrawingsSaveBOM: int = 385
swClearanceShowIgnored: int = 386
swClearanceIgnoreEqual: int = 387
swClearanceSubAssyAsComp: int = 388
swClearanceCreateFasteners: int = 389
swClearanceMakeTransparent: int = 390
swClearanceDisplayOption: int = 391
swStopDebuggingVstaOnExit: int = 392
swOverrideQuantityColumnName: int = 393
swAutoSizePropertyManager: int = 394
swUserEnablePlasticsMode2: int = 395
swStepExportSplitPeriodic: int = 396
swStepExportFaceEdgeProps: int = 397
swSATExportSplitPeriodic: int = 398
swSATExportFaceEdgeProps: int = 399
swDXFHighQualityExport: int = 400
swDetailingNotesLeaderJustificationSnapping: int = 401
swDetailingAutoInsertCenterMarksForSlots: int = 402
swStepExportConfigurationData: int = 403
swImageQualityZoomToFitForPreviewImages: int = 404
swTiffPrintAllSheets: int = 405
swTiffPrintUseSheetSize: int = 406
swDrawingAutoSpaceDimsOnDelete: int = 407
swDetailingTablesUseTemplateSettings: int = 408
swSaveNewComponentsToExternalFile: int = 409
swDoublePrimeMark: int = 410
swDrawingHideEnds: int = 411
swCenterLineMarkLinear: int = 412
swCenterLineMarkCircular: int = 413
swCenterLineMarkEndsOnlyLinear: int = 414
swCenterLineMarkEndsOnlyCircular: int = 415
swPreciseRenderingOfOverlappingGeometry: int = 416
swEnableMouseGestures: int = 417
swPartExportFlatPattern: int = 418
swHoleTableReuseDeleted: int = 419
swHoleTableAddNewAtEnd: int = 420
swFlatPatternOpt_SimplifyBends: int = 421
swFlatPatternOpt_CornerTreatment: int = 422
swSATExportMultLumpsToSingleBody: int = 423
swPartDimXpertBlockTolerance: int = 424
swPartDimXpertLocationInclinedPlane: int = 425
swPartDimXpertChainHoleDimensionChain: int = 426
swPartDimXpertChainPocketDimensionChain: int = 427
swPartDimXpertGeometricApplyMMC: int = 428
swPartDimXpertGeometricCreateBasicDimension: int = 429
swPartDimXpertGeometricBasicDimensionChain: int = 430
swPartDimXpertGeometricPositionAtMMC: int = 431
swPartDimXpertGeometricPositionComposite: int = 432
swPartDimXpertGeometricSurfaceProfileComposite: int = 433
swPartDimXpertDisplayEliminateDuplicates: int = 434
swPartDimXpertDisplayShowInstanceCount: int = 435
swDisplayPlaneSections: int = 436
swDisplaySimulationSymbol: int = 437
swStoreImagesWithModel: int = 438
swImageQualityUseOldTangentEdgeDisplay: int = 439
swAddDimensionsToSketchEntity: int = 440
swDetailingOrthoViewLabels_PerStandard: int = 441
swDetailingOrthoViewLabels_AboveView: int = 442
swDetailingOrthoViewLabelsEnableShow: int = 443
swUseModelColorInDrawings: int = 444
swDetailingShowDimensionUnits: int = 445
swUseFolderAsDefaultSearchLocation: int = 446
swDetailingAutoInsertCenterMarksForHolesAsm: int = 447
swDetailingAutoInsertCenterMarksForFilletsAsm: int = 448
swDetailingAutoInsertCenterMarksForSlotsAsm: int = 449
swTableHoleDualDimensionDisplay: int = 450
swTableHoleShowUnitsForDualDisplay: int = 451
swDXFExportHiddenLayersOn: int = 452
swDXFExportHiddenLayersWarnIsOn: int = 453
swDetailingLinkParentViewConfiguration: int = 454
swLockRecentDocumentsList: int = 455
swDxfAllSheetsToPaperSpace: int = 456
swFlatPatternOpt_DisableSplitters: int = 457
swFlatPatternOpt_WhenFlattenedShowPunches: int = 458
swFlatPatternOpt_WhenFlattenedShowProfiles: int = 459
swFlatPatternOpt_WhenFlattenedShowCenters: int = 460
swUserEnableFreezeBar: int = 461
swAddDimensionsToLineEntity: int = 462
swAddDimensionsToRectangleEntity: int = 463
swAddDimensionsToArcEntity: int = 464
swAddDimensionsToCircleEntity: int = 465
swAddDimensionsToSlotEntity: int = 466
swUseChangedDimensions: int = 467
swImportDoclessModelInAssem: int = 468
swAddDrivenDimensions: int = 469
swExtRefShowXInFeatureTree: int = 470
swLargeAsmModeUseLargeDesignReview: int = 471
swTablePunchShowUnitsForDualDisplay: int = 472
swPunchTableCombineTags: int = 473
swPunchTableCombineSameSize: int = 474
swFlatPatternOpt_ShowGrainDirection: int = 475
swFlatPatternOpt_ShowFixedFace: int = 476
swAutoNormalToSketchMode: int = 477
swUseSpeedpakModelColorInDrawings: int = 478
swTablePunchDualDimensionsDisplay: int = 479
swDrawingEliminateDuplicateModelNotesOnInsert: int = 480
swDrawingDisableNoteMergeWhenDragging: int = 481
swDrawingReuseViewLettersFromDeletedAuxilary: int = 482
swFeatureManagerEnableTreeFilter: int = 483
swDxfExportAllSheetsToPaperSpace: int = 484
swDisplayAmbientOcclusionShadows: int = 485
swDraftQualityAmbientOcclusion: int = 486
swQuickViewTransparencyEnabled: int = 487
swQuickViewTransparencyDynamic: int = 488
swDetailingDimsShowLeadingZeros: int = 489
swHoleTableShowAnsiInchSize: int = 490
swSaveWithoutCostingData: int = 491
swLoadEnvelopeLightweight: int = 492
swLoadEnvelopeReadOnly: int = 493
swDetailingSectionHideShoulders: int = 494
swLargeAsmModeDismissAutoUpdate: int = 495
swStepExport3DCurveFeatures: int = 497
swDetailingAutoInsertDowelSymForHolesPart: int = 499
swDetailingAutoInsertDowelSymForHolesAsm: int = 500
swDetailingDimsApplyUpdatedRules: int = 501
swDetailingAngularRunningDisplayAsChain: int = 502
swDetailingAngularRunningExtensionLineExtend: int = 5030
swDetailingAngularRunningRunBidirectionally: int = 504
swDetailingDimsAutoJogAngularRunning: int = 505
swDetailingLinearDimPrecisionLinkWithModel: int = 506
swDetailingAltLinearDimPrecisionLinkWithModel: int = 507
swDetailingDisplayDualBasicDimensionInOneBox: int = 509
swAutoScaleTextureSFDecalsToModelSize: int = 510
swLargeAsmModeAutoCheckUpdateAllComponents: int = 511
swDisplaySpeedpakGraphicsCircle: int = 512
swSheetMetalBendNotesUseDocLeaderLength: int = 513
swSheetMetalBendNotesLeaderJustificationSnapping: int = 514
swEnableSoundsForSolidWorksEvents: int = 515
swSearchShowSolidWorksSearchBox: int = 516
swSearchDissectionScheduleDaily: int = 517
swDrawingDisplaySketchHatchBehindGeometry: int = 518
swDetailingRadialDimsDisplayWithSolidLeader: int = 519
swSketchCreateDimensionOnlyWhenEntered: int = 520
swPurgeAllBodiesForNonActiveConfigurations: int = 521
swDetailingAutoInsertDowelSymbols: int = 522
swDetailingAutoInsertDowelSymbolsAsm: int = 523
swSaveReminderAutoDismissEnable: int = 524
swDrawingDisplaySketchPicturesOnSheetBehindGeometry: int = 525
swDetailingShowUnitsForDualDisplay: int = 526
swImageQualityWireframeHighCurveQuality: int = 527
swDetailingCenterOfMassScaleByView: int = 528
swDisplayCenterOfMassSymbol: int = 529
swTiffPrintPadText: int = 530
swUpdateExternFilesDispList: int = 531
swDrawingsDefaultDisplayTypeHLREdgeQualityWhenShaded: int = 532
swDrawingSheetsUseDifferentSheetFormat: int = 533
swDetailingMiscView_PerStandard: int = 534
swDetailingMiscView_AboveView: int = 535
swDetailingMiscView_AddViewLabelOnViewCreation: int = 536
swDetailingHighlightElements: int = 537
swDetailingAllUpperCase: int = 538
swDetailingMiscView_RemoveSpaceInScale: int = 539
swWarnStartingSketchInContextAssembly: int = 540
swDetailingAuxView_SimplifiedDetailed: int = 541
swDetailingAuxView_RemoveSpaceInScale: int = 543
swDetailingAuxView_RotateViewToHorizontalSheet: int = 544
swDetailingAuxView_RotateClockwiseCounterclockwise: int = 545
swEdgeQualityShadedEdgeViews: int = 546
swDetailingSectionView_RemoveSpaceInScale: int = 549
swColorUseSelectedItemColorsSeedsPatterns: int = 550
swDimensionsExtensionLineStyleSameAsLeader: int = 551
swDraftingStandardUppercase: int = 552
swEdgeQualityWireframeHiddenViews: int = 553
swDetailingSplitWhenTextIsSolidLeaderAligned: int = 555
swEdgesDefaultBulkSelection: int = 556
swDisplayPatternInformationTooltips: int = 557
swAssemblyUpdateModelGraphicsWhenSavingFiles: int = 558
swDetailingOrthoView_AddViewLabelOnViewCreation: int = 559
swDetailingOrthoView_RemoveSpaceInScale: int = 560
swDetailingSplitDualDimensions: int = 561
swDetailingDetailView_RemoveSpaceInScale: int = 562
swEdgesShadedModeDisplayOptimizeForThinParts: int = 563
swWhileOpeningAssembliesAutoDismissMessages: int = 564
swDetailingMiscView_DisplayLabelAboveView: int = 565
swDetailingSplitTextDualDimensions: int = 566
swDetailingOrthoView_DisplayLabelAboveView: int = 567
swIGESExportSplitPeriodic: int = 568
swRebuildSaveNewConfig: int = 569
swTextSizeUseOperatingSystemScale: int = 570
swPageSetupScaleDraftEdges: int = 571
swWeldmentEnableAutomaticCutList: int = 572
swWeldmentEnableAutomaticUpdate: int = 573
swDisplayCompAnnotations: int = 575
swShowZoneLines: int = 576
swDetailingAngDimensionsRemoveInsignificantZeros: int = 577
swShowMateReferenceErrors: int = 578
swDetailingDimensionsToleranceInwardRounding: int = 579
swDetailingNoDimSpecificOptionSpecified: int = 580
swPDFExportIncludeLayersNotToPrint: int = 581
swEDrawingsIncludeLayersNotToPrint: int = 582
swTIFIncludeLayersNotToPrint: int = 583
swSketchAddConstToRectEntity: int = 584
swSketchAddConstLineDiagonalType: int = 585
swDisableDerivedConfigurations: int = 586
swFlatPatternOpt_WhenFlattenedShowGussetProfiles: int = 587
swFlatPatternOpt_WhenFlattenedShowGussetCenters: int = 588
swImportSLDXMLImportSketchData: int = 591
swImportSLDXMLImportMechanismSketchObjectsAsBlocks: int = 592
swAMFCompression: int = 593
swAMFMaterials: int = 594
swAMFColors: int = 595
swEnhanceSmallFaceSelectionPrecision: int = 596
swWeldmentRenameCutlistDescriptionPropertyValue: int = 597
swDetailingLocationLabelAddSameSheetNumber: int = 598
swDetailingConnectionLinesHolePatternsCenterMarks: int = 599
swDetailingAuxView_IncludeLocationLabelsForNewViews: int = 600
swDetailingDetailView_IncludeLocationLabelsForNewViews: int = 601
swDetailingSectionView_IncludeLocationLabelsForNewViews: int = 602
swDrawingSheetsListNumFirstInZoneCallout: int = 603
swDrawingSheetsContinueColumnIteration: int = 604
swDrawingEnableSymbolAddingNewRevision: int = 605
swImportSLDXMLImportAssemblyMatesData: int = 606
swNoteParagraphAutoNumbering: int = 607
swBreakAlignWithParent: int = 608
swShowAnnotationInAnnotationViews: int = 609
swPrintGrid: int = 610
swPrintZoneLines: int = 611
swShowToolboxFavoritesFolder: int = 612
swDetailingCenterMarkScaleByViewScale: int = 613
swDrawingSheetsMatchCustomPropVals: int = 614
swSaveAsmAsPartPreserveIDs: int = 615
swHideShowSketchDimensions: int = 616
swPDFViewOnSave: int = 617
swDisplayDatumCoordSystems: int = 618
swMakeFirstSelectionTransparentInMateDialog: int = 619
swMatchConfigurationNames: int = 620
swDetailingLinearForeshortenedAutomatic: int = 621
swDetachSegmentOnDragMode: int = 622
swDetailingDiameterForeshortenedAutomatic: int = 623
swShowBreadcrumbsOnSelection: int = 624
swDetailingShowPeriodWithBorders: int = 625
swDetailingBorderDoubleLine: int = 628
swDetailingBorderShowZoneDividers: int = 629
swDetailingBorderShowColumns: int = 630
swDetailingBorderShowRows: int = 631
swPointAxisCoordSystemHideNames: int = 632
swFeatureManagerEnableRenamingComponent: int = 633
swDynamicReferenceVisualization_Parent: int = 634
swDynamicReferenceVisualization_Child: int = 635
sw3MFAppearances: int = 636
sw3MFMaterials: int = 637
sw3MFDecals: int = 638
swForceEnableImportDiagnosis: int = 639
swDisplayCounterpartLocationLabel: int = 640
swExtRefLoadRefDocsInMemory: int = 641
swScaleSketchOnFirstDimension: int = 642
sw3MFShowInfoOnSave: int = 643
swExtRefIncludeSubFolders: int = 644
swExtRefExcludeActiveFoldersAndRecentSaveLocations: int = 645
swSheetMetalOverrideTemplateParam: int = 646
swSheetMetalOverrideTemplateAllowance: int = 647
swSheetMetalOverrideTemplateRelief: int = 648
swShadedSketchContours: int = 650
swDetailingRadialDimsDisplayNearSideMessages: int = 651
swCollabAddTimeStampToComments: int = 652
swCollabShowCommentsInPropertyManager: int = 653
swDetailingScaleForJaggedStyle: int = 654
swDetailingDetailViewLabels_ScaleForJaggedOutline: int = 655
swFeatureManagerEnablePreviewHiddenComponents: int = 656
swWeldmentCollectIdenticalBodies: int = 657
swLargeAsmModePreviewHiddenComponent: int = 658
swLargeAsmModeVerificationOnRebuild: int = 659
swLargeAsmModeImageQualityPerfomance: int = 660
sw3DPDFCompressLossyTessellation: int = 661
swDisplayDecals: int = 662
swDisplayPartingLines: int = 663
swDisplaySketchPlanes: int = 664
swDisplayWeldBead: int = 665
swIFCOmniClassPreference: int = 666
swIFCUniClass2Preference: int = 667
swIFCCustomPropsPreference: int = 668
swIFCMaterialsMassPropertiesPreference: int = 669
swDisplayEquationIds: int = 670
swMagMatePreAlign: int = 671
swOptimizeMatePlacement: int = 672
swPdfIncludeBookmarks: int = 673
swDisplayGraphicsComponents: int = 675
swDraftingStandardAllUppercaseForTable: int = 676
swTransferHoleWizardSizeComboBoxSettings: int = 677
swAssemblyAllowCreationOfMisalignedMates: int = 678
swVrmlStlImportAsPSMesh: int = 679
swSolidBBoxDescriptionUseDefault: int = 680
swSheetMetalBodiesDescriptionUseDefault: int = 681
swVrmlStlImportSegmented: int = 682
swEnableVSTAVersion3: int = 683
swViewDispGlobalBBox: int = 684
swDisplayComponentDimXpertAnnotations: int = 685
swImportNeutral_SolidandSurface: int = 686
swImportNeutral_FreeCurvesAndPoints: int = 687
swImportNeutralReferencePlane: int = 688
swImportNeutral_AttributesAndProperties: int = 689
swImportNeutralRunDiagnostics: int = 690
swMultiCAD_Enable3DInterconnect: int = 691
swDrawingTurnOffAutomaticSolveModeAndUndo: int = 692
swSketchTurnOffAutomaticSolveModeAndUndo: int = 693
swImportSolidBody: int = 694
swImportSurfaceBody: int = 695
swImportReferencePlane: int = 696
swImportReferenceAxis: int = 697
swImportUnconsumedSketchesAndCurves: int = 698
swImportCustomProperties: int = 699
swImportMaterialProperties: int = 700
swImportDissolveTopLevelAssemblyOnOpen: int = 701
swImportIgnoreHiddenEntities: int = 702
swImportToolBodiesFromUGNX: int = 703
swIncludePMI: int = 704
swAssemblyAllowGraphicsComponent: int = 705
swCheckCrashSolutions: int = 706
swMakeTrimEntityConstruction: int = 707
swIgnoreConstructionEntity: int = 708
swLockRotationConcentricMates: int = 709
swASMSLDPRT_ExcludeComponentsByVisibility: int = 710
swASMSLDPRT_ExcludeComponentsByBBoxVolume: int = 712
swASMSLDPRT_ExcludeIfToolboxComponents: int = 713
swASMSLDPRT_IncludeMassProperties: int = 716
swEnableAllowCosmeticThreadsUpgrade: int = 718
swSheetMetalUseMaterial: int = 719
swPDFExportShadedEdgesHighQuality: int = 720
swBomTableShowCustomTextinBOMHeader_ForTopLevelOnlyBOM: int = 721
swBomTableShowCustomTextinBOMHeader_ForPartOnlyBOM: int = 722
swBomTableShowCustomTextinBOMHeader_ForIndentedBOM: int = 723
swBomTableShowConfigurationInBOMHeader_ForTopLevelOnlyBOM: int = 724
swBomTableShowConfigurationInBOMHeader_ForPartOnlyBOM: int = 725
swBomTableShowConfigurationInBOMHeader_ForIndentedBOM: int = 726
swEdit3DPDFTemplate: int = 727
swPLYBinaryFormat: int = 728
swPLYPreview: int = 729
swPLYIncludeColors: int = 730
swDisplayScrollbarsInGraphicsViewDrawings: int = 731
swDisplayScrollbarsInGraphicsViewPartsAndAssemblies: int = 732
swShowBreadcrumbsAtMousePointer: int = 733
swIncludeDocumentsOpenedFromOtherDocuments: int = 734
swIncludeSubfoldersForDrawingsSearchInPackAndGo: int = 735
swAutomaticallyPopupSelectionToolForPreciseLocation: int = 736
swCombineCutlistItemsInBOM: int = 737
swEditNameWithSlowDoubleClick: int = 738
swSheetMetalMBDDisplaySheetMetalBendNotes: int = 739
swSheetMetalMBDUseDocumentLeaderLength: int = 740
swSheetMetalMBDLeaderJustificationSnapping: int = 741
swSheetMetalMBDShowFixedFace: int = 742
swSheetMetalMBDShowGrainDirection: int = 743
swSheetMetalMBDFormat: int = 744
swEnablePerformancePipeline: int = 745
swReferenceOnlyEnvelopeComponentType: int = 746
swReferenceInContextOfTopLevelAssembly: int = 747
swDisplayDataMarkNewConfig: int = 749
swAllowCreationOfReferencesExternalToModel: int = 750
swDetailingAnnotationShowTypeInThreadCallouts: int = 751
swDetailingChainDimensionAddOverallDimensions: int = 752
swDetailingChainDimensionAddLastReferenceDimension: int = 753
swDraftingStandardAllUppercaseForDimensionsAndHoleCallouts: int = 754
swBackupAfterMeshOrRunSimulationStudy: int = 755
swIncludeDataForDelmia: int = 756
swWeldmentGenerateCutlistIDs: int = 757
swMultiCAD_ApplyOnlyToParts: int = 758
swMultiCAD_CreateNewComponentsAsExternalFiles: int = 759
swFeatureManagerShowTranslatedNameInFMTree: int = 760
swAutomaticSyncSettings: int = 761
swAutoSyncSettingsToInclude_SystemOptions: int = 762
swAutoSyncSettingsToInclude_FileLocations: int = 763
swAutoSyncSettingsToInclude_Customizations: int = 764
swEnable3DEXPERIENCEIntegration: int = 765
swShowCADFamilyConfigOnly3dexpIntegration: int = 766
swShowCADAndOtherConfig3dexpIntegration: int = 767
swEnable3DEXPERIENCEFileCompatibilityUpdate: int = 768
swImportNeutralAnalyticalConversion: int = 769
swUsePositiveInertiaTensorNotation: int = 770
swDisplayBendLines: int = 771
swTIFExportIncludeDrawingsPaperColor: int = 772
swPDFExportIncludeDrawingsPaperColor: int = 773
swSaveFileProperties: int = 774
swSaveFilePropertiesForEachComp: int = 775
swIncludeSketchData: int = 776
swSystemNotificationHideGraphicsNotification: int = 778
swDetailingModeSaveModelData: int = 779
swDetailingModeIncludeStandardViewsInViewPalette: int = 780
swStoreOLEImagesWithModel: int = 781
swDetailingAnnotationApplyNewCTDepthArchForToNewParts: int = 782
swCreateConfigurationTableOnOpen: int = 783
swExtRefForceSaveToCurrentVersion: int = 784
swDisplayTempAxesOnMouseHover: int = 785
swStepExportAtomicSave: int = 786
swStepExportAppearances: int = 787
swDisplayMeshBREPFacetFins: int = 788
swEdgesDefaultBulkSelection2: int = 789
swWeldmentUseEnglishDescriptionNameInCutlist: int = 790
swMultiCAD_3DInterconnectMaintainLinks: int = 791
swMultiCAD_3DInterconnectManualBreakLink: int = 792
swMultiCAD_3DInterconnectLinksFlag: int = 793
swSketchPreviewDimensionOnSelect: int = 794
swCollinearChainDimensionOffsetText: int = 795
swCollinearChainDimensionArrowHeadTermination: int = 796
swHardwareAccSilhouetteEdges: int = 797
swDispDimXpertDimOnTopOfModel: int = 798
swDimOverriddenHighlight: int = 799
swSketchSuppressedDimProfileErrorOption: int = 800
swDisplayTopLevelEnvelopes: int = 801
swDisplayComponentEnvelopes: int = 802
swDisplayMarkups: int = 803
swDisplayMotionSymbol: int = 804
swDrawingOpenInDetailingMode: int = 805
swDxfExportViewAsBlock: int = 806
swDetailingAutoInsertCosmeticThreadForHolesAsm: int = 807
swSpeedpakUpdateSlider: int = 808
swNoteZoomToFit: int = 809
swIFCExportUsePropertySetMappingFile: int = 810
swSheetMetalDimensionFlangeSketch: int = 811
swSeeThroughTransparentComponents: int = 812
swDisplayCartoon: int = 813
swDisplayRealViewGraphics: int = 814
swSMGExportSWBOM: int = 815
swSMGExportSWAssemEnvelope: int = 816
swSMGExportSWAppearance: int = 817
swSMGExportSWDecals: int = 818
swSMGExportSWExplodedAndSavedViews: int = 819
swSMGExportSWPMI: int = 820
swPMIOverwriteColor: int = 821
swSMGMergeFileIntoOneActorPerPart: int = 822
swSMGExportInstanceNames: int = 823
swSMGExportMetaProps: int = 824
swSMGOverloadAssemTreeNames: int = 825
swSMGExportAsBodies: int = 826
swSMGExportFreeFaces: int = 827
swSMGExportHiddenCompNOSHOW: int = 828
swAbsChordalError: int = 829
swAbsNormalDeviation: int = 830
swAbsEdgeLength: int = 831
swSMGEnableHealing: int = 832
swGenerateCutlistIDsInDocUnits: int = 833
swAutoResolveLightweightCompUponExpInFMTree: int = 834
swViewShowAnnotationTextExpression: int = 835
swOverrideTreeDisplaySysSettings: int = 836
swSecondaryComponentDescription: int = 837
swSecondaryConfigurationName: int = 838
swSecondaryConfigurationDescription: int = 839
swTertiaryDisplayStateName: int = 840
swDoNotShowConfigOrDisplayStateName: int = 841
swSecondaryPhysicalProductDescription: int = 842
swSecondaryEnterpriseItemNumber: int = 843
swTertiaryFileTitle: int = 844
swTertiaryRevision: int = 845
swAssemblyEnableCreationOfMatesUsingAI: int = 846
swDisplayDspbrAppearances: int = 847
swShowDismissedMessagesIconInStatusBar: int = 848
swWarnOnDupCompRefsForDlg: int = 849
swEnableInterfDetProgressDlg: int = 850
swDrawingDisallowCreationOfMirrorViews: int = 851
swImportPSEnableTemplates: int = 852
swImportAssemblyHybrid: int = 853
swEnableInterfDetMultiThread: int = 854
swEnableSaveToVersion: int = 855
swFamilyTableDimName: int = 856

# swUserPreferencesLanguages_e (SwConst)
swLang_Chinese: int = 0
swLang_Chinese_Simplified: int = 1
swLang_Czech: int = 2
swLang_English: int = 3
swLang_French: int = 4
swLang_German: int = 5
swLang_Italian: int = 6
swLang_Japanese: int = 7
swLang_Korean: int = 8
swLang_Polish: int = 9
swLang_Portuguese_Brazilian: int = 10
swLang_Russian: int = 11
swLang_Spanish: int = 12
swLang_Turkish: int = 13

# swUserUnitsType_e (SwConst)
swLengthUnit: int = 0
swAngleUnit: int = 1

# swVariablePitchHelixRegionParameter_e (SwConst)
swVariablePitchHelixRegionParameter_Revolution: int = 0
swVariablePitchHelixRegionParameter_Pitch: int = 1
swVariablePitchHelixRegionParameter_Height: int = 2
swVariablePitchHelixRegionParameter_Diameter: int = 3

# swVariableRadiusFilletOptions_e (SwConst)
swSmoothTransition: int = 0
swStraightTransition: int = 1

# swVersionCompatibilityResult_e (SwConst)
swVersionCompatibilityResult_Completed: int = 0
swVersionCompatibilityResult_FailUnknown: int = 1
swVersionCompatibilityResult_FailFileNotResolved: int = 2
swVersionCompatibilityResult_FailInvalidVersion: int = 3

# swVerticalJustification_e (SwConst)
swVerticalJustificationNone: int = 0
swVerticalJustificationTop: int = 1
swVerticalJustificationMiddle: int = 2
swVerticalJustificationBottom: int = 3

# swViewAlignment_e (SwConst)
swViewAlignNone: int = 0
swViewAlignedChildren: int = 1
swViewAligned: int = 2
swViewAlignBoth: int = 3

# swViewDisplayMode_e (SwConst)
swViewDisplayMode_Wireframe: int = 1
swViewDisplayMode_HiddenLinesRemoved: int = 2
swViewDisplayMode_HiddenLinesGrayed: int = 3
swViewDisplayMode_Shaded: int = 4
swViewDisplayMode_ShadedWithEdges: int = 5
swViewDisplayMode_ShadedCurvatureOn: int = 6
swViewDisplayMode_ShadedCurvatureOFF: int = 7
swViewDisplayMode_StripesOn: int = 8
swViewDisplayMode_StripesOff: int = 9
swViewDisplayMode_PerspectiveOn: int = 10
swViewDisplayMode_PerspectiveOff: int = 11
swViewDisplayMode_Faceted: int = 12
swViewDisplayMode_IntegratedPreview: int = 13

# swViewDisplayType_e (SwConst)
swIsViewSectioned: int = 0
swIsViewPerspective: int = 1
swIsViewShaded: int = 2
swIsViewWireFrame: int = 3
swIsViewHiddenLinesRemoved: int = 4
swIsViewHiddenInGrey: int = 5
swIsViewCurvature: int = 6
swIsViewStripe: int = 7

# swViewEntityType_e (SwConst)
swViewEntityType_Edge: int = 1
swViewEntityType_Vertex: int = 2
swViewEntityType_Face: int = 3
swViewEntityType_SilhouetteEdge: int = 4

# swViewIndication_e (SwConst)
swViewIndication_ArrowMethod: int = 0
swViewIndication_SameAsSection: int = 1

# swViewNotify_e (SwConst)
swViewRepaintNotify: int = 1
swViewChangeNotify: int = 2
swViewDestroyNotify: int = 3
swViewRepaintPostNotify: int = 4
swViewBufferSwapNotify: int = 5
swViewDestroyNotify2: int = 6
swViewPerspectiveViewNotify: int = 7
swViewRenderLayer0Notify: int = 8
swViewUserClearSelectionsNotify: int = 9
swViewPrintNotify: int = 10
swViewGraphicsRenderPostNotify: int = 11
swViewDisplayModeChangePreNotify: int = 12
swViewDisplayModeChangePostNotify: int = 13
swViewPrintNotify2: int = 14

# swViewOrientationUpAxisFlyout_e (SwConst)
swViewOrientationUpAxisFlyout_Y_Up: int = 0
swViewOrientationUpAxisFlyout_Z_Up: int = 1

# swViewportDisplay_e (SwConst)
swViewportSingle: int = 1
swViewportTwoViewHorizontal: int = 2
swViewportTwoViewVertical: int = 3
swViewportFourView: int = 4

# swVisibilityState_e (SwConst)
swVisibilityStateHide: int = 1
swVisibilityStateShown: int = 2
swVisibilityStateUnknown: int = 3

# swVrmlOutputVersion_e (SwConst)
swVrmlOutputVersion_97: int = 1
swVrmlOutputVersion_01: int = 2

# swWeldBeadSide_e (SwConst)
swWeldBeadArrowSide: int = 0
swWeldBeadOtherSide: int = 1

# swWeldBeadType_e (SwConst)
swWeldBeadTypeFull: int = 0
swWeldBeadTypeIntermittent: int = 1
swWeldBeadTypeStaggered: int = 2

# swWeldSymbolContourTypes_e (SwConst)
swWeldContourNone: int = 1
swWeldContourFlat: int = 2
swWeldContourConvex: int = 3
swWeldContourConcave: int = 4

# swWeldSymbolField_e (SwConst)
swFieldWeldNone: int = 1
swFieldWeldUp: int = 2
swFieldWeldDown: int = 3

# swWeldSymbolSymmetric_e (SwConst)
swWeldSymmetric: int = 1
swWeldDashedLineOnTop: int = 2
swWeldDashedLineOnBottom: int = 3

# swWeldSymbolTextTypes_e (SwConst)
swWeldLeftTextAbove: int = 1
swWeldSymbolTextAbove: int = 2
swWeldRightTextAbove: int = 3
swWeldStaggerTextAbove: int = 4
swWeldLeftTextBelow: int = 5
swWeldSymbolTextBelow: int = 6
swWeldRightTextBelow: int = 7
swWeldStaggerTextBelow: int = 8
swWeldProcessText: int = 9

# swWeldmentTrimExtendOptionType_e (SwConst)
swWeldmentTrimExtendOption_AllowTrimmedExtensionTrim: int = 1
swWeldmentTrimExtendOption_AllowTrimmingExtensionTrim: int = 2
swWeldmentTrimExtendOption_CopedCut: int = 4
swWeldmentTrimExtendOption_WeldGap: int = 8

# swWindowState_e (SwConst)
swWindowNormal: int = 0
swWindowMaximized: int = 1
swWindowMinimized: int = 2

# swWireRouteError_e (SWRoutingLib)
swWireRouteError_WireNotRouted: int = 1
swWireRouteError_WireSegmentsBranching: int = 2
swWireRouteError_WireSegmentsDisjoint: int = 3
swWireRouteError_WireMissingFromToComponent: int = 4
swWireRouteError_WireMismatchedFromComponent: int = 5
swWireRouteError_WireMismatchedToComponent: int = 6
swWireRouteError_WireMismatchedFromPin: int = 7
swWireRouteError_WireMismatchedToPin: int = 8
swWireRouteError_WirePathViolatesBendRadius: int = 9

# swWitnessLineVisibility_e (SwConst)
swWitnessLineBoth: int = 0
swWitnessLineFirst: int = 1
swWitnessLineSecond: int = 2
swWitnessLineNone: int = 3

# swWrapMethods_e (SwConst)
swWrapMethods_Analytical: int = 0
swWrapMethods_SplineSurface: int = 1

# swWrapSketchType_e (SwConst)
swWrapSketchType_Emboss: int = 0
swWrapSketchType_Engrave: int = 1
swWrapSketchType_Scribe: int = 2

# swWzdGeneralHoleTypes_e (SwConst)
swWzdCounterBore: int = 0
swWzdCounterSink: int = 1
swWzdHole: int = 2
swWzdPipeTap: int = 3
swWzdTap: int = 4
swWzdLegacy: int = 5
swWzdCounterBoreSlot: int = 6
swWzdCounterSinkSlot: int = 7
swWzdHoleSlot: int = 8

# swWzdHoleAuxiliaryConstants_e (SwConst)
NUM_HOLE_GENERIC_TYPES: int = 9
NUM_HOLE_TYPES: int = 91
NUM_HOLE_STANDARD_TYPES: int = 249

# swWzdHoleCosmeticThreadTypes_e (SwConst)
swCosmeticThreadNone: int = 0
swCosmeticThreadWithCallout: int = 1
swCosmeticThreadWithoutCallout: int = 2

# swWzdHoleCounterSinkHeadClearanceTypes_e (SwConst)
swHeadClearanceIncreasedCsink: int = 0
swHeadClearanceAddToCbore: int = 1

# swWzdHoleHcoilTapTypes_e (SwConst)
swTapTypePlug: int = 0
swTapTypeBottom: int = 1

# swWzdHoleScrewClearanceTypes_e (SwConst)
swScrewClearanceClose: int = 0
swScrewClearanceNormal: int = 1
swScrewClearanceLoose: int = 2

# swWzdHoleStandardFastenerTypes_e (SwConst)
swStandardAnsiInchBinding: int = 0
swStandardAnsiInchButton: int = 1
swStandardAnsiInchFillister: int = 2
swStandardAnsiInchHexBolt: int = 3
swStandardAnsiInchHexBoltFinished: int = 4
swStandardAnsiInchHexBoltHeavy: int = 5
swStandardAnsiInchHexScrew: int = 6
swStandardAnsiInchHexWasherScrew: int = 7
swStandardAnsiInchPan: int = 8
swStandardAnsiInchSocketCapScrew: int = 9
swStandardAnsiInchSocketShoulderScrew: int = 10
swStandardAnsiInchSquare: int = 11
swStandardAnsiInchTruss: int = 12
swStandardAnsiInchFlatSocket82: int = 13
swStandardAnsiInchFlatHead100: int = 14
swStandardAnsiInchFlatHead82: int = 15
swStandardAnsiInchOval: int = 16
swStandardAnsiInchHcoilTapDrills: int = 17
swStandardAnsiInchAllDrillSizes: int = 18
swStandardAnsiInchFractionalDrillSizes: int = 19
swStandardAnsiInchLetterDrillSizes: int = 20
swStandardAnsiInchPipeTapDrills: int = 21
swStandardAnsiInchScrewClearances: int = 22
swStandardAnsiInchTapDrills: int = 23
swStandardAnsiInchNumberDrillSizes: int = 24
swStandardAnsiInchTaperedPipeTap: int = 25
swStandardAnsiInchBottomingTappedHole: int = 26
swStandardAnsiInchTappedHole: int = 27
swStandardAnsiMetricButton: int = 28
swStandardAnsiMetricHexBolt: int = 29
swStandardAnsiMetricHexCapScrew: int = 30
swStandardAnsiMetricHexScrewFormed: int = 31
swStandardAnsiMetricPan: int = 32
swStandardAnsiMetricSocketHeadCapScrew: int = 33
swStandardAnsiMetricSocketShoulderScrew: int = 34
swStandardAnsiMetricFlatSocket82: int = 35
swStandardAnsiMetricFlatHead82: int = 36
swStandardAnsiMetricOval: int = 37
swStandardAnsiMetricHcoilTapDrills: int = 38
swStandardAnsiMetricDrillSizes: int = 39
swStandardAnsiMetricScrewClearances: int = 40
swStandardAnsiMetricTapDrills: int = 41
swStandardAnsiMetricBottomingTappedHole: int = 42
swStandardAnsiMetricTappedHole: int = 43
swStandardBSICheese: int = 44
swStandardBSIHexBolt: int = 45
swStandardBSIHexCapScrew: int = 46
swStandardBSIHexMachineScrew: int = 47
swStandardBSIPanHead: int = 48
swStandardBSISocketCapScrew: int = 49
swStandardBSIFlatSocketCap: int = 50
swStandardBSIFlatHead: int = 51
swStandardBSIOvalHead: int = 52
swStandardBSIHcoilTapDrills: int = 53
swStandardBSIDrillSizes: int = 54
swStandardBSIScrewClearances: int = 55
swStandardBSITapDrills: int = 56
swStandardBSITappedHoleBottoming: int = 57
swStandardBSITappedHole: int = 58
swStandardBSITaperedPipeTap: int = 59
swStandardDINHeavyHexBolt: int = 60
swStandardDINHexFlangeBolt: int = 61
swStandardDINCheeseHead: int = 62
swStandardDINHexBolt: int = 63
swStandardDINHexCapScrew: int = 64
swStandardDINHexMachineScrew: int = 65
swStandardDINPan: int = 66
swStandardDINSocketHeadCap: int = 67
swStandardDINSocketCTSKFlatHead: int = 68
swStandardDINCTSKFlatHead: int = 69
swStandardDINCTSKRaisedHead: int = 70
swStandardDINHcoilTapDrills: int = 71
swStandardDINDrillSizes: int = 72
swStandardDINScrewClearances: int = 73
swStandardDINTapDrills: int = 74
swStandardDINTappedHoleBottoming: int = 75
swStandardDINTappedHole: int = 76
swStandardDINTaperedPipeTap: int = 77
swStandardDMECCorePins: int = 78
swStandardDMECXCorePins: int = 79
swStandardDMETHXEjectorPins: int = 80
swStandardDMEStandardLeaderPins: int = 81
swStandardDMEReturnPins: int = 82
swStandardDMESocketCapScrew: int = 83
swStandardDMESupportPillarSHCS: int = 84
swStandardDMESpruPullerPins: int = 85
swStandardDMEStripperBolt: int = 86
swStandardDMEFlatSocket82: int = 87
swStandardDMEFlatHead100: int = 88
swStandardDMEFlatHead82: int = 89
swStandardDMEOval: int = 90
swStandardDMESupportPillarClearance: int = 91
swStandardDMEFractionalDrillSizes: int = 92
swStandardDMEHcoilTapDrills: int = 93
swStandardDMEAllDrillSizes: int = 94
swStandardDMELetterDrillSizes: int = 95
swStandardDMENumberDrillSizes: int = 96
swStandardDMEPipeTapDrills: int = 97
swStandardDMEScrewClearances: int = 98
swStandardDMECCorePinClearances: int = 99
swStandardDMECXCorePinClearances: int = 100
swStandardDMETHXEjectorPinClearances: int = 101
swStandardDMELeaderPinClearances: int = 102
swStandardDMEReturnPinClearances: int = 103
swStandardDMESpruPullerPinClearances: int = 104
swStandardDMETapDrills: int = 105
swStandardDMEBottomingTappedHole: int = 106
swStandardDMETappedHole: int = 107
swStandardDMETaperedPipeTap: int = 108
swStandardHascoMetricCCorePins: int = 109
swStandardHascoMetricGuideBushings: int = 110
swStandardHascoMetricGuidePillars: int = 111
swStandardHascoMetricLocatingGuideBushings: int = 112
swStandardHascoMetricLocatingGuidePillars: int = 113
swStandardHascoMetricSocketCapScrew: int = 114
swStandardHascoMetricShoulderScrew: int = 115
swStandardHascoMetricCTSKFlatHead: int = 116
swStandardHascoMetricDrillSizes: int = 117
swStandardHascoMetricScrewClearances: int = 118
swStandardHascoMetricCorePinClearances: int = 119
swStandardHascoMetricCenteringSleeve: int = 120
swStandardHascoMetricEjectorRodClearances: int = 121
swStandardHascoMetricBottomingTappedHole: int = 122
swStandardHascoMetricTappedHole: int = 123
swStandardHcoilInchInsert10Dia: int = 124
swStandardHcoilInchInsert15Dia: int = 125
swStandardHcoilInchInsert20Dia: int = 126
swStandardHcoilInchInsert25Dia: int = 127
swStandardHcoilInchInsert30Dia: int = 128
swStandardHcoilMetricInsert10Dia: int = 129
swStandardHcoilMetricInsert15Dia: int = 130
swStandardHcoilMetricInsert20Dia: int = 131
swStandardHcoilMetricInsert25Dia: int = 132
swStandardHcoilMetricInsert30Dia: int = 133
swStandardISOCheeseHead: int = 134
swStandardISOHexBolt: int = 135
swStandardISOHexCapScrew: int = 136
swStandardISOHexMachineScrew: int = 137
swStandardISOPan: int = 138
swStandardISOSocketHeadCap: int = 139
swStandardISOSocketCTSKFlatHead: int = 140
swStandardISOCTSKFlatHead: int = 141
swStandardISOCTSKRaisedHead: int = 142
swStandardISODrillSizes: int = 143
swStandardISOScrewClearances: int = 144
swStandardISOTapDrills: int = 145
swStandardISOTappedHoleBottoming: int = 146
swStandardISOTappedHole: int = 147
swStandardISOTaperedPipeTap: int = 148
swStandardJISCheeseHead: int = 149
swStandardJISFillisterHead: int = 150
swStandardJISButton: int = 151
swStandardJISHexBolt: int = 152
swStandardJISHexCapScrew: int = 153
swStandardJISHexMachineScrew: int = 154
swStandardJISPan: int = 155
swStandardJISSocketHeadCap: int = 156
swStandardJISSocketShoulderScrew: int = 157
swStandardJISFlatCTSKHead: int = 158
swStandardJISRaisedCTSKHead: int = 159
swStandardJISDrillSizes: int = 160
swStandardJISScrewClearances: int = 161
swStandardJISTapDrills: int = 162
swStandardJISTappedHoleBottoming: int = 163
swStandardJISTappedHole: int = 164
swStandardJISTaperedPipeTap: int = 165
swStandardPCSReturnPins: int = 166
swStandardPCSCorePins: int = 167
swStandardPCSEjectorPins: int = 168
swStandardPCSStandardLeaderPins: int = 169
swStandardPCSSocketCapScrew: int = 170
swStandardPCSStripperBolt: int = 171
swStandardPCSSupportPillarSHCS: int = 172
swStandardPCSFlatHead100: int = 173
swStandardPCSFlatHead82: int = 174
swStandardPCSOval: int = 175
swStandardPCSFlatSocket82: int = 176
swStandardPCSHcoilTapDrills: int = 177
swStandardPCSFractionalDrillSizes: int = 178
swStandardPCSNumberDrillSizes: int = 179
swStandardPCSPipeTapDrills: int = 180
swStandardPCSScrewClearances: int = 181
swStandardPCSAllDrillSizes: int = 182
swStandardPCSEjectorPinClearances: int = 183
swStandardPCSLetterDrillSizes: int = 184
swStandardPCSSupportPillarClearances: int = 185
swStandardPCSCorePinClearances: int = 186
swStandardPCSLeaderPinClearances: int = 187
swStandardPCSReturnPinClearances: int = 188
swStandardPCSTapDrills: int = 189
swStandardPCSBottomingTappedHole: int = 190
swStandardPCSTappedHole: int = 191
swStandardPCSTaperedPipeTap: int = 192
swStandardProgressiveSocketCapScrew: int = 193
swStandardProgressiveReturnPins: int = 194
swStandardProgressiveCorePins: int = 195
swStandardProgressiveEjectorPins: int = 196
swStandardProgressiveSpruePullerPins: int = 197
swStandardProgressiveSupportPillarSHCS: int = 198
swStandardProgressiveStripperBolt: int = 199
swStandardProgressiveStandardLeaderPins: int = 200
swStandardProgressiveFlatSocket82: int = 201
swStandardProgressiveOval: int = 202
swStandardProgressiveFlatHead100: int = 203
swStandardProgressiveFlatHead82: int = 204
swStandardProgressiveHcoilTapDrills: int = 205
swStandardProgressiveFractionalDrillSizes: int = 206
swStandardProgressiveNumberDrillSizes: int = 207
swStandardProgressivePipeTapDrills: int = 208
swStandardProgressiveScrewClearances: int = 209
swStandardProgressiveAllDrillSizes: int = 210
swStandardProgressiveEjectorPinClearances: int = 211
swStandardProgressiveLetterDrillSizes: int = 212
swStandardProgressiveSupportPillarClearances: int = 213
swStandardProgressiveCorePinClearances: int = 214
swStandardProgressiveLeaderPinClearances: int = 215
swStandardProgressiveSpruePullerPinClearances: int = 216
swStandardProgressiveReturnPinClearances: int = 217
swStandardProgressiveTapDrills: int = 218
swStandardProgressiveTappedHole: int = 219
swStandardProgressiveBottomingTappedHole: int = 220
swStandardProgressiveTaperedPipeTap: int = 221
swStandardSuperiorReturnPins: int = 222
swStandardSuperiorEjectorPins: int = 223
swStandardSuperiorSpruePullerPins: int = 224
swStandardSuperiorSupportPillarSHCS: int = 225
swStandardSuperiorStripperBolt: int = 226
swStandardSuperiorSocketCapScrew: int = 227
swStandardSuperiorStandardLeaderPins: int = 228
swStandardSuperiorFlatHead100: int = 229
swStandardSuperiorFlatHead82: int = 230
swStandardSuperiorOval: int = 231
swStandardSuperiorFlatSocket82: int = 232
swStandardSuperiorHcoilTapDrills: int = 233
swStandardSuperiorFractionalDrillSizes: int = 234
swStandardSuperiorNumberDrillSizes: int = 235
swStandardSuperiorPipeTapDrills: int = 236
swStandardSuperiorScrewClearances: int = 237
swStandardSuperiorAllDrillSizes: int = 238
swStandardSuperiorEjectorPinClearances: int = 239
swStandardSuperiorLetterDrillSizes: int = 240
swStandardSuperiorSupportPillarClearances: int = 241
swStandardSuperiorLeaderPinClearances: int = 242
swStandardSuperiorSpruePullerPinClearances: int = 243
swStandardSuperiorReturnPinClearances: int = 244
swStandardSuperiorTapDrills: int = 245
swStandardSuperiorTappedHole: int = 246
swStandardSuperiorBottomingTappedHole: int = 247
swStandardSuperiorTappedHole2: int = 247
swStandardSuperiorBottomingTappedHole2: int = 249
swStandardSuperiorTaperedPipeTap: int = 248
swStandardDINHexSocketHead6912: int = 249
swStandardDINStraightPipeTappedHole: int = 250
swStandardDINConduitTappedHole: int = 351
swStandardDINEnsatTappedHoleforAL: int = 352
swStandardDINEnsatTappedHoleforCU: int = 353
swStandardDINEnsatTappedHoleforST: int = 354
swStandardGBDrillSizes: int = 355
swStandardGBScrewClearances: int = 356
swStandardGBTapDrills: int = 357
swStandardGBTappedHoleBottoming: int = 358
swStandardGBTappedHole: int = 359
swStandardGBTaperedPipeTap: int = 360
swStandardGBHexagonSocketHeadCapScrews: int = 361
swStandardGBHexagonLobularSocketCountersunkHeadScrews: int = 362
swStandardGBHexagonLobularSocketRaisedCountersunkHeadScrews: int = 363
swStandardGBHexagonLobularSocketHeadCapScrewsPropertyClass: int = 364
swStandardGBSlottedRaisedCountersunkHeadScrews: int = 365
swStandardGBSlottedCountersinkHeadWoodScrews: int = 366
swStandardGBSlottedRaisedCountersunkHeadWoodScrews: int = 367
swStandardGBCrossRecessedCountersunkHeadWoodScrews: int = 368
swStandardGBCrossRecessedRaisedCountersunkHeadWoodScrews: int = 369
swStandardGBSlottedCountersunkHeadTappingScrews: int = 370
swStandardGBSlottedRaisedCountersunkHeadTappingScrews: int = 371
swStandardGBCrossRecessedCountersunkHeadTappingScrews: int = 372
swStandardGBCrossRecessedRaisedCountersunkHeadTappingScrews: int = 373
swStandardGBSlottedCheeseHeadScrews: int = 374
swStandardGBHexagonLobularSocketHeadCapScrewsPropertyClass4: int = 375
swStandardGBHexagonHeadBoltsGB: int = 376
swStandardGBHexagonHeadBoltsFullThreadProductGradeC: int = 377
swStandardGBHexagonHeadBoltsFullThreadProductGradesAB: int = 378
swStandardGBHexagonHeadBoltsProductGradeC: int = 379
swStandardKSDrillSizes: int = 450
swStandardKSScrewClearances: int = 451
swStandardKSTapDrills: int = 452
swStandardKSTaperedPipeTap: int = 453
swStandardKSBottomingTappedHole: int = 454
swStandardKSTappedHole: int = 455
swStandardKSFlatCrossHeadScrew: int = 456
swStandardKSRaisedCrossHeadScrew: int = 457
swStandardKSSocketHeadCapScrew: int = 458
swStandardKSHexHeadBoltA: int = 459
swStandardKSHexHeadBoltB: int = 460
swStandardKSHexHeadBoltC: int = 461
swStandardKSCheeseSlottedHead: int = 462
swStandardISDrillSizes: int = 550
swStandardISScrewClearances: int = 551
swStandardISTapDrills: int = 552
swStandardISTaperedPipeTap: int = 553
swStandardISBottomingTappedHole: int = 554
swStandardISTappedHole: int = 555
swStandardISCrossRecessFlatHeadScrew: int = 556
swStandardISCrossRecessPanHeadScrew: int = 557
swStandardISCrossRecessRaisedHeadScrew: int = 558
swStandardISHexagonHeadBoltC: int = 559
swStandardISHexagonHeadScrewA: int = 560
swStandardISHexagonHeadScrewB: int = 561
swStandardISHexagonHeadScrewC: int = 562
swStandardISSlottedCheeseHeadScrew: int = 563
swStandardISSocketHeadCapScrew: int = 564
swStandardASDrillSizes: int = 650
swStandardASScrewClearances: int = 651
swStandardASTapDrills: int = 652
swStandardASTaperedPipeTap: int = 653
swStandardASBottomingTappedHole: int = 654
swStandardASTappedHole: int = 655
swStandardASCrossCountersunkHeadScrew: int = 657
swStandardASRaisedCrossCountersunkHeadScrew: int = 658
swStandardASPanCrossHeadScrew: int = 659
swStandardASPanSlottedHeadScrew: int = 660
swStandardASCheeseHeadScrew: int = 661
swStandardASMushroomHeadScrew: int = 662
swStandardASSocketHeadCapScrew: int = 663
swStandardASHexBoltGradesAB: int = 664
swStandardASUnifiedHexBolt: int = 665
swStandardASHexStructuralBolt: int = 666
swStandardASUnifiedHexScrew: int = 667
swStandardASHexScrewGradesAB: int = 668
swStandardASHexBoltGradeC: int = 669
swStandardASHexScrewGradeC: int = 670
swStandardDINHexSocketHeadFine912: int = 701
swStandardDINHexSocketHeadThin7984: int = 702
swStandardAnsiInchDowelHole: int = 703
swStandardAnsiMetricDowelHole: int = 704
swStandardASDowelHole: int = 705
swStandardBSIDowelHole: int = 706
swStandardDINDowelHole: int = 707
swStandardGBDowelHole: int = 708
swStandardISDowelHole: int = 709
swStandardISODowelHole: int = 710
swStandardJISDowelHole: int = 711
swStandardKSDowelHole: int = 712
swStandardPEMInch300SCNuts: int = 906
swStandardPEMInchAluminumSCNuts: int = 901
swStandardPEMInchNon_lockingNuts: int = 905
swStandardPEMInchSelf_clinchingNuts: int = 909
swStandardPEMInchSelf_lockingNuts: int = 910
swStandardPEMInchThinSheet: int = 912
swStandardPEMInchTRI_DENT: int = 913
swStandardPEMInchWeldNuts: int = 908
swStandardPEMInchBlindFasteners: int = 902
swStandardPEMInchFloating: int = 903
swStandardPEMInchMiniature: int = 904
swStandardPEMInchPEMHEXFasteners: int = 914
swStandardPEMInchPEMSERTFlushFasteners: int = 907
swStandardPEMInchSelf_lockingFasteners: int = 911
swStandardPEMInchBlindSO: int = 947
swStandardPEMInchConcealedStandoffs: int = 948
swStandardPEMInchKEYHOLEStandoffs: int = 949
swStandardPEMInchSNAP_TOPSBStandoffs: int = 950
swStandardPEMInchSNAP_TOPSCStandoffs: int = 951
swStandardPEMInchTHStandoffs: int = 952
swStandardPEMInchTSStandoffs: int = 953
swStandardPEMInchUStandoffs: int = 954
swStandardPEMInchConcealedStuds: int = 929
swStandardPEMInchFHDogPointStuds: int = 932
swStandardPEMInchFlushheadStuds: int = 931
swStandardPEMInchHigh_strengthStuds: int = 934
swStandardPEMInchHSDogPointStuds: int = 935
swStandardPEMInchLow_displacementStuds: int = 936
swStandardPEMInchNon_flushheadStuds: int = 937
swStandardPEMInchFlushheadPins: int = 930
swStandardPEMInchFlushPilotPins: int = 933
swStandardPEMMetric300SCNuts: int = 920
swStandardPEMMetricAluminumSCNuts: int = 915
swStandardPEMMetricNon_lockingNuts: int = 919
swStandardPEMMetricSelf_clinchingNuts: int = 923
swStandardPEMMetricSelf_lockingNuts: int = 924
swStandardPEMMetricThinSheet: int = 926
swStandardPEMMetricTRI_DENT: int = 927
swStandardPEMMetricWeldNuts: int = 922
swStandardPEMMetricBlindFasteners: int = 916
swStandardPEMMetricFloating: int = 917
swStandardPEMMetricMiniature: int = 918
swStandardPEMMetricPEMHEXFasteners: int = 928
swStandardPEMMetricPEMSERTFlushFasteners: int = 921
swStandardPEMMetricSelf_lockingFasteners: int = 925
swStandardPEMMetricBlindSO: int = 955
swStandardPEMMetricConcealedStandoffs: int = 956
swStandardPEMMetricKEYHOLEStandoffs: int = 957
swStandardPEMMetricSNAP_TOPSBStandoffs: int = 958
swStandardPEMMetricSNAP_TOPSCStandoffs: int = 959
swStandardPEMMetricTHStandoffs: int = 961
swStandardPEMMetricTSStandoffs: int = 960
swStandardPEMMetricUStandoffs: int = 962
swStandardPEMMetricConcealedStuds: int = 938
swStandardPEMMetricFHDogPointStuds: int = 941
swStandardPEMMetricFlushheadStuds: int = 940
swStandardPEMMetricHigh_strengthStuds: int = 943
swStandardPEMMetricHSDogPointStuds: int = 944
swStandardPEMMetricLow_displacementStuds: int = 945
swStandardPEMMetricNon_flushheadStuds: int = 946
swStandardPEMMetricFlushheadPins: int = 939
swStandardPEMMetricFlushPilotPins: int = 942

# swWzdHoleStandards_e (SwConst)
swStandardAnsiInch: int = 0
swStandardAnsiMetric: int = 1
swStandardBSI: int = 2
swStandardDME: int = 3
swStandardDIN: int = 4
swStandardHascoMetric: int = 5
swStandardHelicoilInch: int = 6
swStandardHelicoilMetric: int = 7
swStandardISO: int = 8
swStandardJIS: int = 9
swStandardPCS: int = 10
swStandardProgressive: int = 11
swStandardSuperior: int = 12
swStandardGB: int = 13
swStandardKS: int = 14
swStandardIS: int = 15
swStandardAS: int = 16
swStandardPEMInch: int = 17
swStandardPEMMetric: int = 18

# swWzdHoleThreadEndCondition_e (SwConst)
swEndThreadTypeBLIND: int = 0
swEndThreadTypeTHROUGH_ALL: int = 1
swEndThreadTypeTHROUGH_NEXT: int = 2

# swWzdHoleTypes_e (SwConst)
swSimple: int = 0
swTapered: int = 1
swCounterBored: int = 2
swCounterSunk: int = 3
swCounterDrilled: int = 4
swSimpleDrilled: int = 5
swTaperedDrilled: int = 6
swCounterBoredDrilled: int = 7
swCounterSunkDrilled: int = 8
swCounterDrilledDrilled: int = 9
swCounterBoreBlind: int = 10
swCounterBoreBlindCounterSinkMiddle: int = 11
swCounterBoreBlindCounterSinkTop: int = 12
swCounterBoreBlindCounterSinkTopmiddle: int = 13
swCounterBoreThru: int = 14
swCounterBoreThruCounterSinkBottom: int = 15
swCounterBoreThruCounterSinkMiddle: int = 16
swCounterBoreThruCounterSinkMiddleBottom: int = 17
swCounterBoreThruCounterSinkTop: int = 18
swCounterBoreThruCounterSinkTopBottom: int = 19
swCounterBoreThruCounterSinkTopMiddle: int = 20
swCounterBoreThruCounterSinkTopMiddleBottom: int = 21
swHoleBlind: int = 22
swHoleBlindCounterSinkTop: int = 23
swCounterSinkBlind: int = 24
swHoleThru: int = 25
swHoleThruCounterSinkBottom: int = 26
swHoleThruCounterSinkTop: int = 27
swHoleThruCounterSinkTopBottom: int = 28
swCounterSinkThru: int = 29
swCounterSinkThruCounterSinkBottom: int = 30
swTapBlind: int = 31
swTapBlindCounterSinkTop: int = 32
swTapThru: int = 33
swTapThruCounterSinkBottom: int = 34
swTapThruCounterSinkTop: int = 35
swTapThruCounterSinkTopBottom: int = 36
swPipeTapBlind: int = 37
swPipeTapBlindCounterSinkTop: int = 38
swPipeTapThru: int = 39
swPipeTapThruCounterSinkBottom: int = 40
swPipeTapThruCounterSinkTop: int = 41
swPipeTapThruCounterSinkTopBottom: int = 42
swCounterSinkBlindWithoutHeadClearance: int = 43
swCounterSinkThruWithoutHeadClearance: int = 44
swCounterSinkThruCounterSinkBottomWithoutHeadClearance: int = 45
swTapBlindCosmeticThread: int = 46
swTapBlindCosmeticThreadCounterSinkTop: int = 47
swTapThruCosmeticThread: int = 48
swTapThruCosmeticThreadCounterSinkTop: int = 49
swTapThruCosmeticThreadCounterSinkBottom: int = 50
swTapThruCosmeticThreadCounterSinkTopBottom: int = 51
swTapThruThreadThru: int = 52
swTapThruThreadThruCounterSinkTop: int = 53
swTapThruThreadThruCounterSinkBottom: int = 54
swTapThruThreadThruCountersinkTopBottom: int = 55
swTapBlindRemoveThread: int = 56
swCounterBoreSlotBlind: int = 57
swCounterBoreSlotBlindCounterSinkMiddle: int = 58
swCounterBoreSlotBlindCounterSinkTop: int = 59
swCounterBoreSlotBlindCounterSinkTopMiddle: int = 60
swCounterBoreSlotThru: int = 61
swCounterBoreSlotThruCounterSinkBottom: int = 62
swCounterBoreSlotThruCounterSinkMiddle: int = 63
swCounterBoreSlotThruCounterSinkMiddleBottom: int = 64
swCounterBoreSlotThruCounterSinkTop: int = 65
swCounterBoreSlotThruCounterSinkTopBottom: int = 66
swCounterBoreSlotThruCounterSinkTopMiddle: int = 67
swCounterBoreSlotThruCounterSinkTopMiddleBottom: int = 68
swSlotBlind: int = 69
swSlotBlindCounterSinkTop: int = 70
swCounterSinkSlotBlind: int = 71
swSlotThru: int = 72
swSlotThruCounterSinkBottom: int = 73
swSlotThruCounterSinkTop: int = 74
swSlotThruCounterSinkTopBottom: int = 75
swCounterSinkSlotThru: int = 76
swCounterSinkSlotThruCounterSinkBottom: int = 77
swCounterSinkSlotBlindWithoutHeadClearance: int = 78
swCounterSinkSlotThruWithoutHeadClearance: int = 79
swCounterSinkSlotThruCounterSinkBottomWithoutHeadClearance: int = 90

# swZeroQuantityDisplay_e (SwConst)
swZeroQuantityDashed: int = 1
swZeroQuantityZero: int = 2
swZeroQuantityBlank: int = 3

# swZonalSectionViewZones_e (SwConst)
swZonalSectionViewZones_swZonalSectionViewZone_1: int = 1
swZonalSectionViewZones_swZonalSectionViewZone_2: int = 2
swZonalSectionViewZones_swZonalSectionViewZone_3: int = 4
swZonalSectionViewZones_swZonalSectionViewZone_4: int = 8
swZonalSectionViewZones_swZonalSectionViewZone_5: int = 16
swZonalSectionViewZones_swZonalSectionViewZone_6: int = 32
swZonalSectionViewZones_swZonalSectionViewZone_7: int = 64
swZonalSectionViewZones_swZonalSectionViewZone_8: int = 128

# swZoneMargin_e (SwConst)
swZoneTopMargin: int = 0
swZoneBottomMargin: int = 1
swZoneRightMargin: int = 2
swZoneLeftMargin: int = 3

# swZoneSizeDistribution_e (SwConst)
swZoneSizeDistribution_50mmFromCenter: int = 0
swZoneSizeDistribution_EvenlySized: int = 1

# swZoomLevelOnOpenType_e (SwConst)
swZoomLevelOnOpenType_LastSave: int = 0
swZoomLevelOnOpenType_ToFit: int = 1
swZoomLevelOnOpenType_ToSheet: int = 2

# swcActivateBodyResult_e (SldCostingAPI)
swcActivateBodyResult_Success: int = 0
swcActivateBodyResult_GenericFailure: int = 1

# swcBodyStatus_e (SldCostingAPI)
swcBodyStatus_NotAnalysed: int = 0
swcBodyStatus_Analysed: int = 1
swcBodyStatus_Excluded: int = 2
swcBodyStatus_AssignedCustomCost: int = 3

# swcBodyType_e (SldCostingAPI)
swcBodyType_SheetMetal: int = 0
swcBodyType_Machined: int = 1
swcBodyType_Custom: int = 2
swcBodyType_Structural: int = 3
swcBodyType_Undefined: int = 4
swcBodyType_GeneralBody: int = 5

# swcCostFeatureType_e (SldCostingAPI)
swcMachinedBodiesFolderType: int = 0
swcSheetMetalBodiesFolderType: int = 1
swcSetupBodyFolderType: int = 2
swcStructuralBodiesFolderType: int = 3
swcCustomBodiesFolderType: int = 4
swcWeldingFolderType: int = 5
swcCustomOperationsFolderType: int = 6
swcNoCostAssignedFolderType: int = 7
swcMachinedBodyItemType: int = 8
swcSheetMetalBodyItemType: int = 9
swcCustomBodyItemType: int = 10
swcMultiBodySetupCostItem: int = 11
swcSheetMetalCutPathItemType: int = 12
swcSheetMetalBendsFolderType: int = 13
swcSheetMetalCustomOperationsFolderType: int = 14
swcSheetMetalCutPathesFolderType: int = 15
swcSheetMetalLibraryFeaturesFolderType: int = 16
swcSheetMetalLibraryNoCostAssignedFolderType: int = 17
swcSheetMetalSetupCostFolderType: int = 18
swcSheetMetalItemFeatureType: int = 19
swcSheetMetalItemSetupCost: int = 20
swcSheetMetalItemCustomOperation: int = 21
swcMachiningChamferFeatureItemType: int = 22
swcMachiningChamferOperationItemType: int = 23
swcMachiningFaceAdditionalOperationItem: int = 24
swcMachiningFaceFeatureItemType: int = 25
swcMachiningFaceOperationItemType: int = 26
swcMachiningMillFeatureItemType: int = 27
swcMachiningLocalSetupCostItemType: int = 28
swcMachiningMillAdditionalOperationItemType: int = 29
swcMachiningMillOperationItemType: int = 30
swcMachiningPatternedHoleFeatureItemType: int = 31
swcMachiningPatternedHoleSubFeatureItemType: int = 32
swcMachiningSetupCostFeatureItem: int = 33
swcMachiningSetupCostItemType: int = 34
swcMachiningSetupCostOperationItemType: int = 35
swcMachiningItemCustomOperation: int = 36
swcMachiningPlateCutpathItem: int = 37
swcMachiningHoleFeatureItem: int = 38
swcMachiningOperationHoleDrill: int = 39
swcMachiningOperationHoleCDrill: int = 40
swcMachiningOperationHoleTapping: int = 41
swcMachiningPlateCutpathFolderType: int = 42
swcMachiningCustomOperationFolderType: int = 43
swcMachiningHoleOperationsFolderType: int = 44
swcMachiningLibraryFeaturesFolderType: int = 45
swcMachiningMillOperationsFolderType: int = 46
swcMachiningTurnOperationsFolderType: int = 47
swcMachiningNCAFolderType: int = 48
swcMachiningSetupCostFolderType: int = 49
swcMachiningVolumeFeatureItemType: int = 50
swcMachiningVolumeOperationItemType: int = 51
swcMachiningVolumeAdditionalOperationItem: int = 52
swcMachiningLibraryFeatureType: int = 53
swcMachiningEndProfileFeatureItem: int = 54
swcMachiningGrooveFeatureItem: int = 55
swcNoCostAssignedBody: int = 56
swcMachiningFilletFeatureItem: int = 57
swcMachineSetupCostSubFolderType: int = 58
swcMachineOperationSetupCostSubFolderType: int = 59
swcMachineCustomSetupCostSubFolderType: int = 60
swcMachineSetupCostItemType: int = 61
swcMachiningItemBendFeatureType: int = 62
swcAdditiveFeatureType: int = 63
swcWeldFeatureItemType: int = 64
swcWeldOperationItemType: int = 65
swcEndCutFeaturesFolderType: int = 66
swcEndCutFeatureItemType: int = 67
swcStructuralBodyItemType: int = 68
swcGussetsFolderType: int = 69
swcEndcapFolderType: int = 70

# swcCostingType_e (SldCostingAPI)
swcCostingType_Common: int = 0
swcCostingType_SheetMetal: int = 1
swcCostingType_Machining: int = 2
swcCostingType_Structural: int = 3

# swcCustomStockCostInfoType_e (SldCostingAPI)
swcCustomStockCostType_Unknown: int = 0
swcCustomStockCostType_SavedCostingData: int = 1
swcCustomStockCostType_Volume: int = 2
swcCustomStockCostType_CustomCost: int = 3

# swcCustomStockImportType_e (SldCostingAPI)
swcCustomStockImportType_Unknown: int = 0
swcCustomStockImportType_Configuration: int = 1
swcCustomStockImportType_ReferencePart: int = 2

# swcDefaultMachiningTool_e (SldCostingAPI)
swcDefaultMachiningTool_FlatEndMill: int = 0
swcDefaultMachiningTool_BallEndMill: int = 1
swcDefaultMachiningTool_FaceMill: int = 2
swcDefaultMachiningTool_HSSDrill: int = 3
swcDefaultMachiningTool_CarbideDrill: int = 4
swcDefaultMachiningTool_ODTurning: int = 5
swcDefaultMachiningTool_IDTurning: int = 6

# swcFinishingOperationType_e (SldCostingAPI)
swcFinishingOperationType_Roughing: int = 0
swcFinishingOperationType_Semifinishing: int = 1
swcFinishingOperationType_Finishing: int = 2

# swcLengthUnit_e (SldCostingAPI)
swcLengthUnit_mm: int = 0
swcLengthUnit_inch: int = 1

# swcMarkUpType_e (SldCostingAPI)
swcMarkUpType_TotalCost: int = 0
swcMarkUpType_MaterialCost: int = 1
swcMarkUpType_None: int = 2

# swcMassUnit_e (SldCostingAPI)
swcMassUnit_kg: int = 0
swcMassUnit_lb: int = 1

# swcMethodType_e (SldCostingAPI)
swcMethodType_Sheetmetal: int = 0
swcMethodType_Machining: int = 1
swcMethodType_Structural: int = 2
swcMethodType_Plastic: int = 3
swcMethodType_Casting: int = 4
swcMethodType_3dPrinting: int = 5
swcMethodType_MachinedPlate: int = 6

# swcMoldCalculationMethod_e (SldCostingAPI)
swcMoldCalculationMethod_WallThickness: int = 0
swcMoldCalculationMethod_CycleTime: int = 1

# swcPlane_e (SldCostingAPI)
swcPlane_XY: int = 0
swcPlane_YZ: int = 1
swcPlane_XZ: int = 2

# swcRemovedMaterialProcessingType_e (SldCostingAPI)
swcProcessingType_Standard: int = 0
swcProcessingType_Volume: int = 1

# swcRunnerSystem_e (SldCostingAPI)
swcRunnerSystem_HotRunner: int = 0
swcRunnerSystem_ColdRunner: int = 1

# swcSheetMetalBlankSizeType_e (SldCostingAPI)
swcSheetMetalBlankSizeType_BoundingBox: int = 0
swcSheetMetalBlankSizeType_FlatPattern: int = 1
swcSheetMetalBlankSizeType_CustomSize: int = 2
swcSheetMetalBlankSizeType_CustomArea: int = 3

# swcSlotFeatureRecognitionType_e (SldCostingAPI)
swcSlotFeatureRecognitionType_Slot: int = 0
swcSlotFeatureRecognitionType_Volume: int = 1

# swcStockType_e (SldCostingAPI)
swcStockType_Unknown: int = 0
swcStockType_Block: int = 1
swcStockType_Plate: int = 2
swcStockType_Cylinder: int = 3
swcStockType_Custom: int = 4

# swcStructuralStockCostType_e (SldCostingAPI)
swcStructuralStockCostType_Unknown: int = 0
swcStructuralStockCostType_PerLength: int = 1
swcStructuralStockCostType_PerUnitLength: int = 2

# swcUnitSystem_e (SldCostingAPI)
swcUnitSystem_mm_kg: int = 0
swcUnitSystem_inch_lb: int = 1

# swcUpdateCostError_e (SldCostingAPI)
swcUpdateCostError_None: int = 0
swcUpdateCostError_TemplateUnavailable: int = 1
swcUpdateCostError_MaterialUnavailable: int = 2

# swcVolumeFeatureCalculationType_e (SldCostingAPI)
swcVolumeFeatureCalculationType_MachiningOperation: int = 0
swcVolumeFeatureCalculationType_CostPerVolume: int = 1

# swsAccelerationComponent_e (CosmosWorksLib)
swsAccelerationComponentAX: int = 0
swsAccelerationComponentAY: int = 1
swsAccelerationComponentAZ: int = 2
swsAccelerationComponentARES: int = 3
swsAccelerationComponentBX: int = 4
swsAccelerationComponentBY: int = 5
swsAccelerationComponentBZ: int = 6
swsAccelerationComponentANG: int = 7

# swsAccelerationUnit_e (CosmosWorksLib)
swsAccelerationUnit_MetersPerSquareSec: int = 0
swsAccelerationUnit_InchesPerSquareSec: int = 1
swsAccelerationUnit_CentimetersPerSquareSec: int = 2
swsAccelerationUnit_g: int = 3

# swsAddDefaultDropTestStudyPlotResultError_e (CosmosWorksLib)
swsDropTestResultNoError: int = 0
swsDropTestResultRangeError: int = 1
swsDropTestResultNodalStressRangeError: int = 2
swsDropTestResultElementalStressRangeError: int = 3
swsDropTestResultDisplacementRangeError: int = 4
swsDropTestResultElementalStrainRangeError: int = 5

# swsAddDefaultFatigueStudyPlotResultError_e (CosmosWorksLib)
swsFatigueResultNoError: int = 0
swsFatigueResultRangeError: int = 1

# swsAddDefaultFrequencyOrBucklingStudyPlotResultError_e (CosmosWorksLib)
swsFrequencyResultNoError: int = 0
swsFrequencyMaxModeShapeValueRangeError: int = 1
swsFrequencyResultDisplacementRangeError: int = 2

# swsAddDefaultNonLinearStudyPlotResultError_e (CosmosWorksLib)
swsNonLinearResultNoError: int = 0
swsNonLinearResultRangeError: int = 1
swsNonLinearResultNodalStressComponentRangeError: int = 2
swsNonLinearResultElementalStressComponentRangeError: int = 3
swsNonLinearResultDisplacementComponentRangeError: int = 4
swsNonLinearResultNodalStrainComponentRangeError: int = 5
swsNonLinearResultElementalStrainComponentRangeError: int = 6

# swsAddDefaultOptimizationDesignStudyPlotResultError_e (CosmosWorksLib)
swsOptimizationDesignResultNoError: int = 0
swsOptimizationDesignResultDesignValueRangeError: int = 1

# swsAddDefaultStaticStudyPlotResultError_e (CosmosWorksLib)
swsStaticResultNoErrror: int = 0
swsStaticResultTypeRangeError: int = 1
swsStaticResultElementalStressComponentRangeError: int = 2
swsStaticResultDisplacementComponentRangeError: int = 3
swsStaticResultNodalStrainRangeError: int = 4
swsStaticResultElementalStrainRangeError: int = 5
swsStaticResultNodalStressComponentRangeError: int = 6

# swsAddDefaultThermalStudyPlotResultError_e (CosmosWorksLib)
swsThermalResultNoError: int = 0
swsThermalResultRangeError: int = 1

# swsAnalysisStudyType_e (CosmosWorksLib)
swsAnalysisStudyTypeStatic: int = 0
swsAnalysisStudyTypeFrequency: int = 1
swsAnalysisStudyTypeBuckling: int = 2
swsAnalysisStudyTypeThermal: int = 3
swsAnalysisStudyTypeOptimization: int = 4
swsAnalysisStudyTypeNonlinear: int = 5
swsAnalysisStudyTypeDropTest: int = 6
swsAnalysisStudyTypeFatigue: int = 7
swsAnalysisStudyTypeDynamic: int = 8
swsAnalysisStudyTypePressureVessel: int = 9
swsAnalysisStudyTypeReserved1: int = 10
swsAnalysisStudyTypeReserved2: int = 11
swsAnalysisStudyTypeReserved3: int = 12
swsAnalysisStudyTypeTopology_Static: int = 13

# swsAngularAccelerationUnit_e (CosmosWorksLib)
swsAngularAccelerationUnit_RadiansPerSquareSec: int = 0
swsAngularAccelerationUnit_HertzPerSec: int = 1
swsAngularAccelerationUnit_RPMSquare: int = 2

# swsAngularVelocityUnit_e (CosmosWorksLib)
swsAngularVelocityUnit_RadiansPerSec: int = 0
swsAngularVelocityUnit_Hertz: int = 1
swsAngularVelocityUnit_RPM: int = 2

# swsBaseExcitationEndEditError_e (CosmosWorksLib)
swsBaseExcitationError_NoError: int = 0
swsBaseExcitationError_NotAvailableForThisStudy: int = 1
swsBaseExcitationError_InvalidExcitationType: int = 2
swsBaseExcitationError_ExcitationTypeNotAvailable: int = 3
swsBaseExcitationError_NoProperFixtures: int = 4
swsBaseExcitationError_InvalidFixtureNameOrEntity: int = 5
swsBaseExcitationError_ImproperUnits: int = 6
swsBaseExcitationError_SelectAtleastOneDirection: int = 7
swsBaseExcitationError_SelectOnlyOneDirection: int = 8
swsBaseExcitationError_SelectOnlyThirdDirection: int = 9
swsBaseExcitationError_SelectAtleastOneDirectionOfThatInRestraint: int = 10
swsBaseExcitationError_InvalidValue: int = 11

# swsBaseExcitationType_e (CosmosWorksLib)
swsBaseExcitationType_Displacement: int = 0
swsBaseExcitationType_Velocity: int = 1
swsBaseExcitationType_Acceleration: int = 2

# swsBeamBodyConnectionType_e (CosmosWorksLib)
swsBeamBodyConnectionRigid: int = 0
swsBeamBodyConnectionPin: int = 1
swsBeamBodyConnectionSlide: int = 2
swsBeamBodyConnectionManual: int = 3

# swsBeamBodyManualConnectionType_e (CosmosWorksLib)
swsBeamBodyManualConnectionHinge1stDirection: int = 0
swsBeamBodyManualConnectionHinge2ndDirection: int = 1
swsBeamBodyManualConnectionHingeAlongBeam: int = 2
swsBeamBodyManualConnectionSlide1stDireciton: int = 3
swsBeamBodyManualConnectionSlide2ndDirection: int = 4
swsBeamBodyManualConnectionSlideAlongBeam: int = 5

# swsBeamForceType_e (CosmosWorksLib)
swsBeamForceAxial: int = 0
swsBeamForceShearDirection1: int = 1
swsBeamForceShearDirection2: int = 2
swsBeamForceMomentDirection1: int = 3
swsBeamForceMomentDirection2: int = 4
swsBeamForceTorque: int = 5

# swsBeamNonUniformLoadDef_e (CosmosWorksLib)
swsTotalLoad: int = 0
swsCentralLoad: int = 1
swsTableDrivenLoad: int = 2

# swsBeamNonUniformLoadType_e (CosmosWorksLib)
swsTriangularLoad: int = 0
swsParabolicLoad: int = 1
swsEllipticalLoad: int = 2

# swsBeamStressComponent_e (CosmosWorksLib)
swsBeamStressComponentAxial: int = 0
swsBeamStressComponentBendingLocalDir1: int = 1
swsBeamStressComponentBendingLocalDir2: int = 2
swsBeamStressComponentWorstCase: int = 3

# swsBeamStressType_e (CosmosWorksLib)
swsBeamStressAxial: int = 0
swsBeamStressBendingDirection1: int = 1
swsBeamStressBendingDirection2: int = 2
swsBeamStressTorsional: int = 3
swsBeamStressWorstCase: int = 4

# swsBeamType_e (CosmosWorksLib)
swsBeamTypeBeam: int = 0
swsBeamTypeTruss: int = 1

# swsBearingConnectionType_e (CosmosWorksLib)
swsDistributedConnType: int = 0
swsRigidConnType: int = 1
swsSpringConnType: int = 2

# swsBearingConnectorErrors_e (CosmosWorksLib)
swsBearingConnectorErrCode_Successful: int = 0
swsBearingConnectorErrCode_NoActiveDoc: int = 1
swsBearingConnectorErrCode_NoActiveStudy: int = 2
swsBearingConnectorErrCode_SetOperationNotSupported: int = 3
swsBearingConnectorErrCode_InvalidSelectionForHousing: int = 4
swsBearingConnectorErrCode_InvalidSelectionForShaft: int = 5
swsBearingConnectorErrCode_SourceAndTargetSelectionsSwitched: int = 6
swsBearingConnectorErrCode_InvalidUnitType: int = 7
swsBearingConnectorErrCode_OutOfRangeLateralStiffness: int = 8
swsBearingConnectorErrCode_OutOfRangeAxialStiffness: int = 9
swsBearingConnectorErrCode_OutOfRangeTiltStiffness: int = 10
swsBearingConnectorErrCode_OutOfRangeShaftStabilizeStiffness: int = 11
swsBearingConnectorErrCode_InadequateEntitiesSelection: int = 12
swsBearingConnectorErrCode_MoreThanOneFaceSelectedForShaft: int = 13
swsBearingConnectorErrCode_MoreThanOneFaceOrEdgeSelectedForHousing: int = 14
swsBearingConnectorErrCode_FacesOrEdgesSelectedFromSingleComponent: int = 15
swsBearingConnectorErrCode_LenByDiamRatioGreaterThan2ForShaft: int = 16
swsBearingConnectorErrCode_InvalidConnectionType: int = 17

# swsBearingLoadDistributionType_e (CosmosWorksLib)
swsBearingLoadDistributionTypeSinusoidal: int = 0
swsBearingLoadDistributionTypeParabolic: int = 1

# swsBearingLoadEndEditError_e (CosmosWorksLib)
swsBearingLoadEndEditErrorSuccessful: int = 0
swsBearingLoadEndEditErrorCoordinateSystemCylindricalFaces: int = 1
swsBearingLoadEndEditErrorIncorrectOrNullEntity: int = 2
swsBearingLoadEndEditErrorEntityExists: int = 3
swsBearingLoadEndEditErrorSelectFace: int = 4
swsBearingLoadEndEditErrorNoEntityAtIndex: int = 5
swsBearingLoadEndEditErrorSpecifyValue: int = 6
swsBearingLoadEndEditErrorSelectFaceWithCylindricalSurface: int = 7
swsBearingLoadEndEditErrorHasMassElement: int = 8
swsBearingLoadEndEditErrorHasBeamBody: int = 9
swsBearingLoadEndEditErrorIndexExceedsNumberOfEntities: int = 10
swsBearingLoadEndEditErrorNoEntity: int = 11
swsBearingLoadEndEditErrorSelectOneForceDirection: int = 12
swsBearingLoadEndEditErrorSelectForceDirection: int = 13
swsBearingLoadEndEditErrorSetXDirection: int = 14
swsBearingLoadEndEditErrorSetYDirection: int = 15
swsBearingLoadEndEditErrorNullEntity: int = 16
swsBearingLoadEndEditErrorBodyExcludedFromAnalysis: int = 17

# swsBearingStiffnessShaftStabilizeType_e (CosmosWorksLib)
swsBearingStiffnessShaftStabilizeAuto: int = 0
swsBearingStiffnessShaftStabilizeUserDef: int = 1

# swsBearingStiffnessType_e (CosmosWorksLib)
swsBearingStiffnessRigid: int = 0
swsBearingStiffnessFlexible: int = 1

# swsBoltConnectorEndEditError_e (CosmosWorksLib)
swsBoltConnectorEndEditErrorSuccessful: int = 0
swsBoltConnectorEndEditErrorSelectFace: int = 1
swsBoltConnectorEndEditErrorSelectConicalSurface: int = 2
swsBoltConnectorEndEditErrorIncorrectHeadDiameter: int = 3
swsBoltConnectorEndEditErrorSelectEdge: int = 4
swsBoltConnectorEndEditErrorSelectCircularEdge: int = 5
swsBoltConnectorEndEditErrorSelectCylindricalThreadFace: int = 6
swsBoltConnectorEndEditErrorIncorrectShankDiameter: int = 7
swsBoltConnectorEndEditErrorSelectMass: int = 8
swsBoltConnectorEndEditErrorSelectConcentricEntities: int = 9
swsBoltConnectorEndEditErrorSpecifyYoungModulus: int = 10
swsBoltConnectorEndEditErrorSpecifyTemperatureCoefficient: int = 11
swsBoltConnectorEndEditErrorSpecifyPoissonsRatio: int = 12
swsBoltConnectorEndEditErrorDefineMaterial: int = 13
swsBoltConnectorEndEditErrorSpecifyPreloadValue: int = 14
swsBoltConnectorEndEditErrorSpecifyFrictionValue: int = 15
swsBoltConnectorEndEditErrorSelectPlanarFace: int = 16
swsBoltConnectorEndEditErrorSelectBoltHeadAndNut: int = 17
swsBoltConnectorEndEditErrorSelectFaceForHeadNutFaceForThread: int = 18
swsBoltConnectorEndEditErrorSelectConicalFaceAndBoltNut: int = 19
swsBoltConnectorEndEditErrorSelectConicalFaceAndFaceForThread: int = 20
swsBoltConnectorEndEditErrorSelectReferencePlane: int = 21
swsBoltConnectorEndEditErrorSelectFacesFromMultilayerBolt: int = 22
swsBoltConnectorEndEditErrorSelectCoaxialCylindricalSurfaces: int = 23
swsBoltConnectorEndEditErrorSelectConcentricCylindricalFaces: int = 24
swsBoltConnectorEndEditErrorBoltDiameterBiggerShankContactFaceDiameter: int = 25
swsBoltConnectorEndEditErrorSelectBoltNut: int = 26
swsBoltConnectorEndEditErrorEntityAlreadyExits: int = 27
swsBoltConnectorEndEditErrorNoEntity: int = 28
swsBoltConnectorEndEditErrorIncorrectNutDiameter: int = 29
swsBoltConnectorEndEditErrorDocumentIsPart: int = 30
swsBoltConnectorEndEditErrorSelectNutOrHead: int = 31
swsBoltConnectorEndEditErrorSelectEdgesOnShells: int = 32
swsBoltConnectorEndEditErrorNoObjectAtIndex: int = 33
swsBoltConnectorEndEditErrorEntitySelectionBoxesEmpty: int = 34
swsBoltConnectorEndEditErrorSelectOneEntity: int = 35
swsBoltConnectorEndEditErrorTooManyEntities: int = 36
swsBoltConnectorEndEditErrorNoShearEffectSelected: int = 37
swsBoltConnectorEndEditErrorNoMultiBoltSelected: int = 38
swsBoltConnectorEndEditErrorBodyHasMassElement: int = 39
swsBoltConnectorEndEditErrorBodyExcludedFromAnalysis: int = 40
swsBoltConnectorEndEditErrorNullEntity: int = 41
swsBoltConnectorEndEditErrorBodyHasBeamElement: int = 42
swsBoltConnectorEndEditErrorInvalidForAnalysis: int = 43
swsBoltConnectorEndEditErrorInvalidConnectionType: int = 44

# swsBoltConnectorError_e (CosmosWorksLib)
swsBoltConnectorErrorSuccessful: int = 0
swsBoltConnectorErrorInvalidMesh: int = 1
swsBoltConnectorErrorNonLinearStudyAndPartDocument: int = 2
swsBoltConnectorErrorInvalidStudy: int = 3
swsBoltConnectorErrorSelectEntity: int = 4
swsBoltConnectorErrorSelectFaceWithConicalSurface: int = 5
swsBoltConnectorErrorSelectEdgeWithCircularLine: int = 6
swsBoltConnectorErrorSelectFaceWithCylindricalSurface: int = 7
swsBoltConnectorErrorSelectCylindricalThreadFace: int = 8
swsBoltConnectorErrorSelectConcentricEntities: int = 9
swsBoltConnectorErrorSelectDatumPlane: int = 10
swsBoltConnectorErrorSelectEdge: int = 11
swsBoltConnectorErrorSelectFace: int = 12
swsBoltConnectorErrorSameEntityHeadAndNut: int = 13
swsBoltConnectorErrorSelectAssemblyDocument: int = 14
swsBoltConnectorErrorNoObjectForNutOrHead: int = 15
swsBoltConnectorErrorSelectNutOrHead: int = 16
swsBoltConnectorErrorArrayEmpty: int = 17
swsBoltConnectorErrorSelectCircularEdgeOnShells: int = 18
swsBoltConnectorErrorBoltDiameterTooLarge: int = 19
swsBoltConnectorErrorBodyExcludedFromAnalysis: int = 20
swsBoltConnectorErrorEdgeFromSameFace: int = 21

# swsBoltMaterialSource_e (CosmosWorksLib)
swsBoltMaterialSourceSolidWorks: int = 0
swsBoltMaterialSourceCustomDefined: int = 1
swsBoltMaterialSourceLibraryFiles: int = 2

# swsBoltMaterialType_e (CosmosWorksLib)
swsBoltMaterialTypeCustom: int = 0
swsBoltMaterialTypeLibrary: int = 1

# swsBoltType_e (CosmosWorksLib)
swsBoltTypeStandardOrCounterboreNut: int = 0
swBoltTypeCountersinkWithNut: int = 1
swsBoltTypeStandardOrCounterboreScrew: int = 2
swsBoltTypeCountersinkScrew: int = 3
swsBoltTypeFoundationBolt: int = 4

# swsCRSectionType_e (CosmosWorksLib)
swsSolidCircular: int = 0
swsHollowCircular: int = 1
swsSolidRectangular: int = 2
swsHollowRectangular: int = 3

# swsCableEndEditErrors_e (CosmosWorksLib)
swsCableErrCode_Successful: int = 0
swsCableErrCode_NoActiveDoc: int = 1
swsCableErrCode_NoActiveStudy: int = 2
swsCableErrCode_SetOperationNotSupported: int = 3
swsCableErrCode_InvalidSelection: int = 4
swsCableErrCode_InvalidNonCoAxialSelection: int = 5
swsCableErrCode_InvalidCoAxialSelection: int = 6
swsCableErrCode_InvalidNonConcentricSelection: int = 7
swsCableErrCode_OffsetOptionNotAvailable: int = 9
swsCableErrCode_ZeroDiameterValue: int = 14
swsCableErrCode_InvalidUnitType: int = 15
swsCableErrCode_InvalidMaterialSourceType: int = 16
swsCableErrCode_SetMaterialPropertyNA: int = 17
swsCableErrCode_SetLibraryMaterialNA: int = 18
swsCableErrCode_InvalidLibraryMaterialDetails: int = 19
swsCableErrCode_OutOfRangeYoungsModulus: int = 20
swsCableErrCode_OutOfRangeShearModulus: int = 21
swsCableErrCode_OutOfRangeThermalCoefficient: int = 22
swsCableErrCode_OutOfRangeDensity: int = 23
swsCableErrCode_InadequateEntitiesSelection: int = 24
swsCableErrCode_OutOfRangeAxialStrengthValue: int = 25
swsCableErrCode_OutOfRangePreLoadForceValue: int = 26

# swsCentrifugalForceEndEditError_e (CosmosWorksLib)
swsCentrifugalForceEndEditErrorSuccessful: int = 0
wsCentrifugalForceEndEditErrorSpecifyAxisEdgeOrCylindricalFace: int = 1

# swsCentrifugalForceError_e (CosmosWorksLib)
swsCentrifugalForceErrorSuccessful: int = 0
swsCentrifugalForceErrorSelectAxisEdgeOrCylindricalFace: int = 1
swsCentrifugalForceErrorFaceNotCylindrical: int = 2
swsCentrifugalForceErrorEdgeNotLinear: int = 3
swsCentrifugalForceErrorAlreadyDefined: int = 4
swsCentrifugalForceErrorInvalidStudyType: int = 5

# swsColorChartNumberFormatOptionValue_e (CosmosWorksLib)
swsColorChartNumberFormatScientific: int = 0
swsColorChartNumberFormatFloating: int = 1
swsColorChartNumberFormatGeneral: int = 2

# swsColorChartOptionLegendTypeValue_e (CosmosWorksLib)
swsColorChartOptionLegendDefault: int = 0
swsColorChartOptionLegendRainbow: int = 1
swsColorChartOptionLegendGrayScale: int = 2
swsColorChartOptionLegendUserDefined: int = 3
swsColorChartOptionLegendUnsupported: int = 4
swsColorChartOptionLegendColorBlindFriendly: int = 5

# swsColorChartPositionValue_e (CosmosWorksLib)
swsColorChartPredefinedPosition: int = 0
swsColorChartUserDefined: int = 1

# swsColorChartWidthOptionValue_e (CosmosWorksLib)
swsColorChartWidthWide: int = 0
swsColorChartWidthNormal: int = 1
swsColorChartWidthThin: int = 2

# swsColorNumberFormatUseDiffNumberFormatOptionValue_e (CosmosWorksLib)
swsColorChartNumberFormatUseDiffNoFormatFloating: int = 0
swsColorChartNumberFormatUseDiffNoFormatGeneral: int = 1

# swsCompositeShellOptionsError_e (CosmosWorksLib)
swsCompositeShellOptionsErrorNoError: int = 0
swsCompositeShellOptionsErrorPlyOutRange: int = 1
swsCompositeShellOptionsErrorSandwich3Plies: int = 2
swsCompositeShellOptionsErrorIncompatibleToMappingType: int = 3
swsCompositeShellOptionsErrorUnitOutRange: int = 4
swsCompositeShellOptionsErrorWrongEntity: int = 5
swsCompositeShellOptionsErrorMaterialUndefined: int = 6
swsCompositeShellOptionsErrorNotCompositeShell: int = 7
swsCompositeShellOptionsErrorWrongInput: int = 8
swsCompositeShellOptionsErrorThicknessInvalid: int = 9
swsCompositeShellOptionsErrorMaterialInvalid: int = 10
swsCompositeShellOptionsErrorFailed: int = 11

# swsCompositeShellOptionsMappingType_e (CosmosWorksLib)
swsCompositeShellOptionsSurfaceMapping: int = 0
swsCompositeShellOptionsPlanarMapping: int = 1

# swsConnectAnalysisDatabaseError_e (CosmosWorksLib)
swsConnectAnalysisDatabaseErrorSuccess: int = 0
swsConnectAnalysisDatabaseErrorFailed: int = 1
swsConnectAnalysisDatabaseErrorInvalidPath: int = 2
swsConnectAnalysisDatabaseErrorInvalidResults: int = 3

# swsConnectorConnectionType_e (CosmosWorksLib)
swsConnectorConnectionType_Rigid: int = 0
swsConnectorConnectionType_Distributed: int = 1

# swsContactComponentEndEditError_e (CosmosWorksLib)
swsContactComponentEndEditErrorSuccessful: int = 0
swsContactComponentEndEditErrorContactComponentCannotBeCreated: int = 1
swsContactComponentEndEditErrorInvalidContactType: int = 2
swsContactComponentEndEditErrorSelectComponentOrBody: int = 3
swsContactComponentEndEditErrorIncorrectCoefficientOfFriction: int = 4
swsContactComponentEndEditErrorSelectSolidBodyOrComponent: int = 5
swsContactComponentEndEditErrorTooManyBodiesOrComponents: int = 6
swsContactComponentEndEditErrorCannotSpecifyFreeContact: int = 7
swsContactComponentEndEditErrorBodiesNotTouchingBodies: int = 8

# swsContactSetEndEditError_e (CosmosWorksLib)
swsContactSetEndEditErrorSuccessful: int = 0
swsContactSetEndEditErrorNoEntityAtIndex: int = 1
swsContactSetEndEditErrorEntityAlreadySpecified: int = 2
swsContactSetEndEditErrorInvalidContactSetType: int = 3
swsContactSetEndEditErrorInvalidOption: int = 4
swsContactSetEndEditErrorSpecifyFacesEdgesOrVerticesForSource: int = 5
swsContactSetEndEditErrorSpecifyOneTargetPlaneForVirtualWall: int = 6
swsContactSetEndEditErrorOnlyFacesAllowedForTarget: int = 7
swsContactSetEndEditErrorStiffnessCannotBeNegative: int = 8
swsContactSetEndEditErrorStiffnessMustBePositive: int = 9
swsContactSetEndEditErrorIncorrectCoefficientFriction: int = 10
swsContactSetEndEditErrorVerticesAndEdgesForBondingAndSurfaceContacts: int = 11
swsContactSetEndEditErrorThermalResistanceMustBePositive: int = 12
swsContactSetEndEditErrorContactSetsMustBeUnique: int = 13
swsContactSetEndEditErrorNodeToNodeContactAndSourceTargetFaces: int = 14
swsContactSetEndEditErrorBondTouchingFacesInDropTestStudies: int = 15
swsContactSetEndEditErrorShrinkFitAndnterferingSourceTargetBodies: int = 16

# swsContactSetError_e (CosmosWorksLib)
swsContactSetErrorSuccess: int = 0
swsContactSetErrorInvalidArray: int = 1
swsContactSetErrorNoEntities: int = 2
swsContactSetErrorInvalidType: int = 3
swsContactSetErrorSpecifyFacesEdgesOrVertices: int = 4
swsContactSetErrorSelectOneTargetPlane: int = 5
swsContactSetErrorSelectOnlyFaces: int = 6
swsContactSetErrorFaceForSourceAndTarget: int = 7
swsContactSetErrorVerticesEdgesForBondingSurfaceContacts: int = 8
swsContactSetErrorSourceTargetFacesMustTouch: int = 9
swsContactSetErrorBondedContactForTouchingFaces: int = 10
swsContactSetErrorShrinkFitNeedsIntereference: int = 11
swsContactSetErrorCannotCreateContactPair: int = 12

# swsContactSetTypeStaticNonLinear_e (CosmosWorksLib)
swsContactSetTypeStaticNonLinearNoPenetration: int = 0
swsContactSetTypeStaticNonLinearBonded: int = 1
swsContactSetTypeStaticNonLinearShrinkFit: int = 2
swsContactSetTypeStaticNonLinearFree: int = 3
swsContactSetTypeStaticNonLinearVirtualWall: int = 4

# swsContactSetTypeThermal_e (CosmosWorksLib)
swsContactSetTypeThermalResistance: int = 0
swsContactSetTypeThermalBonded: int = 1
swsContactSetTypeThermalInsulated: int = 2

# swsContactSuppressUnsuppressError_e (CosmosWorksLib)
swsContactSuppressUnsuppressErrorSuccessful: int = 0
swsContactSuppressUnsuppressErrorContactNotFound: int = 1
swsContactSuppressUnsuppressErrorInvalidName: int = 2

# swsContactType_e (CosmosWorksLib)
swsContactTypeBonded: int = 0
swsContactTypeFreeOrInsulated: int = 1
swsContactTypeAllowPenetration: int = 1
swsContactTypeStaticNoPenetration: int = 2

# swsConvectionEndEditError_e (CosmosWorksLib)
swsConvectionEndEditErrorSuccessful: int = 0
swsConvectionEndEditErrorNoEntityAtIndex: int = 1
swsConvectionEndEditErrorEntityAlreadyAdded: int = 2
swsConvectionEndEditErrorNoEntitySelected: int = 3
swsConvectionEndEditErrorSelectFace: int = 4
swsConvectionEndEditErrorSelectFaceOrEdge: int = 5

# swsConvectionError_e (CosmosWorksLib)
swsConvectionErrorSuccessful: int = 0
swsConvectionErrorFacesAndShellEdgesAllowed: int = 1
swsConvectionErrorSelectFacesOrShellEdge: int = 2
swsConvectionErrorInvalidStudyType: int = 3
swsConvectionErrorInvalidArray: int = 4
swsConvectionErrorEmptyArray: int = 5

# swsCoordinateType_e (CosmosWorksLib)
swsCoordinateTypeCartesian: int = 1
swsCoordinateTypeSpherical: int = 2
swsCoordinateTypeCylindrical: int = 3

# swsCopyItemsError_e (CosmosWorksLib)
swsCopyItem_Success: int = 0
swsCopyItem_CopyFailure: int = 1
swsCopyItem_DifferentJointVersion: int = 2
swsCopyItem_InstanceAlreadyDefined: int = 3
swsCopyItem_SourceTargetStudyPairInvalid: int = 4
swsCopyItem_SourceItemNotFound: int = 5
swsCopyItem_TargetStudyNotFound: int = 6
swsCopyItem_SourceStudyNotActive: int = 7
swsCopyItem_InvalidArray: int = 8
swsCopyItem_UnknownError: int = 9

# swsCosmosExportOption_e (CosmosWorksLib)
swsExportFEMOnly: int = 1
swsExportGeometryOnly: int = 2

# swsCreateAnalysisDatabaseError_e (CosmosWorksLib)
swsCreateAnalysisDBSuccessful: int = 0
swsCreateAnalysisDBUseHighQualityMesh: int = 1
swsCreateAnalysisDBDefineRigidVirtualWallContact: int = 2
swsCreateAnalysisDBDefineInitialTemperature: int = 3
swsCreateAnalysisDBMultipleLoadsUseSameTimeCurve: int = 4
swsCreateAnalysisDBSetUpDropTestStudy: int = 5
swsCreateAnalysisDBNeedOneOrMoreStaticStudies: int = 6
swsCreateAnalysisDBNoFatigueEvent: int = 7
swsCreateAnalysisDBTimeDependentOrAmplitideOnlyLoads: int = 8
swsCreateAnalysisDBNoSNCurve: int = 9
swsCreateAnalysisDBMeshNotIdentical: int = 11
swsCreateAnalysisDBNoValidShell: int = 12
swsCreateAnalysisDBEXMaterialPropertyNotDefined: int = 13
swsCreateAnalysisDBEXValue: int = 14
swsCreateAnalysisDBPoissonsRatio: int = 15
swsCreateAnalysisDBThermalConductivityNotDefined: int = 16
swsCreateAnalysisDBRemoveOrChangeCreep: int = 17
swsCreateAnalysisDBMaterialNotDefinedForShells: int = 18
swsCreateAnalysisDBMaterialNotDefined: int = 19
swsCreateAnalysisDBMaterialNotDefinedForComponents: int = 20
swsCreateAnalysisDBNoSolidBody: int = 21
swsCreateAnalysisDBAuthorizationFailed: int = 22
swsCreateAnalysisDBMeshFailed: int = 23
swsCreateAnalysisDBFailed: int = 24

# swsCreateDeformedBodyAdvancedOption_e (CosmosWorksLib)
swsCreateDeformedBodyAdvanced_OutputBodyOnly: int = 1
swsCreateDeformedBodyAdvanced_OutputTessellation: int = 2
swsCreateDeformedBodyAdvanced_OutputSurfaces: int = 4
swsCreateDeformedBodyAdvanced_OutputMesh: int = 8

# swsCreateDeformedBodyError_e (CosmosWorksLib)
swsCreateDeformedBody_CorruptData: int = 1
swsCreateDeformedBody_UnfitFace: int = 2
swsCreateDeformedBody_FailToSew: int = 3
swsCreateDeformedBody_DisjointBodies: int = 4
swsCreateDeformedBody_FailedToSubtractBody: int = 5
swsCreateDeformedBody_IncorrectParameters: int = 6
swsCreateDeformedBody_Failed: int = 7
swsCreateDeformedBody_IncorrectStepNumber: int = 8
swsCreateDeformedBody_NoActiveStudy: int = 9
swsCreateDeformedBody_NonSupportedStudy: int = 10
swsCreateDeformedBody_InvalidPath: int = 11

# swsCreateDeformedBodyFailedSewOption_e (CosmosWorksLib)
swsCreateDeformedBodyFailedSewAsDefault: int = 1
swsCreateDeformedBodyFailedSewAsTessellation: int = 2
swsCreateDeformedBodyFailedSewAsSurfaces: int = 3
swsCreateDeformedBodyFailedSewCancel: int = 4

# swsCreateDeformedBodyOption_e (CosmosWorksLib)
swsCreateDeformedBodyAsPart: int = 1
swsCreateDeformedBodyAsConfiguration: int = 2

# swsCyclicRestraintError_e (CosmosWorksLib)
swsCyclicRestraintErrorSuccessful: int = 0
swsCyclicRestraintErrorInvalidStudyType: int = 1
swsCyclicRestraintErrorNotApplicableForBeams: int = 2
swsCyclicRestraintErrorNoFirstFace: int = 3
swsCyclicRestraintErrorNoSecondFace: int = 4
swsCyclicRestraintErrorNoAxis: int = 5
swsCyclicRestraintErrorUnSuccessful: int = 6

# swsDampingType_e (CosmosWorksLib)
swsDampingType_Modal: int = 0
swsDampingType_Rayleigh: int = 1

# swsDefaultStaticResultTypes_e (CosmosWorksLib)
swsStaticResultNodalStress: int = 0
swsStaticResultElementalStress: int = 1
swsStaticResultDisplacement: int = 2
swsStaticResultNodalStrain: int = 3
swsStaticResultElementalStrain: int = 4
swsStaticResultFactorOfSafety: int = 5
swsStaticResultBoltPinCheck: int = 6

# swsDeformType_e (CosmosWorksLib)
swsAutomatic: int = 0
swsTrueScale: int = 1
swsUserDefined: int = 2

# swsDeleteStudyPlotsResultTypes_e (CosmosWorksLib)
swsDeleteStudyPlotsNoError: int = 0
swsDeleteStudyPlotsError: int = 1

# swsDisplacementComponent_e (CosmosWorksLib)
swsDisplacementComponentUX: int = 0
swsDisplacementComponentUY: int = 1
swsDisplacementComponentUZ: int = 2
swsDisplacementComponentURES: int = 3
swsDisplacementComponentRFX: int = 4
swsDisplacementComponentRFY: int = 5
swsDisplacementComponentRFZ: int = 6
swsDisplacementComponentRFRES: int = 7
swsDisplacementComponentRX: int = 8
swsDisplacementComponentRY: int = 9
swsDisplacementComponentRZ: int = 10
swsDisplacementComponentRMX: int = 11
swsDisplacementComponentRMY: int = 12
swsDisplacementComponentRMZ: int = 13
swsDisplacementComponentRMRES: int = 14

# swsDisplayOption_e (CosmosWorksLib)
swsShowSolidAndShells: int = 0
swsShowBeam: int = 1

# swsDistributedMassError_e (CosmosWorksLib)
swsDistributedMassError_NoError: int = 0
swsDistributedMassError_NotAvailable: int = 1
swsDistributedMassError_ImproperEntities: int = 2
swsDistributedMassError_SelectOnlyFaces: int = 3
swsDistributedMassError_InvalidUnits: int = 4
swsDistributedMassError_InvalidMass: int = 5

# swsDistributedSimulationError_e (CosmosWorksLib)
swsDistributedSimulation_NoError: int = 0
swsDistributedSimulation_NetSimulationNotSupport: int = 1
swsDistributedSimulation_NetComputerNotAvailable: int = 2
swsDistributedSimulation_EmptyNetComputerNames: int = 3
swsDistributedSimulation_UnaccessNetComputerNames: int = 4
swsDistributedSimulation_NetComputerNameWrongType: int = 5
swsDistributedSimulation_NoStudySupportNetSimulation: int = 6
swsDistributedSimulation_UnknownError: int = 7

# swsDropHeightType_e (CosmosWorksLib)
swsDropHeightType_FromCentroid: int = 0
swsDropHeightType_FromLowestPoint: int = 1

# swsDropTargetOrientationType_e (CosmosWorksLib)
swsDropTargetOrientationType_NormalToGravity: int = 0
swsDropTargetOrientationType_ParallelToRefPlane: int = 1

# swsDropTargetStiffnessType_e (CosmosWorksLib)
swsDropTargetStiffnessType_RigidTarget: int = 0
swsDropTargetStiffnessType_FlexibleTarget: int = 1

# swsDropTestSetUpError_e (CosmosWorksLib)
swsDropTestSetUpError_NoError: int = 0
swsDropTestSetUpError_AvailableOnlyForDropTestStudy: int = 1
swsDropTestSetUpError_SetUpAlreadyAdded: int = 2
swsDropTestSetUpError_GravityEntityIsNULL: int = 3
swsDropTestSetUpError_GravityEntityShouldBeEdgeFaceOrPlane: int = 4
swsDropTestSetUpError_ShouldBeStraightEdgeOrPlaneFace: int = 5
swsDropTestSetUpError_SetupNotExists: int = 6

# swsDropTestStudyResultType_e (CosmosWorksLib)
swsDropTestResultNodalStress: int = 0
swsDropTestResultElementalStress: int = 1
swsDropTestResultDisplacement: int = 2
swsDropTestResultElementalStrain: int = 3

# swsDropType_e (CosmosWorksLib)
swsDropType_DropHeight: int = 0
swsDropType_VelocityAtImpact: int = 1

# swsDuplicateStudyError_e (CosmosWorksLib)
swsDuplicateStudyErrorNoError: int = 0
swsDuplicateStudyErrorFailed: int = 1

# swsDynamicAnalysisSubType_e (CosmosWorksLib)
swsDynamicAnalysisSubTypeTransient: int = 0
swsDynamicAnalysisSubTypeHarmonic: int = 1
swsDynamicAnalysisSubTypeRandom: int = 2
swsDynamicAnalysisSubTypeResponse: int = 3

# swsDynamicExtraFrequenciesError_e (CosmosWorksLib)
swsDynamicExtraFrequenciesError_NoError: int = 0
swsDynamicExtraFrequenciesError_NotAvailable: int = 1
swsDynamicExtraFrequenciesError_NotAvailableForSubType: int = 2
swsDynamicExtraFrequenciesError_DynamicParamEmpty: int = 3
swsDynamicExtraFrequenciesError_OutOfRange: int = 4
swsDynamicExtraFrequenciesError_InvalidInput: int = 5

# swsDynamicInitialConditionError_e (CosmosWorksLib)
swsDynamicInitialConditionError_NoError: int = 0
swsDynamicInitialConditionError_NotAvailable: int = 1
swsDynamicInitialConditionError_InvalidEntityArray: int = 2
swsDynamicInitialConditionError_SelectOnlyJoints: int = 3
swsDynamicInitialConditionError_SelectOnlyBeams: int = 4
swsDynamicInitialConditionError_NoFacesOnBeamsAllowed: int = 5
swsDynamicInitialConditionError_SelectOnlyFaceBodyOrComps: int = 6
swsDynamicInitialConditionError_InvalidRefGeom: int = 7
swsDynamicInitialConditionError_RefGeomAlreadySelected: int = 8
swsDynamicInitialConditionError_OnlyEdgePlaneOrFaceForReference: int = 9
swsDynamicInitialConditionError_OnlyFlatFaceOrStraightEdge: int = 10
swsDynamicInitialConditionError_InvalidType: int = 11
swsDynamicInitialConditionError_CheckAtleastOneComp: int = 12
swsDynamicInitialConditionError_AllValuesZero: int = 13
swsDynamicInitialConditionError_CheckOnlyThirdComp: int = 14

# swsDynamicInitialConditionType_e (CosmosWorksLib)
swsDynamicInitialConditionType_Displacement: int = 0
swsDynamicInitialConditionType_Velocity: int = 1
swsDynamicInitialConditionType_Acceleration: int = 2

# swsEdgeWeldConnectorSafetyFactorLiftOption_e (CosmosWorksLib)
swsEdgeWeldConnectorSafetyFactorLiftOption_USAutomotiveLifts: int = 0
swsEdgeWeldConnectorSafetyFactorLiftOption_UnderTheHookLifting: int = 1

# swsEdgeWeldConnectorTypes_e (CosmosWorksLib)
swsEdgeWeldConnectorFilletDoubleSided: int = 0
swsEdgeWeldConnectorFilletSingleSided: int = 1
swsEdgeWeldConnectorGrooveDoubleSided: int = 2
swsEdgeWeldConnectorGrooveSingleSided: int = 3

# swsEdgeWeldCreationErrorCode_e (CosmosWorksLib)
swsEdgeWeldCreationError_NoError: int = 0
swsEdgeWeldCreationError_InvalidModelDoc: int = 1
swsEdgeWeldCreationError_InvalidOrNullFace: int = 2
swsEdgeWeldCreationError_InvalidWeldStyle: int = 3
swsEdgeWeldCreationError_NoEdgeSelection: int = 4
swsEdgeWeldCreationError_WrongEdgeSelection: int = 5

# swsEdgeWeldSolverCode_e (CosmosWorksLib)
swsEdgeWeldSolverCodeAWS: int = 0
swsEdgeWeldSolverCodeEURO: int = 1

# swsElasticConnectorEndEditError_e (CosmosWorksLib)
swsElasticConnectorEndEditErrorSuccessful: int = 0
swsElasticConnectorEndEditErrorNoEntityAtIndex: int = 1
swsElasticConnectorEndEditErrorEntityAlreadyAdded: int = 2
swsElasticConnectorEndEditErrorSelectFace: int = 3
swsElasticConnectorEndEditErrorSelectPlanarFace: int = 4
swsElasticConnectorEndEditErrorSelectNonNegativeValueForNormalOrShearStiffness: int = 5
swsElasticConnectorEndEditErrorSelectNonZeroValueForNormalOrShearStiffness: int = 6
swsElasticConnectorEndEditErrorSelectEntity: int = 7
swsElasticConnectorEndEditErrorHasBeamBody: int = 8
swsElasticConnectorEndEditErrorHasMassElement: int = 9
swsElasticConnectorEndEditErrorBodyExcludedFromAnalysis: int = 10
swsElasticConnectorEndEditErrorNullEntity: int = 11

# swsElasticConnectorError_e (CosmosWorksLib)
swsElasticConnectorErrorSuccessful: int = 0
swsElasticConnectorErrorInvalidMesh: int = 1
swsElasticConnectorErrorNonlinearStudyAndPartDocument: int = 2
swsElasticConnectorErrorInvalidStudy: int = 3
swsElasticConnectorErrorInvalidArray: int = 4
swsElasticConnectorErrorSelectFace: int = 5
swsElasticConnectorErrorSelectPlanarFace: int = 6
swsElasticConnectorErrorNoEntityNoObject: int = 7
swsElasticConnectorErrorNullOrEmptyArray: int = 8
swsElasticConnectorErrorFaceHasRemoteMassOrBeamBody: int = 9
swsElasticConnectorErrorBodyExcludedFromAnalysis: int = 10

# swsElectrodeMaterialTypes_e (CosmosWorksLib)
swsElectrodeMaterialE60: int = 0
swsElectrodeMaterialE70: int = 1
swsElectrodeMaterialE80: int = 2
swsElectrodeMaterialE90: int = 3
swsElectrodeMaterialE100: int = 4
swsElectrodeMaterialCustomSteel: int = 5
swsElectrodeMaterial1100: int = 6
swsElectrodeMaterial4043: int = 7
swsElectrodeMaterial5183: int = 8
swsElectrodeMaterial5356: int = 9
swsElectrodeMaterial5554: int = 10
swsElectrodeMaterial5556: int = 11
swsElectrodeMaterial5654: int = 12
swsElectrodeMaterialCustomAl: int = 13

# swsEnvelopePlotType_e (CosmosWorksLib)
swsEnvelopePlotType_Maximum: int = 0
swsEnvelopePlotType_Minimum: int = 1
swsEnvelopePlotType_AbsoluteMaximum: int = 2

# swsEstimatedWeldSizeUnits_e (CosmosWorksLib)
swsEstimatedWeldSizeUnits_mm: int = 0
swsEstimatedWeldSizeUnits_cm: int = 1
swsEstimatedWeldSizeUnits_m: int = 2
swsEstimatedWeldSizeUnits_in: int = 3
swsEstimatedWeldSizeUnits_ft: int = 4
swsEstimatedWeldSizeUnits_ft_in: int = 5
swsEstimatedWeldSizeUnits_am: int = 6
swsEstimatedWeldSizeUnits_nm: int = 7
swsEstimatedWeldSizeUnits_micron: int = 8
swsEstimatedWeldSizeUnits_mil: int = 9
swsEstimatedWeldSizeUnits_microIn: int = 10

# swsExportSmoothedMeshError_e (CosmosWorksLib)
swsExportSmoothedMesh_Succeeded: int = 0
swsExportSmoothedMesh_IncorrectParameters: int = 1
swsExportSmoothedMesh_Failed: int = 2
swsExportSmoothedMesh_NoActiveStudy: int = 3
swsExportSmoothedMesh_NonSupportedStudy: int = 4
swsExportSmoothedMesh_InvalidPath: int = 5
swsExportSmoothedMesh_PlotDataUnavailable: int = 6
swsExportSmoothedMesh_ConfigurationNameAlreadyExist: int = 7
swsExportSmoothedMesh_CorruptedInputData: int = 8
swsExportSmoothedMesh_PlotDoesNotExist: int = 9

# swsExportSmoothedMeshOption_e (CosmosWorksLib)
swsSaveSmoothedMeshIntoCurrentActiveConfiguration: int = 0
swsSaveSmoothedMeshIntoNewConfiguration: int = 1
swsSaveSmoothedMeshIntoNewPart: int = 2

# swsFOS_CompositeCriterion_e (CosmosWorksLib)
swsFOSCompositeCriterion_Tsai_Hill: int = 0
swsFOSCompositeCriterion_Tsai_Wu: int = 1
swsFOSCompositeCriterion_Max_Normal_Stress: int = 2
swsFOSCompositeCriterion_Automatic: int = 3

# swsFOS_DistributionOpt_e (CosmosWorksLib)
swsFOS_DistributionOpt_Distribution: int = 1
swsFOS_DistributionOpt_AreaBelowFOS: int = 2

# swsFOS_ErrorCode_e (CosmosWorksLib)
swsFOS_ErrorCode_NoError: int = 0
swsFOS_ErrorCode_NullPostApp: int = 1
swsFOS_ErrorCode_PlyNumExceeded: int = 2
swsFOS_ErrorCode_NoSolidBodiesSel: int = 3
swsFOS_ErrorCode_InvalidSelEntityArr: int = 4
swsFOS_ErrorCode_NoPersistID: int = 5
swsFOS_ErrorCode_InvalidSolidMgr: int = 6
swsFOS_ErrorCode_InvalidSel: int = 7
swsFOS_ErrorCode_FailureFrmGetPlotData: int = 8

# swsFOS_NonCompositeCriterion_e (CosmosWorksLib)
swsFOSNonCompositeCriterion_VonMisesHencky: int = 0
swsFOSNonCompositeCriterion_Tresca: int = 1
swsFOSNonCompositeCriterion_MohrCoulomb: int = 2
swsFOSNonCompositeCriterion_Coulomb: int = 3
swsFOSNonCompositeCriterion_Automatic: int = 4

# swsFOS_NormalShellFaceOption_e (CosmosWorksLib)
swsFOS_NormalShellFaceOption_Top: int = 1
swsFOS_NormalShellFaceOption_Bottom: int = 2
swsFOS_NormalShellFaceOption_Min: int = 3
swsFOS_NormalShellFaceOption_Max: int = 4

# swsFOS_ShellFaceOption_e (CosmosWorksLib)
swsFOS_ShellFaceOption_TopFace: int = 1
swsFOS_ShellFaceOption_BottomFace: int = 2
swsFOS_ShellFaceOption_MinAmongTopAndBottomFace: int = 3
swsFOS_ShellFaceOption_MaxAmongTopAndBottomFace: int = 4

# swsFactorOfSafetyStressLimitOption_e (CosmosWorksLib)
swsFactorOfSafetyStressLimitOption_YieldStrength: int = 0
swsFactorOfSafetyStressLimitOption_UltimateStrength: int = 1
swsFactorOfSafetyStressLimitOption_UserDefined: int = 2

# swsFatigueAlternatingStressOption_e (CosmosWorksLib)
swsFatigueAlternatingStressOption_StressIntensity: int = 0
swsFatigueAlternatingStressOption_EquivalentStress: int = 1
swsFatigueAlternatingStressOption_MaxAbsPrincipal: int = 2

# swsFatigueCalculationsOption_e (CosmosWorksLib)
swsFatigueCalculationsOption_WholeModel: int = 0
swsFatigueCalculationsOption_SurfaceOnly: int = 1

# swsFatigueCalculations_e (CosmosWorksLib)
swsFatigueCalculations_WholeModel: int = 0
swsFatigueCalculations_SurfaceOnly: int = 1

# swsFatigueComponent_e (CosmosWorksLib)
swsFatigueComponent_Life: int = 0
swsFatigueComponent_Damage: int = 1
swsFatigueComponent_LoadFactor: int = 2
swsFatigueComponent_BiaxialityIndicator: int = 3

# swsFatigueEventEndEditError_e (CosmosWorksLib)
swsFatigueEventError_NoError: int = 0
swsFatigueEventError_ImproperStudy: int = 1
swsFatigueEventError_ImproperEvent: int = 2
swsFatigueEventError_ImproperStudyNames: int = 3
swsFatigueEventError_LoadHistoryCurveTypeImproper: int = 4
swsFatigueEventError_XCurveDataImproper: int = 5
swsFatigueEventError_YCurveDataImproper: int = 6
swsFatigueEventError_XAndYPointsNotSameInNumber: int = 7
swsFatigueEventError_NoOfPointsShouldBeMoreThan3: int = 8
swsFatigueEventError_XPointsShouldBeInIncreasingOrder: int = 9
swsFatigueEventError_ImproperNoOfCycles: int = 10
swsFatigueEventError_InvalidLoadingtype: int = 11
swsFatigueEventError_CannotApplyLoadingRatio: int = 12
swsFatigueEventError_CannotApplyRepeats: int = 13
swsFatigueEventError_InvalidRepeats: int = 14
swsFatigueEventError_CannotApplyStartTime: int = 15
swsFatigueEventError_InvalidStartTime: int = 16
swsFatigueEventError_StudyNamesScalesAndStepsDifferentInNumber: int = 17
swsFatigueEventError_ImproperVarNamesOrVarScalesOrVarSteps: int = 18
swsFatigueEventError_NumberOfStudiesAssociationShouldbeAtleast1: int = 19
swsFatigueEventError_NumberOfStudiesAssociationShouldbeAtleast2: int = 20
swsFatigueEventError_AssociatedStudyShouldBeStaticNonlinearOrDynamicModalTimeHistory: int = 21

# swsFatigueEventInteraction_e (CosmosWorksLib)
swsFatigueEventInteraction_Random: int = 0
swsFatigueEventInteraction_NoInteraction: int = 1

# swsFatigueLoadHistoryCurveType_e (CosmosWorksLib)
swsFatigueLoadHistoryCurveType_AmplitudeOnly: int = 0
swsFatigueLoadHistoryCurveType_SamplingRateAndAmplitude: int = 1
swsFatigueLoadHistoryCurveType_TimeAndAmplitude: int = 2

# swsFatigueLoadingType_e (CosmosWorksLib)
swsFatigueLoadingType_FullyReversed: int = 0
swsFatigueLoadingType_ZeroBased: int = 1
swsFatigueLoadingType_LoadingRatio: int = 2
swsFatigueLoadingType_NonProportional: int = 3

# swsFatigueMeanStressCorrectionType_e (CosmosWorksLib)
swsFatigueMeanStressCorrectionType_None: int = 0
swsFatigueMeanStressCorrectionType_Goodman: int = 1
swsFatigueMeanStressCorrectionType_Gerber: int = 2
swsFatigueMeanStressCorrectionType_Soderberg: int = 3

# swsFatiguePlotType_e (CosmosWorksLib)
swsFatiguePlotType_Life: int = 0
swsFatiguePlotType_Damage: int = 1
swsFatiguePlotType_LoadFactor: int = 2
swsFatiguePlotType_BiaxialityIndicator: int = 3

# swsFatigueRandomVibrationComputationalMethod_e (CosmosWorksLib)
swsFatigue_NarrowBand: int = 0
swsFatigue_Steinberg: int = 1
swsFatigue_Wirsching: int = 2

# swsFatigueStudyResultType_e (CosmosWorksLib)
swsFatigueStudy_LifePlot: int = 0
swsFatigueStudy_DamagePlot: int = 1
swsFatigueStudy_LoadFactor: int = 2
swsFatigueStudy_BiAxialityIndicatorPlot: int = 3

# swsFatigueStudySubOption_e (CosmosWorksLib)
swsFatigueConstantAmplitude: int = 0
swsFatigueVariableAmplitude: int = 1
swsFatigueHarmonic: int = 2
swsFatigueRandomVibration: int = 3

# swsFlipOffsetDir_e (CosmosWorksLib)
swsNegativeDir: int = 0
swsPositiveDir: int = 1

# swsForceEndEditError_e (CosmosWorksLib)
swsForceEndEditErrorSuccessful: int = 0
swsForceEndEditErrorNoEntityAtIndex: int = 1
swsForceEndEditErrorEntityAlreadyExists: int = 2
swsForceEndEditErrorNoEntitiesSelected: int = 3
swsForceEndEditErrorSelectFaceEdgeOrVertex: int = 4
swsForceEndEditErrorReferenceGeometryEntityNotSelected: int = 5
swsForceEndEditErrorSelectFaceEdgePlaneOrAxisForReferenceGeometry: int = 6
swsForceEndEditErrorSelectFace: int = 7
swsForceEndEditErrorSelectCoordinateSystem: int = 8
swsForceEndEditErrorVariableForceCannotBeAppliedToVerticesOrEdges: int = 9
swsForceEndEditErrorSelectReferenceAxisOrCylindricalFaceForTorque: int = 10
swsForceEndEditErrorMagnitudeForceMustBeLargerZero: int = 11
swsForceEndEditErrorVariableForceCannotBeAppliedToVertices: int = 12

# swsForceError_e (CosmosWorksLib)
swsForceErrorSuccessful: int = 0
swsForceErrorSelectFacesEdgesVerticesOrPoints: int = 1
swsForceErrorSelectFaceEdgePlaneOrAxis: int = 2
swsForceErrorApplyNormalForceToFacesAndShellEdges: int = 3
swsForceErrorSelectReferenceAxisOrCylindricalFace: int = 4
swsForceErrorInvalidStudyType: int = 5
swsForceErrorInvalidArray: int = 6
swsForceErrorInvalidForceType: int = 7
swsForceErrorNoEntities: int = 8
swsForceErrorCannotApplyNonuniformForce: int = 9
swsForceErrorCannotApplyForce: int = 10
swsForceErrorCannotApplyNonuniformLoadOnMultipleBeam: int = 18
swsForceErrorCannotApplyZeroLoading: int = 19
swsForceErrorInvalidSelectionType: int = 20
swsForceErrorNonUniformBeamLoadInvalidTableData: int = 21
swsForceErrorNonUniformBeamLoadInvalidTableDistData: int = 22

# swsForceType_e (CosmosWorksLib)
swsForceTypeForceOrMoment: int = 0
swsForceTypeNormal: int = 1
swsForceTypeTorque: int = 2

# swsForceUnit_e (CosmosWorksLib)
swsForceUnitNOrNm: int = 0
swsForceUnitlbOrlbin: int = 1
swsForceUnitkgfOrkgfcm: int = 2

# swsFosPlotErrorCode_e (CosmosWorksLib)
swsFos_NoError: int = 0
swsFos_NoView: int = 1
swsFos_NullPostApp: int = 2
swsFos_NoDatabase: int = 3
swsFos_NoPostFile: int = 4
swsFos_APIExists: int = 5
swsFos_InvalidComponent: int = 6
swsFos_InvalidResults: int = 7
swsFos_NoMaterialFound: int = 8
swsFos_ComponentsHidden: int = 9
swsFos_AllMaterialFailed: int = 10
swsFos_InvalidShellOption: int = 11
swsFos_InvalidSelEntityArr: int = 12
swsFos_NoPersistID: int = 13
swsFos_InvalidSolidMgr: int = 14
swsFos_InvalidSel: int = 15
swsFos_FailureFrmGetPlotData: int = 16

# swsFrequencyBucklingResultDisplacementComponentTypes_e (CosmosWorksLib)
swsFrequencyBucklingDisplacement_UX: int = 0
swsFrequencyBucklingDisplacement_UY: int = 1
swsFrequencyBucklingDisplacement_UZ: int = 2
swsFrequencyBucklingDisplacement_URES: int = 3

# swsFrequencyCapOption_e (CosmosWorksLib)
swsFrequencyCapAutomatic: int = 0
swsFrequencyCapUserDefined: int = 1

# swsFrequencyStudyOption_e (CosmosWorksLib)
swsFrequencyStudyOptionNumberFrequencies: int = 0
swsFrequencyStudyOptionUseUpperBoundFrequency: int = 1

# swsFrequencyUnit_e (CosmosWorksLib)
swsFrequencyUnit_RadiansPerSec: int = 0
swsFrequencyUnit_CyclesPerSec: int = 1

# swsGapType_e (CosmosWorksLib)
swsGapTypeAlwaysIgnoreClearance: int = 0
swsGapTypeIgnoreIfSmallerThanSpecifiedClearance: int = 1

# swsGaussIntegrationOrder_e (CosmosWorksLib)
swsGaussIntegrationOrder_2Pt: int = 0
swsGaussIntegrationOrder_3Pt: int = 1

# swsGeneralSpringError_e (CosmosWorksLib)
swsGeneralSpringErrorSuccessful: int = 0
swsGeneralSpringErrorInvalidMesh: int = 1
swsGeneralSpringErrorInvalidStudy: int = 2
swsGeneralSpringErrorSelectFace: int = 3
swsGeneralSpringErrorSelectCoordSys: int = 4
swsGeneralSpringErrorSelectTwoFaces: int = 5
swsGeneralSpringErrorSourceTargetEntitiesSame: int = 6
swsGeneralSpringErrorNumberFacesLessThanTwo: int = 7
swsGeneralSpringErrorNoObjectForSourceOrTarget: int = 8
swsGeneralSpringErrorSelectionsOnSameComponent: int = 9
swsGeneralSpringErrorHasRemoteMass: int = 10
swsGeneralSpringErrorBodyExcludedFromAnalysis: int = 11
swsGeneralSpringErrorFaceDispNull: int = 12
swsGeneralSpringErrorFaceOnBeam: int = 13
swsGeneralSpringErrorNegativeStiffness: int = 14
swsGeneralSpringErrorNegativePreloadForce: int = 15
swsGeneralSpringErrorStiffnessAllZero: int = 16
swsGeneralSpringErrorFeatureNotReady: int = 17
swsGeneralSpringErrorFeatureNotSupported: int = 18
swsGeneralSpringErrorFeatureNotLicensed: int = 19

# swsGenerateReportError_e (CosmosWorksLib)
swsGenerateReportErrorNoError: int = 0
swsGenerateReportErrorWrongPath: int = 1
swsGenerateReportErrorWrongConfiguration: int = 2
swsGenerateReportErrorInvalidModelDoc: int = 3
swsGenerateReportErrorInactiveStudy: int = 4
swsGenerateReportErrorFailed: int = 5

# swsGeoStarExportUnit_e (CosmosWorksLib)
swsGeoStarExportUnit_mm: int = 0
swsGeoStarExportUnit_cm: int = 1
swsGeoStarExportUnit_m: int = 2
swsGeoStarExportUnit_in: int = 3
swsGeoStarExportUnit_ft: int = 4

# swsGravityEndEditError_e (CosmosWorksLib)
swsGravityEndEditErrorSuccessful: int = 0
swsGravityEndEditErrorSpecifyReferencePlaneFaceOrEdge: int = 1
swsGravityEndEditErrorValuesCannotBeZeros: int = 2

# swsGravityError_e (CosmosWorksLib)
swsGravityErrorSuccessful: int = 0
swsGravityErrorSelectFaceEdgeOrPlane: int = 1
swsGravityErrorFaceNotPlanar: int = 2
swsGravityErrorEdgeNotStraight: int = 3
swsGravityErrorGravityAlreadyDefined: int = 4
swsGravityErrorInvalidStudy: int = 5

# swsHeatFluxEndEditError_e (CosmosWorksLib)
swsHeatFluxEndEditErrorSuccessful: int = 0
swsHeatFluxEndEditErrorNoEntityAtIndex: int = 1
swsHeatFluxEndEditErrorEntityAlreadyExists: int = 2
swsHeatFluxEndEditErrorNoEntities: int = 3
swsHeatFluxEndEditErrorSelectFace: int = 4
swsHeatFluxEndEditErrorSelectFacesOrShellEdge: int = 5
swsHeatFluxEndEditErrorSelectrVertexForSensorLocation: int = 6
swsHeatFluxEndEditErrorLowerboundTemperatureHigherThanUpperbound: int = 7
swsHeatFluxEndEditErrorThermostatForTransientStudiesOnly: int = 8

# swsHeatFluxError_e (CosmosWorksLib)
swsHeatFluxErrorSuccessful: int = 0
swsHeatFluxErrorNoFaces: int = 1
swsHeatFluxErrorNoFacesOrShellEdges: int = 2
swsHeatFluxErrorInvalidStudy: int = 3
swsHeatFluxErrorInvalidArray: int = 4
swsHeatFluxErrorNoEntities: int = 5

# swsHeatPowerEndEditError_e (CosmosWorksLib)
swsHeatPowerEndEditErrorSuccessful: int = 0
swsHeatPowerEndEditErrorNoEntityAtIndex: int = 1
swsHeatPowerEndEditErrorEntityAlreadyExists: int = 2
swsHeatPowerEndEditErrorNoEntitiesSelected: int = 3
swsHeatPowerEndEditErrorSelectVerticesEdgesFacesComponentsOrBodies: int = 4
swsHeatPowerEndEditErrorSelectFaceEdgeOrVertex: int = 5
swsHeatPowerEndEditErrorSelectVertexForThermostatLocation: int = 6
swsHeatPowerEndEditErrorLowerboundTemperatureHigherThanUpperbound: int = 7
swsHeatPowerEndEditErrorNotValidForSteadyStateAnalysis: int = 8
swsHeatPowerEndEditErrorVertexCannotBeUsedForSensorLocation: int = 9

# swsHeatPowerError_e (CosmosWorksLib)
swsHeatPowerErrorSuccessful: int = 0
swsHeatPowerErrorSelectFaceEdgeVertexComponentOrBody: int = 1
swsHeatPowerErrorSelectFacesEdgesOrVertices: int = 2
swsHeatPowerErrorInvalidStudy: int = 3
swsHeatPowerErrorInvalidArray: int = 4
swsHeatPowerErrorNoEntities: int = 5

# swsImportStudyFeaturesErrorCode_e (CosmosWorksLib)
swsImportStudyFeaturesError_NoError: int = 0
swsImportStudyFeaturesError_ComponentNotFound: int = 1
swsImportStudyFeaturesError_StudyToImportNotFoundOrInvalid: int = 2
swsImportStudyFeaturesError_ConfigurationMismatch: int = 3
swsImportStudyFeaturesError_Unknown: int = 4
swsImportStudyFeaturesError_NotAssembly: int = 5
swsImportStudyFeaturesError_StudyNotActive: int = 6
swsImportStudyFeaturesError_NoPrePlotView: int = 7

# swsImportStudyFeaturesFilterType_e (CosmosWorksLib)
swsImportStudyFeaturesFilterType_All: int = 0
swsImportStudyFeaturesFilterType_AllBodyTypesMaterials: int = 1
swsImportStudyFeaturesFilterType_AllConnectorsContacts: int = 2
swsImportStudyFeaturesFilterType_AllFixtures: int = 4
swsImportStudyFeaturesFilterType_AllExternalLoads: int = 8
swsImportStudyFeaturesFilterType_AllMeshControls: int = 16

# swsIncompatibleBondingOption_e (CosmosWorksLib)
swsIncompatibleBondingOption_Automatic: int = 0
swsIncompatibleBondingOption_Simplified: int = 1
swsIncompatibleBondingOption_MoreAccurate: int = 2

# swsInterpolationType_e (CosmosWorksLib)
swsInterpolationType_Logarithmic: int = 0
swsInterpolationType_Linear: int = 1

# swsIsoClippingErrorCode_e (CosmosWorksLib)
swsIsoClippingNoError: int = 0
swsIsoClippingCosworksViewNotPresent: int = 1
swsIsoClippingIsoPlanesError: int = 2
swsIsoClippingPlotNotFound: int = 3
swsIsoClippingPostDataNotExist: int = 4
swsIsoClippingIsoValueError: int = 5
swsIsoClippingIsoVariantValueError: int = 6
swsIsoClippingIsoInvalidVariantError: int = 7
swsIsoClippingNotAvailable: int = 8

# swsJointType_e (CosmosWorksLib)
swsRigid: int = 0
swsPivot: int = 1
swsSpherical: int = 2

# swsLinearUnit_e (CosmosWorksLib)
swsLinearUnitMillimeters: int = 0
swsLinearUnitCentimeters: int = 1
swsLinearUnitMeters: int = 2
swsLinearUnitInches: int = 3
swsLinearUnitFeet: int = 4
swsLinearUnitFeetInches: int = 5
swsLinearUnitAngstrom: int = 6
swsLinearUnitNanoMeter: int = 7
swsLinearUnitMicron: int = 8
swsLinearUnitMil: int = 9
swsLinearUnitMicronIn: int = 10

# swsLinkConnectorEndEditError_e (CosmosWorksLib)
swsLinkConnectorEndEditErrorSuccessful: int = 0
swsLinkConnectorEndEditErrorEntityAlreadyExists: int = 1
swsLinkConnectorEndEditErrorSelectDatumPointOrVertices: int = 2
swsLinkConnectorEndEditErrorSelectEntity: int = 3
swsLinkConnectorEndEditErrorNullEntity: int = 4
swsLinkConnectorEndEditErrorHasBeamBody: int = 5
swsLinkConnectorEndEditErrorHasMassElement: int = 6
swsLinkConnectorEndEditErrorBodyExcludedFromAnalysis: int = 7

# swsLinkConnectorError_e (CosmosWorksLib)
swsLinkConnectorErrorSuccessful: int = 0
swsLinkConnectorErrorInvalidMesh: int = 1
swsLinkConnectorErrorNonlinearStudyPartDocument: int = 2
swsLinkConnectorErrorInvalidStudy: int = 3
swsLinkConnectorErrorSelectAssemblyDocument: int = 4
swsLinkConnectorErrorEmptyEntity: int = 5
swsLinkConnectorErrorSelectVertexOrDatumPoint: int = 6
swsLinkConnectorErrorHasRemoteMassOrBeamBody: int = 7
swsLinkConnectorErrorBodyExcludedFromAnalysis: int = 8

# swsLinkageRodEndEditErrors_e (CosmosWorksLib)
swsLinkageRodErrCode_Successful: int = 0
swsLinkageRodErrCode_NoActiveDoc: int = 1
swsLinkageRodErrCode_NoActiveStudy: int = 2
swsLinkageRodErrCode_SetOperationNotSupported: int = 3
swsLinkageRodErrCode_InvalidSelection: int = 4
swsLinkageRodErrCode_InvalidNonCoAxialSelection: int = 5
swsLinkageRodErrCode_InvalidCoAxialSelection: int = 6
swsLinkageRodErrCode_InvalidNonConcentricSelection: int = 7
swsLinkageRodErrCode_InvalidJointTypeSel: int = 8
swsLinkageRodErrCode_OffsetOptionNotAvailable: int = 9
swsLinkageRodErrCode_InvalidRodSectionType: int = 10
swsLinkageRodErrCode_InvalidArray: int = 11
swsLinkageRodErrCode_InvalidParamsCount: int = 12
swsLinkageRodErrCode_InvalidParamDataType: int = 13
swsLinkageRodErrCode_ZeroParamValue: int = 14
swsLinkageRodErrCode_InvalidUnitType: int = 15
swsLinkageRodErrCode_InvalidMaterialSourceType: int = 16
swsLinkageRodErrCode_SetMaterialPropertyNA: int = 17
swsLinkageRodErrCode_SetLibraryMaterialNA: int = 18
swsLinkageRodErrCode_InvalidLibraryMaterialDetails: int = 19
swsLinkageRodErrCode_OutOfRangeYoungsModulus: int = 20
swsLinkageRodErrCode_OutOfRangePoissonRatio: int = 21
swsLinkageRodErrCode_OutOfRangeThermalCoefficient: int = 22
swsLinkageRodErrCode_InvalidMass: int = 23
swsLinkageRodErrCode_InadequateEntitiesSelection: int = 24

# swsLoadCaseManagerError_e (CosmosWorksLib)
swsLoadCaseManager_NoError: int = 0
swsLoadCaseManager_LoadCaseManagerNotShown: int = 1
swsLoadCaseManager_InvalidLoadName: int = 2
swsLoadCaseManager_InvalidLoadCaseName: int = 3
swsLoadCaseManager_InvalidCombinationName: int = 4
swsLoadCaseManager_LoadIsSuppressed: int = 5
swsLoadCaseManager_LoadCaseIsSuppressed: int = 6
swsLoadCaseManager_CombinationIsSuppressed: int = 7
swsLoadCaseManager_InvalidDataInput: int = 8
swsLoadCaseManager_InvalidEquation: int = 9
swsLoadCaseManager_NoLoadCasesToRun: int = 10
swsLoadCaseManager_CannotRunStudy: int = 11
swsLoadCaseManager_CannotCreateMesh: int = 12
swsLoadCaseManager_UnknownError: int = 13

# swsLoadsAndRestraintsError_e (CosmosWorksLib)
swsLoadsAndRestraintsErrorSuccessful: int = 0
swsLoadsAndRestraintsErrorNotFoundAtIndex: int = 1
swsLoadsAndRestraintsError_NotFoundWithGivenName: int = 2
swsLoadsAndRestraintsError_InvalidComponentsCount: int = 3
swsLoadsAndRestraintsError_InvalidSelection: int = 4
swsLoadsAndRestraintsError_InvalidSelectionsMixedTogether: int = 5
swsLoadsAndRestraintsError_InvalidOrNullFace: int = 6
swsLoadsAndRestraintsError_InvalidLicense: int = 7
swsLoadsAndRestraintsError_NoLBCDefined: int = 8

# swsLoadsAndRestraintsManagerBearingLoadError_e (CosmosWorksLib)
swsLoadsAndRestraintsManagerBearingLoadErrorSuccessful: int = 0
swsLoadsAndRestraintsManagerBearingLoadErrorInvalidArray: int = 1
swsLoadsAndRestraintsManagerBearingLoadErrorNoObjectForFace: int = 2
swsLoadsAndRestraintsManagerBearingLoadErrorCoordinateSystemEmpty: int = 3
swsLoadsAndRestraintsManagerBearingLoadErrorSelectFace: int = 4
swsLoadsAndRestraintsManagerBearingLoadErrorSelectCoordinateSystem: int = 5
swsLoadsAndRestraintsManagerBearingLoadErrorCoordinateSystemAndCylindricalFaces: int = 6
swsLoadsAndRestraintsManagerBearingLoadErrorInvalidMesh: int = 7
swsLoadsAndRestraintsManagerBearingLoadErrorInvalidStudy: int = 8
swsLoadsAndRestraintsManagerBearingLoadErrorBodyExcludedFromAnalysis: int = 9

# swsLoadsAndRestraintsType_e (CosmosWorksLib)
swsLoadsAndRestraintsTypePressure: int = 1
swsLoadsAndRestraintsTypeRestraint: int = 2
swsLoadsAndRestraintsTypeForce: int = 3
swsLoadsAndRestraintsTypeGravity: int = 4
swsLoadsAndRestraintsTypeCentrifugal: int = 5
swsLoadsAndRestraintsTypeTemperature: int = 6
swsLoadsAndRestraintsTypeConvection: int = 7
swsLoadsAndRestraintsTypeHeatPower: int = 8
swsLoadsAndRestraintsTypeHeatFlux: int = 9
swsLoadsAndRestraintsTypeRadiation: int = 10
swsLoadsAndRestraintsTypeRemoteLoad: int = 11
swsLoadsAndRestraintsTypeConnectors: int = 12
swsLoadsAndRestraintsTypeBearingLoads: int = 13
swsLoadsAndRestraintsTypeVelocity: int = 14
swsLoadsAndRestraintsTypeBaseExcitation: int = 15
swsLoadsAndRestraintsTypeMeshControl: int = 21
swsLoadsAndRestraintsTypeRemoteMass: int = 31

# swsMassUnits_e (CosmosWorksLib)
swsMassUnit_Milligram: int = 0
swsMassUnit_Gram: int = 1
swsMassUnit_Kilogram: int = 2
swsMassUnit_Pound: int = 3

# swsMaterialDataCurveError_e (CosmosWorksLib)
swsMaterialDataCurveErrorSuccessful: int = 0
swsMaterialDataCurveErrorCannotBeDefined: int = 1
swsMaterialDataCurveErrorIndexValues: int = 2
swsMaterialDataCurveErrorIndexForMooneyRivlinAndOgeden: int = 3
swsMaterialDataCurveErrorIndexForViscoElastic: int = 4
swsMaterialDataCurveErrorInvalidArray: int = 5
swsMaterialDataCurveErrorTemperatures: int = 6
swsMaterialDataCurveErrorNeedDataPoints: int = 7

# swsMaterialErrorWarning_e (CosmosWorksLib)
swsMaterialErrorWarningSuccessful: int = 0
swsMaterialErrorWarningInvalidLinearElasticAnisotropicMaterialModel: int = 1
swsMaterialErrorWarningInvalidMaterialModel: int = 2
swsMaterialErrorWarningFatigueSNCurvesCycles: int = 3
swsMaterialErrorWarningUniqueStressRatioForEachSNCurve: int = 4
swsMaterialErrorWarningTooManyPointsSNCurve: int = 5
swsMaterialErrorWarningDefineProperty: int = 6
swsMaterialErrorWarningMaterialPropertyValue: int = 7
swsMaterialErrorWarningEXNotDefined: int = 8
swsMaterialErrorWarningEXValue: int = 9
swsMaterialErrorWarningDefineCurveForEx: int = 10
swsMaterialErrorWarningMaterialTemperatureCurveForNitinol: int = 11
swsMaterialErrorWarningNUXYValue: int = 12
swsMaterialErrorWarningDensityNotDefined: int = 13
swsMaterialErrorWarningrKXNotDefined: int = 14
swsMaterialErrorWarningDefineStressStrainCurve: int = 15
swsMaterialErrorWarningDefinePointForStressStrainCurve: int = 16
swsMaterialErrorWarningSIGT_S1_F1_S2_F2Values: int = 17
swsMaterialErrorWarningSIGT_S1LessThanSIGT_F1: int = 18
swsMaterialErrorWarningSIGT_S2LessThanSIGT_F1: int = 19
swsMaterialErrorWarningSIGT_F2LessThanSIGT_S2: int = 20
swsMaterialErrorWarningSIGC_S1LessThanSIGC_F1: int = 21
swsMaterialErrorWarningSIGC_S2LessThanSIGC_F1: int = 22
swsMaterialErrorWarningSIGC_F2LessThanSIGC_S2: int = 23
swsMaterialErrorWarningCreepWithForceControl: int = 24
swsMaterialErrorWarningMaterialTemperatureDependencyIgnored: int = 30
swsMaterialErrorWarningOnlyBilinearPlasticityForDropTestStudies: int = 31
swsMaterialErrorWarningNUXYNotDefined: int = 32

# swsMaterialFatigueSNCurveError_e (CosmosWorksLib)
swsMaterialFatigueSNCurveErrorSuccessful: int = 0
swsMaterialFatigueSNCurveErrorIndexValues: int = 1
swsMaterialFatigueSNCurveErrorInvalidArray: int = 2
swsMaterialFatigueSNCurveErrorCycles: int = 3
swsMaterialFatigueSNCurveErrorCurveDataPoints: int = 4
swsMaterialFatigueSNCurveErrorStressValuesMustBeUnique: int = 5

# swsMaterialModelType_e (CosmosWorksLib)
swsMaterialModelTypeLinearElasticIsotropic: int = 0
swsMaterialModelTypeLinearElasticOrthtropic: int = 1
swsMaterialModelTypeLinearElasticAnisotropic: int = 2
swsMaterialModelTypeNonlinearElastic: int = 3
swsMaterialModelTypeElastoPlasticvonMisesKinematic: int = 4
swsMaterialModelTypeElastoPlasticTrescaKinematic: int = 5
swsMaterialModelTypeElastoPlasticDruckerPrager: int = 6
swsMaterialModelTypeHyperElasticMooneyRivlin: int = 7
swsMaterialModelTypeHyperElasticOgden: int = 8
swsMaterialModelTypeHyperElasticBlatzko: int = 9
swsMaterialModelTypeViscoElastic: int = 10
swsMaterialModelTypeNitinol: int = 11
swsMaterialModelTypeCreepExponential: int = 12

# swsMaterialReferencePlaneError_e (CosmosWorksLib)
swsMaterialReferencePlaneErrorSuccessful: int = 0
swsMaterialReferencePlaneErrorSpecifyPlaneOrAxis: int = 1

# swsMaterialSNCurveSource_e (CosmosWorksLib)
swsMaterialSNCurveSourceUserDefined: int = 0
swsMaterialSNCurveSourceASMEAustenticSteel: int = 1
swsMaterialSNCurveSourceASMECarbonSteel: int = 2
swsMaterialSNCurveSourceEquation: int = 3

# swsMaterialSourceType_e (CosmosWorksLib)
swsMaterial_Custom: int = 0
swsMaterial_Library: int = 1

# swsMaterialSource_e (CosmosWorksLib)
swsMaterialSourceSolidWorks: int = 0
swsMaterialSourceCustomDefined: int = 1
swsMaterialSourceCentorLibrary: int = 2
swsMaterialSourceLibraryFiles: int = 3

# swsMaterialStressStrainCurveError_e (CosmosWorksLib)
swsMaterialStressStrainCurveErrorSuccessful: int = 0
swsMaterialStressStrainCurveErrorInvalidForMaterial: int = 1
swsMaterialStressStrainCurveErrorInvalidArray: int = 2
swsMaterialStressStrainCurveErrorTemperatures: int = 3
swsMaterialStressStrainCurveErrorNeedDataPoints: int = 4

# swsMaterialTemperatureCurveForPropertyError_e (CosmosWorksLib)
swsMaterialTemperatureCurveForPropertyErrorSuccessful: int = 0
swsMaterialTemperatureCurveForPropertyErrorPropertyNotDefined: int = 1
swsMaterialTemperatureCurveForPropertyErrorNotApplicable: int = 2
swsMaterialTemperatureCurveForPropertyErrorNotAllowed: int = 3
swsMaterialTemperatureCurveForPropertyErrorInvalidArray: int = 4
swsMaterialTemperatureCurveForPropertyErrorNeedDataPoints: int = 5
swsMaterialTemperatureCurveForPropertyErrorTermperatures: int = 6

# swsMaterialTemperature_e (CosmosWorksLib)
swsMaterialTemperatureDependent: int = 0
swsMaterialTemperatureNotDependent: int = 1

# swsMeshCompatibility_e (CosmosWorksLib)
swsMeshCompatibilityCompatible: int = 0
swsMeshCompatibiltyIncompatible: int = 1

# swsMeshControlError_e (CosmosWorksLib)
swsMeshControlErrorSuccessful: int = 0
swsMeshControlErrorNoEntityAtIndex: int = 1
swsMeshControlErrorEntityAlreadyExists: int = 2
swsMeshControlErrorNoEntities: int = 3
swsMeshControlErrorSelectVerticesEdgesFacesBodiesOrComponents: int = 4
swsMeshControlErrorSelectFaceEdgeOrVertex: int = 5
swsMeshControlErrorElementSize: int = 6
swsMeshControlErrorNumberOfLayers: int = 7

# swsMeshControlMeshingError_e (CosmosWorksLib)
swsMeshControlMeshingErrorSuccessful: int = 0
swsMeshControlMeshingErrorInvalidMeshControlName: int = 1
swsMeshControlMeshingErrorMeshControlNotFound: int = 2
swsMeshControlMeshingErrorMeshControlUnsuccessful: int = 3

# swsMeshControlWeightFactor_e (CosmosWorksLib)
swsMeshControlWeightFactorDefault: int = 0
swsMeshControlWeightFactorHighest: int = 1

# swsMeshCopyErrorCode_e (CosmosWorksLib)
swsMeshCopy_NoError: int = 0
swsMeshCopy_StudyNotActive: int = 1
swsMeshCopy_InvalidStudyName: int = 2
swsMeshCopy_NotSupportedForBeamMesh: int = 3
swsMeshCopy_MeshTypeDifferentForBothStudies: int = 4
swsMeshCopy_UnSupportedStudies: int = 5

# swsMeshElementNodeLocation_e (CosmosWorksLib)
swsMeshElementNodeLocationSuccessful: int = 0
swsMeshElementNodeLocationNoNode: int = 1
swsMeshElementNodeLocationNoElement: int = 2

# swsMeshElementQualityKPI_e (CosmosWorksLib)
swsMeshElementQualityKPI_JacobianRatio: int = 0
swsMeshElementQualityKPI_AspectRatio: int = 1
swsMeshElementQualityKPI_Volume: int = 2
swsMeshElementQualityKPI_Area: int = 3
swsMeshElementQualityKPI_ElemSkewRatio: int = 4

# swsMeshFlipShellError_e (CosmosWorksLib)
swsMeshFlipShellErrorSuccessful: int = 0
swsMeshFlipShellErrorInvalidArray: int = 1
swsMeshFlipShellErrorEmptyArray: int = 2
swsMeshFlipShellErrorNotShell: int = 3
swsMeshFlipShellErrorSelectFaces: int = 4
swsMeshFlipShellErrorMeshInformationNotFound: int = 5

# swsMeshKPIErrCode_e (CosmosWorksLib)
swsMeshKPIErrCode_Success: int = 0
swsMeshKPIErrCode_KPINotSupported: int = 1
swsMeshKPIErrCode_ImproperInput: int = 2
swsMeshKPIErrCode_InvalidMeshData: int = 3
swsMeshKPIErrCode_ImproperGaussOrder: int = 4
swsMeshKPIErrCode_InternalError: int = 5

# swsMeshQuality_e (CosmosWorksLib)
swsMeshQualityDraft: int = 0
swsMeshQualityHigh: int = 1

# swsMeshQueryErrorCode_e (CosmosWorksLib)
swsMeshQuery_NoError: int = 0
swsMeshQuery_DataBaseNotAvailable: int = 1
swsMeshQuery_NoElements: int = 2
swsMeshQuery_NoNodes: int = 3
swsMeshQuery_Failed: int = 10

# swsMeshShellNormal_e (CosmosWorksLib)
swsMeshShellNormalNotFoundOrFaceNotSelected: int = -1
swsMeshShellNormalTopFace: int = 0
swsMeshShellNormalBottomFace: int = 1

# swsMeshState_e (CosmosWorksLib)
swsMeshStateNoMesh: int = 0
swsMeshStateExistsAndCurrent: int = 1
swsMeshStateExistsAndNotCurrent: int = 2
swsMeshStateFailed: int = 3
swsMeshStateInterrupted: int = 4

# swsMeshType_e (CosmosWorksLib)
swsMeshTypeSolid: int = 0
swsMeshTypeMidSurface: int = 1
swsMeshTypeSurfaces: int = 2
swsMeshTypeMixed: int = 3
swsMeshTypeBeam: int = 4

# swsMesherTypeNew_e (CosmosWorksLib)
swsMesherType_Standard: int = 0
swsMesherType_CB: int = 1
swsMesherType_BCB: int = 2

# swsMesherType_e (CosmosWorksLib)
swsMesherTypeStandard: int = 0
swsMesherTypeAlternate: int = 1
swsMesherTypeAlternateCB: int = 2

# swsModeCombinationMethod_e (CosmosWorksLib)
swsModeCombinationMethod_SRSS: int = 0
swsModeCombinationMethod_AbsSum: int = 1
swsModeCombinationMethod_CQC: int = 2
swsModeCombinationMethod_NRL: int = 3

# swsMomentUnit_e (CosmosWorksLib)
swsMomentUnit_NewtonMeter: int = 0
swsMomentUnit_PoundForceInch: int = 1
swsMomentUnit_KilogramForceCentimeter: int = 2

# swsMultipleContactsEditErrorCode_e (CosmosWorksLib)
swsMultipleContactsEditErrorCode_Success: int = 0
swsMultipleContactsEditErrorCode_NoTypeSelectedForMixedContactTypesSelection: int = 1
swsMultipleContactsEditErrorCode_NoDefaultContactIsSelected: int = 2
swsMultipleContactsEditErrorCode_GivenContactIsNotAddedYet: int = 3
swsMultipleContactsEditErrorCode_NoSuchContactExists: int = 4
swsMultipleContactsEditErrorCode_MultipleContactSetMgrIsNull: int = 5
swsMultipleContactsEditErrorCode_InvalidPropertiesAreApplied: int = 6
swsMultipleContactsEditErrorCode_GivenContactSetDidNotMeetMinCriteria: int = 7
swsMultipleContactsEditErrorCode_GivenContactIsAlreadyAdded: int = 8
swsMultipleContactsEditErrorCode_OperationNotSupported: int = 9
swsMultipleContactsEditErrorCode_NoPenetrationSelfContactSetsCannotBeEditedWithOtherContactTypes: int = 10
swsMultipleContactsEditErrorCode_VirtualWallContactSetsCannotBeEditedWithOtherContactTypes: int = 11
swsMultipleContactsEditErrorCode_BondedContactsWithBeamsCannotBeEditedWithOtherNonBeamContactTypes: int = 12

# swsNForceType_e (CosmosWorksLib)
swsNForceTypeNormal: int = 0
swsNForceTypeFriction: int = 1
swsNForceTypeTotal: int = 2

# swsNameViewOrientation_e (CosmosWorksLib)
swsNameViewOrientation_NormalTo: int = 0
swsNameViewOrientation_Front: int = 1
swsNameViewOrientation_Back: int = 2
swsNameViewOrientation_Left: int = 3
swsNameViewOrientation_Right: int = 4
swsNameViewOrientation_Top: int = 5
swsNameViewOrientation_Bottom: int = 6
swsNameViewOrientation_Isometric: int = 7
swsNameViewOrientation_Trimetric: int = 8
swsNameViewOrientation_Dimetric: int = 9
swsNameViewOrientation_AssociateWithCurrView: int = 10

# swsNastranExportOption_e (CosmosWorksLib)
swsNastranExportOption_ShortFree: int = 0
swsNastranExportOption_LongFree: int = 1
swsNastranExportOption_ShortFixed: int = 2
swsNastranExportOption_LongFixed: int = 3

# swsNastranExportUnit_e (CosmosWorksLib)
swsNastranExportUnit_SI: int = 0
swsNastranExportUnit_IPS: int = 1
swsNastranExportUnit_MKS: int = 2

# swsNoPenetrationOption_e (CosmosWorksLib)
swsNoPenetrationOptionNodeToNode: int = 0
swsNoPenetrationOptionNodeToSurface: int = 1
swsNoPenetrationOptionSurfaceToSurface: int = 2

# swsNodalResultsOfElementError_e (CosmosWorksLib)
swsNodalResultsOfElementError_NoError: int = 0
swsNodalResultsOfElementError_InvalidStudy: int = 1
swsNodalResultsOfElementError_InvalidResultType: int = 2
swsNodalResultsOfElementError_InvalidComponent: int = 3
swsNodalResultsOfElementError_InvalidStep: int = 4
swsNodalResultsOfElementError_InvalidUnits: int = 5
swsNodalResultsOfElementError_InvalidShellFace: int = 6
swsNodalResultsOfElementError_InvalidElements: int = 7
swsNodalResultsOfElementError_InvalidElementGroup: int = 8
swsNodalResultsOfElementError_ResultsNotAvailable: int = 9

# swsNonLinearOptionControlMethodType_e (CosmosWorksLib)
swsNonLinearControl_Force: int = 0
swsNonLinearControl_Displacement: int = 1
swsNonLinearControl_ArcLength: int = 2

# swsNonLinearOptionIntegrationMethodType_e (CosmosWorksLib)
swsNonLinearIntegration_Newmark: int = 0
swsNonLinearIntegration_WilsonTheta: int = 1
swsNonLinearIntegration_CentralDifference: int = 2

# swsNonLinearOptionIterativeMethodType_e (CosmosWorksLib)
swsNonLinearIterative_ModifiedNewtonRaphson: int = 0
swsNonLinearIterative_NewtonRaphson: int = 1

# swsNonLinearStudyOptionsError_e (CosmosWorksLib)
swsNonLinearStudyOptionsErrorSuccessful: int = 0
swsNonLinearStudyOptionsErrorStartEndStepsAndIncrement: int = 1
swsNonLinearStudyOptionsErrorAutoSteppingParameters: int = 2
swsNonLinearStudyOptionsErrorStartTimeLessThanEndTime: int = 3
swsNonLinearStudyOptionsErrorSolutionSteps: int = 4
swsNonLinearStudyOptionsErrorSelectVerticesOrDatumPoint: int = 5
swsNonLinearStudyOptionsErrorSelectDisplacementControlType: int = 6
swsNonLinearStudyOptionsErrorSelectArcLengthControlType: int = 7
swsNonLinearStudyOptionsErrorSelectTimeCurve: int = 8
swsNonLinearStudyOptionsErrorSelectDirectSolver: int = 9
swsNonLinearStudyOptionsErrorSelectForceControl: int = 10
swsNonLinearStudyOptionsErrorWrongArcLengthUnit: int = 11
swsNonLinearStudyOptionsErrorEmptyDispatch: int = 12
swsNonLinearStudyTimeCurveErrorInvalidStudyType: int = 13
swsNonLinearStudyInvalidDisplaceComponentValue: int = 14
swsNonLinearStudyInvalidDisplaceComponentUnitValue: int = 15
swsNonLinearStudyInvalidArcLengthMultiplierValue: int = 16
swsNonLinearStudyInvalidArcLengthMaximumDisplacementValue: int = 17
swsNonLinearStudyInvalidArcLengthMaximumLoadValue: int = 18
swsNonLinearStudyInvalidArcLengthStepsValue: int = 19
swsNonLinearStudyInvalidSingularityEliminationfactorValue: int = 20

# swsNonlinearAnalysisSubType_e (CosmosWorksLib)
swsNonlinearAnalysisSubTypeStatic: int = 0
swsNonlinearAnalysisSubTypeDynamic: int = 1

# swsNonlinearStudyResultTypes_e (CosmosWorksLib)
swsNonlinearResultNodalStress: int = 0
swsNonlinearResultElementalStress: int = 1
swsNonlinearResultDisplacement: int = 2
swsNonlinearResultNodalStrain: int = 3
swsNonlinearResultElementalStrain: int = 4

# swsOptimizationStudyResultType_e (CosmosWorksLib)
swsOptimizationStudyResult_InitialAndFinalIterations: int = 0
swsOptimizationStudyResult_AllIterations: int = 1

# swsPVResultCombinationError_e (CosmosWorksLib)
swsPVResultCombinationError_NoError: int = 0
swsPVResultCombinationError_NotAvailable: int = 1
swsPVResultCombinationError_AtleastTwoItemsNeeded: int = 2
swsPVResultCombinationError_StudyNamesNotProper: int = 3
swsPVResultCombinationError_ItemsNotSameInNumber: int = 4
swsPVResultCombinationError_InvalidFactors: int = 5
swsPVResultCombinationError_InvalidStudy: int = 6
swsPVResultCombinationError_CombineAnalysisNotDone: int = 7
swsPVResultCombinationError_CombineIncompatibleResults: int = 8
swsPVResultCombinationError_CombineIncompatibleMesh: int = 9
swsPVResultCombinationError_CombineIncompatibleConfiguration: int = 10
swsPVResultCombinationError_CombineIncompatibleRestraints: int = 11
swsPVResultCombinationError_CombineIncompatibleSolidsMaterials: int = 12
swsPVResultCombinationError_CombineIncompatibleShellsMaterials: int = 13
swsPVResultCombinationError_CombineIncompatibleContact: int = 14
swsPVResultCombinationError_CombineIncompatibleConnectors: int = 15
swsPVResultCombinationError_CombineIncompatiblePlanarType: int = 16

# swsPVResultCombinationType_e (CosmosWorksLib)
swsPVResultCombinationType_Linear: int = 0
swsPVResultCombinationType_SRSS: int = 1

# swsPhaseAngleUnit_e (CosmosWorksLib)
swsPhaseAngleUnit_Deg: int = 0
swsPhaseAngleUnit_Rad: int = 1

# swsPinConnectorEndEditError_e (CosmosWorksLib)
swsPinConnectorEndEditErrorSuccessful: int = 0
swsPinConnectorEndEditErrorNoEntityAtIndex: int = 1
swsPinConnectorEndEditErrorEntityAlreadyAdded: int = 2
swsPinConnectorEndEditErrorSelectEntity: int = 3
swsPinConnectorEndEditErrorSelectFace: int = 4
swsPinConnectorEndEditErrorSelectFaceCylindricalSurface: int = 5
swsPinConnectorEndEditErrorSelectConcentricCylindricalFacesConnector: int = 6
swsPinConnectorEndEditErrorRadiiNotEqual: int = 7
swsPinConnectorEndEditErrorSelectAssemblyDocument: int = 8
swsPinConnectorEndEditErrorSelectConcentricCylindricalFacesConnection: int = 9
swsPinConnectorEndEditErrorIndexTooBig: int = 10
swsPinConnectorEndEditErrorHasBeamBody: int = 11
swsPinConnectorEndEditErrorHasMassElement: int = 12
swsPinConnectorEndEditErrorSelectCircularEdges: int = 13
swsPinConnectorEndEditErrorSelectDifferentBody: int = 14
swsPinConnectorEndEditErrorSelectFacesFromSameHole: int = 15
swsPinConnectorEndEditErrorSpecifyPositiveValue: int = 16
swsPinConnectorEndEditErrorPinMass: int = 17
swsPinConnectorEndEditErrorTensileStressArea: int = 18
swsPinConnectorEndEditErrorTesileStressAreaLarge: int = 19
swsPinConnectorEndEditErrorPinBoltStrength: int = 20
swsPinConnectorEndEditErrorSafetyFactor: int = 21
swsPinConnectorEndEditErrorSelectCircularEdge: int = 22
swsPinConnectorEndEditErrorBodyExcludedFromAnalysis: int = 23
swsPinConnectorEndEditErrorNullEntity: int = 24
swsPinConnectorEndEditErrorIncludeStrengthData: int = 25
swsPinConnectorEndEditErrorInvalidForAnalysis: int = 26
swsPinConnectorEndEditErrorInvalidConnectionType: int = 27

# swsPinConnectorError_e (CosmosWorksLib)
swsPinConnectorErrorSuccesful: int = 0
swsPinConnectorErrorInvalidMesh: int = 1
swsPinConnectorErrorNonlinearStudyPartDocument: int = 2
swsPinConnectorErrorInvalidStudy: int = 3
swsPinConnectorErrorNoObject: int = 4
swsPinConnectorErrorSelectFace: int = 5
swsPinConnectorErrorFaceNotCylindrical: int = 6
swsPinConnectorErrorSelectConcentricCylindricalFacesForConnector: int = 7
swsPinConnectorErrorComponentConcentricFacesRadiiNotEqual: int = 8
swsPinConnectorErrorInvalidArray: int = 9
swsPinConnectorErrorSelectAssemblyDocument: int = 10
swsPinConnectorErrorSelectFacesFromSameHoleForSource: int = 11
swsPinConnectorErrorSelectFaceFromSameHoleForTarget: int = 12
swsPinConnectorErrorNullOrEmptyArray: int = 13
swsPinConnectorErrorEntitySameForComponents: int = 14
swsPinConnectorErrorSelectDifferentBody: int = 15
swsPinConnectorErrorArrayEmtpy: int = 16
swsPinConnectorErrorArrayHasBeamBody: int = 17
swsPinConnectorErrorSelectConcentricCylindricalFacesForConnection: int = 18
swsPinConnectorErrorSelectCircularEdgesOnShells: int = 19
swsPinConnectorErrorBodyExcludedFromAnalysis: int = 20

# swsPinballUnit_e (CosmosWorksLib)
swsPinballmm: int = 0
swsPInballcm: int = 1
swsPinballm: int = 2
swsPinballin: int = 3
swsPinballft: int = 4
swsPinballftin: int = 5
swsPinballam: int = 6
swsPinaballnm: int = 7
swsPinballmicron: int = 8
swsPinballmil: int = 9
swsPinballmicronIn: int = 10

# swsPlotBoundarySettingsOptionValue_e (CosmosWorksLib)
swsPlotBoundaryNone: int = 0
swsPlotBoundaryModel: int = 1
swsPlotBoundaryMesh: int = 2
swsPlotBoundaryTranslucentSingleColor: int = 3
swsPlotBoundaryTranslucentPartColor: int = 4

# swsPlotDeformedShapeOptionScaleFactorContactValue_e (CosmosWorksLib)
swsPlotDeformedShapeContactAutomatic: int = 0
swsPlotDeformedShapeContactTrueValue: int = 1

# swsPlotDeformedShapeOptionScaleFactorLargeDispValue_e (CosmosWorksLib)
swsPlotDeformedShapeLargeDispAutomatic: int = 0
swsPlotDeformedShapeLargeDispTrueValue: int = 1

# swsPlotDeformedShapeOptionScaleFactorOtherValue_e (CosmosWorksLib)
swsPlotDeformedShapeOtherAutomatic: int = 0
swsPlotDeformedShapeOtherTrueValue: int = 1

# swsPlotDeformedShapeOptionSuperImposeValue_e (CosmosWorksLib)
swsPlotDeformedShapeSuperImposeModel_TranslucentPartColor: int = 0
swsPlotDeformedShapeSuperImposeModel_TranslucentSingleColor: int = 1

# swsPlotDeformedShapeOptionValue_e (CosmosWorksLib)
swsPlotDeformedShapeShowResultsOnUnDeformedShape: int = 0
swsPlotDeformedShapeShowResultsOnDeformedShape: int = 1

# swsPlotFringeSettingsOptionValue_e (CosmosWorksLib)
swsPlotFringePoint: int = 0
swsPlotFringeLine: int = 1
swsPlotFringeDiscrete: int = 2
swsPlotFringeContinuous: int = 3

# swsPlotResultTypes_e (CosmosWorksLib)
swsResultDisplacementOrAmplitude: int = 1
swsResultStress: int = 2
swsResultStrain: int = 3
swsResultFactorOfSafety: int = 4
swsResultThermal: int = 5
swsResultFatigue: int = 12
swsResultVelocity: int = 19
swsResultAcceleration: int = 20
swsResultDesignInsight: int = 22
swsResultBeamDiagram: int = 54
swsResultPinBoltBearing: int = 56
swsResultEdgeWeldConnector: int = 58
swsResultBeamStress: int = 59
swsResultEquivalentStress: int = 67

# swsPlotSettingsErrorCode_e (CosmosWorksLib)
swsPlotSettings_NoError: int = 0
swsPlotSettings_InvalidPlotName: int = 1
swsPlotSettings_InvalidNumberOfParameters: int = 2
swsPlotSettings_InvalidParameters: int = 3
swsPlotSettings_InvalidSelectionEntities: int = 4
swsPlotSettings_UnableToFetchLegendData: int = 5
swsPlotSettings_InvalidFringeOption: int = 6
swsPlotSettings_WrongBoundaryOption: int = 7
swsPlotSettings_FailToGetColors: int = 8
swsPlotSettings_WrongRGBValues: int = 9
swsPlotSettings_InvalidInput: int = 10
swsPlotSettings_InvalidAlphaValue: int = 11

# swsPlotShowExcludedBodiesOptionValue_e (CosmosWorksLib)
swsPlotExcludedBodyTranslucentSingleColor: int = 0
swsPlotExcludedBodyTranslucentPartColor: int = 1

# swsPlotShowHiddenBodiesOptionValue_e (CosmosWorksLib)
swsPlotHiddenBodyTranslucentSingleColor: int = 0
swsPlotHiddenBodyTranslucentPartColor: int = 1

# swsPreLoadForceType_e (CosmosWorksLib)
swsPreLoadForceTypeCompression: int = 0
swsPreLoadForceTypeTension: int = 1

# swsPreloadForce_e (CosmosWorksLib)
swsPreloadForceAxial: int = 0
swsPreloadForceTorque: int = 1

# swsPressureEndEditError_e (CosmosWorksLib)
swsPressureEndEditErrorSuccessful: int = 0
swsPressureEndEditErrorNoEntityAtIndex: int = 1
swsPressureEndEditErrorEntityAlreadyAdded: int = 2
swsPressureEndEditErrorNoEntities: int = 3
swsPressureEndEditErrorSelectFacesOrShellEdges: int = 4
swsPressureEndEditErrorSelectFaceOrShellEdge: int = 5
swsPressureEndEditErrorRefGeomPreExist: int = 6
swsPressureEndEditErrorSelectFaceEdgePlaneOrAxis: int = 7
swsPressureEndEditErrorSelectCoordinateSystem: int = 8

# swsPressureError_e (CosmosWorksLib)
swsPressureErrorSuccessful: int = 0
swsPressureErrorSelectFaceOrFaces: int = 1
swsPressureErrorSelectFacesOrShellEdges: int = 2
swsPressureErrorSelectFaceEdgePlaneOrAxis: int = 3
swsPressureErrorPressureType: int = 4
swsPressureErrorInvalidStudy: int = 5
swsPressureErrorInvalidArray: int = 6
swsPressureErrorCannotApplyPressure: int = 7

# swsPressureReferenceGeometryCylindricalType_e (CosmosWorksLib)
swsPressureReferenceGeometryCylindricalTypeRadial: int = 1
swsPressureReferenceGeometryCylindricalTypeCircumferential: int = 2
swsPressureReferenceGeometryCylindricalTypeAxial: int = 3

# swsPressureReferenceGeometryEdgeType_e (CosmosWorksLib)
swsPressureReferenceGeometryEdgeTypeAlongEdge: int = 3

# swsPressureReferenceGeometryPlanarType_e (CosmosWorksLib)
swsPressureReferenceGeometryPlanarTypeAlongPlaneDir1: int = 1
swsPressureReferenceGeometryPlanarTypeAlongPlaneDir2: int = 2
swsPressureReferenceGeometryPlanarTypeNormalToPlane: int = 3

# swsPressureReferenceGeometryReferenceAxisType_e (CosmosWorksLib)
swsPressureReferenceGeometryReferenceAxisTypeRadial: int = 1
swsPressureReferenceGeometryReferenceAxisTypeCircumferential: int = 2
swsPressureReferenceGeometryReferenceAxisTypeAxial: int = 3

# swsPressureType_e (CosmosWorksLib)
swsPressureTypeNormal: int = 0
swsPressureTypeUseReferenceGeometry: int = 1

# swsPressureUnit_e (CosmosWorksLib)
swsPressureUnit_NewtonsPerMeterSquared: int = 0
swsPressureUnit_PSI: int = 1
swsPressureUnit_KilogramForcePerCentimeterSquared: int = 2
swsPressureUnit_NewtonsPerMillimeterSquared: int = 3

# swsProbePostResultErrorCode_e (CosmosWorksLib)
swsProbePostResultError_Success: int = 0
swsProbePostResultError_NoActiveView: int = 1
swsProbePostResultError_NoActiveStudy: int = 2
swsProbePostResultError_ResultPlotActivationFailure: int = 3
swsProbePostResultError_UsedBeforeCallingBeginProbing: int = 4
swsProbePostResultError_InvalidOrEmptyInputArray: int = 5
swsProbePostResultError_ActiveStudyIsNotRun: int = 6
swsProbePostResultError_MeshDataLoadFailure: int = 7
swsProbePostResultError_ProbingNotSupportedOnShellForSectionPlot: int = 8
swsProbePostResultError_ProbingNotSupportedOnDeformationPlot: int = 9
swsProbePostResultError_ProbingNotSupportedOnSectionPlotExplodedAfterClip: int = 10
swsProbePostResultError_InitializationFailure: int = 11
swsProbePostResultError_NoAssociatedStudyFoundForFatigueAnalysis: int = 12
swsProbePostResultError_NoResultOrMeshPlotIsActivated: int = 13
swsProbePostResultError_NotAllNodeElemsAreAnnotated: int = 14

# swsProbePostResultNodeElementSelectionWarning_e (CosmosWorksLib)
swsProbePostResultNodeElemSelectionWarning_FewElemsLieOnBeamGaps: int = 1
swsProbePostResultNodeElemSelectionWarning_FewNodeElemsNotOnSectionPlane: int = 2
swsProbePostResultNodeElemSelectionWarning_FewNodeElemsOutOfRange: int = 4
swsProbePostResultNodeElemSelectionWarning_FewNodeElemsLieOnNonRenderedBody: int = 8

# swsProbePostResultOption_e (CosmosWorksLib)
swsProbePostResultOption_AtLocation: int = 0
swsProbePostResultOption_FromSensors: int = 1
swsProbePostResultOption_OnSelectedEntities: int = 2
swsProbePostResultOption_AtDistance: int = 3
swsProbePostResultOption_AtNodeElemNumber: int = 4

# swsRadiationEndEditError_e (CosmosWorksLib)
swsRadiationEndEditErrorSuccessful: int = 0
swsRadiationEndEditErrorNoEntityAtIndex: int = 1
swsRadiationEndEditErrorEntityAlreadyExists: int = 2
swsRadiationEndEditErrorNoEntities: int = 3
swsRadiationEndEditErrorSelectFace: int = 4
swsRadiationEndEditErrorSelectFaceOrEdge: int = 5
swsRadiationEndEditErrorEmissivity: int = 6
swsRadiationEndEditErrorViewFactor: int = 7

# swsRadiationError_e (CosmosWorksLib)
swsRadiationErrorSuccessful: int = 0
swsRadiationErrorSelectFaces: int = 1
swsRadiationErrorSelectFaceOrShellEdge: int = 2
swsRadiationErrorInvalidStudy: int = 3
swsRadiationErrorRadiationType: int = 4
swsRadiationErrorInvalidArray: int = 5
swsRadiationErrorEmtpyArray: int = 6

# swsRadiationOpenSystem_e (CosmosWorksLib)
swsRadiationOpenSystemClosed: int = 0
swsRadiationOpenSystemOpen: int = 1

# swsRadiationType_e (CosmosWorksLib)
swsRadiationTypeSurfaceToAmbient: int = 0
swsRadiationTypeSurfaceToSurface: int = 1

# swsRandomVibrationAnalysisMethod_e (CosmosWorksLib)
swsRandomVibrationAnalysisMethod_Standard: int = 0
swsRandomVibrationAnalysisMethod_Approximate: int = 1

# swsRandomVibrationCorrelationOption_e (CosmosWorksLib)
swsRandomVibrationCorrelationOption_FullyCorrelated: int = 0
swsRandomVibrationCorrelationOption_FullyUnCorrelated: int = 1
swsRandomVibrationCorrelationOption_PartiallyCorrelated: int = 2

# swsRefDispType_e (CosmosWorksLib)
swsNone: int = 0
swsDatumPlane: int = 1
swsCoordSys: int = 2
swsDatumAxis: int = 3

# swsReferencePressureOption_e (CosmosWorksLib)
swsReferencePressureOption_UseFld: int = 0
swsReferencePressureOption_Define: int = 1

# swsRemoteLoadCheckCode_e (CosmosWorksLib)
swsRemoteLoadCheckCode_None: int = 0
swsRemoteLoadCheckCode_Load: int = 1
swsRemoteLoadCheckCode_Displacement: int = 2

# swsRemoteLoadConnectionType_e (CosmosWorksLib)
swsRemoteLoadConnectionType_Rigid: int = 0
swsRemoteLoadConnectionType_Distributed: int = 1

# swsRemoteLoadEndEditError_e (CosmosWorksLib)
swsRemoteLoadEndEditError_NoError: int = 0
swsRemoteLoadEndEditError_SelectFaceEdgeOrVertex: int = 1
swsRemoteLoadEndEditError_SelectCoordinateSystem: int = 2
swsRemoteLoadEndEditError_InvalidLoadType: int = 3
swsRemoteLoadEndEditError_InvalidStudyType: int = 4
swsRemoteLoadEndEditError_InvalidArray: int = 5
swsRemoteLoadEndEditError_EmptyArray: int = 6
swsRemoteLoadEndEditError_EntityAlreadyAdded: int = 7
swsRemoteLoadEndEditError_InvalidUnits: int = 8
swsRemoteLoadEndEditError_InvalidMassArray: int = 9
swsRemoteLoadEndEditError_InvalidMass: int = 10
swsRemoteLoadEndEditError_CheckAtleastOneComp: int = 11
swsRemoteLoadEndEditError_InvalidForAnalysis: int = 12
swsRemoteLoadEndEditError_InvalidForNonSolid: int = 13
swsRemoteLoadEndEditError_InvalidForRigid: int = 14
swsRemoteLoadEndEditError_DisplacementMustBe0ForTopology: int = 15
swsRemoteLoadEndEditError_InvalidConnectionType: int = 16

# swsRemoteLoadType_e (CosmosWorksLib)
swsRemoteLoadType_DirectLoad: int = 0
swsRemoteLoadType_RigidLoadOrMass: int = 1
swsRemoteLoadType_RigidDisplacement: int = 2
swsRemoteLoadType_DirectDisplacement: int = 3

# swsRemoteLoadWeightingFactor_e (CosmosWorksLib)
swsRemoteLoadWeightingFactor_Default_Constant: int = 0
swsRemoteLoadWeightingFactor_Linear: int = 1
swsRemoteLoadWeightingFactor_Quadratic: int = 2
swsRemoteLoadWeightingFactor_Cubic: int = 3

# swsReportFolderValue_e (CosmosWorksLib)
swsResultFolderAsReportFolder: int = 0
swsUserDefinedReportFolder: int = 1

# swsResistanceType_e (CosmosWorksLib)
swsResistanceTypeTotal: int = 0
swsResistanceTypeDistributed: int = 1

# swsRestraintEndEditError_e (CosmosWorksLib)
swsRestraintEndEditErrorSuccess: int = 0
swsRestraintEndEditErrorNoIndex: int = 1
swsRestraintEndEditErrorEntityExists: int = 2
swsRestraintEndEditErrorNoEntity: int = 3
swsRestraintEndEditErrorSelectFaceEdgeOrVertices: int = 4
swsRestraintEndEditErrorSelectFaces: int = 5
swsRestraintEndEditErrorSelectCylindricalFaces: int = 6
swsRestraintEndEditErrorSelectSphericalFaces: int = 7
swsRestraintEndEditErrorSelectFaceEdgeVertexOrFaces: int = 8
swsRestraintEndEditErrorSelectPlaneAxisEdgeFaceOrCylinder: int = 9
swsRestraintEndEditErrorCyclicSymmetryRestraint: int = 10
swsRestraintEndEditErrorSelectTwoFaces: int = 11
swsRestraintEndEditErrorSelectAxis: int = 12
swsRestraintEndEditErrorDefineDisplacementComponent: int = 13
swsRestraintEndEditErrorCannotRestrainRefGeometryEntity: int = 14

# swsRestraintError_e (CosmosWorksLib)
swsRestraintErrorSuccess: int = 0
swsRestraintErrorSelectFacesEdgesOrVertices: int = 1
swsRestraintErrorSelectPlanarFace: int = 2
swsRestraintErrorSpecifyCylindricalFace: int = 3
swsRestraintErrorSpecifySphericalFace: int = 4
swsRestraintErrorSpecifyFaceEdgePlaneOrAxis: int = 6
swsRestraintErrorSelectFace: int = 7
swsRestraintErrorInMeshType: int = 8
swsRestraintErrorInvalidStudyType: int = 9
swsRestraintErrorNoEntities: int = 10
swsRestraintErrorInvalidArray: int = 11
swsRestraintErrorSpecifyTwoFacesOneAxis: int = 12
swsRestraintErrorInvalidRestraintType: int = 13
swsRestraintErrorCannotApplyRestraint: int = 14
swsRestraintErrorInvalidMesh: int = 15

# swsRestraintType_e (CosmosWorksLib)
swsRestraintTypeFixed: int = 0
swsRestraintTypeImmovable: int = 1
swsRestraintTypeSymmetric: int = 2
swsRestraintTypeRoller: int = 3
swsRestraintTypeHinge: int = 4
swsRestraintTypeReferenceGeometry: int = 5
swsRestraintTypeFlatFace: int = 6
swsRestraintTypeCylindricalFaces: int = 7
swsRestraintTypeSphericalSurface: int = 8
swsRestraintTypeCyclicSymmetry: int = 9

# swsResultEnvelopeBoundary (CosmosWorksLib)
swsResultEnvelopeBoundary_Max: int = 0
swsResultEnvelopeBoundary_Min: int = 1
swsResultEnvelopeBoundary_AbsMax: int = 2

# swsResultFolderValue_e (CosmosWorksLib)
swsSolidWorksDocumentFolder: int = 0
swsUserDefinedFolder: int = 1

# swsResultOptionsSensorOption_e (CosmosWorksLib)
swsResultOptionsSensorOption_None: int = -1
swsResultOptionsSensorOption_AllTrackedDataSensors: int = 0
swsResultOptionsSensorOption_SpecificSensor: int = 1

# swsResultPlotColorOption_ErrorCode_e (CosmosWorksLib)
swsResultPlotColorOption_NoError: int = 0
swsResultPlotColorOption_WrongBoundaryOption: int = 1
swsResultPlotColorOption_FailToGetColors: int = 2
swsResultPlotColorOption_WrongRGBValues: int = 3

# swsResultPlotDelete_ErrorCode_e (CosmosWorksLib)
swsResultPlotDelete_NoError: int = 0
swsResultPlotDelete_InvalidResultType: int = 1
swsResultPlotDelete_InvalidResultComponent: int = 2
swsResultPlotDelete_FailToDelete: int = 3

# swsResultPlotErrorCode_e (CosmosWorksLib)
swsResultPlot_NoError: int = 0
swsResultPlot_InvalidStudy: int = 1
swsResultPlot_FailedPlotCreation: int = 2
swsResultPlot_InvalidSelectedEntities: int = 3
swsResultPlot_InvalidInputArgInCombiWithTensorVectorFlag: int = 4
swsResultPlot_InvalidResultType: int = 5
swsResultPlot_InvalidComponentType: int = 6
swsResultPlot_InvalidUnitType: int = 7
swsResultPlot_IsAvailableOnlyForElements: int = 8
swsResultPlot_InvalidMeshAppliedToStudy: int = 9
swsResultPlot_TryingToSetInvalidProperty: int = 10
swsResultPlot_IsAvailableOnlyForNodes: int = 11
swsResultPlot_InvalidStudyType: int = 12
swsResultPlot_ImproperResultsEquation: int = 13
swsResultPlot_PlotDoesNotExist: int = 14
swsResultPlot_EquivalentStressNotApplicable: int = 15
swsResultPlot_CosworksViewNotPresent: int = 16
swsResultPlot_InvalidExternalResultsFile: int = 17
swsResultPlot_InvalidIsoValueRange: int = 18
swsResultPlot_InvalidSmoothingCycleRange: int = 19
swsResultPlot_MeshInformationNotFound: int = 20

# swsResultStressLinearizationErrors_e (CosmosWorksLib)
swsStressLinearization_Success: int = 0
swsStressLinearization_StudyNotSupported: int = 1
swsStressLinearization_MeshTypeNotSupported: int = 2
swsStressLinearization_InvalidReferencePlane: int = 3
swsStressLinearization_DatabaseNotAvailable: int = 4
swsStressLinearization_IncorrectNumberOfIntermediatePoints: int = 5
swsStressLinearization_ElementsNotFoundForEndPoints: int = 6
swsStressLinearization_ElementsFromDifferentComponents: int = 7
swsStressLinearization_AllElementsNotFoundForIntermediatePoints: int = 8
swsStressLinearization_SpecifiedPointsNotOnSectionPlane: int = 9
swsStressLinearization_ElementalValuesNotSupported: int = 10
swsStressLinearization_VectorPlotNotSupported: int = 11
swsStressLinearization_InvalidResultComponent: int = 12
swsStressLinearization_InvalidNumberOfPointsSelected: int = 13

# swsResultsDisplacementAndVelocityOption_e (CosmosWorksLib)
swsResultsDisplacementAndVelocityOption_None: int = -1
swsResultsDisplacementAndVelocityOption_Relative: int = 0
swsResultsDisplacementAndVelocityOption_Absolute: int = 1

# swsResultsError_e (CosmosWorksLib)
swsResultsErrorSuccessful: int = 0
swsResultsErrorDatabaseNotAvailable: int = 1
swsResultsErrorIncorrectStepNumber: int = 2
swsResultsErrorIncorrectReferenceEntity: int = 3
swsResultsErrorNoResultType: int = 4
swsResultsErrorInvalidComponent: int = 5
swsResultsErrorIncorrectCodeNumber: int = 6
swsResultsErrorInvalidEntity: int = 7
swsResultsErrorIncompatibleStudy: int = 8
swsResultsErrorIncorrectModeShape: int = 9

# swsResultsRotationalDisplacementUnit_e (CosmosWorksLib)
swsResultsRotationalDisplacementUnitDeg: int = 0
swsResultsRotationalDisplacementUnitDegMin: int = 1
swsResultsRotationalDisplacementUnitDegMinSec: int = 2
swsResultsRotationalDisplacementUnitRad: int = 3

# swsRigidConnectorEndEditError_e (CosmosWorksLib)
swsRigidConnectorEndEditErrorSuccessful: int = 0
swsRigidConnectorEndEditErrorNoEntityAtIndex: int = 1
swsRigidConnectorEndEditErrorEntityAlreadyAdded: int = 2
swsRigidConnectorEndEditErrorSelectTargetEntityOrFaces: int = 3
swsRigidConnectorEndEditErrorSelectFace: int = 4
swsRigidConnectorEndEditErrorIndexTooBig: int = 5
swsRigidConnectorEndEditErrorHasBeamBody: int = 6
swsRigidConnectorEndEditErrorHasMassBody: int = 7
swsRigidConnectorEndEditErrorFacesOnSameComponent: int = 8
swsRigidConnectorEndEditErrorBodyExcludedFromAnalysis: int = 9
swsRigidConnectorEndEditErrorNullEntity: int = 10

# swsRigidConnectorError_e (CosmosWorksLib)
swsRigidConnectorErrorSuccessful: int = 0
swsRigidConnectorErrorInvalidMesh: int = 1
swsRigidConnectorErrorNonlinearStudyPartDocument: int = 2
swsRigidConnectorErrorInvalidStudy: int = 3
swsRigidConnectorErrorSelectAssemblyDocument: int = 4
swsRigidConnectorErrorInvalidSourceArray: int = 5
swsRigidConnectorErrorNoObjectForFace: int = 6
swsRigidConnectorErrorInvalidTargetArray: int = 7
swsRigidConnectorErrorNoObjectForTarget: int = 8
swsRigidConnectorErrorSelectFace: int = 9
swsRigidConnectorErrorSameEntityAtFaceAndTargetArray: int = 10
swsRigidConnectorErrorBodyHasRemoteMass: int = 11
swsRigidConnectorErrorNullOrEmptyArray: int = 12
swsRigidConnectorErrorFacesFromSameComponent: int = 13
swsRigidConnectorErrorBodyExcludedFromAnalysis: int = 14

# swsRotationUnit_e (CosmosWorksLib)
swsRotationUnit_Degrees: int = 0
swsRotationUnit_DegreesMin: int = 1
swsRotationUnit_DegreesMinSec: int = 2
swsRotationUnit_Radians: int = 3

# swsRunAnalysisError_e (CosmosWorksLib)
swsRunAnalysisErrorSuccessful: int = 0
swsRunAnalysisErrorUseHighQualityMesh: int = 1
swsRunAnalysisErrorDefineRigidVirtualWallContact: int = 2
swsRunAnalysisDefineInitialTemperature: int = 3
swsRunAnalysisErrorMultipleLoadsUseSameTimeCurve: int = 4
swsRunAnalysisErrorSetUpDropTestStudy: int = 5
swsRunAnalysisErrorNeedOneOrMoreStaticStudies: int = 6
swsRunAnalysisErrorNoFatigueEvent: int = 7
swsRunAnalysisErrorTimeDependentOrAmplitideOnlyLoads: int = 8
swsRunAnalysisErrorNoSNCurve: int = 9
swsRunAnalysisErrorMeshNotIdentical: int = 11
swsRunAnalysisErrorNoValidShell: int = 12
swsRunAnalysisErrorEXMaterialPropertyNotDefined: int = 13
swsRunAnalysisErrorEXValue: int = 14
swsRunAnalysisErrorPoissonsRatio: int = 15
swsRunAnalysisErrorThermalConductivityNotDefined: int = 16
swsRunAnalysisErrorRemoveOrChangeCreep: int = 17
swsRunAnalysisErrorMaterialNotDefinedForShells: int = 18
swsRunAnalysisErrorMaterialNotDefined: int = 19
swsRunAnalysisErrorMaterialNotDefinedForComponents: int = 20
swsRunAnalysisErrorNoSolidBody: int = 21
swsRunAnalysisErrorAuthorizationFailed: int = 22
swsRunAnalysisErrorMeshNotFound: int = 23
swsRunAnalysisErrorAnalysisFailed: int = 24
swsRunAnalysisErrorStudyNotExist: int = 25
swsRunAnalysisErrorPadaptiveNotSupportLargeDisplacement: int = 26
swsRunAnalysisErrorPadaptiveNotSupportCyclicSymmetry: int = 27
swsRunAnalysisErrorPadaptiveNotSupportNoPenetration: int = 28
swsRunAnalysisErrorPadaptiveNotSupportRemoteLoadMassGapContactConnector: int = 29
swsRunAnalysisErrorInvalidLBC: int = 30

# swsRunStressHotSpotDiagnosticsError_e (CosmosWorksLib)
swsRunStressHotSpotDiagnostics_NoError: int = 0
swsRunStressHotSpotDiagnostics_NotSupportedForThisStudy: int = 1
swsRunStressHotSpotDiagnostics_ImproperSensitivityFactor: int = 2
swsRunStressHotSpotDiagnostics_ResultsNotAvailable: int = 3
swsRunStressHotSpotDiagnostics_ImproperMeshRefineLevels: int = 4
swsRunStressHotSpotDiagnostics_ImproperReductionFactor: int = 5
swsRunStressHotSpotDiagnostics_ImproperGrowthRatio: int = 6
swsRunStressHotSpotDiagnostics_ImproperResultRestoreOption: int = 7

# swsRunStudiesErrorCode_e (CosmosWorksLib)
swsRunStudiesErrorCode_Success: int = 0
swsRunStudiesErrorCode_NoStudyIsSelectedOrDefined: int = 1
swsRunStudiesErrorCode_InvalidStudiesAreSelected: int = 2
swsRunStudiesErrorCode_UnknownError: int = 3
swsRunStudiesErrorCode_AllStudiesRunFailed: int = 4
swsRunStudiesErrorCode_FewStudiesRunFailed: int = 5
swsRunStudiesErrorCode_NoActiveStudy: int = 6

# swsRunStudiesResultsErrorCode_e (CosmosWorksLib)
swsRunStudiesResultsErrorCode_Success: int = 0
swsRunStudiesResultsErrorCode_InvalidInputArg: int = 1
swsRunStudiesResultsErrorCode_ResultsNotAvailable: int = 2
swsRunStudiesResultsErrorCode_ReachedEndOfResults: int = 3

# swsRunStudiesRunMeshOptionErrorCode_e (CosmosWorksLib)
swsRunStudiesRunMeshOptionErrorCode_Success: int = 0
swsRunStudiesRunMeshOptionErrorCode_StudyAlreadyAdded: int = 1
swsRunStudiesRunMeshOptionErrorCode_StudyIsNotAdded: int = 2
swsRunStudiesRunMeshOptionErrorCode_OptionCannotBeReplaced: int = 3
swsRunStudiesRunMeshOptionErrorCode_InvalidOptionApplied: int = 4

# swsRunStudiesRunMeshOptions_e (CosmosWorksLib)
swsRunStudiesRunMeshOptions_MeshOnly: int = 0
swsRunStudiesRunMeshOptions_MeshAndRun: int = 1

# swsRunStudiesStatusCode_e (CosmosWorksLib)
swsRunStudiesStatusCode_AnalysisSucceeded: int = 0
swsRunStudiesStatusCode_MeshSucceeded: int = 1
swsRunStudiesStatusCode_AnalysisFailed: int = 2
swsRunStudiesStatusCode_MeshFailed: int = 3
swsRunStudiesStatusCode_UnknownError: int = 4

# swsSaveResultsOption_e (CosmosWorksLib)
swsSaveResultsOption_ForAllSolutionSteps: int = 0
swsSaveResultsOption_ForSpecifiedSolutionSteps: int = 1

# swsSaveeDrawingsErrorCode_e (CosmosWorksLib)
swsSaveeDrawings_NoError: int = 0
swsSaveeDrawings_CosworksViewNotPresent: int = 1
swsSaveeDrawings_PlotNotFoundError: int = 2
swsSaveeDrawings_ResultFolderNotFound: int = 3
swsSaveeDrawings_DatabaseNotFound: int = 4
swsSaveeDrawings_PostFilesNull: int = 5
swsSaveeDrawings_PlotNotActive: int = 6
swsSaveeDrawings_NotAvailableForCurrentMesh: int = 7
swsSaveeDrawings_PostDataFilesNotPresent: int = 8
swsSaveeDrawings_NoPlots: int = 9
swsSaveeDrawings_PlotSaveError: int = 10

# swsSelectionType_e (CosmosWorksLib)
swsSelectionFaceEdgeVertexPoint: int = 0
swsSelectionBeamEndJoints: int = 1
swsSelectionBeams: int = 2

# swsSetDampingRatiosError_e (CosmosWorksLib)
swsSetDampingRatiosError_NoError: int = 0
swsSetDampingRatiosError_NotAvailable: int = 1
swsSetDampingRatiosError_InvalidRows: int = 2
swsSetDampingRatiosError_InvalidArray: int = 3
swsSetDampingRatiosError_InCorrectValues: int = 4
swsSetDampingRatiosError_OptionsNotAvailable: int = 5

# swsShellEndEditError_e (CosmosWorksLib)
swsShellEndEditErrorSuccessful: int = 0
swsShellEndEditErrorShellThickness: int = 1
swsShellEndEditErrorFormulation: int = 2
swsShellEndEditErrorNotEntityAtIndex: int = 3
swsShellEndEditErrorSelectFace: int = 4
swsShellEndEditErrorFaceAlreadyExists: int = 5
swsShellEndEditErrorFaceAlreadyDefinedAsShell: int = 6
swsShellEndEditErrorNoEntitySelected: int = 7
swsShellEndEditErrorUnit: int = 8
swsShellEndEditErrorOffsetOption: int = 9
swsShellEndEditErrorOffsetValue: int = 10

# swsShellFace_e (CosmosWorksLib)
swsShellFace_Top: int = 0
swsShellFace_Bottom: int = 1
swsShellFace_Membrane: int = 2
swsShellFace_Bending: int = 3

# swsShellFormulation_e (CosmosWorksLib)
swsShellFormulationThin: int = 0
swsShellFormulationThick: int = 1
swsShellFormulationComposite: int = 2

# swsShellManagerError_e (CosmosWorksLib)
swsShellManagerErrorSuccessful: int = 0
swsShellManagerErrorCannotApplyShellForStudy: int = 1
swsShellManagerErrorCannotApplyShellForMesh: int = 2
swsShellManagerErrorEmptyArray: int = 3
swsShellManagerErrorInvalidArray: int = 4
swsShellManagerErrorSelectFacesOnly: int = 5
swsShellManagerErrorFaceAlreadyDefinedAsShell: int = 6
swsShellManagerErrorFaceAlreadyExists: int = 7

# swsShellOffsetOption_e (CosmosWorksLib)
swsShellOffsetOption_Middle: int = 0
swsShellOffsetOption_Top: int = 1
swsShellOffsetOption_Bottom: int = 2
swsShellOffsetOption_SpecifyRatio: int = 3

# swsShrinkFitOption_e (CosmosWorksLib)
swsShrinkFitOptionNodeToSurface: int = 0
swsShrinkFitOptionSurfaceToSurface: int = 1

# swsSimAdaptiveMethodType_e (CosmosWorksLib)
swsNoneMethod: int = 0
swsHAdaptive: int = 1
swsPAdative: int = 2

# swsSimMassPropertiesError_e (CosmosWorksLib)
swsSimMassPropertiesErrorSuccessful: int = 0
swsSimMassPropertiesErrorBodiesNotFound: int = 1
swsSimMassPropertiesErrorBoltNotFound: int = 2
swsSimMassPropertiesErrorPinNotFound: int = 3
swsSimMassPropertiesErrorRemoteLoadNotFound: int = 4
swsSimMassPropertiesErrorDistributedMassNotFound: int = 5
swsSimMassPropertiesErrorBoltMassNotIncluded: int = 6
swsSimMassPropertiesErrorPinMassNotIncluded: int = 7
swsSimMassPropertiesErrorRemoteLoadMassNotIncluded: int = 8
swsSimMassPropertiesErrorUnsuccessful: int = 9
swsSimMassPropertiesErrorLinkageRodNotFound: int = 10
swsSimMassPropertiesErrorLinkageRodMassNotIncluded: int = 11
swsSimMassPropertiesErrorCableNotFound: int = 12
swsSimMassPropertiesErrorCableMassNotIncluded: int = 13

# swsSimulationElementTypes_e (CosmosWorksLib)
swsSolidElement: int = 0
swsShellElement: int = 1
swsBeamElement: int = 2
swsTrussElement: int = 3

# swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_e (CosmosWorksLib)
swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_ModelOrMesh: int = 0
swsSimulationOptionDefaultPlotsBoundaryColorInRGBBoundaryOption_TranslucentSingleColor: int = 1

# swsSimulationOptionDefaultPlotsBoundaryColorInRGBError_e (CosmosWorksLib)
swsSimulationOptionDefaultPlotsBoundaryColorInRGBNoError: int = 0
swsSimulationOptionDefaultPlotsBoundaryColorInRGBWrongBoundaryOption: int = 1
swsSimulationOptionDefaultPlotsBoundaryColorInRGBGetColorUnsuccessful: int = 2

# swsSolverType_e (CosmosWorksLib)
swsSolverTypeAutomatic: int = 0
swsSolverTypeDirectSparse: int = 1
swsSolverTypeFFEPlus: int = 2
swsSolverTypeCASI: int = 5
swsSolverTypeAbaqus: int = 6
swsSolverTypeINTEL: int = 7
swsSolverTypeINTELCluster: int = 8

# swsSpotWeldConnectorEndEditError_e (CosmosWorksLib)
swsSpotWeldConnectorEndEditErrorSuccessful: int = 0
swsSpotWeldConnectorEndEditErrorNullEntity: int = 1
swsSpotWeldConnectorEndEditErrorEntityAlreadyExists: int = 2
swsSpotWeldConnectorEndEditErrorFaceIsEmpty: int = 3
swsSpotWeldConnectorEndEditErrorSelectParallelFaces: int = 5
swsSpotWeldConnectorEndEditErrorPlanesShouldTouch: int = 6
swsSpotWeldConnectorEndEditErrorGapTooBig: int = 7
swsSpotWeldConnectorEndEditErrorSelectDatumPoints: int = 8
swsSpotWeldConnectorEndEditErrorPositiveStudDiameter: int = 9
swsSpotWeldConnectorEndEditErrorStudDiameter: int = 10
swsSpotWeldConnectorEndEditErrorHasBeamBody: int = 11
swsSpotWeldConnectorEndEditErrorHasMassElement: int = 12
swsSpotWeldConnectorEndEditErrorSpotWeldDiameter: int = 13
swsSpotWeldConnectorEndEditErrorIndexTooBig: int = 14
swsSpotWeldConnectorEndEditErrorNoEntityAtIndex: int = 15
swsSpotWeldConnectorEndEditErrorSelectFace: int = 16
swsSpotWeldConnectorEndEditErrorInvalidPoints: int = 17
swsSpotWeldConnectorEndEditErrorBodyExcludedFromAnalysis: int = 18

# swsSpotWeldConnectorError_e (CosmosWorksLib)
swsSpotWeldConnectorErrorSuccessful: int = 0
swsSpotWeldConnectorErrorInvalidMesh: int = 1
swsSpotWeldConnectorErrorNonlinearStudyPartDocument: int = 2
swsSpotWeldConnectorErrorInvalidStudy: int = 3
swsSpotWeldConnectorErrorNullDispatch: int = 4
swsSpotWeldConnectorErrorSelectAssemblyDocument: int = 5
swsSpotWeldConnectorErrorSelectFace: int = 6
SpotWeldConnectorErrorSelectVerticesOrDatumPoint: int = 7
swsSpotWeldConnectorErrorPlanesNotParallel: int = 8
swsSpotWeldConnectorErrorPlanesTouching: int = 9
swsSpotWeldConnectorErrorGapTooBig: int = 10
swsSpotWeldConnectorErrorSelectDatumPoints: int = 11
swsSpotWeldConnectorErrorPostWeldInvalidPoints: int = 12
swsSpotWeldConnectorErrorInvalidArray: int = 13
swsSpotWeldConnectorErrorEmptyArray: int = 14
swsSpotWeldConnectorErrorHasRemoteMass: int = 15
swsSpotWeldConnectorErrorBodyExcludedFromAnalysis: int = 16

# swsSpringConnectorEndEditError_e (CosmosWorksLib)
swsSpringConnectorEndEditErrorSuccessful: int = 0
swsSpringConnectorEndEditErrorNoEntity: int = 1
swsSpringConnectorEndEditErrorSelectFace: int = 2
swsSpringConnectorEndEditErrorSelectPlanarFace: int = 3
swsSpringConnectorEndEditErrorSelectTwoParallelPlanarFaces: int = 4
swsSpringConnectorEndEditErrorSelectFaceWithCylindricalSurface: int = 5
swsSpringConnectorEndEditErrorSelectConcentricCylindricalFaces: int = 6
swsSpringConnectorEndEditErrorRadiiNotEqual: int = 7
swsSpringConnectorEndEditErrorNormalTangentialOrRotationalStiffness: int = 8
swsSpringConnectorEndEditErrorStiffness: int = 9
swsSpringConnectorEndEditErrorSelectDatumPointOrVertex: int = 10
swsSpringConnectorEndEditErrorEntityAlreadyExists: int = 11
swsSpringConnectorEndEditErrorNoEntityAtIndex: int = 12
swsSpringConnectorEndEditErrorIndexInvalidForRemovalOfEntity: int = 13
swsSpringConnectorEndEditErrorHasBeamBody: int = 14
swsSpringConnectorEndEditErrorHasMassElement: int = 15
swsSpringConnectorEndEditErrorSelectionsBelongToSameBody: int = 16
swsSpringConnectorEndEditErrorNullEntity: int = 17
swsSpringConnectorEndEditErrorBodyExcludedFromAnalysis: int = 18

# swsSpringConnectorError_e (CosmosWorksLib)
swsSpringConnectorErrorSuccessful: int = 0
swsSpringConnectorErrorInvalidMesh: int = 1
swsSpringConnectorErrorNonlinearStudyPartDocument: int = 2
swsSpringConnectorErrorInvalidStudy: int = 3
swsSpringConnectorErrorSelectEntities: int = 4
swsSpringConnectorErrorSelectFace: int = 5
swsSpringConnectorErrorSelectFaceWithCylindricalSurface: int = 6
swsSpringConnectorErrorSelectTwoConcentricCylindricalFaces: int = 7
swsSpringConnectorErrorCylindricalFacesRadiiNotEqual: int = 8
swsSpringConnectorErrorSelectPlanarFace: int = 9
swsSpringConnectorErrorSelectTwoPlanarFaces: int = 10
swsSpringConnectorErrorSourceTargetEntitiesSame: int = 11
swsSpringConnectorErrorStudyNonlinearAndSpringSubtypeValue: int = 12
swsSpringConnectorErrorInvalidArray: int = 13
swsSpringConnectorErrorNumberPlanarFacesLessThanTwo: int = 14
swsSpringConnectorErrorNoObjectForSourceOrTarget: int = 15
swsSpringConnectorErrorSelectDatumPoint: int = 16
swsSpringConnectorErrorTooManyEntitiesForSpringType: int = 17
swsSpringConnectorErrorSelectionsOnToSameComponent: int = 18
swsSpringConnectorErrorHasRemoteMass: int = 19
swsSpringConnectorErrorEmptyArray: int = 20
swsSpringConnectorErrorSpringSubtypeInvalidForShellMesh: int = 21
swsSpringConnectorErrorBodyExcludedFromAnalysis: int = 22

# swsSpringConnectorType_e (CosmosWorksLib)
swsSpringConnectoryTypeFlatParallelFaces: int = 0
swsSpringConnectoryTypeConcentricCylindricalFaces: int = 1
swsSpringConnectoryTypeBetweenVertices: int = 2

# swsSpringSubType_e (CosmosWorksLib)
swsSpringSubTypeFlatParallelFaces: int = 0
swsSpringSubTypeConcentricCylindricalFaces: int = 1
swsSpringSubTypeBetweenVertices: int = 2

# swsSpringType_e (CosmosWorksLib)
swsSpringTypeCompressionExtension: int = 0
swsSpringTypeCompression: int = 1
swsSpringTypeExtension: int = 2

# swsStaticResultDisplacementComponentTypes_e (CosmosWorksLib)
swsStaticDisplacement_UX: int = 0
swsStaticDisplacement_UY: int = 1
swsStaticDisplacement_UZ: int = 2
swsStaticDisplacement_URES: int = 3
swsStaticDisplacement_RFX: int = 4
swsStaticDisplacement_RFY: int = 5
swsStaticDisplacement_RFZ: int = 6
swsStaticDisplacement_RFRES: int = 7
swsStaticDisplacement_RX: int = 8
swsStaticDisplacement_RY: int = 9
swsStaticDisplacement_RZ: int = 10
swsStaticDisplacement_RMX: int = 11
swsStaticDisplacement_RMY: int = 12
swsStaticDisplacement_RMZ: int = 13
swsStaticDisplacement_RMRES: int = 14

# swsStaticResultElementalStrainComponentTypes_e (CosmosWorksLib)
swsStaticElementalStrain_EPSX: int = 0
swsStaticElementalStrain_EPSY: int = 1
swsStaticElementalStrain_EPSZ: int = 2
swsStaticElementalStrain_GMXY: int = 3
swsStaticElementalStrain_GMXZ: int = 4
swsStaticElementalStrain_GMYZ: int = 5
swsStaticElementalStrain_ESTRN: int = 6
swsStaticElementalStrain_SEDENS: int = 7
swsStaticElementalStrain_ENERGY: int = 8
swsStaticElementalStrain_E1: int = 9
swsStaticElementalStrain_E2: int = 10
swsStaticElementalStrain_E3: int = 11

# swsStaticResultElementalStressComponentTypes_e (CosmosWorksLib)
swsStaticElementalStress_SX: int = 0
swsStaticElementalStress_SY: int = 1
swsStaticElementalStress_SZ: int = 2
swsStaticElementalStress_TXY: int = 3
swsStaticElementalStress_TXZ: int = 4
swsStaticElementalStress_TYZ: int = 5
swsStaticElementalStress_P1: int = 6
swsStaticElementalStress_P2: int = 7
swsStaticElementalStress_P3: int = 8
swsStaticElementalStress_VON: int = 9
swsStaticElementalStress_INT: int = 10
swsStaticElementalStress_TRI: int = 11
swsStaticElementalStress_ERR: int = 12
swsStaticElementalStress_CONTACTPRESS: int = 13

# swsStaticResultNodalStrainComponentTypes_e (CosmosWorksLib)
swsStaticNodalStrain_EPSX: int = 0
swsStaticNodalStrain_EPSY: int = 1
swsStaticNodalStrain_EPSZ: int = 2
swsStaticNodalStrain_GMXY: int = 3
swsStaticNodalStrain_GMXZ: int = 4
swsStaticNodalStrain_GMYZ: int = 5
swsStaticNodalStrain_ESTRN: int = 6
swsStaticNodalStrain_E1: int = 7
swsStaticNodalStrain_E2: int = 8
swsStaticNodalStrain_E3: int = 9

# swsStaticResultNodalStressComponentTypes_e (CosmosWorksLib)
swsStaticNodalStress_SX: int = 0
swsStaticNodalStress_SY: int = 1
swsStaticNodalStress_SZ: int = 2
swsStaticNodalStress_TXY: int = 3
swsStaticNodalStress_TXZ: int = 4
swsStaticNodalStress_TYZ: int = 5
swsStaticNodalStress_P1: int = 6
swsStaticNodalStress_P2: int = 7
swsStaticNodalStress_P3: int = 8
swsStaticNodalStress_VON: int = 9
swsStaticNodalStress_INT: int = 10
swsStaticNodalStress_TRI: int = 11

# swsStiffnessType_e (CosmosWorksLib)
swsStiffnessTypeDistributed: int = 0
swsStiffnessTypeTotal: int = 1

# swsStrainComponent_e (CosmosWorksLib)
swsStrainComponentEPSX: int = 0
swsStrainComponentEPSY: int = 1
swsStrainComponentEPSZ: int = 2
swsStrainComponentGMXY: int = 3
swsStrainComponentGMXZ: int = 4
swsStrainComponentGMYZ: int = 5
swsStrainComponentESTRN: int = 6
swsStrainComponentSEDENS: int = 7
swsStrainComponentENERGY: int = 8
swsStrainComponentE1: int = 9
swsStrainComponentE2: int = 10
swsStrainComponentE3: int = 11

# swsStrainEnergyDensityUnit_e (CosmosWorksLib)
swsStrainEnergyDensityUnit_NewtonMeterPerCubicMeter: int = 0
swsStrainEnergyDensityUnit_FootPoundPerCubicFeet: int = 1
swsStrainEnergyDensityUnit_CaloriesPerCubicMeter: int = 2

# swsStrainEnergyUnit_e (CosmosWorksLib)
swsStrainEnergyUnit_NewtonMeter: int = 0
swsStrainEnergyUnit_FootPound: int = 1
swsStrainEnergyUnit_Calories: int = 2

# swsStrengthUnit_e (CosmosWorksLib)
swsStrengthUnitPascal: int = 0
swsStrengthUnitPSI: int = 1
swsStrengthUnitKilogramsPerSquareCentimeter: int = 2
swsStrengthUnitNewtonPerSquareMillimeter: int = 3
swsStrengthUnitKSI: int = 4

# swsStressComponent_e (CosmosWorksLib)
swsStressComponentSX: int = 0
swsStressComponentSY: int = 1
swsStressComponentSZ: int = 2
swsStressComponentTXY: int = 3
swsStressComponentTXZ: int = 4
swsStressComponentTYZ: int = 5
swsStressComponentP1: int = 6
swsStressComponentP2: int = 7
swsStressComponentP3: int = 8
swsStressComponentVON: int = 9
swsStressComponentINT: int = 10
swsStressComponentTRI: int = 11
swsStressComponentERR: int = 12
swsStressComponentCP: int = 13
swsStressComponentVONDC: int = 100

# swsStressHotSpotPlotError_e (CosmosWorksLib)
swsStressHotSpotPlot_NoError: int = 0
swsStressHotSpotPlot_NoHotSpotsToPlot: int = 1
swsStressHotSpotPlot_NodalHotSpotsNotAvailable: int = 2

# swsStressHotSpotResultsRestoreOptions_e (CosmosWorksLib)
swsStressHotSpotResultsRestoreOption_OriginalMesh: int = 0
swsStressHotSpotResultsRestoreOption_FinalMesh: int = 1

# swsStudyError_e (CosmosWorksLib)
swsNewStudyErrorSuccessful: int = 0
swsNewStudyErrorNoSolidBody: int = 1
swsNewStudyErrorSameNameStudyExistsOrInvalidStudyName: int = 2
swsNewStudyErrorTypeNotDefined: int = 3
swsNewStudyErrorInvalidMeshType: int = 4
swsNewStudyErrorInvalidStudySubOption: int = 5

# swsStudyExportError_e (CosmosWorksLib)
swsStudyExportError_NoError: int = 0
swsStudyExportError_OptimizationNotAvailable: int = 1
swsStudyExportError_TransientThermalNotAvailable: int = 2
swsStudyExportError_DropTestNotAvailable: int = 3
swsStudyExportError_CreepMaterial: int = 4
swsStudyExportError_RemoteLoadConnectorNotAvailable: int = 5
swsStudyExportError_LoadOnPointsNotAvailable: int = 6
swsStudyExportError_WrongFileOption: int = 7
swsStudyExportError_WrongCosmosExportOptionForNoMesh: int = 8
swsStudyExportError_WrongCosmosExportOption: int = 9
swsStudyExportError_WrongNastranExportOption: int = 10
swsStudyExportError_Wrong_NastranExportUnit: int = 11
swsStudyExportError_WrongCosmosExportUnit: int = 12

# swsStudyExportOption_e (CosmosWorksLib)
swsStudyExportOption_Cosmos: int = 0
swsStudyExportOption_Ansys: int = 1
swsStudyExportOption_Nastran: int = 2
swsStudyExportOption_PatranNeutral: int = 3
swsStudyExportOption_IdeasUniversal: int = 4
swsStudyExportOption_Exodus: int = 5
swsStudyExportOption_Abaqus: int = 6

# swsStudyMeshError_e (CosmosWorksLib)
swsStudyErrorSuccessful: int = 0
swsStudyErrorNoValidShells: int = 1
swsStudyErrorNoSolidBody: int = 2
swsStudyErrorElementSizeTooSmall: int = 3
swsStudyErrorElementSizeTooBig: int = 4
swsStudyErrorSpecifyPositiveValue: int = 5
swsStudyErrorSpecifyElementSizeScaleFactor: int = 6
swsStudyErrorSpecifyToleranceScaleFactor: int = 7

# swsSuppressionState_e (CosmosWorksLib)
swsSupressionStateSuppressed: int = 0
swsSupressionStateUnsuppressed: int = 1

# swsSymmetricalBoltType_e (CosmosWorksLib)
swsSymmtricalBoltTypeOneHalfSymmetry: int = 0
swsSymmtricalBoltTypeOneQuarterSymmetry: int = 1

# swsTableDrivenDistOption_e (CosmosWorksLib)
swsPercentage: int = 0
swsDistance: int = 1

# swsTableDrivenInterpolationType_e (CosmosWorksLib)
swsLinear: int = 0
swsCubic: int = 1

# swsTemperatureCurveError_e (CosmosWorksLib)
swsTemperatureCurveErrorSuccessful: int = 0
swsTemperatureCurveErrorInvalidStudy: int = 1
swsTemperatureCurveErrorCurveCannotBeUsed: int = 2
swsTemperatureCurveErrorNeedDataPoints: int = 3

# swsTemperatureEndEditError_e (CosmosWorksLib)
swsTemperatureEndEditErrorSuccessful: int = 0
swsTemperatureEndEditErrorNoEntityAtIndex: int = 1
swsTemperatureEndEditErrorEntityAlreadyExists: int = 2
swsTemperatureEndEditErrorNoEntities: int = 3
swsTemperatureEndEditErrorSelectVerticesEdgesFacesComponentsOrBodies: int = 4
swsTemperatureEndEditErrorCannotSetInitialTemperatureType: int = 5

# swsTemperatureError_e (CosmosWorksLib)
swsTemperatureErrorSuccessful: int = 0
swsTemperatureErrorSelectVerticesEdgesFacesBodiesOrComponents: int = 1
swsTemperatureErrorInvalidStudy: int = 2
swsTemperatureErrorInvalidArray: int = 3
swsTemperatureErrorEmptyArray: int = 4

# swsTemperatureType_e (CosmosWorksLib)
swsTemperatureTypeInital: int = 0
swsTemperatureTypeFixed: int = 1

# swsTemperatureUnit_e (CosmosWorksLib)
swsTemperatureUnitKelvin: int = 0
swsTemperatureUnitFahrenheit: int = 1
swsTemperatureUnitCelsius: int = 2

# swsTensileStressAreaUnit_e (CosmosWorksLib)
swsTensileStressAreaUnitMillimetersSquared: int = 0
swsTensileStressAreaUnitCentimetersSquared: int = 1
swsTensileStressAreaUnitMetersSquared: int = 2
swsTensileStressAreaUnitInchesSquared: int = 3
swsTensileStressAreaUnitFeetSquared: int = 4

# swsThermalComponent_e (CosmosWorksLib)
swsThermalComponentTEMP: int = 0
swsThermalComponentGRADX: int = 1
swsThermalComponentGRADY: int = 2
swsThermalComponentGRADZ: int = 3
swsThermalComponentGRADN: int = 4
swsThermalComponentHFLUXX: int = 5
swsThermalComponentHFLUXY: int = 6
swsThermalComponentHFLUXZ: int = 7
swsThermalComponentHFLUXN: int = 8

# swsThermalOption_e (CosmosWorksLib)
swsThermalOption_InputTemperature: int = 0
swsThermalOption_TemperatureFromThermalStudy: int = 1
swsThermalOption_TemperatureFromFlow: int = 2

# swsThermalRelaxationFactor_e (CosmosWorksLib)
swsThermalRelaxationFactorAutomatic: int = 0
swsThermalRelaxationFactorFixed: int = 1

# swsThermalResultComponentTypes_e (CosmosWorksLib)
swsThermalResultComponentTypes_TEMP: int = 0
swsThermalResultComponentTypes_GRADX: int = 1
swsThermalResultComponentTypes_GRADY: int = 2
swsThermalResultComponentTypes_GRADZ: int = 3
swsThermalResultComponentTypes_GRADN: int = 4
swsThermalResultComponentTypes_HFLUXX: int = 5
swsThermalResultComponentTypes_HFLUXY: int = 6
swsThermalResultComponentTypes_HFLUXZ: int = 7
swsThermalResultComponentTypes_HFLUXN: int = 8

# swsThermalSolutionType_e (CosmosWorksLib)
swsThermalSolutionTypeTransient: int = 0
swsThermalSolutionTypeSteadyState: int = 1

# swsThreadsPerLengthUnit_e (CosmosWorksLib)
swsThreadsPerLengthUnitPerMillimete: int = 0
swsThreadsPerLengthUnitPerInch: int = 1

# swsTimeCurveError_e (CosmosWorksLib)
swsTimeCurveErrorSuccessful: int = 0
swsTimeCurveErrorInvalidStudyType: int = 1
swsTimeCurveErrorCannotUseWithRestraint: int = 2
swsTimeCurveErrorNeedTwoOrMoreDataPoints: int = 3
swsTimeCurveErrorInvalidDataPoints: int = 4

# swsTimeIntegrationMethod_e (CosmosWorksLib)
swsTimeIntegrationMethod_Newmark: int = 0
swsTimeIntegrationMethod_WilsonTheta: int = 1

# swsTimeUnits_e (CosmosWorksLib)
swsSecond: int = 0
swsMinute: int = 1
swsHour: int = 2
swsDay: int = 3

# swsTopologyActivationOption_e (CosmosWorksLib)
ActivationOption_Deactivate: int = 0
ActivationOption_Activate: int = 1

# swsTopologyDemoldDirectionOption_e (CosmosWorksLib)
swsTopologyDemoldDirection_TwoDirectionMidPlane: int = 0
swsTopologyDemoldDirection_PullDirectionOnly: int = 1
swsTopologyDemoldDirection_Stamping: int = 2

# swsTopologyIterationOption_e (CosmosWorksLib)
IterationOption_Auto: int = 0
IterationOption_UserDef: int = 1

# swsTopologyPreservedContactConnectorOption_e (CosmosWorksLib)
PreservedContactConnectorOption_ContactsOnly: int = 0
PreservedContactConnectorOption_ConnectorsOnly: int = 1
PreservedContactConnectorOption_ContactsAndConnectors: int = 2
PreservedContactConnectorOption_None: int = 3

# swsTopologyPreservedRegionOption_e (CosmosWorksLib)
PreservedRegion_LoadsOnly: int = 0
PreservedRegion_FixturesOnly: int = 1
PreservedRegion_LoadsAndFixtures: int = 2
PreservedRegion_None: int = 3

# swsTopologyStudyConstraintComparator_e (CosmosWorksLib)
swsTopologyConstraintComparator_IsLessThan: int = 0
swsTopologyConstraintComparator_IsGreaterThan: int = 1
swsTopologyConstraintComparator_IsInBetween: int = 2

# swsTopologyStudyConstraintType_e (CosmosWorksLib)
swsTopologyConstraintType_Displacement: int = 0
swsTopologyConstraintType_Mass: int = 1
swsTopologyConstraintType_Stress: int = 2
swsTopologyConstraintType_FactorOfSafety: int = 3

# swsTopologyStudyConstraintValuationOption_e (CosmosWorksLib)
swsTopologyConstraintValuationOption_AbsValue: int = 0
swsTopologyConstraintValuationOption_MultiplicationFactor: int = 1

# swsTopologyStudyDisplacementComponentType_e (CosmosWorksLib)
swsTopologyDisplacementCompType_UX: int = 0
swsTopologyDisplacementCompType_UY: int = 1
swsTopologyDisplacementCompType_UZ: int = 2
swsTopologyDisplacementCompType_URES: int = 3
swsTopologyDisplacementCompType_UX_ABS: int = 4
swsTopologyDisplacementCompType_UY_ABS: int = 5
swsTopologyDisplacementCompType_UZ_ABS: int = 6

# swsTopologyStudyDisplacementConstraintLocationOption_e (CosmosWorksLib)
swsTopologyDisplacementConstraintLocationOption_Auto: int = 0
swsTopologyDisplacementConstraintLocationOption_UserDefine: int = 1

# swsTopologyStudyDisplacementConstraintValuationOption_e (CosmosWorksLib)
swsTopologyDisplacementConstraintValuation_AbsValue: int = 0
swsTopologyDisplacementConstraintValuation_MultiplicationFactor: int = 1

# swsTopologyStudyDisplacementCoordinateSysOption_e (CosmosWorksLib)
swsTopologyDisplacementCoordinateSysOption_Global: int = 0
swsTopologyDisplacementCoordinateSysOption_UserDefine: int = 1

# swsTopologyStudyError_e (CosmosWorksLib)
swsTopoErrCode_Success: int = 0
swsTopoErrCode_TopologyStudyManagerIsNotInitialized: int = 1
swsTopoErrCode_InvalidGoalType: int = 2
swsTopoErrCode_NoGoalHasBeenSet: int = 3
swsTopoErrCode_MinimizeMassGoalHasNotBeenSet: int = 4
swsTopoErrCode_MaximizeStiffnessGoalHasNotBeenSet: int = 5
swsTopoErrCode_MinimizeMaximumDisplacementGoalHasNotBeenSet: int = 6
swsTopoErrCode_OnlyOneMassConstraintCanBeDefined: int = 7
swsTopoErrCode_OnlyOneDisplacementConstraintWithAutoDefineCanBeDefined: int = 8
swsTopoErrCode_ConstraintNotFound: int = 9
swsTopoErrCode_DefaultConstraintCannotBeRemoved: int = 10
swsTopoErrCode_ConstraintDefinitionLimitReached: int = 11
swsTopoErrCode_ManufacturingControlNotFound: int = 12
swsTopoErrCode_OnlyOneThicknessControlCanBeDefined: int = 13
swsTopoErrCode_OnlyOneDemoldControlCanBeDefined: int = 14
swsTopoErrCode_OnlyOneSymmetryControlCanBeDefined: int = 15
swsTopoErrCode_OnlyOneFrequencyConstraintCanBeDefined: int = 16
swsTopoErrCode_SetOperationNotSupported: int = 17
swsTopoErrCode_CannotCreatFOSIfStressAlrdyPrsnt: int = 18
swsTopoErrCode_CannotCreatStressIfFOSAlrdyPrsnt: int = 19
swsTopoErrCode_OnlyOneStressConstraintCanBeDefined: int = 20
swsTopoErrCode_OnlyOneFOSConstraintCanBeDefined: int = 21

# swsTopologyStudyFactorOfSafetyComponentType_e (CosmosWorksLib)
swsTopologyFactorOfSafetyCompType_MaxVONMises: int = 0

# swsTopologyStudyGoalType_e (CosmosWorksLib)
swsTopologyGoalType_MaximizeStiffness: int = 0
swsTopologyGoalType_MinimizeMaximumDisplacement: int = 1
swsTopologyGoalType_MinimizeMass: int = 2

# swsTopologyStudyMassConstraintOption_e (CosmosWorksLib)
swsTopologyMassConstraintOption_AbsoluteValue: int = 0
swsTopologyMassConstraintOption_Percentage: int = 1

# swsTopologyStudyStressComponentType_e (CosmosWorksLib)
swsTopologyStressCompType_VONMises: int = 0

# swsTopologyStudyStressConstraintValuationOption_e (CosmosWorksLib)
swsTopologyStressConstraintValuation_AbsValue: int = 0
swsTopologyStressConstraintValuation_Percentage: int = 1

# swsTopologyStudy_DemoldControlErrors_e (CosmosWorksLib)
swsTopoDCErrCode_Success: int = 0
swsTopoDCErrCode_SetOperationNotSupported: int = 1
swsTopoDCErrCode_InvalidEntitySelectedAsEdge: int = 2
swsTopoDCErrCode_InvalidDirectionOptionSelected: int = 3
swsTopoDCErrCode_InvalidEntitySelectedAsPlane: int = 4
swsTopoDCErrCode_NotAvailableForCurrentDirectionOption: int = 5
swsTopoDCErrCode_PlaneSelectionNotAvailable: int = 6
swsTopoDCErrCode_PlaneSelectionRequired: int = 7
swsTopoDCErrCode_EdgeSelectionNotAvailable: int = 8
swsTopoDCErrCode_EdgeSelectionRequired: int = 9

# swsTopologyStudy_DisplacementConstraintErrors_e (CosmosWorksLib)
swsTopoDispErrCode_Success: int = 0
swsTopoDispErrCode_SetOperationNotSupported: int = 1
swsTopoDispErrCode_InvalidConstraintValue: int = 2
swsTopoDispErrCode_LessThanEqualToZeroConstraintValue: int = 3
swsTopoDispErrCode_InvalidComponent: int = 4
swsTopoDispErrCode_InvalidConstraintValuationOption: int = 5
swsTopoDispErrCode_InvalidUnit: int = 6
swsTopoDispErrCode_InvalidComparator: int = 7
swsTopoDispErrCode_UnitNotAvailable: int = 8
swsTopoDispErrCode_InvalidSelectionForVertex: int = 9
swsTopoDispErrCode_CannotSetVertex: int = 10
swsTopoDispErrCode_InvalidLocationOption: int = 11
swsTopoDispErrCode_InvalidVertexCount: int = 12
swsTopoDispErrCode_CoordinateSysNAError: int = 13
swsTopoDispErrCode_CoordinateSysInvalidOption: int = 14
swsTopoDispErrCode_CoordinateSysInvalidSelection: int = 15
swsTopoDispErrCode_CoordinateSysNotSelected: int = 16
swsTopoDispErrCode_ConstraintNotFound: int = 17
swsTopoDispErrCode_InvalidArray: int = 18

# swsTopologyStudy_FOSConstraintErrors_e (CosmosWorksLib)
swsTopoFOSErrCode_Success: int = 0
swsTopoFOSErrCode_SetOperationNotSupported: int = 1
swsTopoFOSErrCode_InvalidConstraintValue: int = 2
swsTopoFOSErrCode_LessThanEqualToZeroConstraintValue: int = 3
swsTopoFOSErrCode_InvalidComponent: int = 4
swsTopoFOSErrCode_OutOfRangeValue: int = 5
swsTopoFOSErrCode_InvalidComparator: int = 6
swsTopoFOSErrCode_ConstraintNotFound: int = 7
swsTopoFOSErrCode_MaterialWithInvalidYieldStrength: int = 8

# swsTopologyStudy_FrequencyConstraintErrors_e (CosmosWorksLib)
swsTopoFreqErrCode_Success: int = 0
swsTopoFreqErrCode_SetOperationNotSupported: int = 1
swsTopoFreqErrCode_InvalidConstraintValue: int = 2
swsTopoFreqErrCode_LessThanEqualToZeroConstraintValue: int = 3
swsTopoFreqErrCode_HMSFreqLessThanLMSFreq: int = 4
swsTopoFreqErrCode_ModeShapesNotInAscendingOrder: int = 5
swsTopoFreqErrCode_EnterRangeOfValues: int = 6
swsTopoFreqErrCode_UnequalSizedArrays: int = 7
swsTopoFreqErrCode_InvalidModeShapeData: int = 8
swsTopoFreqErrCode_InvalidComparatorData: int = 9
swsTopoFreqErrCode_InvalidFreqValuesData: int = 10
swsTopoFreqErrCode_ModeShapeDataIsNotSet: int = 11
swsTopoFreqErrCode_ComparatorDataIsNotSet: int = 12
swsTopoFreqErrCode_FreqValuesDataIsNotSet: int = 13
swsTopoFreqErrCode_InvalidArray: int = 14
swsTopoFreqErrCode_ConstraintNotFound: int = 15

# swsTopologyStudy_MassConstraintErrors_e (CosmosWorksLib)
swsTopoMassErrCode_Success: int = 0
swsTopoMassErrCode_SetOperationNotSupported: int = 1
swsTopoMassErrCode_InvalidConstraintValue: int = 2
swsTopoMassErrCode_LessThanEqualToZeroConstraintValue: int = 3
swsTopoMassErrCode_GreaterThan100PercentApplied: int = 4
swsTopoMassErrCode_GreaterThanTotalMassOfModel: int = 5
swsTopoMassErrCode_InvalidUnit: int = 6
swsTopoMassErrCode_InvalidPreferenceOption: int = 7
swsTopoMassErrCode_ConstraintNotFound: int = 8

# swsTopologyStudy_MinMaxDisplacementGoalErrors_e (CosmosWorksLib)
swsTopoDGErrCode_Success: int = 0
swsTopoDGErrCode_SetOperationNotSupported: int = 1
swsTopoDGErrCode_InvalidComponent: int = 2
swsTopoDGErrCode_CoordinateSysNAError: int = 3
swsTopoDGErrCode_CoordinateSysInvalidOption: int = 4
swsTopoDGErrCode_CoordinateSysInvalidSelection: int = 5
swsTopoDGErrCode_CoordinateSysNotSelected: int = 6
swsTopoDGErrCode_InvalidVertexCount: int = 7
swsTopoDGErrCode_InvalidArray: int = 8
swsTopoDGErrCode_InvalidEntities: int = 9

# swsTopologyStudy_PreservedRegionErrors_e (CosmosWorksLib)
swsTopoPRErrCode_Success: int = 0
swsTopoPRErrCode_SetOperationNotSupported: int = 1
swsTopoPRErrCode_InvalidFaceCount: int = 2
swsTopoPRErrCode_InvalidAreaDepth: int = 3
swsTopoPRErrCode_InvalidAreaDepthUnit: int = 4
swsTopoPRErrCode_InvalidArray: int = 5
swsTopoPRErrCode_InvalidEntities: int = 6

# swsTopologyStudy_StressConstraintErrors_e (CosmosWorksLib)
swsTopoStressErrCode_Success: int = 0
swsTopoStressErrCode_SetOperationNotSupported: int = 1
swsTopoStressErrCode_InvalidConstraintValue: int = 2
swsTopoStressErrCode_LessThanEqualToZeroConstraintValue: int = 3
swsTopoStressErrCode_InvalidComponent: int = 4
swsTopoStressErrCode_InvalidConstraintValuationOption: int = 5
swsTopoStressErrCode_InvalidUnit: int = 6
swsTopoStressErrCode_InvalidComparator: int = 7
swsTopoStressErrCode_UnitNotAvailable: int = 8
swsTopoStressErrCode_LessThanPermittedValue: int = 9
swsTopoStressErrCode_ConstraintNotFound: int = 10
swsTopoStressErrCode_OutOfRangePercentageValue: int = 11

# swsTopologyStudy_SymmetryControlErrors_e (CosmosWorksLib)
swsTopoSCErrCode_Success: int = 0
swsTopoSCErrCode_SetOperationNotSupported: int = 1
swsTopoSCErrCode_InvalidEntitySelectedAsPlane: int = 2
swsTopoSCErrCode_InvalidTypeSelected: int = 3
swsTopoSCErrCode_IncorrectPlaneSelectionsForGivenSymmetryType: int = 4
swsTopoSCErrCode_SetSymmetryTypeBeforeSelectingPlane: int = 5

# swsTopologyStudy_ThicknessControlErrors_e (CosmosWorksLib)
swsTopoTCErrCode_Success: int = 0
swsTopoTCErrCode_SetOperationNotSupported: int = 1
swsTopoTCErrCode_InvalidThickness: int = 2
swsTopoTCErrCode_InvalidThicknessUnit: int = 3

# swsTopologySymmetryControlOption_e (CosmosWorksLib)
swsTopologySymmetryControlType_HalfSymmetry: int = 0
swsTopologySymmetryControlType_QuarterSymmetry: int = 1
swsTopologySymmetryControlType_OneEighthSymmetry: int = 2

# swsTrendTrackerErrorCode_e (CosmosWorksLib)
swsTrendTracker_NoError: int = 0
swsTrendTracker_InvalidStudyType: int = 1
swsTrendTracker_InvalidTrendTrackerObj: int = 2
swsTrendTracker_FailedCreation: int = 3
swsTrendTracker_SetBaseLineActionFailed: int = 4

# swsUnitSystem_e (CosmosWorksLib)
swsUnitSystemSI: int = 0
swsUnitSystemIPS: int = 1
swsUnitSystemMKS: int = 2
swsUnitSystemSIWithMPA: int = 3

# swsUnit_e (CosmosWorksLib)
swsUnitSI: int = 0
swsUnitEnglish: int = 1
swsUnitMetric: int = 2

# swsUserPreferenceDoubleValue_e (CosmosWorksLib)
swsPlotShowHiddenBodyTransparency: int = 0
swsPlotShowExcludedBodyTransparency: int = 1
swsPlotDeformedShapeSuperImposeModelTranslucentTransparency: int = 2
swsPlotBeamDiagramTransparency: int = 3
swsPlotBoundaryTransparency: int = 4

# swsUserPreferenceIntegerValue_e (CosmosWorksLib)
swsDefaultSolverValue: int = 0
swsDefaultResultFolder: int = 1
swsReportPublishOption: int = 2
swsColorChartPosition: int = 3
swsPlotSettingsFringeOption: int = 4
swsPlotSettingsBoundaryOption: int = 5
swsPlotShowExcludedBodiesOption: int = 6
swsPlotShowHiddenBodiesOption: int = 7
swsPlotBoundaryOptionTranslucentSingleColorSetting: int = 8
swsPlotBoundaryOptionMeshColor: int = 9
swsPlotShowExcludedBodyTranslucentSingleColor: int = 10
swsPlotShowHiddenBodyTranslucentSingleColor: int = 11
swsPlotDeformedShapeOptionSetting: int = 12
swsPlotDeformedShapeResultScaleContact: int = 13
swsPlotDeformedShapeResultScaleLarge: int = 14
swsPlotDeformedShapeResultOther: int = 15
swsPlotDeformedShapeOptionSetSuperImposeOption: int = 16
swsReportPublishOptionReportFolderUserDefinedPath: int = 17
swsColorChartPositionUserDefinedXValue: int = 18
swsColorChartPositionUserDefinedYValue: int = 19
swsColorChartWidthOption: int = 20
swsColorChartNumberFormatOption: int = 21
swsColorChartColorOptionChartColorNumber: int = 22
swsColorChartColorOptionBaseChartColorNumber: int = 23
swsColorChartColorOptionLegendType: int = 24
swsColorChartNumberFormatLegendPrecision: int = 25
swsColorChartNumberFormatUseDiffNoFormatOption: int = 26
swsColorChartColorOptionvonMisesColorValue: int = 27
swsPlotDeformedShapeOptionTranslucentColor: int = 28
swsPlotBoundaryOptionModelColor: int = 29
swsEMailType: int = 30
swsMesherType: int = 31

# swsUserPreferenceStringValue_e (CosmosWorksLib)
swsUserDefinedResultFolderLocation: int = 0
swsSolidWorksDocumentFolderSubFolderLocation: int = 1
swsSolidWorksUserDefinedReportFolderLocation: int = 2
swsEMailSendFrom: int = 3
swsEMailSendTo: int = 4
swsEMailSMTP: int = 5
swsEMailPort: int = 6
swsEMailAccount: int = 7
swsEMailPassword: int = 8

# swsUserPreferenceToggle_e (CosmosWorksLib)
swsResultFolderUnderSubFolder: int = 0
swsResultFolderKeepTempDataBase: int = 1
swsTrendTrackerBackUpModelsRestoreIteration: int = 2
swsShowReportOnPublish: int = 3
swsPlotAnnotationShowMinValue: int = 4
swsPlotAnnotationShowMaxValue: int = 5
swsPlotAnnotationShowRangeBasedOnShowCompOnly: int = 6
swsPlotShowExcludedBodies: int = 7
swsPlotShowHiddenBodies: int = 8
swsPlotDeformedShapeOptionSuperImposeModelOnDeformedShape: int = 9
swsColorChartDisplay: int = 10
swsColorChartDetails: int = 11
swsColorChartNumberFormatUseDifferentNumberFormat: int = 12
swsColorChartColorNoOfChartColorFlip: int = 13
swsColorChartColorSpecifyColorForvonMisesPlot: int = 14
swsLoadAllStudies_e: int = 15
swsEMailAuthentication: int = 16
swsAverageStressesAtMidnodes: int = 17
swsEnforceSaveAfterMeshAndAfterSolve: int = 18
swsIncludeMeshInCopyStudy: int = 19
swsIncludeResultsInCopyStudy: int = 20
swsAutomaticallyDetectUnderConstrainedBodies: int = 21

# swsVelocityComponent_e (CosmosWorksLib)
swsVelocityComponentVX: int = 0
swsVelocityComponentVY: int = 1
swsVelocityComponentVZ: int = 2
swsVelocityComponentVRES: int = 3
swsVelocityComponentAVX: int = 4
swsVelocityComponentAVY: int = 5
swsVelocityComponentAVZ: int = 6
swsVelocityComponentAVRES: int = 7

# swsVelocityUnit_e (CosmosWorksLib)
swsVelocityUnit_MillimetersPerSec: int = 0
swsVelocityUnit_CentimetersPerSec: int = 1
swsVelocityUnit_MetersPerSec: int = 2
swsVelocityUnit_InchesPerSec: int = 3

# swsWallType_e (CosmosWorksLib)
swsWallTypeRigid: int = 0
swsWallTypeFlexible: int = 1

# swsWeakMaterial_e (CosmosWorksLib)
swsWeakMaterialCustom: int = 0
swsWeakMaterialFirstFaceMaterial: int = 1
swsWeakMaterialSecondFaceMaterial: int = 2

# swsWeldResultErrorCode_e (CosmosWorksLib)
swsWeldResult_NoError: int = 0
swsWeldResult_NoView: int = 1
swsWeldResult_InvalidUnit: int = 2
swsWeldResult_ResultsNotAvailable: int = 3
swsWeldResult_InvalidConnectorName: int = 4
swsWeldResult_NoPersistID: int = 5
swsWeldResult_MeshDataNotAvailable: int = 6
swsWeldResult_NodeIndexListUnAvailable: int = 7

# swsWeldStrengthUnits_e (CosmosWorksLib)
swsWeldStrengthUnits_NewtonOverMeterSquare: int = 0
swsWeldStrengthUnits_PSI: int = 1
swsWeldStrengthUnits_KgfOverCentimeterSquare: int = 2
swsWeldStrengthUnits_MPa: int = 3
swsWeldStrengthUnits_KSI: int = 4

# swsWindowsBasicColors_e (CosmosWorksLib)
swsLightRed: int = 8421631
swsLightYellow: int = 8454143
swsPaleGreen: int = 8454016
swsSpringGreen: int = 8453888
swsCyan: int = 16777088
swsDodgerBlue: int = 16744448
swsPlum: int = 12615935
swsViolet: int = 16744703
swsRed: int = 255
swsYellow: int = 65535
swsGreenYellow: int = 65408
swsLawnGreen: int = 4259584
swsAqua: int = 16776960
swsDeepSkyBlue: int = 12615680
swsMediumPurple: int = 12615808
swsMagenta: int = 16711935
swsLightSalmon: int = 4210816
swsCoral: int = 4227327
swsLime: int = 65280
swsTeal: int = 8421376
swsRoyalBlue: int = 8404992
swsSgiSlateBlue: int = 16744576
swsDarkRed: int = 4194432
swsSgiSalmon: int = 8388863
swsMaroon: int = 128
swsOrange: int = 33023
swsGreen: int = 32768
swsSapGreen: int = 4227072
swsBlue: int = 16711680
swsMidnightBlue: int = 10485760
swsPurple: int = 8388736
swsSgiBeet: int = 16711808
swsDeepGray: int = 64
swsTan: int = 16512
swsDarkOliveGreen: int = 16384
swsDarkGreen: int = 4210688
swsNavy: int = 8388608
swsDarkBlue: int = 4194304
swsDarkPurple: int = 4194368
swsIndigo: int = 8388672
swsBlack: int = 0
swsOlive: int = 32896
swsKhaki: int = 4227200
swsGray: int = 8421504
swsLightSeaGreen: int = 8421440
swsSilver: int = 12632256
swsWhite: int = 16777215

