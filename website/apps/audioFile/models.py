from django.db import models
from django.utils.translation import ugettext as _

import wave

class AudioFile(models.Model):
    title = models.CharField(_('Title'), max_length=256, )
    audiofile = models.FileField(_('Audio File'), upload_to='audiofiles', )

    def __unicode__(self):
        return "%s" % self.title

    def get_info(self):

        audioData = wave.open(self.audiofile.path, 'r')

        title = self.audiofile.name
        number_of_channels = audioData.getnchannels()
        number_of_frames = audioData.getnframes()
        frequency = audioData.getframerate()

        return title, number_of_channels, number_of_frames, frequency


    def get_sample_data(self, startPos=0, num_of_samples=44100, skip=1000):

        audioData = wave.open(self.audiofile.path, 'r')
        audioData.setpos(startPos)
        samples = audioData.readframes(num_of_samples)
        number_of_channels = audioData.getnchannels()

        from struct import unpack
        npts=len(num_of_samples)
        formatstr = '%ih' % (npts/2)
        int_data = unpack(formatstr, samples)

        format_data = []
        i = 0
        skip *= number_of_channels

        for sample in int_data:
            i += number_of_channels
            if i % skip != 0:
                continue
            format_data.append(sample)

        return format_data