clear
m4a_list = ls('dataset/test/zsl/');
m4a_list = m4a_list(3:size(m4a_list,1),:);
FS = 16000;
for i = (1:size(m4a_list,1))
    m4a_name = join(['dataset/test/zsl/',m4a_list(i,:)]);
    wv_name = join([m4a_name(:,1:size(m4a_name,2)-3),'wav']);
    [m4a,fs] = audioread(m4a_name);
    wv = resample(m4a,FS,fs);
    audiowrite(wv_name,wv,FS)
end

    
    

 