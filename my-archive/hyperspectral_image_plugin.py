from typing import TYPE_CHECKING

import numpy as np
from pathlib import Path

from nomad.datamodel.data import ArchiveSection, EntryData
from nomad.datamodel.metainfo.annotations import ELNAnnotation, SectionProperties
from nomad.datamodel.metainfo.plot import PlotlyFigure, PlotSection
from nomad.metainfo import Package, Quantity, Section, SubSection

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger



m_package = Package(name = 'hyperspectral_image_plugin', description = 'A plugin to store hyperspectral image data.')

class Acquisition_metadata(ArchiveSection):

    m_def = Section(
        a_eln=ELNAnnotation(
            properties=SectionProperties(
                order=[
                    'interleave',
                    'data-type',
                    'samples',
                    'bands',
                    'sample-binning',
                    'spectral-binning',
                    'line-bining',
                    'shutter',
                    'gain',
                    'framerate',
                    'temperature',
                    'imager-serial-number',
                    'rotation',
                    'pixel-size',
                    'byte-order',
                    'header-offset',
                    'flip-radiometric-calibration',
                    'wavelenth',
                    'wavelength-unit',
                    'reflection-scale-factor',
                    'label',
                    'history'
                ],
            ),
        ),
    )

    interleave = Quantity(
        type=str,
        description='The interleave format of the hyperspectral image data (e.g., BSQ, BIL, BIP).',
        a_eln={'choices': ['BSQ', 'BIL', 'BIP']
        },
    )

    data_type = Quantity(
        type=str,
        description='The data type of the hyperspectral image data (e.g., uint16, float32).',
        a_eln={
            'choices': ['uint16', 'float32']
        },
    )

    samples = Quantity(
        type=int,
        description='The number of samples in the hyperspectral image data.',
        a_eln={
            "component": "NumberEditQuantity"
        },
    )

    bands = Quantity(
        type=int,
        description='The number of bands in the hyperspectral image data.',
        a_eln={
            "component": "NumberEditQuantity"
        }
    )

    sample_binning = Quantity(
        type=int,
        description='The binning factor for the samples in the hyperspectral image data.',
        a_eln={
            "component": "NumberEditQuantity"
        }
    )

    spectral_binning = Quantity(
        type=int,
        description='The binning factor for the spectral dimension in the hyperspectral image data.',
        a_eln={
            "component": "NumberEditQuantity"
        }
    )

    line_binning = Quantity(
        type=int,
        description='The binning factor for the line dimension in the hyperspectral image data.',
        a_eln={
            "component": "NumberEditQuantity"
        }
    )

    shutter = Quantity(
        type=str,
        description='The shutter type used during the acquisition of the hyperspectral image data (e.g., global, rolling).',
        a_eln={
            'choices': ['global', 'rolling']
        }
    )

    gain = Quantity(
        type=float,
        description='The gain setting used during the acquisition of the hyperspectral image data.',
        a_eln={
            "component": "NumberEditQuantity"
        }
    )

    framerate = Quantity(
        type=float,
        description='The frame rate at which the hyperspectral image data was acquired.',
        a_eln={
            "component": "NumberEditQuantity"
        }
    )

    temperature = Quantity(
        type=float,
        description='The temperature of the sensor during the acquisition of the hyperspectral image data.',
        a_eln={
            "component": "NumberEditQuantity"
        }
    )

    imager_serial_number = Quantity(
        type=str,
        description='The serial number of the imager used during the acquisition of the hyperspectral image data.',
        a_eln={
            "component": "TextEditQuantity"
        }
    )

    rotation = Quantity(
        type=float,
        description='The rotation angle of the hyperspectral image data.',
        a_eln={
            "component":"NumberEditQuantity"
        }
    )

    pixel_size = Quantity(
        type=float,
        description='The pixel size of the hyperspectral image data.',
        a_eln={
            "component": "NumberEditQuantity"
        }
    )

    byte_order = Quantity(
        type=str,
        description='The byte order of the hyperspectral image data (e.g., little-endian, big-endian).',
        a_eln={
            'choices': ['little-endian', 'big-endian']
        }
    )

    header_offset = Quantity(
        type=int,
        description='The offset in bytes to the start of the hyperspectral image data from the beginning of the file.',
        a_eln={
            "component": "NumberEditQuantity"
        }
    )

    flip_radiometric_calibration = Quantity(
        type=bool,
        description='Whether to flip the radiometric calibration of the hyperspectral image data.',
        a_eln={
            "component": "BooleanEditQuantity"
        }
    )

    wavelength = Quantity(
        type=np.ndarray,
        description='The wavelength values corresponding to each band in the hyperspectral image data.',
        a_eln={
            "component": "ArrayEditQuantity",
            "array_type": "float",
            "shape": ["bands"]
        }
    )

    wavelength_unit = Quantity(
        type=str,
        description='The unit of the wavelength values (e.g., nm, μm).',
        a_eln={
            "component": "TextEditQuantity"
        }
    )

    reflection_scale_factor = Quantity(
        type=float,
        description='The scale factor used to convert the hyperspectral image data to reflectance values.',
        a_eln={
            "component": "NumberEditQuantity"
        }
    )

    label = Quantity(
        type=str,
        description='A label for the acquisition metadata.',
        a_eln={
            "component": "TextEditQuantity"
        }
    )

    history = Quantity(
        type=str,
        description='A history of the acquisition metadata.',
        a_eln={
            "component": "TextEditQuantity"
            }
        )


class HyperspectralImageData(EntryData):
    m_def = Section(
        a_eln=ELNAnnotation(
            properties=(SectionProperties(
                order=[
                    'acquisition-metadata',
                    'data-file',
                    'preview-image',
                    'label',
                    'history',
                    ],
               ),
            ),
        )
    )

    acquisition_metadata = SubSection(
        section_def=Acquisition_metadata,
        description='The acquisition metadata for the hyperspectral image data.',
    )

    data_file = Quantity(
        type=Path,
        description='The file path to the hyperspectral image data file.',
        a_eln={
            "component": "FileEditQuantity"
        }
    )

    preview_image = Quantity(
        type=Path,
        description='The file path to a preview image of the hyperspectral image data.',
        a_eln={
            "component": "FileEditQuantity"
        }
    )

    label = Quantity(
        type=str,
        description='A label for the hyperspectral image data.',
        a_eln={
            "component": "TextEditQuantity"
        }
    )

    history = Quantity(
        type=str,
        description='A history of the hyperspectral image data.',
        a_eln={
            "component": "TextEditQuantity"
        }
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)
        # Additional normalization steps can be added here if needed.

m_package.__init_metainfo__()