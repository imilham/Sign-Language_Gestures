# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: object_detection/protos/losses.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$object_detection/protos/losses.proto\x12\x17object_detection.protos\"\xfe\x05\n\x04Loss\x12\x44\n\x11localization_loss\x18\x01 \x01(\x0b\x32).object_detection.protos.LocalizationLoss\x12H\n\x13\x63lassification_loss\x18\x02 \x01(\x0b\x32+.object_detection.protos.ClassificationLoss\x12\x45\n\x12hard_example_miner\x18\x03 \x01(\x0b\x32).object_detection.protos.HardExampleMiner\x12 \n\x15\x63lassification_weight\x18\x04 \x01(\x02:\x01\x31\x12\x1e\n\x13localization_weight\x18\x05 \x01(\x02:\x01\x31\x12M\n\x16random_example_sampler\x18\x06 \x01(\x0b\x32-.object_detection.protos.RandomExampleSampler\x12I\n\x11\x65qualization_loss\x18\x07 \x01(\x0b\x32..object_detection.protos.Loss.EqualizationLoss\x12V\n\x15\x65xpected_loss_weights\x18\x12 \x01(\x0e\x32\x31.object_detection.protos.Loss.ExpectedLossWeights:\x04NONE\x12#\n\x18min_num_negative_samples\x18\x13 \x01(\x02:\x01\x30\x12*\n\x1f\x64\x65sired_negative_sampling_ratio\x18\x14 \x01(\x02:\x01\x33\x1a?\n\x10\x45qualizationLoss\x12\x11\n\x06weight\x18\x01 \x01(\x02:\x01\x30\x12\x18\n\x10\x65xclude_prefixes\x18\x02 \x03(\t\"Y\n\x13\x45xpectedLossWeights\x12\x08\n\x04NONE\x10\x00\x12\x15\n\x11\x45XPECTED_SAMPLING\x10\x01\x12!\n\x1dREWEIGHTING_UNMATCHED_ANCHORS\x10\x02\"\xb7\x03\n\x10LocalizationLoss\x12J\n\x0bweighted_l2\x18\x01 \x01(\x0b\x32\x33.object_detection.protos.WeightedL2LocalizationLossH\x00\x12W\n\x12weighted_smooth_l1\x18\x02 \x01(\x0b\x32\x39.object_detection.protos.WeightedSmoothL1LocalizationLossH\x00\x12L\n\x0cweighted_iou\x18\x03 \x01(\x0b\x32\x34.object_detection.protos.WeightedIOULocalizationLossH\x00\x12K\n\x14l1_localization_loss\x18\x04 \x01(\x0b\x32+.object_detection.protos.L1LocalizationLossH\x00\x12N\n\rweighted_giou\x18\x05 \x01(\x0b\x32\x35.object_detection.protos.WeightedGIOULocalizationLossH\x00\x42\x13\n\x11localization_loss\">\n\x1aWeightedL2LocalizationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\"V\n WeightedSmoothL1LocalizationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x10\n\x05\x64\x65lta\x18\x02 \x01(\x02:\x01\x31\"\x1d\n\x1bWeightedIOULocalizationLoss\"\x14\n\x12L1LocalizationLoss\"\x1e\n\x1cWeightedGIOULocalizationLoss\"\xd1\x05\n\x12\x43lassificationLoss\x12V\n\x10weighted_sigmoid\x18\x01 \x01(\x0b\x32:.object_detection.protos.WeightedSigmoidClassificationLossH\x00\x12V\n\x10weighted_softmax\x18\x02 \x01(\x0b\x32:.object_detection.protos.WeightedSoftmaxClassificationLossH\x00\x12j\n\x17weighted_logits_softmax\x18\x05 \x01(\x0b\x32G.object_detection.protos.WeightedSoftmaxClassificationAgainstLogitsLossH\x00\x12^\n\x14\x62ootstrapped_sigmoid\x18\x03 \x01(\x0b\x32>.object_detection.protos.BootstrappedSigmoidClassificationLossH\x00\x12Y\n\x16weighted_sigmoid_focal\x18\x04 \x01(\x0b\x32\x37.object_detection.protos.SigmoidFocalClassificationLossH\x00\x12g\n#penalty_reduced_logistic_focal_loss\x18\x06 \x01(\x0b\x32\x38.object_detection.protos.PenaltyReducedLogisticFocalLossH\x00\x12\x64\n!weighted_dice_classification_loss\x18\x07 \x01(\x0b\x32\x37.object_detection.protos.WeightedDiceClassificationLossH\x00\x42\x15\n\x13\x63lassification_loss\"E\n!WeightedSigmoidClassificationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\"c\n\x1eSigmoidFocalClassificationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x10\n\x05gamma\x18\x02 \x01(\x02:\x01\x32\x12\r\n\x05\x61lpha\x18\x03 \x01(\x02\"]\n!WeightedSoftmaxClassificationLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x0blogit_scale\x18\x02 \x01(\x02:\x01\x31\"j\n.WeightedSoftmaxClassificationAgainstLogitsLoss\x12 \n\x11\x61nchorwise_output\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x0blogit_scale\x18\x02 \x01(\x02:\x01\x31\"w\n%BootstrappedSigmoidClassificationLoss\x12\r\n\x05\x61lpha\x18\x01 \x01(\x02\x12\x1d\n\x0ehard_bootstrap\x18\x02 \x01(\x08:\x05\x66\x61lse\x12 \n\x11\x61nchorwise_output\x18\x03 \x01(\x08:\x05\x66\x61lse\">\n\x1fPenaltyReducedLogisticFocalLoss\x12\r\n\x05\x61lpha\x18\x01 \x01(\x02\x12\x0c\n\x04\x62\x65ta\x18\x02 \x01(\x02\"\xa1\x02\n\x10HardExampleMiner\x12\x1d\n\x11num_hard_examples\x18\x01 \x01(\x05:\x02\x36\x34\x12\x1a\n\riou_threshold\x18\x02 \x01(\x02:\x03\x30.7\x12K\n\tloss_type\x18\x03 \x01(\x0e\x32\x32.object_detection.protos.HardExampleMiner.LossType:\x04\x42OTH\x12%\n\x1amax_negatives_per_positive\x18\x04 \x01(\x05:\x01\x30\x12\"\n\x17min_negatives_per_image\x18\x05 \x01(\x05:\x01\x30\":\n\x08LossType\x12\x08\n\x04\x42OTH\x10\x00\x12\x12\n\x0e\x43LASSIFICATION\x10\x01\x12\x10\n\x0cLOCALIZATION\x10\x02\">\n\x14RandomExampleSampler\x12&\n\x18positive_sample_fraction\x18\x01 \x01(\x02:\x04\x30.01\"p\n\x1eWeightedDiceClassificationLoss\x12$\n\x15squared_normalization\x18\x01 \x01(\x08:\x05\x66\x61lse\x12(\n\x19is_prediction_probability\x18\x02 \x01(\x08:\x05\x66\x61lse')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.losses_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_LOSS']._serialized_start=66
  _globals['_LOSS']._serialized_end=832
  _globals['_LOSS_EQUALIZATIONLOSS']._serialized_start=678
  _globals['_LOSS_EQUALIZATIONLOSS']._serialized_end=741
  _globals['_LOSS_EXPECTEDLOSSWEIGHTS']._serialized_start=743
  _globals['_LOSS_EXPECTEDLOSSWEIGHTS']._serialized_end=832
  _globals['_LOCALIZATIONLOSS']._serialized_start=835
  _globals['_LOCALIZATIONLOSS']._serialized_end=1274
  _globals['_WEIGHTEDL2LOCALIZATIONLOSS']._serialized_start=1276
  _globals['_WEIGHTEDL2LOCALIZATIONLOSS']._serialized_end=1338
  _globals['_WEIGHTEDSMOOTHL1LOCALIZATIONLOSS']._serialized_start=1340
  _globals['_WEIGHTEDSMOOTHL1LOCALIZATIONLOSS']._serialized_end=1426
  _globals['_WEIGHTEDIOULOCALIZATIONLOSS']._serialized_start=1428
  _globals['_WEIGHTEDIOULOCALIZATIONLOSS']._serialized_end=1457
  _globals['_L1LOCALIZATIONLOSS']._serialized_start=1459
  _globals['_L1LOCALIZATIONLOSS']._serialized_end=1479
  _globals['_WEIGHTEDGIOULOCALIZATIONLOSS']._serialized_start=1481
  _globals['_WEIGHTEDGIOULOCALIZATIONLOSS']._serialized_end=1511
  _globals['_CLASSIFICATIONLOSS']._serialized_start=1514
  _globals['_CLASSIFICATIONLOSS']._serialized_end=2235
  _globals['_WEIGHTEDSIGMOIDCLASSIFICATIONLOSS']._serialized_start=2237
  _globals['_WEIGHTEDSIGMOIDCLASSIFICATIONLOSS']._serialized_end=2306
  _globals['_SIGMOIDFOCALCLASSIFICATIONLOSS']._serialized_start=2308
  _globals['_SIGMOIDFOCALCLASSIFICATIONLOSS']._serialized_end=2407
  _globals['_WEIGHTEDSOFTMAXCLASSIFICATIONLOSS']._serialized_start=2409
  _globals['_WEIGHTEDSOFTMAXCLASSIFICATIONLOSS']._serialized_end=2502
  _globals['_WEIGHTEDSOFTMAXCLASSIFICATIONAGAINSTLOGITSLOSS']._serialized_start=2504
  _globals['_WEIGHTEDSOFTMAXCLASSIFICATIONAGAINSTLOGITSLOSS']._serialized_end=2610
  _globals['_BOOTSTRAPPEDSIGMOIDCLASSIFICATIONLOSS']._serialized_start=2612
  _globals['_BOOTSTRAPPEDSIGMOIDCLASSIFICATIONLOSS']._serialized_end=2731
  _globals['_PENALTYREDUCEDLOGISTICFOCALLOSS']._serialized_start=2733
  _globals['_PENALTYREDUCEDLOGISTICFOCALLOSS']._serialized_end=2795
  _globals['_HARDEXAMPLEMINER']._serialized_start=2798
  _globals['_HARDEXAMPLEMINER']._serialized_end=3087
  _globals['_HARDEXAMPLEMINER_LOSSTYPE']._serialized_start=3029
  _globals['_HARDEXAMPLEMINER_LOSSTYPE']._serialized_end=3087
  _globals['_RANDOMEXAMPLESAMPLER']._serialized_start=3089
  _globals['_RANDOMEXAMPLESAMPLER']._serialized_end=3151
  _globals['_WEIGHTEDDICECLASSIFICATIONLOSS']._serialized_start=3153
  _globals['_WEIGHTEDDICECLASSIFICATIONLOSS']._serialized_end=3265
# @@protoc_insertion_point(module_scope)
