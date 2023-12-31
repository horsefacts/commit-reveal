const colors = ["red", "orange", "yellow", "green", "sky", "violet"];

export const getColor = (tokenId: number) => {
  return colors[tokenId % colors.length];
};
