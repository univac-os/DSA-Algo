function capitalizeTitle(title: string): string {
    const words=title.split(" ");
    const res=words.map(word =>{
        if (word.length <=2){
            return word.toLowerCase();
        }
        else{
            return word.charAt(0).toUpperCase()+ word.slice(1).toLowerCase();
        }
    });
    return res.join(" ");
};